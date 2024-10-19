"""daily max, daily avg, and nighttime hour ethane"""

import csv

ethane_data = []

with open("ethane_cleaning2.csv", "r") as file:  # opens data
    reader = csv.DictReader(file)  # reads data
    for row in reader:
        ethane_data.append(row)  # adds each row by row based on reader of csv

etha_daily_totals = {}
etha_daily_max = {}

# for every entry (i.e. row), checks if location/date are in empty dict and then math
for entry in ethane_data:
    daysSince2017 = entry["daysSince2017"]
    time = entry["Time"]
    site_id = entry["Site ID"]
    value = float(entry["Value"])

    if (
        site_id,
        daysSince2017,
    ) not in etha_daily_totals:  # adds each location/date/val/time to dict
        etha_daily_totals[(site_id, daysSince2017)] = {"sum": 0, "count": 0}

    etha_daily_totals[(site_id, daysSince2017)]["sum"] += value
    etha_daily_totals[(site_id, daysSince2017)]["count"] += 1

    if (
        site_id,
        daysSince2017,
    ) not in etha_daily_max:  # adds each location date value time to dictionary
        etha_daily_max[(site_id, daysSince2017)] = {"max_value": value, "time": time}
    else:  # if comes to location date mix that you've already hit
        if (
            value > etha_daily_max[(site_id, daysSince2017)]["max_value"]
        ):  # overrides previous if bigger
            etha_daily_max[(site_id, daysSince2017)] = {
                "max_value": value,
                "time": time,
            }

etha_daily_averages = {}  # new dict for daily avgs
for (
    key,
    totals,
) in etha_daily_totals.items():  # checks "key" location and date and calcs avgs
    site_id, daysSince2017 = key
    average = totals["sum"] / totals["count"]
    etha_daily_averages[(site_id, daysSince2017)] = average

# print("Daily Averages:")
# for (site_id, daysSince2017), avg in etha_daily_averages.items():
# print(f"Location: {site_id}, Date: {daysSince2017}, Daily Average: {avg}")

# print("\nDaily Max Values:")
# for (site_id, daysSince2017), max_info in etha_daily_max.items():
# #print(f"Location: {site_id}, Date: {daysSince2017}, Max Value: {max_info['max_value']}, Time: {max_info['time']}")

nighttime_averages = {}

from datetime import datetime

for entry in ethane_data:
    daysSince2017 = entry["daysSince2017"]
    time = entry["Time"]
    site_id = entry["Site ID"]
    value = float(entry["Value"])


# code that exports daily avgs as csv with location, date, daily avg
# with open("etha_daily_averages.csv", "w", newline="") as file:
# writer = csv.writer(file)
# writer.writerow(["site_id", "daysSince2017", "Daily Average"])  # Write header
# for (site_id, daysSince2017), avg in etha_daily_averages.items():
# writer.writerow([site_id, daysSince2017, avg])

# code that exports daily maxs as csv with location, date, daily max, and time
# with open("etha_daily_max_values.csv", "w", newline="") as file:
# writer = csv.writer(file)
# writer.writerow(["site_id", "daysSince2017", "Max Value", "Time"])  # Write header
# for (site_id, daysSince2017), max_info in etha_daily_max.items():
# writer.writerow([site_id, daysSince2017, max_info["max_value"], max_info["time"]])
