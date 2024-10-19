"""For Loops and Range()"""

# you can use to iterate over every element in sequence
# example
xs: list[str] = ["w", "x", "y", "z"]
index1: int = 0


# def while_loop(sequence: list[str]) -> None:
# xs: list[str] = ["w", "x", "y", "z"]
# index1: int = 0
# while index1 < len(xs):
# print(xs[index1])
# index1 += 1


# def for_loops(sequence: list[str]) -> None:
# for elem in sequence:
# print(elem)


# def good_boy(names: list[str]) -> None:
# for x in names:
# print(type(x))
# print(f"Good boy, {x}!")


def indexed_names(names: list[str]) -> None:
    for index in range(0, len(names)):
        print(f"{index}: {names[index]}")
