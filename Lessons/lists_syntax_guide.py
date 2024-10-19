"""Practice with Lists"""

my_numbers: list[float] = list()  # constructor; example of initializing empty list
my_numbers: list[float] = []  # literal

my_numbers.append(1.5)
# print(my_numbers)
# print(len(my_numbers))
my_numbers.append(2.3)
# print(my_numbers[0]) --> example of subscription syntax with lists
# print(my_numbers[len(my_numbers)]) --> example of index error with lists
game_points: list[int] = [102, 86, 94]  # example of initializing already populated list
# print(game_points)
# game_points[0] = 100: example of reassigning certain item in list with subscription
# print(game_points)
# print(game_points[2])
# game_points.pop(2) --> example of removing items from list
# game_points.append(102) YES you can have duplicates in a list


def display(int_list: list[int]) -> None:
    """displays each item in a list of integers"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(game_points)
