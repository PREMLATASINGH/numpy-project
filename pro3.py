import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data={
    "date":["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05"]
   , "product":["Apple","Banana","Apple","Kiwi","Banana"],
   "quantity":[2,5,13,24,4],
   "price":[100,600,400,100,200]}
df=pd.DataFrame(data)
print(df)
plt.hist(df)
plt.show()
print(type(df))
print(df.isnull().sum())
df["Revenue"]=df["quantity"]*df["price"]
total_revenue=np.sum(df["Revenue"])
print("total revenue:",total_revenue)
daily_revenue=df.groupby("date")["Revenue"].sum()
print(daily_revenue)
print(df.describe())
print(df.info())


