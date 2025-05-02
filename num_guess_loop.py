#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: april, 2025
# The program generates a random correct guess.
# It then uses a loop to keep asking the user to
# guess the number until they guess correctly.
import random


def main():
    random_number = random.randint(0, 9)

    while True:
        user_num_str = input("Guess the number (between 0 and 9): ")

        try:
            user_num = int(user_num_str)
        except ValueError:
            print("{user_num} it is not an integer.")
            break

        if user_num == random_number:
            print(f"You guessed it! The number was {random_number}.")
            break
        else:
            print("Wrong guess. Try again.")


if __name__ == "__main__":
    main()
