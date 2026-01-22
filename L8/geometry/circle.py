import math

def area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Raza trebuie sa fie >= 0.")
    return math.pi * radius * radius

def circumference(radius: float) -> float:
    if radius < 0:
        raise ValueError("Raza trebuie sa fie >= 0.")
    return 2 * math.pi * radius
