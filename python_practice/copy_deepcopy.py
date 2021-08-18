import copy

a = 10  # 第一个对象
b = a  # 第一个对象
print(id(a), id(b))  # 两个ID相等
a = 20  # 生成了第二个对象
print(id(a), id(b))  # 两个ID不等
print(a, b)
print('____________________')

name1 = {'A', 'B', 'C'}
name2 = name1
print(id(name1), id(name2))  # 两个ID相等，是同一个对象
name1.add('D')
print(id(name1), id(name2))  # 两个ID相等，是同一个对象
print(name1, name2)

print('____________________')

name3 = {'A', 'B', 'C'}
name4 = name3.copy()
print(id(name3), id(name4))  # 两个ID不等，是2个对象
name3.add('D')
print(id(name3), id(name4))  # 两个ID不等，是2个对象
print(name3, name4)

print('____________________')

name5 = ['A', 'B', 'C', ['D', 'E']]
name6 = name5.copy()  # 浅copy
print(id(name5), id(name6))  # 两个ID不等，是2个对象
print(name5, name6)
name5[3].append('F')
name5.append('H')
print(id(name5), id(name6))  # 两个ID不等，是2个对象
print(name5, name6)

print('____________________')

name7 = ['A', 'B', 'C', ['D', 'E']]
name8 = copy.deepcopy(name7)  # 深copy
print(id(name7), id(name8))  # 两个ID不等，是2个对象
print(name7, name8)
name7[3].append('F')
name7.append('H')
print(id(name7), id(name8))  # 两个ID不等，是2个对象
print(name7, name8)
