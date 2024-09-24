import pandas as pd

# data = pd.Series([10,20,30,40])
# print(data)

data = {"name" : ["shivam", "shiv", "AAAAAC"],
        "Age": [34, 45, 56],
        "city": ["chd", "USA", "Japan"]}

df = pd.DataFrame(data)
df.to_csv("output.csv" index=False)
# print(df)

