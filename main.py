#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 作者：刘明朔
# 时间：
# 邮箱：mingshuoliu98@163.com
import sys
from PyQt5 import QtWidgets
from form import Ui_Form
from pipeline_mysql import MysqlPipeline
from get_value import get_data
import easyquotation
import datetime
from tkinter.filedialog import *
import os
import pandas as pd


class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):
    sql_host = 'localhost'
    sql_port = 3306
    sql_user = 'root'
    sql_pwd = '174873'
    sql_db = 'my_trade_info'
    sql_tb = 'bounds_trade'
    ready = False

    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)
        self.cursor = MysqlPipeline(host=self.sql_host, port=self.sql_port, user=self.sql_user, password=self.sql_pwd, db=self.sql_db)
        self.lst_day = self._lst_day()

    @staticmethod
    def _lst_day():
        today = datetime.date.today()
        lst_day = today if today.weekday()/4 <= 1 else today - datetime.timedelta(today.weekday() % 4)
        return lst_day
    
    def _init_db(self):
        # self.cursor.create_database(self.sql_db)
        # self.cursor.change_database(self.sql_db)
        key_tuples = [
            ('op_id', 'INT', 'PRIMARY KEY AUTO_INCREMENT'),
            ('code', 'VARCHAR(255)', 'NOT NULL'),
            ('name', 'VARCHAR(255)', 'NOT NULL'),
            ('type', 'VARCHAR(255)', 'NOT NULL'),
            ('op_date', 'date', 'NOT NULL'),
            ('op_type', 'int', 'NOT NULL'),
            ('vol', 'INT', 'NOT NULL'),
            ('price', 'FLOAT', 'NOT NULL'),
        ]
        self.cursor.create_table(table_name=self.sql_tb, key_tuples=key_tuples)
        self.textEdit.setText("已创建数据库和表")

    def _test(self):
        self.textEdit.setText("你点击了按钮")

    def to_update(self):
        sql = '''select code, name, type from bounds_hold group by name having cur_price = Null; '''
        data = self.cursor.fetch_all(sql)
        return

    def update_price(self):
        tb = 'bounds_hold'
        code = self.line_code_price.text()
        price = float(self.line_curPrice.text())
        self.cursor.update_price(table=tb, code=code, cur_price=price)
        self.textEdit_2.setText('\t'.join([code, str(price), 'done!']))
        return

    def backup_price(self):
        backup_tb = 'backup_price'
        clear_sql = 'truncate {tb};'.format(tb=backup_tb)
        self.cursor.execute(clear_sql)
        update_sql = 'insert into {tb} select code, name, cur_price, cur_date from bounds_hold;'.format(tb=backup_tb)
        self.cursor.execute(update_sql)
        self.textEdit_2.setText('Already backup!')
        return

    def update_ready(self):
        clear_sql = '''truncate table bounds_hold;'''
        self.cursor.execute(clear_sql)
        sql = '''select code, name, type, sum(vol*op_type) as hold_vol, round(sum(vol*price*op_type)/sum(vol*op_type), 4) as hold_cost, curdate() as cur_date
                             from bounds_trade group by name having sum(vol*op_type) >0'''
        data = self.cursor.fetch_all(sql)
        keys = ['code', 'name', 'type', 'hold_vol', 'hold_cost', 'cur_date']
        for i, line in enumerate(data):
            info_dict = dict(zip(keys, line))
            code = line[0]
            price = self.get_price(code)
            info_dict['cur_price'] = price
            self.cursor.insert_item(table='bounds_hold', item=info_dict)
        self.textEdit_2.setText('Yes, I\'m ready！')
        return

    def update_hold(self):
        sql = '''select code, name, type, hold_vol, hold_cost, cur_date, cur_price from bounds_hold'''
        data = self.cursor.fetch_all(sql)
        self.tableWidget.setRowCount(len(data))
        for i, line in enumerate(data):
            for j, info in enumerate(line):
                item = QtWidgets.QTableWidgetItem(str(info))
                self.tableWidget.setItem(i, j, item)
        return

    def show_hold(self):
        sql = '''select code, name, type, sum(vol*op_type) as hold_vol, round(sum(vol*price*op_type)/sum(vol*op_type), 4) as hold_cost, curdate() as cur_date
                     from bounds_trade group by name having sum(vol*op_type) >0'''
        data = self.cursor.fetch_all(sql)
        self.tableWidget.setRowCount(len(data))
        # keys = ['code', 'name', 'type', 'hold_vol', 'hold_cost', 'cur_date', 'cur_price']
        for i, line in enumerate(data):
            for j, info in enumerate(line):
                item = QtWidgets.QTableWidgetItem(str(info))
                self.tableWidget.setItem(i, j, item)
            code = line[0]
            price, lst_trade_day = self.get_price(code)
            item_price = QtWidgets.QTableWidgetItem(str(price))
            self.tableWidget.setItem(i, len(line), item_price)
            item_trade_day = QtWidgets.QTableWidgetItem(str(lst_trade_day))
            self.tableWidget.setItem(i, len(line)+1, item_trade_day)
        print('done!')

    def entry(self):
        scr_info = {
            'code': '',
            'name': '',
            'type': '',
            'op_date': '',
            'op_type': 0,
            'vol': '',
            'price': '',
        }
        op_type = {
            '买入': 1,
            '卖出': -1
        }
        scr_info['code'] = self.line_code.text()
        scr_info['name'] = self.line_name.text()
        scr_info['type'] = self.comboBox_type.currentText()
        scr_info['op_date'] = self.line_date.text()
        scr_info['op_type'] = op_type[self.comboBox_op_type.currentText()]
        scr_info['vol'] = self.line_vol.text()
        scr_info['price'] = self.line_price.text()
        try:
            self.cursor.insert_item(self.sql_tb, scr_info)
            self.textEdit.setText("成功插入一条交易记录")
        except Exception as e:
            self.textEdit.setText(e)
    
    def get_files(self):
        initial_dir = r'D:\刘明朔的文件夹\学习—大学学习资料\大3（上）资料合集\固收 吴文锋'
        f_name = askopenfilename(initialdir=initial_dir)
        # f_dir = askdirectory()
        self.label.setText(f_name)
        # files = os.listdir(f_name)
        # for file_name in files:
        #     self.comboBox.addItem(file_name)
        df = pd.read_excel(f_name)
        self.tableWidget_insert.setRowCount(len(df))
        for i, row in df.iterrows():
            for j, info in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(info))
                self.tableWidget_insert.setItem(i, j, item)
                
    def get_price(self, stock_code):
        qtt = easyquotation.use('sina')
        try:
            info_dict = qtt.real(stock_code)[stock_code]
            now = info_dict['now']
            lst_trade_day = info_dict['date']
        except KeyError:
            lst_trade_day = self.lst_day
            now = get_data(s_date=lst_trade_day, e_date=lst_trade_day, b_code=stock_code)['ed_flp']
        return now, lst_trade_day

    # TODO 功能未实现：
    #   收益率计算
    #   各类型债券收益率统计
    #   债券估值api接口：http://www.shclearing.com/shchapp/web/valuationclient/findvaluationdata


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
