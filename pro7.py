import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data={
    "product":["apple","phone","tablet","phone","laptop","taplet"],
    "quantity":[1,2,1,3,1,2],
    "price":[100,50,300,500,100,300],
    "sales":[100,100,300,1500,100,600]

}
df=pd.DataFrame(data)
print(df)
print(df.head(3))