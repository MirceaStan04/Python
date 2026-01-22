def area(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("Laturile trebuie sa fie >= 0.")
    return length * width

def perimeter(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("Laturile trebuie sa fie >= 0.")
    return 2 * (length + width)
