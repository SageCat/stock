import csv
import json

data = {}

with open('dubai_metro_station_coordinates.csv', encoding='utf-8') as meta_metro_data:
    meta_metro_data_reader = csv.DictReader(meta_metro_data)
    print(type(meta_metro_data_reader))
    # properties = dict([(key, meta_metro_data_reader[key]) for key in ['name']])
    # print(properties)
    for rows in meta_metro_data_reader:
        # print(dict((key, rows[key]) for key in ['type', 'coordinates']))
        # print(rows['type'])
        data['type'] = 'Feature'
        data['geometry'] = dict((key, rows[key]) for key in ['type', 'coordinates'])
        # key = 'geometry'
        data['properties'] = dict((key, rows[key]) for key in ['name'])
        print(rows)
        # print(data)
        with open('output_json.json', 'a', encoding='utf-8') as out_f:
            out_f.write(json.dumps(data))
            out_f.write(',')
