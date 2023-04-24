import random
import sys
lives = 0
heart = u'\u2764\uFE0F'
guessed_word_right = False
clue = [] 
index = 0 

def difficulty(): 
    try:
        userinput_difficulty = int(input("Valitse vaikeustaso (kirjoita 1, 2 tai 3): \n 1. Helppo\n 2. Normaali\n 3. Vaikea\nValintasi: "))
        if userinput_difficulty == 1:
            lives = 9
            return lives
        if userinput_difficulty == 2:
            lives = 6
            return lives
        if userinput_difficulty == 3:
            lives = 3
            return lives
        else:
            print("Käytä vain numeroita 1, 2 tai 3 ! Ole hyvä ja valitse vaikeustasosi uudelleen: ")
            lives = difficulty()
            return lives
    except: 
        print("Kirjaimin ei vaikeustasoa voi valita, yritä uudestaan numeroilla: ")
        lives = difficulty()
        return lives

def update_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters -= 1
        index += 1
    return unknown_letters

# salaisten sanojen nouto tekstitiedostosta: 

try:
    filename = "secret_word_list.txt"
    file = open(filename, "r")
    words_inlist = file.readlines()
    file.close()
    secret_word = random.choice(words_inlist).upper()
    secret_word = secret_word.strip("\n")
    unknown_letters = len(secret_word)
    
    while index < len(secret_word):
        clue.append("?")
        index += 1
except:
    print("Tiedostoa", filename, "ei löytynyt, tarkista tiedoston nimi.")
    sys.exit(1)
    
#PÄÄOHJELMA: Silmukka joka kyselee kokoajan kirjainta kunnes arvataan oikein tai elämät loppuvat

lives = difficulty()

try:
    while lives > 0:
        print(', '.join(clue))
        print("Henkiä jäljellä:", ' '.join(heart * lives))
        guess = input("Arvaa kirjain tai koko sana: ").upper()

        if guess == secret_word:
            guessed_word_right = True
            break
        if guess in secret_word:
            unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
        else:
            print("Väärin. Menetit yhden hengen \n")
            lives -= 1
        if unknown_letters == 0:
            guessed_word_right = True
            break
    if guessed_word_right:
        print("\n Voitit! Salainen sana oli:", secret_word , "\n")
    else:
        print("\n Hävisit! Salainen sana oli:", secret_word, "\n")
except:
    print("Tapahtui virhe, ota yhteyttä koodariin.")
