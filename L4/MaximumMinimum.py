text = input("Introdu numere separate prin virgula: ")
parts = text.split(",")

numbers = []
for p in parts:
    numbers.append(int(p.strip()))

print("Minimul este:", min(numbers))
print("Maximul este:", max(numbers))
