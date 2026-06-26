import math


class Circle:

    def __init__(self, radius):
        """Construct the circle with a radius."""
        self.radius = radius

    def compute_area(self):
        """Compute and return the area of the circle (A = πr²)."""
        return math.pi * (self.radius**2)

    def compute_perimeter(self):
        """Compute and return the perimeter/circumference (C = 2πr)."""
        return 2 * math.pi * self.radius
user_radius = float(input("Enter the radius of the circle: "))

if user_radius >= 0:
    my_circle = Circle(user_radius)

    print(f"\nResults for a circle with radius {my_circle.radius}:")
    print(f"Area: {my_circle.compute_area():.2f}")
    print(f"Perimeter: {my_circle.compute_perimeter():.2f}")
else:
    print("Error: Radius cannot be negative.")
