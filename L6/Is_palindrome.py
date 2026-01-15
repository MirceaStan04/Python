def is_palindrome(text: str) -> bool:
    """
    Verifica daca un sir este palindrom,
    ignorand literele mari si spatiile.
    """
    normalized = "".join(ch.lower() for ch in text if ch != " ")
    return normalized == normalized[::-1]


if __name__ == "__main__":
    text = "A man a plan a canal Panama"
    result = is_palindrome(text)
    print(result)
