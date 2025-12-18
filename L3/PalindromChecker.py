def is_palindrome(word):
    return word == word[::-1]

word = input("Introdu un cuvant: ")

if is_palindrome(word):
    print("Este palindrom (True)")
else:
    print("Nu este palindrom (False)")
