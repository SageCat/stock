import pandas as pd
import requests

columns_name = {'geometry.coordinates': 'coordinates',
                'properties.District': 'district_name_en',
                'properties.BuildingName': 'building_name_en',
                'properties.DateoftheLastCase': 'date_of_the_last_case',
                'properties.地區': 'district_name_cn',
                'properties.大廈名單': 'building_name_cn',
                'properties.FirstReportedDate': 'first_reported_date',
                'properties.相關確診個案': 'related_cases'}

s = 1
e = 20000
points_list = []
while True:
    url = "https://services8.arcgis.com/PXQv9PaDJHzt8rp0/arcgis/rest/services/StayBuildingWithHistory_0227_test_View/FeatureServer/0/query?where=OBJECTID+BETWEEN+{START}+AND+{END}&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token="
    url = url.format(START=s, END=e)
    response = requests.get(url).json()
    temp = response['features']
    if len(temp) != 0:
        s = s + 20000
        e = e + 20000
    else:
        break
    points_list.append(temp)

result_pd = pd.DataFrame(columns=columns_name.values())

for point in points_list:
    temp = pd.json_normalize(point)
    temp = temp.rename(columns=columns_name)
    temp = temp[columns_name.values()]
    temp.replace('nan', 0)
    temp['date_of_the_last_case'] = pd.to_datetime(temp['date_of_the_last_case'], unit='ms')
    temp['first_reported_date'] = pd.to_datetime(temp['first_reported_date'], unit='ms')
    result_pd = pd.concat([result_pd, temp])

result_pd['case_num'] = result_pd['related_cases'].str.split(',').map(len, na_action='ignore')

coordinates_temp = result_pd['coordinates'].apply(lambda x: pd.Series(x))
coordinates_temp.columns = ['Longitude', 'Latitude']
result_pd['Longitude'] = coordinates_temp['Longitude']
result_pd['Latitude'] = coordinates_temp['Latitude']

result_pd.to_csv('result.csv', index=False)
