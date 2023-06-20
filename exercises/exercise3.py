import pandas as pd

from sqlalchemy import create_engine




# Define the source file URL and target database

data_url = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'

database_name = 'cars.sqlite'




# Read the CSV file into a DataFrame, skipping the metadata lines
new_column_names = ["date", "CIN", "name", "petrol", "diesel", "gas", "electro", "hybrid", "plugInHybrid", "others"]
columns_for_sql = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]


df = pd.read_csv(data_url, skiprows=6, skipfooter=4, encoding='latin1', delimiter= ";", usecols=columns_for_sql)


df.set_axis(new_column_names, axis=1, inplace=True)

# # Select and rename the desired columns

# df = df[['A', 'B', 'C', 'M', 'W', 'AG', 'AQ', 'BA', 'BK', 'BU']]

# # df.columns = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']




# Validate and clean the data

df = df[df['CIN'].astype(str).str.match(r'^\d{5}$')]  # CIN validation

df = df[df[['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']].apply(pd.to_numeric, errors='coerce').gt(0).all(axis=1)]  # Positive integer validation




# Create a SQLite database engine and write the DataFrame to a table

engine = create_engine(f'sqlite:///{database_name}')

df.to_sql('cars', engine, if_exists='replace', index=False)