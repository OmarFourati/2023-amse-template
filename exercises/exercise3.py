import pandas as pd
import re


columns_for_sql = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
new_column_names = ["date", "CIN", "name", "petrol", "diesel", "gas", "electro", "hybrid", "plugInHybrid", "others"]
df = pd.read_csv("https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv", sep=";", encoding="utf-8", encoding_errors="replace",skiprows=6, skipfooter=4, usecols=columns_for_sql)

#Data Type for each column
data_types = {
    "date" : str,
    "CIN" : str,
    "name" : str,
}     


#new columns assignement
df.set_axis(new_column_names, axis=1, inplace=True)

df['petrol'] = pd.to_numeric(df['petrol'], errors='coerce', downcast='integer')
df['gas'] = pd.to_numeric(df['gas'], errors='coerce', downcast='integer')
df['electro'] = pd.to_numeric(df['electro'], errors='coerce', downcast='integer')
df['hybrid'] = pd.to_numeric(df['hybrid'], errors='coerce', downcast='integer')
df['plugInHybrid'] = pd.to_numeric(df['plugInHybrid'], errors='coerce', downcast='integer')
df['others'] = pd.to_numeric(df['others'], errors='coerce', downcast='integer')



#Data Type assignement
df = df.astype(data_types)

# CIN validation
is_valid_cin = df['CIN'].apply(lambda x: bool(re.match(r'^0?\d{5}$', str(x))))

df = df.dropna()
print(df.head())
#validation for values > 0
# df = df[df['petrol'].apply(lambda x: isinstance(x, int) and x > 0 if isinstance(x, int) else False)]
# df = df[df['gas'].apply(lambda x: isinstance(x, int) and x > 0 if isinstance(x, int) else False)]
# df = df[df['electro'].apply(lambda x: isinstance(x, int) and x > 0 if isinstance(x, int) else False)]
# df = df[df['hybrid'].apply(lambda x: isinstance(x, int) and x > 0 if isinstance(x, int) else False)]
# df = df[df['plugInHybrid'].apply(lambda x: isinstance(x, int) and x > 0 if isinstance(x, int) else False)]
# df = df[df['others'].apply(lambda x: isinstance(x, int) and x > 0 if isinstance(x, int) else False)]


df.to_sql("cars", "sqlite:///cars.sqlite", if_exists="replace", index=False)

