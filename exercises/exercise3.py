import pandas as pd


columns_for_sql = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
new_column_names = ["date", "CIN", "name", "petrol", "diesel", "gas", "electro", "hybrid", "plugInHybrid", "others"]
df = pd.read_csv("https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv", sep=";", encoding="utf-8", encoding_errors="replace",skiprows=6, skipfooter=4, usecols=columns_for_sql)

column_names = df.columns.tolist()
print(column_names)

df.set_axis(new_column_names, axis=1, inplace=True)
df.to_sql("cars", "sqlite:///cars.sqlite", if_exists="replace", index=False)

