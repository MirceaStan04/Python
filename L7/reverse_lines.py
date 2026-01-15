def reverse_lines(input_file: str, output_file: str) -> None:
    """
    Creeaza un fisier nou in care fiecare rand
    este scris invers (caracterele inversate).
    """
    with open(input_file, "r", encoding="utf-8") as fin:
        lines = fin.readlines()

    with open(output_file, "w", encoding="utf-8") as fout:
        for line in lines:
            fout.write(line.rstrip("\n")[::-1] + "\n")


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    reverse_lines(input_file, output_file)
    print("Fisierul output.txt a fost creat.")
