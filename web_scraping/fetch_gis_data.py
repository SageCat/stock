import json

from pandas import json_normalize

with open('District_Abu Dhabi_20210816.json', encoding='utf-8') as f:
    data = json.load(f)
    #   获取features列表下的所有字段
    df = json_normalize(data, record_path='features')
    #   通过LineString过滤出area数据
    df = df.loc[df['geometry.type'] == 'LineString']

    coordinate_list = list(df['geometry.coordinates'])
    max_latitude = []
    min_latitude = []
    max_longitude = []
    min_longitude = []
    center_point = []

    for i in coordinate_list:
        temp_latitude = []
        temp_longitude = []
        for j in i:
            temp_latitude.append(j[0])
            temp_longitude.append(j[1])
        max_latitude.append(max(temp_latitude))
        min_latitude.append(min(temp_latitude))
        max_longitude.append(max(temp_longitude))
        min_longitude.append(min(temp_longitude))
        # print()
        temp_str = '[' + str((max(temp_longitude) + min(temp_longitude)) / 2) + ',' + str(
            (max(temp_latitude) + min(temp_latitude)) / 2) + ']'
        center_point.append(temp_str)
    df['max_latitude'] = max_latitude
    df['min_latitude'] = min_latitude
    df['max_longitude'] = max_longitude
    df['min_longitude'] = min_longitude
    df['center_point'] = center_point

    #   创建一个临时存放finereport json地图数据的feature List的内容
    temp_str = []
    for i, j, k in zip(df['geometry.coordinates'], df['properties.name_en'], df['center_point']):
        #         print(str(i),j)
        temp_str.append('{"type":"Feature", "geometry":{"type":"MultiPolygon","coordinates": [[' + str(
            i).replace(' ', '') + ']]}, "properties":{"bbox":[],"name":"' + j + '"}}')
    #         temp_str.append('{"type":"Feature", "geometry":{"type":"MultiPolygon","coordinates": [[' + str(i) + ']]}, "properties":{"bbox":[],"name":"' + j + '","center":'+ k +'}}')
    df['district'] = temp_str

new_df = df['district']
temp = ''
for i in new_df:
    temp = temp + i + ','
print(temp)
