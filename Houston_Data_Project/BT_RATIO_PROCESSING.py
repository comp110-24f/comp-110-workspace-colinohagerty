import pandas as pd  # pandas has the csv reader

BT_Ratio_input = pd.read_csv("BT_Ratio_Input.csv")

BT_RATIO_daily_averages = (
    BT_Ratio_input.groupby(["Site ID", "DaysInto2017"])["BT_Ratio"].mean().reset_index()
)

BT_RATIO_daily_averages.rename(
    columns={"BT_Ratio": "BenzTolu_Ratio_Daily_Avg"}, inplace=True
)

# print(BT_RATIO_daily_averages)

BT_RATIO_daily_averages.to_csv("BenzTolu_Ratio_output", index=False)
