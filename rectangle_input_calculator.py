#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program will calculate the Area and Perimeter of a determined rectangle.


def main():
    length = int(input("Enter the length of rectangle (mm): "))
    width = int(input("Enter the width of rectangle (mm): "))

    area = length*width
    perimeter = 2*(length+width)

    print("")
    print("Area is {}mm^2".format(area))
    print("Perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
