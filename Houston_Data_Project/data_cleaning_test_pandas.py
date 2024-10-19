"""Trying to figure out how to average and sum daily value"""

import pandas as pd  # pandas has the csv reader

test_data = pd.read_csv("test_data_cleaning_python.csv")  # reads the csv into this file
# make sure that csv is IN your workspace, not another file or OneDrive

# print(test_data.head()) is function to print first few rows

# new list of averages = csvname.groupby(averaging at each site daily, getmean, restart)
daily_averages = test_data.groupby(["Site_ID", "Date"])["Value"].mean().reset_index()

# in csv, making new column of the list that you just made called "daily_average"
daily_averages.rename(columns={"Value": "daily_average"}, inplace=True)

print(daily_averages)

daily_max = test_data.groupby(["Site_ID", "Date"])["Value"].max().reset_index()

daily_max.rename(columns={"Value": "daily_max"}, inplace=True)


print(daily_max)
