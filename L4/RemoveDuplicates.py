text = input("Introdu numere separate prin virgula: ")
parts = text.split(",")

numbers = []
for p in parts:
    numbers.append(int(p.strip()))

unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)

print("Lista fara duplicate:", unique)
