def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result = result * i
        i = i + 1
    return result

n = int(input("Introdu un numar intreg: "))

print("Factorialul este:", factorial(n))
