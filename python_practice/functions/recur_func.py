# 函数的嵌套
def outer():
    age = 20
    print("Outer Function")

    def inner():
        print('Inner function')

    inner()
    print('Outer Function after')


outer()
'''
Outer Function
Inner function
Outer Function after
'''

# 命名空间
# 1. 内置命名空间：存放python解释器的内容
# 2. 全局命名空间：存放全局变量
# 3. 局部命名空间：存放局部变量
name = 'sage'
print(globals())
print(locals())

# global声明变量，在函数内强行更改全局变量
source = 100


def add():
    global source  # 强行在函数内更改全局变量
    a = source + 1
    source += 1
    print(source)
    print(a)


add()
print(source)


# nonlocal声明局部变量，强行更改变量
def func1():
    a = 100
    print(a, '>>>>>>>>')

    def func2():
        nonlocal a
        a = a + 1
        print(a)

    func2()
    print(a, '---------------')


func1()
