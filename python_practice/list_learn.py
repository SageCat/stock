list_number = list(range(1, 4))
print(list_number)

for i in list_number:
    print(i,end='>>')

for i in range(len(list_number)):
    print(i) #获取索引
    print(list_number[i]) #获取元素