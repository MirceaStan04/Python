def count_words_in_file(filename: str) -> int:
    """
    Citeste continutul unui fisier text si
    returneaza numarul total de cuvinte.
    """
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    return len(words)


if __name__ == "__main__":
    filename = "example.txt"
    result = count_words_in_file(filename)
    print(result)
