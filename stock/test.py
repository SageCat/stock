import numpy as np
import pandas as pd

df = pd.DataFrame([
    {"name": "sage", "num": None},
    {"name": "sage2", "num": '1, 3, 4, 5'},
    {"name": "sage3", "num": '1, 2, 5'},
    {"name": "sage4", "num": '1'}
])

print(df['num'])
# df['num'] = list(df['num'])
df['a'] = df['num'].str.split(',').map(len, na_action='ignore')
print(df)


df2 = pd.DataFrame([
    {"name": "sage2", "num": [1, 2]},
    {"name": "sage3", "num": [3, 4]},
])

df3 = df2['num'].apply(lambda x: pd.Series(x))
df3.columns = ['Longitude', 'Latitude']
print(df3)

df2['Longitude'] = df3['Longitude']
df2['Latitude'] = df3['Latitude']
print(df2)