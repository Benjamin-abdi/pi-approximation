"""
Archimedes' approximation of pi using regular polygons.

The script computes the areas of inscribed and circumscribed
regular n-gons for a unit circle (r = 1), which converge to pi
from below and above as n increases.
"""

import math

def polygon_areas(n):
    area_inscribed = (n / 2) * 1 * math.sin(2 * math.pi / n)
    area_circumscribed = n * 1 * math.tan(math.pi / n)
    
    return area_inscribed, area_circumscribed  #tuple

n_sides = int(input("How many sides does your polygon have? "))

area_in, area_out = polygon_areas(n_sides)


diff_in = math.pi - area_in
diff_out = area_out - math.pi

print(f"Inscribed polygon with {n_sides} sides: {area_in:.6f}, which is {diff_in:.6e} less than pi")
print(f"Circumscribed polygon with {n_sides} sides: {area_out:.6f}, which is {diff_out:.6e} more than pi")

input("\nPress Enter to exit...")