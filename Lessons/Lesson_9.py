"""Practice with While Loops"""


def characters(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index += 1


characters(msg="Howdy")
