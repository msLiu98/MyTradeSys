import requests
import time
import datetime
import pprint


def func_timer(function):
    """
    计时装饰器
    :param function: 待计时函数
    :return: 函数结果
    """
    def function_timer(*args, **kwargs):
        print('[Function: {name} start...]'.format(name=function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('[Function: {name} finished, spent time: {time:.2f}s]'.format(name=function.__name__, time=t1 - t0))
        return result
    return function_timer


def get_info(d_dict):
    b_code = d_dict['bondcode']
    b_abbr = d_dict['bondAbbr']
    v_date = d_dict['vdate']
    ed_flp = d_dict['edayfullprice']  # 日终估价全价
    ed_inst = d_dict['edayaccruedinterest']  # 日终应计利息
    n_price = d_dict['estimatenetprice']  # 估价净价
    # b_type = d_dict['proLittleTypeName']
    # b_type_id = d_dict['proLittleTypeId']  # 这个是查询的时候用
    # cir_place = d_dict['circulationplace']
    col_info = ['b_code', 'b_abbr', 'v_date', 'ed_flp', 'ed_inst', 'n_price']
    return dict(zip(col_info, [b_code, b_abbr, v_date, ed_flp, ed_inst, n_price]))


@func_timer
def get_data(s_date=datetime.date.today(), e_date=datetime.date.today(), b_code="143818"):
    url = 'http://www.shclearing.com/shchapp/web/valuationclient/findvaluationdata'
    s_date = '20190901'
    e_date = '20191221'
    # TODO:cookies 需要改
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "927",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": 'HDSESSIONID=0c04a26a-ffaa-4a58-9c19-374e7461493a; Hm_lvt_d885bd65f967ea9372fc7200bc83fa81=1573901851,1573983399,1575869692,1576112074; Hm_lpvt_d885bd65f967ea9372fc7200bc83fa81=1576112857',
        "Host": "www.shclearing.com",
        "Origin": "http://www.shclearing.com",
        "Referer": "http://www.shclearing.com/cpgz/zqjqysp/zqgz/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    data_list = list()
    for i in range(2):
        form_data = {
            "startTime": s_date,
            "endTime": e_date,
            "bondNames": "",
            "bondCodes": b_code,
            "bondTypes": '402880e5438a816001438a8317730007,4028228167b039d70167f462b891166d,402880e5438a816001438a835ab60009,402880e5438a816001438a82ed5d0006,40289581497587b201497dc6f3d22411,402880e5438a816001438a82cb790005,402880e5438a816001438a839dbb000b,402880e5438a816001438a837f12000a,402880e5438a816001438a82a38f0004,402880e5438a816001438a8273c20003,402880e5438a816001438a833adf0008,ff80808146c9b061014734543a50101f,40289581538a88d60154efee4f657e21,402895815b6f2ffd015bd206344d26bd,402852816c9e6e15016cae4668860ed7,402852816d4fdabc016d5c02fba70208,402895815e88bc79015f00cc5ba65c26,402895815e88bc79015f00cc85035c27,402895815c8fa1ac015d400a02735729,402895815c8fa1ac015d400a4672572a,402895815c8fa1ac015d400a7c08572b,4028958158e66bc401593ab642012e41,4028958158e66bc401593ab664802e46,402880f0437b131f01437b1c606b0003',
            "limit": "60",
            "start": "{start}".format(start=i*60),
            "sortFlag": "1",
            "sortNameFlag": "1",
            "sortDateFlag": "1",
        }
        r = requests.post(url=url, data=form_data, headers=headers)
        print(r.status_code)
        r.encoding = r.apparent_encoding
        js_obj = r.json()
        d_list = js_obj['data']['datas']
        for d_dict in d_list:
            d_info = get_info(d_dict)
            data_list.append(d_info)
    return data_list


def main():
    info = get_data(b_code='1828001')
    for d in info:
        print(d['n_price'])


if __name__ == '__main__':
    main()
