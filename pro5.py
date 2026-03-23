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