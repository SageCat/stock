import re
import urllib.request as request

url = "https://zh.wikipedia.org/wiki/%E5%9C%8B%E9%9A%9B%E5%A5%A7%E5%A7%94%E6%9C%83%E5%9C%8B%E5%AE%B6%E7%B7%A8%E7%A2%BC%E5%88%97%E8%A1%A8"

source_code = request.urlopen(url).read().decode('utf-8')

noc_list = re.findall(r'"center"><tt>(.*?)</tt>', source_code)
# noc_chinese_list = re.findall(r'">([\u4e00-\u9fa5]+)</a>[a-z0-9/<>]*</td>', source_code)
noc_chinese_list = re.findall(r'">([\u4e00-\u9fa5]+)</a>[a-z0-9/<>]*</td>', source_code)
noc_number = re.findall(r'\[([0-9]+)]', source_code)

# 当前奥委会代码
for i in range(0, 208):
    print(noc_list[i], '-', noc_chinese_list[i])

# 仍然使用部分
still_using_noc_list = re.findall(r'<td><tt>([A-Z0-9]{3})</tt></td>', source_code)
for i in range(208, 208 + len(still_using_noc_list)):
    print(still_using_noc_list[i - 208], '-', noc_chinese_list[i])

# 特殊代码
for i in range(208, len(noc_list)):
    print(noc_list[i], '-', noc_chinese_list[i + len(still_using_noc_list)+1])
