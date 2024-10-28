"""List uses and functions for exercise 05"""

__author__ = "730574200"


def only_evens(input: list[int]) -> list[int]:
    """returns a list of only the even ints in a list"""
    even_ints: list[int] = []  # output list diff from input, not changing input
    for elem in input:  # checks every element in input list
        if elem % 2 == 0:  # if even
            even_ints.append(elem)  # adds to output list
    return even_ints


def sub(input: list[int], start: int, end: int) -> list[int]:
    """returns subset of given list from start to end exclusive"""
    subset_list: list[int] = []
    if start < 0:  # if start index is negative
        start = 0  # starts at start of list
    if end > len(input):  # if end is after end of list
        end = len(input)  # sets so that end is max index of list so no index error
    if len(input) == 0:  # if input is empty, output is empty
        return []
    elif start >= end:  # another condition for empty output
        return []
    elif end <= 0:
        return []
    else:  # if normal input of integers, gives you the subset of the list you want
        idx: int = start  # using start as first index
        while idx < end:
            subset_list.append(input[idx])
            idx += 1
    return subset_list


def add_at_index(input: list[int], num_add: int, index_add: int) -> None:
    """adds new num at index of interest in list"""
    if index_add < 0 or index_add > len(input):  # index error raised
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # makes space to move to make room for new num
    backcount: int = (
        len(input) - 1
    )  # reverse indexing to get back to where new num adds
    while backcount > index_add:  # counts back
        input[backcount] = input[
            backcount - 1
        ]  # makes each number after index_add the number to the left
        backcount -= 1
    input[index_add] = num_add  # adds at the duplicated index of interest, index_add
