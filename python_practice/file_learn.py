# 读取文件
with open("test.csv", mode="r", encoding='utf-8') as f:
    # 读取全部内容
    # print(f.read())
    # 读取一行
    # print(f.readline())
    # 循环读，且先读取第一行
    print(f.readline(), end='')
    print("<<<<<<<<<<<<<")
    for i in f:
        print(i, end='')

# 向文件写数据, mode='w',写之前将文件清空      mode='a',追加数据
with open("write.txt", mode='w', encoding='utf-8') as w:
    w.write('I like Dubai City')
    w.write("I like China")

# 读取文件字节数据，写入文件字节数据
with open("read_pic.png", 'rb') as read_pic, open('write_pic.png', 'wb') as write_pic:
    # write_pic.write(read_pic.read())
    for i in read_pic:
        write_pic.write(i)