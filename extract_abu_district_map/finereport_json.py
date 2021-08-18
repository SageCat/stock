import json

from pandas import json_normalize

# with open("geographic/world-area.json", "r") as f:
#     all_data = json.load(f)
#     df = json_normalize(all_data, record_path="features", meta=['type', 'name'], errors='ignore', meta_prefix='mera.',
#                         record_prefix='features')
#     print(df)
#
#     df.to_csv("geographic/world-area.csv")

# with open("geographic/world/China-point.json", "r") as f:
#     all_data = json.load(f)
#     df = json_normalize(all_data, record_path="features", meta=['type'], meta_prefix='meta.',
#                         record_prefix='features.')
#     print(df)
#
#     df.to_csv("geographic/world/China-point.csv")

with open("geographic/world/China-area.json", "r") as f:
    all_data = json.load(f)
    df = json_normalize(all_data, record_path="features", meta=['type'], meta_prefix='meta.',
                        record_prefix='features.')
    print(df)

    df.to_csv("geographic/world/China-area.csv")