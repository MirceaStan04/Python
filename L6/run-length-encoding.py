def run_length_encoding(text: str) -> str:
    """
    Comprima sirul folosind Run-Length Encoding (RLE).
    """
    if not text:
        return ""

    result = []
    current = text[0]
    count = 1

    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            result.append(f"{current}{count}")
            current = ch
            count = 1

    result.append(f"{current}{count}")
    return "".join(result)


if __name__ == "__main__":
    text = "aaabbbbcccdde"
    result = run_length_encoding(text)
    print(result)
