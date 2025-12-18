import random

secret = random.randint(1, 20)

tries = 5
while tries > 0:
    guess = int(input("Ghicește numărul (1-20): "))

    if guess > secret:
        print("Prea mare")
    elif guess < secret:
        print("Prea mic")
    else:
        print("Corect!")
        break

    tries = tries - 1

if tries == 0:
    print("Ai pierdut. Numărul era:", secret)
