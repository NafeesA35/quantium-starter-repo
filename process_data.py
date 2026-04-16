import pandas as pd
import os

data_dir = os.path.join(os.path.dirname(__file__), "data")

files = [
    os.path.join(data_dir, "daily_sales_data_0.csv"),
    os.path.join(data_dir, "daily_sales_data_1.csv"),
    os.path.join(data_dir, "daily_sales_data_2.csv"),
]

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df = df[df["product"] == "pink morsel"]

df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
df["sales"] = df["quantity"] * df["price"]

output = df[["sales", "date", "region"]]

output_path = os.path.join(os.path.dirname(__file__), "output.csv")
output.to_csv(output_path, index=False)

print(f"Done. {len(output)} rows written to {output_path}")
