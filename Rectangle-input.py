#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sept 2021
# This is a program that calculates the area and perimiter of a rectangle with user input.


def main():
    # This is a program that calculates the area and perimiter of a rectangle.

    # input
    length = int(input("Enter Length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print(" area is {0}mm².".format(area))
    print(" perimeter is {0}mm.".format(perimeter))


if __name__ == "__main__":
    main()
