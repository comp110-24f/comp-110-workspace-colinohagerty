"""Functions with lists for unit tests lesson"""


def get_first(input: list[str]) -> str:
    if len(input) == 0:
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    first_element: str = input[0]
    input.pop(0)
    return first_element
