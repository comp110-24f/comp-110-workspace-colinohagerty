"""Coordinates file for importing, CQ04"""

__author__ = "730574200"


def get_coords(xs: str, ys: str) -> None:
    x_index = 0
    while len(xs) > x_index:
        y_index = 0
        while len(ys) > y_index:
            print("(" + xs[x_index] + "," + ys[y_index] + ")")
            y_index += 1
        x_index += 1
