"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "7305742000"


def input_word() -> str:
    """asks user for word and checks length"""
    word: str = input("Enter a 5-character word: ")  # variable from user input
    if len(word) == 5:  # checks length=5
        return word
    else:  # error if length not 5
        print("Error: Word must contain 5 characters.")
        exit()  # put here so that we exit only if the length isn't correct


def input_letter() -> str:
    """asks user for letter and checks length"""
    letter: str = input("Enter a single character: ")  # user inputs letter
    if len(letter) == 1:  # checking to see if only 1 letter
        return letter  # have to include these in then block
    else:  # error if not only 1 letter
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """searches for input letter in word of choice, and how many times it shows up"""
    print("Searching for " + letter + " in " + word)
    instances: int = 0  # variable used for counting
    if word[0] == letter:
        print(letter + " found at index 0")
        instances = instances + 1  # each time you enter an if block, instances grows
    if word[1] == letter:  # cant use elif here since it wouldn't check every index
        print(letter + " found at index 1")
        instances = instances + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        instances = instances + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        instances = instances + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        instances = instances + 1
    if instances > 0:  # use another if here to print the instances if there are any
        print(str(instances) + " instances of " + letter + " found in " + word)
    else:  # only else at the end otherwise you'd leave the function early
        print("No instances of " + letter + " found in " + word)
        return None


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
