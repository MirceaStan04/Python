def reverse_words(sentence: str) -> str:
    """
    Inverseaza ordinea cuvintelor, pastrand literele din fiecare cuvant.
    Elimina spatiile suplimentare.
    """
    words = sentence.split()
    words.reverse()
    return " ".join(words)


if __name__ == "__main__":
    sentence = "soricel un cu joaca se pisica"
    result = reverse_words(sentence)
    print(result)
