"""Practice with scope and global variables"""

word: str = "yoyo"


def remove_chars(msg: str, char: str) -> str:
    copy: str = ""  # cant edit string so have to set it up
    index: int = 0
    while index < len(msg):
        if msg[index] != char:  # if letter NOT char
            copy += msg[index]  # copy = copy + msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))
