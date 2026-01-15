def filter_lines(input_file: str, output_file: str, keyword: str) -> None:
    """
    Creeaza un fisier care contine doar liniile
    ce includ un cuvant cheie specific.
    """
    with open(input_file, "r", encoding="utf-8") as fin:
        lines = fin.readlines()

    with open(output_file, "w", encoding="utf-8") as fout:
        for line in lines:
            if keyword in line:
                fout.write(line)


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "filtered.txt"
    keyword = "Python"
    filter_lines(input_file, output_file, keyword)
    print("Fisierul filtered.txt a fost creat.")
