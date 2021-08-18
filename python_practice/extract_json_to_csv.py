import json

from pandas import json_normalize

with open("Dubai Metro.json", encoding='utf8') as f:
    all_data = json.load(f)
    df = json_normalize(all_data, record_path='features', meta=['type','imageSuffix','imageWidth','imageHeight'], record_prefix='features.')
    print(df)
    df.to_csv('metro.csv', index=False)

'''
    # ['defaultDimension', 'Region'], ['defaultDimension', 'Gender'], ['defaultDimension', 'Cluster'], ['defaultDimension', 'Country'], ['defaultDimension', 'Sector']
    df1 = json_normalize(all_data, record_path=['targets'],
                         meta=['id', 'strategyId', 'categoryId', 'relatedInitiatives', 'name', 'lastUpdated',
                               'updateFrequency', 'dataSource', 'calculationMethodology', 'criticality'],
                         record_prefix='targets->', sep='->', errors='ignore',
                         max_level=2)

    df2 = json_normalize(all_data, record_path=['data'],
                         meta=['id', 'strategyId', 'categoryId', 'relatedInitiatives', 'name', 'lastUpdated',
                               'updateFrequency', 'dataSource', 'calculationMethodology', 'criticality'],
                         record_prefix='data->', sep='->', errors='ignore', max_level=2)

    df = df2.append(df1)
    cols = df.columns.tolist()
    cols = cols[17:28] + cols[0:17] + cols[28:]
    df = df[cols]
    df = df.sort_values('id')
    df.to_csv('hcl.csv', index=False)
'''
