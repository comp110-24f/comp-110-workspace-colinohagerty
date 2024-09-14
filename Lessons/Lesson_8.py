"""Practice with variables and elif"""

# x: int = 1
# x = x + 1
# print(x)

# age: int = 1
# age = age + 1
# print(age)

# weather: str = "cold"


def get_weather_report() -> str:
    weather: str = input("What's the weather today? ")
    print(weather)
    if weather == "rainy" or weather == "cold":
        print("Bring a Jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather")
    return weather


get_weather_report()
