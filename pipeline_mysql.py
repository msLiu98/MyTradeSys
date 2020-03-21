import pymysql
import pandas as pd
import pprint
import easyquotation
import requests
from get_value import get_data
import datetime


class MysqlPipeline(object):
    def __init__(self, host, user, password, port, db):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.db = db
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db, charset='utf8')
        self.cursor = self.conn.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        return

    def create_database(self, db_name):
        db_sql = "CREATE DATABASE {db_name} DEFAULT CHARACTER SET utf8".format(db_name=db_name)
        self.cursor.execute(db_sql)

    def change_database(self, db_name):
        db_sql = "use database {db_name}".format(db_name=db_name)
        self.cursor.execute(db_sql)

    def create_table(self, table_name, key_tuples, default=True):
        key_format = '{key_name} {key_type} {key_restraint}'
        if default:
            sql_format = 'CREATE TABLE IF NOT EXISTS {table_name} ({key_sql})'
            key_sql = ','.join([key_format.format(key_name=key_tuple[0], key_type=key_tuple[1], key_restraint=key_tuple[2]) for key_tuple in key_tuples])
            table_sql = sql_format.format(table_name=table_name, key_sql=key_sql)
            self.cursor.execute(table_sql)

    def drop_table(self, table_name):
        sql_format = 'DROP TABLE IF EXISTS {table_name}'
        table_sql = sql_format.format(table_name=table_name)
        self.cursor.execute(table_sql)

    def insert_item(self, table, item):
        """

        :param table: 存入的表名
        :param item: 列表类型，元素为数据构成的字典
        """
        keys = ', '.join(item.keys())
        values = ', '.join(['%s'] * len(item))
        insert_sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        try:
            if self.cursor.execute(insert_sql, tuple(item.values())):
                # print('Successful')
                self.conn.commit()  # 语句成功执行后再数据库执行
        except Exception as e:
            print('Failed for', e)
            print(item)
            self.conn.rollback()  # 类似于刷新，如果出现错误

    def insert_items(self, table, items):
        """

        :param table: 存入的表名
        :param items: 列表类型，元素为数据构成的字典
        """
        for item in items:
            keys = ', '.join(item.keys())
            values = ', '.join(['%s'] * len(item))
            insert_sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
            try:
                if self.cursor.execute(insert_sql, tuple(item.values())):
                    print('Successful')
                    self.conn.commit()  # 语句成功执行后再数据库执行
            except Exception as e:
                print('Failed for', e)
                self.conn.rollback()  # 类似于刷新，如果出现错误

    def update_price(self, table, cur_price, code):
        update_sql = 'UPDATE {table} SET cur_price = {cur_price}, cur_date = curdate() WHERE code = {code}'.format(table=table, cur_price=cur_price, code=code)
        if self.cursor.execute(update_sql):
            print('Successful')
            self.conn.commit()
        return

    def update_items(self, table, items):
        """

        :param table: 存入更新的表名
        :param items: 列表类型，元素为数据构成的字典
        """
        for item in items:
            keys = ', '.join(item.keys())
            values = ', '.join(['%s'] * len(item))
            update_sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
            update = ','.join([" {key} = %s".format(key=key) for key in item])
            update_sql += update
            try:
                if self.cursor.execute(update_sql, tuple(item.values())):
                    # print('Successful')
                    self.conn.commit()
            except Exception as e:
                print('Failed for', e)
                self.conn.rollback()

    def delete_item(self, table, condition):
        """

        :param table: 数据的表
        :param condition: 删除条件
        """
        delete_sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
        try:
            if self.cursor.execute(delete_sql):
                print('Successful')
                self.conn.commit()
        except Exception as e:
            print('Failed for', e)
            self.conn.rollback()

    def close_cursor(self):
        self.conn.close()

    def fetch_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()


def pre_insert(cursor, sql_tb):
    df_trade = pd.read_csv('trade_info.csv')
    df_trade = pd.read_excel('trade_info.xlsx', converters={'code': str})
    for i, data in df_trade.iterrows():
        cursor.insert_item(sql_tb, dict(data))
        print(data[0])


def get_hold(cursor):
    keys = ['code', 'name', 'hold_vol', 'hold_cost']
    sql = '''select code, name, sum(vol*op_type) as hold_vol, round(sum(vol*price*op_type)/sum(vol*op_type), 4) as hold_cost
             from bounds_trade group by name having sum(vol*op_type) >0'''
    data = cursor.fetch_all(sql)  # 是一个多个元组组成的元组
    print(data)
    
    
def get_price(stock_code):
    qtt = easyquotation.use('sina')
    try:
        info_dict = qtt.real(stock_code)[stock_code]
        now = info_dict['now']
        lst_trade_day = info_dict['date']
    except KeyError:
        today = datetime.date.today()
        lst_day = today if today.weekday() / 4 <= 1 else today - datetime.timedelta(today.weekday() % 4)
        lst_trade_day = lst_day
        now = get_data(s_date=lst_trade_day, e_date=lst_trade_day, b_code=stock_code)['n_price']  # 净价
    col_info = ['code', 'price', 'p_date']
    return dict(zip(col_info, [stock_code, now, lst_trade_day]))


def insert_price(cursor, tb_price):
    sql_code = 'select code from bounds_trade group by name having sum(vol) > 0'
    hold_code = cursor.fetch_all(sql_code)
    for code in hold_code:
        data = get_price(code[0])
        cursor.insert_item(tb_price, data)
    
        
def insert_from_file(cursor, tb_price):
    col_info = ['code', 'price', 'p_date']
    df = pd.read_excel('price_input.xlsx', sheet_name='price_origin', converters={'code': str})
    # df = pd.read_csv('Sheet1.csv')
    for i, data in df.iterrows():
        cursor.insert_item(tb_price, dict(data))
        # 逆回购131800 131810 没有价格
        

def stock_price_backup(cursor, tb_price):
    start = '20190901'
    end = '20191221'
    sql_code = 'select distinct code from bounds_trade'
    all_code = cursor.fetch_all(sql_code)
    sql_code_in = 'select distinct code from {tb_price}'.format(tb_price=tb_price)
    code_in = cursor.fetch_all(sql_code_in)
    code_left = set(all_code) - set(code_in)
    print(code_left)
    col_info = ['code', 'price', 'p_date']
    for code in code_left:
        code = code[0]
        print(code)
        try:
            print('从搜狐爬取！')  # 有缺陷，一些可转债没有信息
            api = 'http://q.stock.sohu.com/hisHq?code=cn_{code}&start={start}&end={end}'.format(code=code, start=start, end=end)
            all_data = requests.get(api).json()[0]['hq']
            for data in all_data:
                date = data[0]
                close = data[2]
                info = dict(zip(col_info, [code, close, date]))
                cursor.insert_item(tb_price, info)
        except KeyError:
            print('从清算所爬取！')
            all_data = get_data(s_date=start, e_date=end, b_code=code)
            for data in all_data:
                close = data['n_price']
                date = data['v_date']
                info = dict(zip(col_info, [code, close, date]))
                cursor.insert_item(tb_price, info)
    

def load_date(cursor, tb_price):
    df = pd.read_excel('trade_date.xlsx', converters={'t_date': str})
    for i, data in df.iterrows():
        cursor.insert_item(tb_price, dict(data))


def main():
    sql_host = 'localhost'
    sql_port = 3306
    sql_user = 'root'
    sql_pwd = '174873'
    sql_db = 'my_trade_info'
    cursor = MysqlPipeline(host=sql_host, port=sql_port, user=sql_user, password=sql_pwd, db=sql_db)
    sql_tb = 'bounds_trade'
    tb_price = 'bounds_price_test'
    # conn = pymysql.connect(host=sql_host, port=sql_port, user=sql_user, passwd=sql_pwd, db=sql_db, charset='utf8')
    load_date(cursor, 'trading_date')
    # cursor.create_database(db_name='test1')  # 连接必须要一个数据库，但是仍然可以创建新数据库，然后切换数据库
    # pre_insert(cursor, sql_tb)
    # info = get_price('002697')
    # insert_price(cursor, tb_price)
    # insert_from_file(cursor, tb_price)
    # stock_price_backup(cursor, tb_price)


if __name__ == '__main__':
    main()
