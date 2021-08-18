import json

from pandas import json_normalize

with open('test/stanford-by876yk8367-geojson.json', encoding='utf-8') as f:
    data = json.load(f)
    #   获取features列表下的所有字段
    df = json_normalize(data, record_path='features')
    # print(df['type'])
    # print(df['id'])
    # print(df['geometry_name'])
    # print(df['bbox'])
    # print(df['geometry.type'])
    # print(df['geometry.coordinates'])
    # print(df['properties.name_engli'])
    # print(df.columns)

    #   通过LineString过滤出area数据
    #     df = df.loc[df['geometry.type'] == 'LineString']
    # #   创建一个临时存放finereport json地图数据的feature List的内容
    temp = '{"geometry":{"coordinates":' + str(
        df['geometry.coordinates'][0]) + ', "type": "MultiPolygon"}, "properties": {"bbox":' + str(
        df['bbox'][0]) + ',"name": "' + str(df['properties.name_engli'][0]) + '"}, "type": "Feature"}'
    with open('test/temp.txt', 'w') as f1:
        f1.write(temp)

# with open('District_Abu Dhabi_20210816.json', encoding='utf-8') as f:
#     data = json.load(f)
#     # print(data)
#     df = json_normalize(data, record_path='features')
#     df = df.loc[df['geometry.type'] == 'LineString']
#     # df.to_csv('afaf.csv', encoding='utf-8')
#     temp_str = '{"geometry":{"coordinates": [[' + str(
#         df['geometry.coordinates']) + ']], "type": "MultiPolygon"}, "properties": {"bbox":[],"name": "' + str(
#         df['properties.name_en']) + '"}, "type": "Feature"}'
#     print(temp_str)
#     print('------')
