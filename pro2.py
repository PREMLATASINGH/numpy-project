import numpy as np
import pandas as pd
data={
    "data":["2026-01-01","2026-01-02","2026-01-03","2026-01-04","2026-01-05"]
   , "product":["A","B","A","C","B"],
   "quantity":[2,1,3,2,4],
   "price":[100,200,100,300,200]
}
df=pd.DataFrame(data)
print(df)