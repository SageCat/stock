import pandas as pd

source_data = pd.read_csv('Result_60.csv')
source_data.sort_values(['Year', 'NOC'])
olympic_year = set(source_data['Year'])
title = list(olympic_year)
title.sort()
country_list = list(set(source_data['NOC']))
country_list.sort()
new_df = pd.DataFrame(columns=title, index=country_list)

for i in title:
    for j in country_list:
        if len(source_data.loc[(source_data['Year'] == i) & (source_data['NOC'] == j), 'gold_medal_number']) > 0:
            new_df.loc[j, i] = \
            source_data.loc[(source_data['Year'] == i) & (source_data['NOC'] == j), 'gold_medal_number'].values[0]
            print(type(source_data.loc[(source_data['Year'] == i) & (source_data['NOC'] == j), 'gold_medal_number']))
        else:
            new_df.loc[j, i] = 0

new_df.to_csv('result_gold_number.csv')
