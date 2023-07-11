import urllib.request
import zipfile
import pandas

#Download zip file
urllib.request.urlretrieve("https://gtfs.rhoenenergie-bus.de/GTFS.zip", "./exercises/exercise5.zip")

# Step 1: Download and unzip the data
zip_file_url = 'https://gtfs.rhoenenergie-bus.de/GTFS.zip'
zip_file_path = 'GTFS.zip'
data_file_name = 'stops.txt'

# Download the ZIP file
urllib.request.urlretrieve(zip_file_url, zip_file_path)

# Unzip the ZIP file and extract the data.csv file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extract(data_file_name)
    
    
columns_to_keep = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]

df = pandas.read_csv(data_file_name, usecols=columns_to_keep)

data_types = {
    "stop_id" : int,
    "stop_name" : str,
    "stop_lat" : float,
    "stop_lon" : float,
    "zone_id" : int
}  

df = df.astype(data_types)

#validate data
df = df[df["zone_id"] == 2001]

df = df[(df["stop_lat"] <= 90) & (df["stop_lat"] >= -90)]
df = df[(df["stop_lon"] <= 90) & (df["stop_lat"] >= -90)]

df.to_sql('stops', 'sqlite:///gtfs.sqlite', if_exists= 'replace', index=False)






