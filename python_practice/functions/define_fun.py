# 有一个返回值的函数
def sum(a, b):
    return a + b


result = sum(2, 3)
print(type(result))
print(result)
'''
<class 'int'>
5
'''


# 有多个返回值的函数
def name_list():
    return 'Lily', 'Bob', 'Tom'


names = name_list()
print(type(names))
print(names)
'''
函数有多个返回值时，返回的是一个元组 tuple
<class 'tuple'>
('Lily', 'Bob', 'Tom')
'''


# 参数  形参: chat_tool    实参：微信，陌陌等
def date_with(chat_tool):  # 形参，也叫关键字参数
    print('1. 打开手机')
    print(f'2. 打开{chat_tool}聊天软件')
    print('3. 我们见面吧')
    print(f'4. 我就是咱们通过{chat_tool}联系上的那个人')


date_with('微信')  # 实参
'''
1. 打开手机
2. 打开微信聊天软件
3. 我们见面吧
4. 我就是咱们通过微信联系上的那个人
'''
date_with('陌陌')  # 实参
'''
1. 打开手机
2. 打开陌陌聊天软件
3. 我们见面吧
4. 我就是咱们通过陌陌联系上的那个人
'''


# 位置参数
def print_numbers(a, b, c):
    print(a, b, c)


print_numbers(2, 3, 4)
print_numbers(4, c=10, b=0)


# 默认值参数的值是可变数据类型
def fun(val, lst=[]):
    lst.append(val)
    print(lst)


fun(100000, [30000])
fun(200000, [])


# 动态传参1  *food 动态接受位置参数
def eat_food(*food):
    print(food)


eat_food('冰淇淋', '煎饼果子', '驴肉火烧', '冰可乐')
'''
('冰淇淋', '煎饼果子', '驴肉火烧', '冰可乐')  是一个元组
'''


# 动态参数2 **food 接收到的是一个字典
def eat_good_food(**food):
    print(food)


eat_good_food(main_food="馒头", sub_food="饮料", food_type="中国餐")
'''
{'main_food': '馒头', 'sub_food': '饮料', 'food_type': '中国餐'}  是一个字典
'''


# 形参：
# 1. 位置参数  a
# 2. 默认值参数  a=100
# 3. 动态传参
# 4. 混合使用顺序：位置参数,*args , 默认值参数,**kwargs

def mix_func(a, *args, b=100, **kwargs):
    print(a, args, b, kwargs)


def any_args_func(*args, **kwargs):
    print(args, kwargs)


mix_func(100, 200, 300, 400, name='sage', age=23)
'''
100 (200, 300, 400) 100 {'name': 'sage', 'age': 23}
'''
any_args_func(100, 200, 300, name='sage', age=23, work='BI')
'''
(100, 200, 300) {'name': 'sage', 'age': 23, 'work': 'BI'}
'''

# 实参：
# 1. 位置参数
# 2. 关键字参数
# 3. 混合参数，先位置，后关键字
