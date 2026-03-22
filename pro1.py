import numpy as np
Sales_data=np.array([
    [200,150,300],
    [220,130,280],
    [250,160,310],
    [270,180,350],
    [300,200,400]])
print(Sales_data)
Total_sales=np.sum(Sales_data)
print("Total Sales:",Total_sales)
avg_sales=np.mean(Sales_data)
print("Average Sales:",avg_sales)
product_sales=np.sum(Sales_data,axis=0)
print("Sales per product:",product_sales)
best_product=np.argmax(product_sales)
print("best product index:",best_product)
daily_sales=np.sum(Sales_data,axis=1)
print("daily sales:",daily_sales)
std_dev=np.std(Sales_data)
print("sales variability:",std_dev)

