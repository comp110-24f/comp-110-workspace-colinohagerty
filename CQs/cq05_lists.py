"""Modifying Lists"""

___author___ = "730574200"


def manual_append(numbers: list[int], num: int) -> None:
    numbers.append(num)
    return None


def double(numbers: list[int]) -> None:
    index: int = 0
    while index < len(numbers):
        numbers[index] *= 2
        index += 1
    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
