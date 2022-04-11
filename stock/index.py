import json
import re
import requests
import pandas as pd
from sqlalchemy import create_engine
import pymysql


# 获取股票代码
def get_stock_code():
    url = "http://67.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124013120183602820856_1649615623910&pn=1&pz=5000&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1649615623911"
    r = requests.get(url)
    pattern = '\{"f1".*?\}'
    temp_text = re.compile(pattern, re.S).findall(r.text)
    stock_list = []
    for i in temp_text:
        temp_dict = json.loads(i)
        stock_list.append(temp_dict["f12"])
    return stock_list


# 获取行业 URL
def get_data(stock_code):
    valid_data = []
    url = ""
    for code in stock_code:
        if str(code).startswith("60"):
            url = "http://push2.eastmoney.com/api/qt/stock/get?ut=fa5fd1943c7b386f172d6893dbfba10b&invt=2&fltt=2&fields=f43,f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f260,f261,f262,f263,f264,f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,f193,f196,f194,f195,f197,f80,f280,f281,f282,f284,f285,f286,f287,f292,f293,f181,f294,f295,f279,f288&secid=1." + str(
                code) + "&wbp2u=|0|0|0|web&cb=jQuery112406820703191275046_1649614900618&_=1649614900619"
        else:
            url = "http://push2.eastmoney.com/api/qt/stock/get?ut=fa5fd1943c7b386f172d6893dbfba10b&invt=2&fltt=2&fields=f43,f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f260,f261,f262,f263,f264,f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,f193,f196,f194,f195,f197,f80,f280,f281,f282,f284,f285,f286,f287,f292,f293,f181,f294,f295,f279,f288&secid=0." + str(
                code) + "&wbp2u=|0|0|0|web&cb=jQuery112406820703191275046_1649614900618&_=1649614900619"
        r = requests.get(url)
        pattern = '\((.*?)\)'
        temp_text = re.compile(pattern, re.S).findall(r.text)
        temp_dic = json.loads(temp_text[0])
        if temp_dic['rc'] == 0:
            valid_data.append(temp_dic['data'])
            print(temp_dic['data'])
    return valid_data


def handle_data(data_list):
    table_column_list = {"f80": "日期", "f71": "均价", "f60": "昨收", "f44": "最高", "f45": "最低", "f104": "总营收", "f116": "总市值",
                         "f84": "总股本", "f193": "主力净比", "f196": "中单净比", "f51": "涨停", "f170": "涨幅", "f169": "涨跌",
                         "f184": "营收同比", "f127": "行业名称", "f197": "小单净比", "f192": "委差", "f191": "委比", "f49": "外盘",
                         "f55": "收益", "f167": "市净率", "f189": "上市日期", "f190": "每股未分配利润", "f92": "每股净资产", "f186": "毛利率",
                         "f117": "流通市值", "f85": "流通股数", "f50": "量比", "f163": "静态市盈率", "f185": "净利润同比", "f105": "净利润",
                         "f187": "净利率", "f137": "今日主力净流入", "f146": "今日中单净流入", "f149": "今日小单净流入", "f143": "今日大单净流入",
                         "f140": "今日超大单净流入", "f46": "今开", "f168": "换手率", "f164": "滚动市盈率", "f58": "股票名称", "f57": "股票代码",
                         "f188": "负债率", "f162": "动态市盈率", "f52": "跌停", "f128": "地域板块名称", "f43": "当日价格", "f195": "大单净比",
                         "f47": "成交量", "f48": "成交额", "f194": "超大单净比", "f173": "ROE"}

    df = pd.DataFrame(columns=table_column_list.values())

    for row in data_list:
        enhanced_data = []
        for key in table_column_list.keys():
            if key == "f80":
                enhanced_data.append(str(json.loads(row[key])[0]["b"])[0:8])
            else:
                enhanced_data.append(row[key])
        df.loc[len(df)] = enhanced_data
        print(enhanced_data)

    df = df.replace(['-'], 0)
    # create sqlalchemy engine
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user="root",
                                   pw="12345678",
                                   db="stock"))
    res = df.to_sql('daily_stock_data', con=engine, if_exists='append', chunksize=1000, index=False)
    print(res)


if __name__ == '__main__':
    handle_data(get_data(get_stock_code()))
