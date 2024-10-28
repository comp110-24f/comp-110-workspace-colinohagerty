import pandas as pd  # pandas has the csv reader

benz_input = pd.read_csv("BENZ_Houston_Input.csv")

BENZ_daily_averages = (
    benz_input.groupby(["Site ID", "DaysInto2017"])["BENZ_Raw"].mean().reset_index()
)

BENZ_daily_averages.rename(columns={"BENZ_Raw": "BENZ_daily_avg"}, inplace=True)

# print(BENZ_daily_averages)

BENZ_daily_averages.to_csv("BENZ_AVG_output", index=False)
