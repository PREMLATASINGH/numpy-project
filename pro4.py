import numpy as np
import pandas as pd
data={
    "customer":["A","B","C","A","B","D"],
    "product":["laptop","phone","tablet","phone","laptop","taplet"],
    "quantity":[1,2,1,3,1,2],
    "price":[1000,500,300,500,1000,300]
}
df=pd.DataFrame(data)
print(df)
print(df.isnull().sum())
df["revenue"]=df["quantity"]*df["price"]
print(df)
total_revenue=np.sum(df["revenue"])
print("total revenue:",total_revenue)