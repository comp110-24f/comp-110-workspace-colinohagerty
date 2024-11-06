"""File to define Bear class."""

__author__ = "730574200"


class Bear:
    """Defines the Bear class."""

    age = int
    hunger_score = int

    def __init__(self):
        """Initializes age and hunger for new bears."""
        self.age = 0  # initializes age and hunger score at 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """What happens when each day passes."""
        self.age += 1  # gets 1 day older each day
        self.hunger_score -= 1  # gets 1 point hungrier each day
        return None

    def eat(self, num_fish: int):
        """Increases hunger score by amount of fish."""
        self.hunger_score += num_fish  # adds num_fish to hunger_score, lowering hunger
