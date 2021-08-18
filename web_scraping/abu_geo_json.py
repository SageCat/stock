import json

from pandas import json_normalize

with open('test/stanford-by876yk8367-geojson.json', encoding='utf-8') as f:
    data = json.load(f)
    #   获取features列表下的所有字段
    df = json_normalize(data, record_path='features')
    temp = '{"geometry":{"coordinates":' + str(
        df['geometry.coordinates'][0]) + ', "type": "MultiPolygon"}, "properties": {"bbox":' + str(
        df['bbox'][0]) + ',"name": "' + str(df['properties.name_engli'][0]) + '"}, "type": "Feature"}'
    with open('test/temp.txt', 'w') as f1:
        f1.write(temp)
