import numpy as np
import pandas as pd
data={
    "date":["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05"]
   , "product":["A","B","A","C","B"],
   "quantity":[2,1,3,2,4],
   "price":[100,200,100,300,200]
}
df=pd.DataFrame(data)
print(df)
df["Revenue"]=df["quantity"]*df["price"]
print(df)
total_revenue=np.sum(df["Revenue"])
print("total revenue:",total_revenue)
product_revenue=df.groupby("product")["Revenue"].sum()
print(product_revenue)
best_product=product_revenue.idxmax()
print("best product:",best_product)
daily_revenue=df.groupby("date")["Revenue"].sum()
print(daily_revenue)