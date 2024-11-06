"""Exercise 06 focused on applications of dictionaries"""

__author__ = "730574200"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Make keys of input dict the values and vice versa"""
    inverted_input: dict[str, str] = {}  # initialize empty return dict
    new_key: str = ""  # initialize inverted key
    new_val: str = ""  # initialize inverted val
    for key in input_dict:  # loop through input keys
        for new_key in inverted_input:  # loop through keys in inverted dict
            if (
                input_dict[key] == new_key
            ):  # if the input val (later inverted key) matches prev inverted key
                raise KeyError("Oops! You can't have two of the same keys")
        new_key = input_dict[key]  # input val is new key
        new_val = key  # input key is new val
        inverted_input[new_key] = new_val
    return inverted_input


def favorite_color(input_colors: dict[str, str]) -> str:
    """Returns most popular fav color in dict"""
    counter_dict: dict[str, int] = {}  # tracks frequency of each color
    fav_color: str = ""  # placeholder fav color
    for name in input_colors:  # for each name
        color = input_colors[name]
        if color in counter_dict:  # if there already, add to count
            counter_dict[color] += 1
        else:
            counter_dict[color] = 1  # if not in counter, start counting
    max_count: int = 0  # placeholder max
    for color in counter_dict:  # goes through counted colors
        if counter_dict[color] > max_count:
            fav_color = color  # says that higher frequency color is fav
            max_count = counter_dict[color]  # sets max count for that color
    return fav_color


def count(input_list: list[str]) -> dict[str, int]:
    """Create dict counting how many times strings are in list"""
    count_dict: dict[str, int] = {}  # initialize empty dict
    for elem in input_list:  # loop input list
        if elem in count_dict:  # if already in dict
            count_dict[elem] += 1  # count it
        else:
            count_dict[elem] = 1  # otherwise, make new key and start count
    return count_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Returns dict of all words in input by starting letter"""
    alphabetical_dict: dict[str, list[str]] = {}  # initializes empty dict
    for word in input_list:  # loops words in input
        test_word = word.lower()  # allows for all to be lowercase in checking
        starting_letter: str = test_word[0]  # starting letter of given word in list
        if starting_letter in alphabetical_dict:  # if already there
            alphabetical_dict[starting_letter].append(word)  # append the list value
        else:
            alphabetical_dict[starting_letter] = [
                word
            ]  # otherwise start the list for that letter
    return alphabetical_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """updates attendance log with new student and day of school"""
    if day in attendance:  # checks if already have role for that day
        for person in attendance[day]:  # if so, checks to see if they're already there
            if student == person:
                return None  # duplicate name quits the function
        attendance[day].append(student)  # otherwise mark student present
    else:
        attendance[day] = [student]  # if not started that day's role
