"""Determine the amount of tea bags, treats, and associated costs for a tea party"""

__author__: str = "730574200"


def main_planner(guests: int) -> None:
    """Prints information about tea bags, treats, and costs for the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    # because guests is an integer, it can be used instead of people here
    # all of these functions use people which is also an integer
    # (and also holds the same conceptual purpose)
    print("Treats: " + str(treats(guests)))
    # when I built the cost function, the variables were different, so I need to define them
    # like this where they match other functions so I can perform everything with one input variable, guests
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))
    return None


def tea_bags(people: int) -> int:
    """Find number of tea bags needed based on number of attendees"""
    return people * 2


def treats(people: int) -> int:
    """Find number of treats needed based on teas each person drinks"""
    # Because tea_bags returns an even number, turning the float into an integer
    # doesn't change the value as an even number times 1.5 returns a whole number
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Find total costs associated with tea party"""
    # The parentheses aren't technically necessary but help me conceptualize the order of operations
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    # This makes our code more useful by connecting to a question that a program can ask you
    # This needs to go last because the main_planner function is called and this function calls
    # every other function as an argument (alln these functions must exist)
    main_planner(guests=int(input("How many guests are attending your tea party?")))
