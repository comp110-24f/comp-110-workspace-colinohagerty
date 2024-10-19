"""Exercise 4 - applying and learning about lists"""

__author__ = "730574200"


def all(numbers: list[int], testnum: int) -> bool:
    """checks to see if all numbers in list match number of interest"""
    index: int = 0  # setting up while loop
    if len(numbers) == 0:  # if empty, returns false
        return False
    while index < len(numbers):  # progresses towards false
        if numbers[index] == testnum:  # checking if that number at that index matches
            index += 1  # if so keep going
        else:
            return False  # if not, exit and false is returned
    return True


def max(numbers: list[int]) -> int:
    """outputs maximum int in list of ints"""
    if len(numbers) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # gives an error if input is not a list of ints
    else:
        id: int = 0  # setting up while loop
        output_num: int = numbers[
            0
        ]  # setting up output variable which starts at start of list
        while id < len(numbers):
            if output_num < numbers[id]:  # i.e. if the number at this index is bigger
                output_num = numbers[id]
                id += 1
            else:
                id += 1
    return output_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """checks if every element in a list is equal"""
    index: int = 0
    if len(list1) != len(list2):  # checks if length is equal
        return False  # false and end if not equal
    else:
        while index < len(list1):
            if list1[index] == list2[index]:  # checks by each index if the same
                index += 1
            else:
                return False  # if not the same, exit and false is returned
    return (
        True  # if you pass through all of while block without hitting else, return True
    )


def extend(list1: list[int], list2: list[int]) -> None:
    """adds list 2 onto the end of list 1"""
    index: int = 0
    while index < len(list2):
        list1.append(list2[index])  # while loop adding each part of list 2 one by one
        index += 1
