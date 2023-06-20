import pandas as pd
import re


columns_for_sql = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
new_column_names = ["date", "CIN", "name", "petrol", "diesel", "gas", "electro", "hybrid", "plugInHybrid", "others"]
df = pd.read_csv("https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv", sep=";", encoding="latin1", encoding_errors="replace",skiprows=6, skipfooter=4, usecols=columns_for_sql)


#new columns assignement
df.set_axis(new_column_names, axis=1, inplace=True)
df['petrol'] = pd.to_numeric(df['petrol'], errors='coerce', downcast='integer')
df['diesel'] = pd.to_numeric(df['petrol'], errors='coerce', downcast='integer')
df['gas'] = pd.to_numeric(df['gas'], errors='coerce', downcast='integer')
df['electro'] = pd.to_numeric(df['electro'], errors='coerce', downcast='integer')
df['hybrid'] = pd.to_numeric(df['hybrid'], errors='coerce', downcast='integer')
df['plugInHybrid'] = pd.to_numeric(df['plugInHybrid'], errors='coerce', downcast='integer')
df['others'] = pd.to_numeric(df['others'], errors='coerce', downcast='integer')



#Data Type assignement
print(df["name"])

# CIN validation
#validation for values > 0
df = df[df['CIN'].astype(str).str.match(r'^\d{5}$')]  # CIN validation
df = df[df['electro'] > 0]
df = df[df["hybrid"] > 0]
df = df[df['gas'] > 0]
df = df[df['petrol'] > 0]
df = df[df['plugInHybrid'] > 0]
df = df[df['others'] > 0]
df = df[df['diesel'] > 0]

df = df.dropna()

data_types = {
    "date" : str,
    "CIN" : str,
    "name" : str,
    "diesel": int,
    "electro": int,
    "gas": int,
    "hybrid": int,
    "plugInHybrid": int,
    "others": int,
    "petrol": int
}    
df = df.astype(data_types)




df.to_sql("cars", "sqlite:///cars.sqlite", if_exists="replace", index=False)

