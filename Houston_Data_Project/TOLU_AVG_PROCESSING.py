import pandas as pd  # pandas has the csv reader

TOLU_input = pd.read_csv("TOLU_AVG_Input.csv")

TOLU_daily_averages = (
    TOLU_input.groupby(["Site ID", "DaysInto2017"])["TOLU_RAW"].mean().reset_index()
)

TOLU_daily_averages.rename(columns={"TOLU_RAW": "TOLU_daily_avg"}, inplace=True)

# print(TOLU_daily_averages)

TOLU_daily_averages.to_csv("TOLU_AVG_output", index=False)
