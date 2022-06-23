#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: June 2022
# This program finds the smallest of 10 random numbers

import random


def smallest(lists):
    # this function finds the smallest in the list
    smallest = lists[0]
    list_counter = 0

    while list_counter < len(lists):
        if lists[list_counter] < smallest:
            smallest = lists[list_counter]

        list_counter = list_counter + 1

    return smallest


def main():

    random_numbers = []

    loop_counter = 0

    print("Here are the 10 numbers:")

    while loop_counter < 10:
        random_variable = random.randint(0, 100)
        random_numbers.append(random_variable)
        loop_counter = loop_counter + 1
    print("")

    # call function
    some_var = smallest(random_numbers)

    print(random_numbers)
    print("\nThe smallest of these 10 numbers is {}".format(some_var))

    print("\nDone.")


if __name__ == "__main__":
    main()
