import math

def main():
    num = 25
    angle = 30  # degrees

    sqrt_val = math.sqrt(num)
    fact_val = math.factorial(num)
    sin_val = math.sin(math.radians(angle))

    print(f"Radacina patrata a {num} este {sqrt_val}")
    print(f"Factorialul lui {num} este {fact_val}")
    print(f"Sinusul unghiului de {angle} grade este {sin_val}")

if __name__ == "__main__":
    main()
