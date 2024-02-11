#!/usr/bin/python3

def calculate_area(radius):
    """
    Calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2


def main():
    radius = 5.0
    area = calculate_area(radius)
    print(f"The area of the circle with radius {radius} is {area:.2f}")


if __name__ == "__main__":
    main()

