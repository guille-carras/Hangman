
from logging import exception
from operator import ne
import random
import os


HANGMAN_IMAGES = ['''

                                                    +---+
                                                    |   |
                                                        |
                                                        |
                                                        |
                                                        |
                                                  =========''', '''
                                                 
                                                    +---+
                                                    |   |
                                                    O   |
                                                        |
                                                        |
                                                        |
                                                  =========
                                               Acierta, ¡carajo!''', '''
                                                 
                                                    +---+
                                                    |   |
                                                    O   |
                                                    |   |
                                                        |
                                                        |
                                                  =========
                                              ¡Ave María purísima!''', '''
                                                 
                                                    +---+
                                                    |   |
                                                    O   |
                                                   /|   |
                                                        |
                                                        |
                                                  =========
                                ¡Definitivamente no me voy a tomar las frías el FDS!''', '''
                                                 
                                                    +---+
                                                    |   |
                                                    O   |
                                                   /|\  |
                                                        |
                                                        |
                                                  =========
                                       ¡Me tocó el más manco de todos!''', '''
                                                 
                                                    +---+
                                                    |   |
                                                    O   |
                                                   /|\  |
                                                   /    |
                                                        |
                                                  =========
                                        ¡No te pondré en el testamento!''', '''
                                                 
                                                    +---+
                                                    |   |
                                                    O   |
                                                   /|\  |
                                                   / \  |
                                                        |
                                                  =========
                                              ¡Gracias por nada! ''']


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


def clean_screen(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def play_again():
    repeat = input("Quieres volver a jugar, presiona [S]í o [No]: ").lower()
    if repeat ==  "s":
        main()
    else:
        print("¡Nos vemos luego!")



def print_head(count_wrong):
    label_head = """
 __      __        _                              _             _  _                                            
 \ \    / /  ___  | |  __   ___   _ __    ___    | |_   ___    | || |  __ _   _ _    __ _   _ __    __ _   _ _  
  \ \/\/ /  / -_) | | / _| / _ \ | '  \  / -_)   |  _| / _ \   | __ | / _` | | ' \  / _` | | '  \  / _` | | ' \ 
   \_/\_/   \___| |_| \__| \___/ |_|_|_| \___|    \__| \___/   |_||_| \__,_| |_||_| \__, | |_|_|_| \__,_| |_||_|
                                                                                    |___/                       
"""
    print(label_head)
    print("=" *46 + " Adivina la palabra " + "="*47)
    print(HANGMAN_IMAGES[count_wrong],"\n")

def comprube(letter, keyword, count_w, hidden):
    if letter in keyword:
        index = []
        for i in range(len(keyword)):
            if letter == keyword[i]:
                index.append(i)
        hidden = [i for i in hidden]
        for i in index:
            hidden[i] = letter
        hidden = " ".join(hidden)
        hidden = hidden.replace(" ", "")
        return hidden, count_w
    else:
        count_w = count_w + 1
        return hidden, count_w


def main():
    win = False
    lose = False
    count_wrong = 0
    secret_word = read_data_search_keyword()
    hidden = lines(secret_word)
    while win == False and lose == False:
        print_head(count_wrong)
        print("+"*50 + "   " + hidden + "   " +"+"*50)
        letter = input("Escriba una letra: ").lower()
        if letter == "*":
            break
        hidden = comprube(letter, secret_word, count_wrong, hidden)
        count_wrong = int(hidden[1])
        hidden = hidden[0]
        if hidden == secret_word:
            win = True
        elif count_wrong > len(HANGMAN_IMAGES) - 1:
            lose = True
        clean_screen()
    if win == True:
        print(f"¡Ganaste!, la palabra era '{secret_word}'.")
        play_again()
    elif lose == True:
        print(f"¡Perdiste!, la palabra era '{secret_word}'.")
        play_again()
        


if __name__ == "__main__":
    main()