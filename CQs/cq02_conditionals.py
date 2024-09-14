"""Practicing conditionals and local variables"""

__author__ = "730574200"


def guess_a_number() -> None:
    guess: str = input("Guess a number: ")
    print("Your guess was " + guess)
    secret: int = 7
    if int(guess) == secret:
        print("You got it!")
    elif int(guess) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
