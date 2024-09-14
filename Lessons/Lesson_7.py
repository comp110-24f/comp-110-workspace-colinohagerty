"""Practice with Conditionals"""

# def less_than_10(num1: int) -> None:
# """tell me if num is < 10"""
# if num1 < 10:
# print("Small number!")
# else:
# print("Big number!")
# print("Have a nice day!")


# def should_I_eat(hungry: bool) -> None:
# """Tells me whether or not to eat based on hunger"""
# if hungry:
# print("Eat!")  # then block
# else:
# print("Go on with your day, dipshit")  # else block
# print("I'm proud of you")  # either way, be kind to yourself


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:  # remember to use == not = since you aren't
        # assigning word a value letter
        return "match!"  # then block
    else:
        return "no match!"  # else block


print(check_first_letter(word="happy", letter="s"))
