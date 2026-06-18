import numpy as np
import pandas as pd
data={
    "customer":["A","B","C","A","B","D"],   
    "product":["apple","phone","tablet","phone","laptop","taplet"],
    "quantity":[1,2,1,3,1,2],
    "price":[100,50,300,500,100,300]
}
df=pd.DataFrame(data)
print(df)
print(df.isnull().sum())
print(df.info())
print(df.describe())
print(df.head())
print(type(df))
print(df.tail())
print(df.shape)
print(df.columns)
print(df.index)
print(df.values)
print(df.groupby("customer").sum())
print(df.groupby("product").sum())
print(df.groupby("price").mean(numeric_only=True))
print(df.groupby("quantity").mean(numeric_only=True))
