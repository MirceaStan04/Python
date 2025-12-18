text = input("Introdu valori separate prin virgula: ")
parts = text.split(",")

values = []
for p in parts:
    values.append(int(p.strip()))

t = tuple(values)
print("Tupla:", t)

search = int(input("Cauta valoarea: "))

if search in t:
    index = t.index(search)
    print(search, "se regaseste in tupla la indexul", index)
else:
    print(search, "nu se regaseste in tupla")
