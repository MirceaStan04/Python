def word_frequency(text):
    text = text.lower()

    punct = ".,!?;:()\"'"
    for ch in punct:
        text = text.replace(ch, " ")

    words = text.split()

    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return freq


text = "Ana si Maria au plecat la mare. Maria are rau de mare."
print(word_frequency(text))
