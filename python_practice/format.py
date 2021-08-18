json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    },
    'students': [
        {'name': 'Tom'},
        {'name': 'James'},
        {'name': 'Jacqueline'}
    ],
}
json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    },
    'students': [
        {'name': 'Tom'},
        {'name': 'James'},
        {'name': 'Jacqueline'}
    ],
}

json_obj = {
    'school': 'ABC primary school',
    'location': 'shenzhen',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    },
    'students': [
        {'name': 'Tom'},
        {'name': 'James'},
        {'name': 'Jacqueline'}
    ],
    # 添加university嵌套列表，加上students,该JSON对象中就有2个嵌套列表了
    'university': [
        {'university_name': 'HongKong university shenzhen'},
        {'university_name': 'zhongshan university shenzhen'},
        {'university_name': 'shenzhen university'}
    ],
}
# 尝试在record_path中写上两个嵌套列表的名字，即record_path = ['students', 'university],结果无济于事
# 于是决定分两次进行解析，分别将record_path设置成为university和students,最终将2个结果合并起来
df1 = pd.json_normalize(json_obj, record_path=['university'],
                        meta=['school', 'location', ['info', 'contacts', 'tel'],
                              ['info', 'contacts', 'email', 'general']],
                        record_prefix='university->',
                        meta_prefix='meta->',
                        sep='->')
df2 = pd.json_normalize(json_obj, record_path=['students'],
                        meta=['school', 'location', ['info', 'contacts', 'tel'],
                              ['info', 'contacts', 'email', 'general']],
                        record_prefix='students->',
                        meta_prefix='meta->',
                        sep='->')
# 将两个结果合并起来并去除重复列
df1.merge(df2, how='left', left_index=True, right_index=True, suffixes=['->', '->']).T.drop_duplicates().T
