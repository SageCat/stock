city_dict = {"Dubai": "UAE", "Beijing": "China", "Shanghai": "China", "New York": "USA", "London": "UK"}


# 根据key获取value
print(city_dict["Beijing"])
'''
China
'''
# 1. 添加数据
city_dict["Paris"] = "France"
print(city_dict)
'''
{'Dubai': 'UAE', 'Beijing': 'China', 'Shanghai': 'China', 'New York': 'USA', 'London': 'UK', 'Paris': 'France'}
'''

print(city_dict.setdefault('Chongqing', 'China'), end='>>>>>')  # setdefault()执行完操作后会执行查询操作并返回value的值
print()
'''
China>>>>>
'''
print(city_dict)
'''
{'Dubai': 'UAE', 'Beijing': 'China', 'Shanghai': 'China', 'New York': 'USA', 'London': 'UK', 'Paris': 'France', 'Chongqing': 'China'}
'''

# 2. 修改数据
city_dict['Beijing'] = '中国'
print(city_dict)
'''
{'Dubai': 'UAE', 'Beijing': '中国', 'Shanghai': 'China', 'New York': 'USA', 'London': 'UK', 'Paris': 'France', 'Chongqing': 'China'}
'''

# 3. 查询
print(city_dict.get('Beijing', '不存在key'))
print(city_dict.get('Guangzhou', '不存在key'))

print(city_dict['Beijing'])

# 4. 删除数据
city_dict.pop('Beijing')
print(city_dict)
'''
{'Dubai': 'UAE', 'Shanghai': 'China', 'New York': 'USA', 'London': 'UK', 'Paris': 'France', 'Chongqing': 'China'}
'''

city_dict.clear()  # 清空数据
print(city_dict)
'''
{}
'''

# setdefault(key, value) 如果不存在key，则新增，如果存在key,则不进行操作
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = {}

for i in lst:
    if i > 5:
        result.setdefault('big', []).append(i)
    else:
        result.setdefault('small', []).append(i)
print(result)
'''
{'small': [1, 2, 3, 4, 5], 'big': [6, 7, 8, 9, 10]}
'''

print(type((10, 20)))  # <class 'tuple'>
a, b = (10, 20)  # 元组的解构
print(a)
print(b)
'''
10
20
'''

# 遍历字典
for k, v in result.items():
    print(k, v)
'''
small [1, 2, 3, 4, 5]
big [6, 7, 8, 9, 10]
'''
print(result.keys())
print(type(result.keys()))
'''
dict_keys(['small', 'big'])
'''
print(result.values())
print(type(result.values()))
'''
dict_values([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
'''
