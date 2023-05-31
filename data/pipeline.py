import sqlite3
import pandas as pd
import os


df1_xslx = pd.read_excel("https://www.stadt-muenster.de/fileadmin/user_upload/stadt-muenster/61_verkehrsplanung/pdf/zaehlstelle_weseler_2018_stundenauswertung.xlsx", engine="openpyxl", skiprows=2)
df2_xslx = pd.read_excel("https://www.stadt-muenster.de/fileadmin/user_upload/stadt-muenster/61_verkehrsplanung/pics/radverkehr/Zaehldaten_2022/Zaehlstelle_Weseler_Strasse_Stundenauswertung_2022.xlsx", engine="openpyxl", skiprows=2)
           
              

df1_xslx = df1_xslx.set_index("Zeit")
df2_xslx = df2_xslx.set_index("Zeit")

df1_xslx = df1_xslx.drop('Unnamed: 0', axis=1)
df2_xslx = df2_xslx.drop('Unnamed: 0', axis=1)

print(df1_xslx)
conn = sqlite3.connect("../data/verkehrszaehlungen.sqlite")

df1_xslx.to_sql("fahraddverkehr_2018", conn, if_exists="replace")
df2_xslx.to_sql("fahraddverkehr_2022", conn, if_exists="replace")


