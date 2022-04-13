import _thread
import json
import random
import re
import time
import pandas as pd
import requests
from sqlalchemy import create_engine


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
def get_data(stock_code, thread_name):
    user_agents = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
    ]

    proxies = [
        {'http': 'socks5://127.0.0.1:10808'},
        # {'https': 'socks5://127.0.0.1:10808'},
        {'http': 'http://127.0.0.1:10809'}
        # {'https': 'http://127.0.0.1:10809'}
    ]

    valid_data = []
    url = ""
    for code in stock_code:
        if str(code).startswith("60"):
            url = "http://push2.eastmoney.com/api/qt/stock/get?ut=fa5fd1943c7b386f172d6893dbfba10b&invt=2&fltt=2&fields=f43,f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f260,f261,f262,f263,f264,f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,f193,f196,f194,f195,f197,f80,f280,f281,f282,f284,f285,f286,f287,f292,f293,f181,f294,f295,f279,f288&secid=1." + str(
                code) + "&wbp2u=|0|0|0|web&cb=jQuery112406820703191275046_1649614900618&_=1649614900619"
        else:
            url = "http://push2.eastmoney.com/api/qt/stock/get?ut=fa5fd1943c7b386f172d6893dbfba10b&invt=2&fltt=2&fields=f43,f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f260,f261,f262,f263,f264,f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,f193,f196,f194,f195,f197,f80,f280,f281,f282,f284,f285,f286,f287,f292,f293,f181,f294,f295,f279,f288&secid=0." + str(
                code) + "&wbp2u=|0|0|0|web&cb=jQuery112406820703191275046_1649614900618&_=1649614900619"
        # time.sleep(random.randint(5, 10))
        time.sleep(1)
        # r_code = 200

        try:
            random_proxies = random.choice(proxies)
            random_agent = user_agents[random.randint(0, len(user_agents) - 1)]
            headers = {
                'User-Agent': random_agent,
            }
            # print(proxies)
            r = requests.get(url, proxies=random_proxies, headers=headers)
            # print(thread_name, '-', r.status_code, ">>>>>>>>>>")
            pattern = '\((.*?)\)'
            temp_text = re.compile(pattern, re.S).findall(r.text)
            temp_dic = json.loads(temp_text[0])
            if temp_dic['rc'] == 0:
                valid_data.append(temp_dic['data'])
                print(thread_name, '-', temp_dic['data'])
        except IndexError as e:
            print(e)
        except ConnectionResetError as e:
            print(e)
        except ConnectionError as e:
            print(e)
        except IOError as e:
            print(e)
        except json.JSONDecodeError as e:
            print(e)
    return valid_data


def handle_data(thread_name, i):
    stock_code_list = get_stock_code()
    # print(get_data(stock_code_list[0:2]))
    start = (i - 1) * 50
    end = i * 50
    data_list = get_data(stock_code_list[start:end], thread_name)

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
        # print(thread_name, '-', enhanced_data)

    df = df.replace(['-'], 0)

    res = df.to_sql('daily_stock_data', con=engine, if_exists='append', chunksize=100, index=False)
    print(thread_name, res)
    result_response[str(thread_name)] = res


if __name__ == '__main__':

    result_response = {}
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user="root",
                                   pw="123456",
                                   db="stock"))
    for i in range(1, 100):
        try:
            _thread.start_new_thread(handle_data, ('Thread-' + str(i), i))
        except:
            print("无法启动线程")

    while 1:
        if len(result_response) == 10:
            break
