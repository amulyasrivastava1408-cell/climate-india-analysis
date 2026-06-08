# Climate Analysis Dataset 2024-2025 

import pandas as pd

df = pd.read_csv("climate_dataset.csv")

print(df.shape)          # how many rows and columns
print(df.head())        # first 5 rows
print(df.tail())        # last 5 rows
print(df.sample(5))      # random 5 rows — avoids bias from head/tail
print(df.columns )       # column names
print(df.dtypes )        # data type of each column
df.info()         # dtypes + non-null counts together

# Summary Statistics 
df.describe()                        # mean, std, min, max, quartiles — numeric only
df.describe(include="object")        # stats for text columns like City, AQI_Category
print(df["AQI"].mean())
print(df["AQI"].median())
print(df["AQI"].std())
print(df["AQI"].min())
print(df["AQI"].max())
df["Temperature_Avg (°C)"].quantile(0.25)   # 25th percentile
df["Temperature_Avg (°C)"].quantile(0.75)   # 75th percentile

print( )

# Missing Value 
print(df.isnull().sum())                       # count of nulls per column
print(df.isnull().sum() / len(df) * 100)        # as percentage
print(df[df["Rainfall (mm)"].isnull()]) 
print( )        # see which rows have nulls

#  Unique Values & Frequency
print(df["City"].unique() )             # what cities exist
print(df["City"].nunique())             # how many unique cities
print(df["AQI_Category"].value_counts())           # frequency of each category
print(df["AQI_Category"].value_counts(normalize=True) * 100)  # as percentage

df.groupby("City")["AQI"].mean()                          # avg AQI per city
df.groupby("City")["Rainfall (mm)"].sum()                 # total rainfall per city
df.groupby(["City", "Season"])["Temperature_Avg (°C)"].mean()   # two-level groupby
df.groupby("Month")["AQI"].mean().sort_index()            # monthly trend
