while True:
    try:
        celsius = float(input("Introdu temperatura in grade Celsius: "))
        break
    except ValueError:
        print("Input invalid. Introdu un numar real.")

fahrenheit = celsius * 9 / 5 + 32
print("Temperatura in Fahrenheit este:", fahrenheit)
