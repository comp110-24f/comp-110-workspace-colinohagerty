"""Summing the elements of a list using different loops"""

__author__ = "730574200"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    total: float = 0.0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    total: float = 0.0
    for x in vals:
        total += x
    return total


def f_range_sum(vals: list[float]) -> float:
    total: float = 0.0
    for index in range(0, len(vals)):
        total += vals[index]
    return total
