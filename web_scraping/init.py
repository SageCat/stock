import re

import requests
from bs4 import BeautifulSoup as bs

'''
# Load the web page content
result = requests.get("https://en.m.wikipedia.org/wiki/List_of_IOC_country_codes")
# Convert into beautifulsoup objects
soup = bs(result.content, features="html.parser")
# print html content
soup.prettify()

noc_table = soup.find("table", attrs={"class": "wikitable sortable"})
noc_data = noc_table.find_all("span", attrs={"class": "monospaced"})
# country_data = noc_table.find_all("a", attrs={"title": re.compile("[a-zA-Z] at the (Olympics|Paralympics)]")})
# print(country_data)
country_code = soup.select(".monospaced")
country_name = soup.select('a[title*= " at the "]')

print(len(country_code))
print(country_name)
for i, j in zip(country_code, country_name):
    pass
    # print(type(i))
    print(i.string, j.string)
    # print(re.findall())
'''

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia?scene=2&clicktime=1579579384&enterid=1579579384&from=groupmessage&isappinstalled=0'
r = requests.get(url)
context = r.content.decode('utf-8')
# print(context)
source_data = re.findall('\[(.*?)]', context)
for i in source_data:
    print(  i)
