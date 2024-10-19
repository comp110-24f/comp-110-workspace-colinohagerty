"""Same as pandas functinality but just using python shit"""

import csv

test_data = []
with open("test_data_cleaning_python.csv", "r") as file:  # opens data
    reader = csv.DictReader(file)  # reads data
    for row in reader:
        test_data.append(row)  # adds each row by row based on reader of csv

daily_totals = {}
daily_max = {}
nighttime_averages = {}  # initialize dict for avg from midnight to 3am

# for every entry (i.e. row), checks if location/date are in empty dict and then math
for entry in test_data:
    date = entry["Date"]
    time = entry["Time"]
    location = entry["Site_ID"]
    value = float(entry["Value"])

    if (location, date) not in daily_totals:  # adds each location/date/val/time to dict
        daily_totals[(location, date)] = {"sum": 0, "count": 0}

    daily_totals[(location, date)]["sum"] += value
    daily_totals[(location, date)]["count"] += 1

    if (
        location,
        date,
    ) not in daily_max:  # adds each location date value time to dictionary
        daily_max[(location, date)] = {"max_value": value, "time": time}
    else:  # if comes to location date mix that you've already hit
        if (
            value > daily_max[(location, date)]["max_value"]
        ):  # overrides previous if bigger
            daily_max[(location, date)] = {"max_value": value, "time": time}

daily_averages = {}  # new dict for daily avgs
for (
    key,
    totals,
) in daily_totals.items():  # checks "key" location and date and calcs avgs
    location, date = key
    average = totals["sum"] / totals["count"]
    daily_averages[(location, date)] = average


print("Daily Averages:")
for (location, date), avg in daily_averages.items():
    print(f"Location: {location}, Date: {date}, Daily Average: {avg}")

print("\nDaily Max Values:")
for (location, date), max_info in daily_max.items():
    print(
        f"Location: {location}, Date: {date}, Max Value: {max_info['max_value']}, Time: {max_info['time']}"
    )

# code that exports daily avgs as csv with location, date, daily avg
with open("daily_averages.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Location", "Date", "Daily Average"])  # Write header
    for (location, date), avg in daily_averages.items():
        writer.writerow([location, date, avg])

# code that exports daily maxs as csv with location, date, daily max, and time
with open("daily_max_values.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Location", "Date", "Max Value", "Time"])  # Write header
    for (location, date), max_info in daily_max.items():
        writer.writerow([location, date, max_info["max_value"], max_info["time"]])
