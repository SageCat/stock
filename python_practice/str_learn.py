name = "Sage is a good boy"
#
name2 = name.upper()
print(name)
print(name2)

# 字符串长度
print(len(name))  # 18

# [start:end:step]
print(name[1:5:2])  # ae
print(name[15:2:-3])  # bo se

# strip() 去掉字符串两边的空格
# split() 切字符串成为一个列表
# join() 将列表组合成字符串
# startswith() 字符串以‘’开头
# endswith() 字符串以‘’结尾
'''
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isal
num', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', '
isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lo
wer', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
 'swapcase', 'title', 'translate', 'upper', 'zfill'
'''

print(dir(str))
