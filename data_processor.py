import pandas as pd


input_files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dataframes = []

for file in input_files:

    data = pd.read_csv(file)
    data = data[data["product"] == "pink morsel"]
    

    data["price"] = data["price"].str.replace('$', '').astype(float)
    data["sales"] = data["quantity"] * data["price"]
    

    data = data[["sales", "date", "region"]]
    

    dataframes.append(data)


final_data = pd.concat(dataframes)


final_data.to_csv("processed_data.csv", index=False)