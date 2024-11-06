import pandas as pd  # pandas has the csv reader

ozone_input = pd.read_csv("ozone_processing.csv")

ozone_daily_averages = (
    ozone_input.groupby(["Site ID", "daysInto2017"])["Value"].mean().reset_index()
)

ozone_daily_averages.rename(columns={"Value": "ozone_daily_avg"}, inplace=True)

# print(ozone_daily_averages)

ozone_daily_averages.to_csv("ozone_avg_output", index=False)
