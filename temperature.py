#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program prints the celsius temperature in fahrenheit
#   user inputs celsius

import math


def fahrenheit():
    # This function prints the celsius temperature in fahrenheit

    # input
    celsius_string = input("Enter the temperature in celsius: ")

    # process/output
    try:
        celsius = int(celsius_string)
        Tf = (9 / 5) * celsius + 32
        print("The temperature in fahrenheit is {}°F".format(Tf))
    except Exception:
        print("{} is not an integer".format(celsius_string))


def main():
    # this function just calls other functions

    fahrenheit()


if __name__ == "__main__":
    main()
