import random
from wordslist import words

# from snowman import steps
import snowman

import colorama 
from colorama import Fore
colorama.init(autoreset=True)


def get_word():
    word = random.choice(words)
    return word.upper()


def start(word):
    """
        This function will be loaded when the start button (1) 
        is pressed from the button options
    """
    letter_dashes = '-' * len(word)
    guessed_letter = []
    lives = 6
    print(f"\n\t{Fore.BLUE}{letter_dashes}")
    print(display_snowman(lives))
    while lives > 0 and len(letter_dashes) > 0:
        secret_letter = input("please enter a letter: ").upper()
        if len(secret_letter) == 1 and secret_letter.isalpha():
            if secret_letter in guessed_letter:
                print(f"\n{Fore.CYAN}You Have Already Guessed This Letter!\n")
                print(f"{Fore.MAGENTA}Try Another Letter!")
                lives -= 1
            elif secret_letter not in word:
                print(f"\n{Fore.RED}Wrong Answer\n")
                print(f"{Fore.MAGENTA}Try Another Letter!")
                lives -= 1 
                guessed_letter.append(secret_letter)
            else:
                print(f"\n{Fore.GREEN}Correct Answer\n")
                guessed_letter.append(secret_letter)

                # changing the dashed lines to string list
                ocurences = list(letter_dashes)
                find_ocurrences = [i for i, letter in enumerate(word) if letter == secret_letter]
                for index in find_ocurrences:
                    ocurences[index] = secret_letter
                letter_dashes = "".join(ocurences)
        else:
            print(f"\n{Fore.YELLOW}Enter A Letter Between A to Z")
        print("the word is: ", word)
        # print("*****************************************************")
        print(display_snowman(lives))
        print("Word: ", letter_dashes)
        print("Guessed Letters: ", guessed_letter)
        print("lives:", lives, "\n")
    
    # condition for win and lose in the game
        if lives == 0:
            print(f"{Fore.RED}YOU LOST, Better Luck Next Time :)")
            print(f"\n{Fore.YELLOW}the correct word was: {Fore.GREEN}{word}\n")
            print(f"{Fore.YELLOW} Do you want to play again? Y/N")
            re_start()
        elif len(letter_dashes) == len(word):
            if letter_dashes == word:
                print(Fore.GREEN + snowman.WIN)
                print(f"{Fore.YELLOW}Congratulation... \n")
                print(f"{Fore.BLUE}YOU {Fore.GREEN}WON!!!\n")
                print(f"{Fore.MAGENTA}we are excited for you!\n")
                print("Do you want to play again? Y/N")
                re_start()
                     

def game_options():
    print("\n")
    print(f"\n{Fore.MAGENTA} How you want to start? ")
    print("press 1 to start the game.")
    print("press 2 to read the rules.")
    chose = input(" ")
    if chose == "1":
        start(get_word())
    elif chose == "2":
        display_rules()
    else:
        print(f"{Fore.RED}Please Choose 1 or 2")
        game_options()
        

# this function will appear at the beginning of the game
def welcome_msg():
    print(
        Fore.MAGENTA +
        """
    ||::|:||   .--------,
    |:||:|:|   |_______ /        .-.
    ||::|:|| ."`  ___  `".    {\('v')/}
    \\\/\///:  .'`   `'.  ;____`(   )'____
     \====/ './  o   o  \|~     ^" "^   //
      \\//   |   ())) .  |   Ready to   /
       ||     \ `.__.'  /|              //
       ||   _{``-.___.-'\|    Play???   /
       || _." `-.____.-'`|    ___       //
       ||`        __ \   |___/   \_______/
     ."||        (__) \    \|     /
    /   `\/       __   vvvvv'\___/
    |     |      (__)        |
     \___/\                 /
       ||  |     .___.     |
       ||  |       |       |
       ||.-'       |       '-.
       ||          |          )
       ||----------'---------'
        """
    )
    print("Welcome to the Snowman!\n")
    # keep asking for name untill S
    while True:
        name = input("What should we call you? \n") 
        if name.isalpha():
            print(f"\tWe are happy to have you {Fore.BLUE}{name}")
            print(f"\t{Fore.YELLOW}Hope you have fun and learn!")
            break
        else:
            print(f"\n{Fore.RED}You Can Only Use Alphabets (A_Z)\n")

    # Displaying game options
    game_options()    


def display_snowman(lives):

    return snowman.steps[lives]


def display_rules():
    print(snowman.RULES)
    print(f"{Fore.YELLOW} Do you want to start the game? Y/N")
    re_start()
    

def re_start():
    while True:
        y_n_answer = input("Y/N: ")
        if y_n_answer.upper() == "Y" or y_n_answer.upper() == "YES":
            start(get_word())
        elif y_n_answer.upper() == "N" or y_n_answer.upper() == "NO":
            # welcome_msg()
            exit()
        else:
            print(f"\n{Fore.RED} please enter yes or no \n")


def main():
    welcome_msg()
    re_start()    


main()
