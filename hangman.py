
import random

def read_data_search_keyword():
    try:
        with open("./Data/data.txt", "r", encoding="utf-8") as f:
            all_text = f.read()
            all_text = all_text.split("\n")
            keyword = random.choice(all_text)
            trans = keyword.maketrans("áéíóú", "aeiou")
            keyword = keyword.translate(trans)
    finally:
        f.close()
    return keyword


def lines(keyword):
    list = ["-" for i in keyword]
    list = "".join(list)
    return list


def main():
    pass


if __name__ == "__main__":
    main()