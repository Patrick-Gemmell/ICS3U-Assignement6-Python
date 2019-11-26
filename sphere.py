#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: november 2019
# This show two functions

import math


def calculate_radius(volume):
    # process
    radius = (3*(volume/(4*math.pi)))**(1/3)

    return radius


def main():
    # calling functions and inputs
    while True:
        volume_user_string = input("Enter the volume of the\
                                    sphere: (integer) ")

        try:
            volume_user_int = int(volume_user_string)
            radius = calculate_radius(volume_user_int)

            print("The area is {0}".format(radius))
            break
        except Exception:
            print("that is an invalid integer")


if __name__ == "__main__":
    main()
