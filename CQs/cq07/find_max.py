"""Function to find max value"""

__author__ = "730574200"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    else:
        max_int: int = 0
        idx: int = 0
        while idx < len(input):
            if max_int < input[idx]:
                max_int = input[idx]
                idx += 1
            else:
                idx += 1
        idxb: int = 0
        while idxb < len(input):
            if input[idxb] == max_int:
                input.pop(idxb)
            else:
                idxb += 1
        return max_int
