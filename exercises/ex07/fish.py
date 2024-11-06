"""File to define Fish class."""

__author__ = "730574200"


class Fish:
    """Defines the Fish class."""

    age = int

    def __init__(self):
        """Initializes new fish."""
        self.age = 0  # for each new fish, it starts at age 0
        return None

    def one_day(self):
        """Ages each fish each day."""
        self.age += 1  # for each new day, fish get older by 1
        return None
