import pandas as pd

# Load the uploaded master_df
master_df = pd.read_csv(r".\data\master_df.csv")

# Identify columns
complaint_columns = [col for col in master_df.columns if "Complaint Type" in col]
orders_columns = master_df.columns[master_df.columns.get_loc("OrderCount") :]

# Replace missing values
master_df[complaint_columns] = master_df[complaint_columns].fillna(0)
master_df["Instructions"] = master_df["Instructions"].fillna("No")
master_df[orders_columns] = master_df[orders_columns].fillna(0)

# Add 'ComplaintTotal' column
master_df["ComplaintTotal"] = master_df[complaint_columns].sum(axis=1)

# Reorder columns
first_complaint_col_idx = master_df.columns.get_loc(complaint_columns[0])
new_col_order = (
    list(master_df.columns[:first_complaint_col_idx])
    + ["ComplaintTotal"]
    + list(master_df.columns[first_complaint_col_idx:-1])
)
master_df = master_df[new_col_order]

# Check if 'OrderCount' is the sum of all columns after it
order_sum_check = (
    master_df["OrderCount"] == master_df[orders_columns[1:]].sum(axis=1)
).all()
print("OrderCount matches the sum of all columns after it:", order_sum_check)

# Save the adjusted dataframe
master_df.to_csv(r".\data\master_df_pprocess1.csv", index=False)
