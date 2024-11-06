"""File to define River class."""

__author__ = "730574200"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Defines the River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0  # day you start with
        self.fish: list[Fish] = []  # no fish to start
        self.bears: list[Bear] = []  # no bears to start
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of all fish and bears, killing them if needed."""
        surviving_fish: list[Fish] = []  # initializing survivor lists
        surviving_bears: list[Bear] = []
        for id in range(0, len(self.fish)):  # goes by index through Fish list
            test_fish: Fish = self.fish[id]  # sets the fish to test
            if test_fish.age <= 3:  # if that fish is age less than or equal to 3
                surviving_fish.append(self.fish[id])  # it survives
        for id in range(0, len(self.bears)):  # repeat same process for bears
            test_bear: Bear = self.bears[id]
            if test_bear.age <= 5:
                surviving_bears.append(self.bears[id])
        self.fish = surviving_fish  # set river lists equal to survivor lists
        self.bears = surviving_bears

        return None

    def bears_eating(self):
        """For each bear, if 5 fish, it eats 3."""
        for id in range(0, len(self.bears)):  # goes through for each bear
            if len(self.fish) >= 5:  # if less than 5, bear does not eat
                eating_bear: Bear = self.bears[
                    id
                ]  # if at least 5 fish...eating bear is bear at that id
                eating_bear.eat(3)  # that bear at that id eats 3
                self.remove_fish(3)  # those 3 fish are removed
            else:
                return None
        return None

    def check_hunger(self):
        """If bear too hungry, starvation."""
        surviving_bears: list[Bear] = []
        for id in range(0, len(self.bears)):  # checks all bear's hunger
            hungry_bear: Bear = self.bears[id]
            if (
                hungry_bear.hunger_score >= 0
            ):  # if that bear has hunger greater than or equal to 0
                surviving_bears.append(hungry_bear)  # it survives
        self.bears = surviving_bears  # sets non-starving bears as survivors
        return None

    def repopulate_fish(self):
        """Pairs of fish have offspring."""
        fish_pairs: int = len(self.fish) // 2  # finds amount of fish to have offspring
        for x in range(0, fish_pairs):  # for each pair, add four new fish
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Pairs of bears have offspring."""
        bear_pairs: int = len(self.bears) // 2  # finds how many bears to have offspring
        for x in range(0, bear_pairs):  # for each pair, add a new bear
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Displays what happens with river."""
        print(f"~~~ Day {self.day}: ~~~")  # prints the day number
        print(f"Fish population: {len(self.fish)}")  # prints how many fish in river
        print(f"Bear population: {len(self.bears)}")  # prints amount of bears in river
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate change in life in river for one week."""
        # call one_river_day 7 times
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes amount many fish from the river."""
        for id in range(0, amount):  # for amount times
            self.fish.pop(0)  # pop the frontmost fish out of the river
