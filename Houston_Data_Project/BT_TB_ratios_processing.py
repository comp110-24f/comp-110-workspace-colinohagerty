"""Finding daily averages of Benz/Tolu and Tolu/Benz ratios in 2017"""

import pandas as pd  # pandas has the csv reader

benztolu_ratio = pd.read_csv("BENZ_TOLU_Houston_2017.csv")

BT_ratio_daily_averages = (
    benztolu_ratio.groupby(["Site ID", "DaysInto2017"])["BT_Ratio"].mean().reset_index()
)

BT_ratio_daily_averages.rename(
    columns={"BT_Ratio": "BT_Ratio_daily_average"}, inplace=True
)

# print(BT_ratio_daily_averages)

TB_ratio_daily_averages = (
    benztolu_ratio.groupby(["Site ID", "DaysInto2017"])["TB_Ratio"].mean().reset_index()
)

TB_ratio_daily_averages.rename(
    columns={"TB_Ratio": "TB_Ratio_daily_average"}, inplace=True
)

# print(TB_ratio_daily_averages)

# BT_ratio_daily_averages.to_csv("BT_ratio_daily_avg", index=False)

# TB_ratio_daily_averages.to_csv("TB_ratio_daily_avg", index=False)
