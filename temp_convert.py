#!/usr/bin/env python3

# Created by Alexander Matheson
# Created on Jan 18 2022
# This program converts celsius to fahrenheit

# this function converts celsius to fahrenheit
def calculate_fahenheit():
    user_string = input("Enter the temperature in celsius: ")
    try:
        celsius = int(user_string)
    except Exception:
        print("Invalid input.")
    else:
        fahrenheit = (9.0 / 5.0) * celsius + 32
        print("{} degrees celsius in fahrenheit is {}"
              . format(celsius, fahrenheit))


def main():
    calculate_fahenheit()


if __name__ == "__main__":
    main()
