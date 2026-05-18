import pandas as pd

df= pd.read_csv('./data_handelling_3/data/researchers.csv')
print(df.shape)
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())