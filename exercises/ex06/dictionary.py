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
        new_key: str = input_dict[key]  # input val is new key
        new_val: str = key  # input key is new val
        inverted_input[new_key] = new_val
    return inverted_input


def favorite_color(input_colors: dict[str, str]) -> str:
    """Returns most popular fav color in dict"""
    counter1: int = 0  # counter holding fav color amount
    counter2: int = 0  # test counter
    fav_color: str = ""  # placeholder fav color
    for name in input_colors:  # loops each name in fav color input
        test_color: str = input_colors[name]  # tests that color
        if input_colors[name] != fav_color:  # if current color not known fav
            for name2 in input_colors:  # loop again through colors
                if (
                    test_color == input_colors[name2]
                ):  # for each color, if match to test
                    counter2 += 1  # add to counter
        if counter2 > counter1:  # if new fav there more than old fav
            fav_color = test_color  # update fav
            counter1 = counter2
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
    if day in attendance:  # if day already there
        attendance[day].append(student)  # records student attendance
    else:
        attendance[day] = [student]  # otherwise adds day for that student
