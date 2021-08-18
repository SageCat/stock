# 列表和字典循环时不能删除
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in list1:
    if i in [2, 3, 4]:
        pass
        # list1.remove(i)
print(list1)
'''
[1, 3, 5, 6, 7, 8, 9]
结果不是期望的值，删除元素后，后面的元素会前置一位，因此循环列表的过程中不要删除元素，否则会导致结果不是期望的数值
'''

# 删除操作的正确方法：把要删除的内容记录到一个新的列表中，然后再根据新列表中的数据，去旧的列表删除数据
deleted_value = []
for i in list1:
    if i in [2, 3, 4]:
        deleted_value.append(i)

for i in deleted_value:
    list1.remove(i)
print(deleted_value)
print(list1)

city_list = ['Beijing', 'Shanghai', 'Chongqing', 'Shenzhen', 'Shijiazhuang', 'Shihezi', 'Shijingshan']
for i in city_list[:]:  # copy了一个city_list列表
    if i.startswith('S') or i.startswith('B'):
        city_list.remove(i)
print(city_list)

print(id(city_list[:]))
print(id(city_list))
'''
2782259525888
2782259516736
'''
