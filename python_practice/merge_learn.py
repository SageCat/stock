import pandas as pd

df1 = pd.DataFrame({"key": ['a', 'b', 'c', 'd', 'e'], "value": range(1, 6)})
df2 = pd.DataFrame({"key": ['a', 'b', 'f', 'h', 'e'], "value": range(5, 10)})

print(df1)
print(df2)
print(">>>>>>>>>>>>>>>>>")
print(df1.merge(df2, left_on="key", right_on='key', how='left'))
