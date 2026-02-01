"""
Archimedes' approximation of pi using regular polygons.

The script computes the areas of inscribed and circumscribed
regular n-gons for a unit circle (r = 1), which converge to pi
from below and above as n increases.
"""

import math

def get_valid_number_of_sides():
    while True:
        try:
            n = int(input("How many sides does your polygon have? "))
            if n < 3:
                print("Error: a polygon must have at least 3 sides.\n")
                continue
            return n
        except ValueError:
            print("Error: please enter a valid integer number.\n")

def get_precision():
    while True:
        try:
            p = int(input("How many decimal places do you want to display? "))
            if p < 0:
                print("Error: precision must be a non-negative integer.\n")
                continue
            return p
        except ValueError:
            print("Error: please enter a valid integer number.\n")

def polygon_areas(n):
    area_inscribed = (n / 2) * 1 * math.sin(2 * math.pi / n)
    area_circumscribed = n * 1 * math.tan(math.pi / n)
    
    return area_inscribed, area_circumscribed  #tuple

def run_program():
    n_sides = get_valid_number_of_sides()
    precision = get_precision()

    area_in, area_out = polygon_areas(n_sides)

    diff_in = math.pi - area_in
    diff_out = area_out - math.pi

    print()
    print(f"Inscribed polygon with {n_sides} sides: {area_in:.{precision}f}, which is {diff_in:.{precision}e} less than pi")
    print(f"Circumscribed polygon with {n_sides} sides: {area_out:.{precision}f}, which is {diff_out:.{precision}e} more than pi")

YES_ANSWERS = {"y", "yes"}

while True:
    run_program()
    print()
    choice = input("Do you want to run the program again? (y/n): " ).strip().lower()
    if choice not in YES_ANSWERS:
        break