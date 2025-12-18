def inverted_index(documents):
    index = {}

    for i in range(len(documents)):
        doc = documents[i].lower()

        words = doc.split()

        for w in words:
            if w not in index:
                index[w] = set()
            index[w].add(i)

    return index


documents = [
    "pisica a stat pe covor",
    "cainele a stat în ceață",
    "pisica și câinele s-au jucat împreună"
]

print(inverted_index(documents))
