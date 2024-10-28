import pandas as pd  # pandas has the csv reader

TB_Ratio_input = pd.read_csv("TB_Ratio_Input.csv")

TB_RATIO_daily_averages = (
    TB_Ratio_input.groupby(["Site ID", "DaysInto2017"])["TB_Ratio"].mean().reset_index()
)

TB_RATIO_daily_averages.rename(
    columns={"TB_Ratio": "ToluBenz_Ratio_Daily_Avg"}, inplace=True
)

# print(TB_RATIO_daily_averages)

TB_RATIO_daily_averages.to_csv("ToluBenz_Ratio_output", index=False)
