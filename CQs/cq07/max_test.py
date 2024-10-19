"""Unit Test of Find_Max"""

__author__ = "730574200"

from CQs.cq07.find_max import find_and_remove_max


# desired return value
def test_return_find_and_remove_max() -> None:
    """should return the max value in a list of ints"""
    grades: list[int] = [4, 5, 6, 3, 7, 2]
    assert find_and_remove_max(grades) == 7


# desired behavior
def test_mutate_find_and_remove_max() -> None:
    "max elements in list should be removed"
    numbers: list[int] = [1, 4, 3, 2, 4]
    find_and_remove_max(numbers)
    assert numbers == [1, 3, 2]


def test_return_edge_find_and_remove_max() -> None:
    "what happens if input are all 0"
    edge: list[int] = [0, 0, 0]
    assert find_and_remove_max(edge) == 0


# if input list is all same num
def test_behavior_edge_find_and_remove_max() -> None:
    "what happens if wrong input of all same num"
    edge_list: list[int] = [1, 1, 1, 1, 1]
    find_and_remove_max(edge_list)
    assert edge_list == []
