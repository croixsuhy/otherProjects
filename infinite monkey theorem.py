from string import ascii_lowercase
from random import choice

"""
Infinite Monkey Theorem
By Croix Suhy

Infinite monkey theorem states that if a monkey presses random buttons infinitely on a keyboard,
it will eventually get to the end result.
"""


########################################################################
# Insert word/sentence below (note: you can only letters and spaces)
# Note the longer the string is, it will take longer
string = "monkey"

# Turn this variable to True to see what's going on in the background
UNDER_THE_HOOD = False
########################################################################


STRING = string.lower()

# ASCII library for convenience
# Generates characters
CHARS = ascii_lowercase + " "


def random():
    global randomString

    # Randomly adds characters to string that are the same size as the user imputed string
    for i in range(len(STRING)):
        randomString += choice(CHARS)


def main():
    global randomString

    # Random string, will be completely randomized
    randomString = ""

    print("Monkey is currently banging the keyboard...")

    while True:
        try:
            # While the string isn't equal to the user imputed string,
            # it will clear the variable and run the randomizer again
            if randomString != STRING:
                if UNDER_THE_HOOD:
                    print(randomString)
                randomString = ""
                random()
            else:
                # When its completed, the loop will end
                print(f"Completed: {randomString}")
                break

        except RuntimeError:
            print("Can not randomize")


if __name__ == "__main__":
    main()
