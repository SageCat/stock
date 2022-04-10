import json
import re
import time

import requests


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
        # time.sleep(1)
        print(url)
        print(code)
        temp_text = re.compile(pattern, re.S).findall(r.text)
        temp_dic = json.loads(temp_text[0])
        if temp_dic['rc'] == 0:
            valid_data.append(temp_dic)
        print(temp_dic)
    return valid_data


if __name__ == '__main__':
    # url_postfix = get_html()
    # print(url_postfix)
    get_data(get_stock_code())
