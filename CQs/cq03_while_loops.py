"""Challenge Question to Practice While Loops and Iterating Over a String"""

__author__ = "730574200"


def num_instances(phrase: str, search_char: str) -> None:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
            index += 1
        else:
            index += 1
    print(count)
