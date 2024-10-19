"""Unit Tests for List Fuctions"""

__author__ = "730574200"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# unit test for only_evens return
def test_return_only_evens() -> None:
    """should give only evens in a list"""
    nums: list[int] = [2, 4, 6, 5, 3, 6]
    assert only_evens(nums) == [
        2,
        4,
        6,
        6,
    ]  # checks that returned list is what we thought


# unit test that only_evens doesn't mutate list
def test_behavior_only_evens() -> None:
    """only_evens should not change the input list"""
    nums: list[int] = [1, 2, 3, 4, 5]
    only_evens(nums)
    assert nums == [1, 2, 3, 4, 5]


# edge case empty list only_evens
def test_edge_only_evens() -> None:
    """empty list should be returned"""
    empty: list[int] = []
    assert only_evens(empty) == []  # checks that empty list gives empty list


# sub should give subset of list
def test_return_sub() -> None:
    """list from start to end, exclusive, should be returned"""
    nums: list[int] = [2, 3, 4, 7, 6]
    assert sub(nums, 2, 4) == [4, 7]  # only 4, 7 because 6 not included since at 4


# sub should not change the original list that's input
def test_behavior_sub() -> None:
    """input list shouldn't be changed by sub"""
    nums: list[int] = [2, 4, 3, 5]
    sub(nums, 1, 3)
    assert nums == [2, 4, 3, 5]  # checks that no mutating is happening


# if start is after end, empty list should be returned
def test_edge_sub() -> None:
    nums: list[int] = [2, 3, 4, 5]
    assert sub(nums, 3, 1) == []  # edge case where start is after end


# add_at_index should not return anything
def test_return_add_at_index() -> None:
    nums: list[int] = [2, 4, 5, 6]
    assert add_at_index(nums, 2, 2) is None


# add_at_index should put new number in at assigned index
def test_behavior_add_at_index() -> None:
    nums: list[int] = [2, 4, 5, 6]
    add_at_index(nums, 2, 2)  # does add_at_index on nums
    assert nums == [2, 4, 2, 5, 6]  # checks for expected output


# checks to make sure that using add_at_index with wrong index gives index error
def test_add_at_index_raises_indexerror() -> None:
    """Makes sure that if index_add is negative or outside input, gives index error"""
    nums: list[int] = [2, 4, 5, 6]
    with pytest.raises(
        IndexError
    ):  # have to use pytest because this IndexError is not value
        add_at_index(
            nums, 5, 4
        )  # 4 is more than max index so index error and 5 not added
