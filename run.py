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
                print(f"{Fore.CYAN}You Have Already Guessed This Letter!")
                print(f"{Fore.MAGENTA}Try Another Letter!")
                lives -= 1
            elif secret_letter not in word:
                print(f"\n{Fore.RED}Wrong Answer")
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
            print(f"{Fore.YELLOW}Enter Letters Between A to Z")
        print("the word is: ", word)
        print("*****************************************************")
        print(display_snowman(lives))
        print("Word: ", letter_dashes)
        print("Guessed Letters: ", guessed_letter)
        print("lives:", lives, "\n")
    
    # condition for win and lose in the game
        if lives == 0:
            print("You lost, try again later")
            print("the correct word was: ", word)
        elif len(letter_dashes) == len(word):
            if letter_dashes == word:
                print(Fore.GREEN + snowman.WIN)
                print(f"{Fore.YELLOW}Congratulation... \n")
                print(f"{Fore.BLUE}YOU {Fore.GREEN}WON!!!\n")
                print(f"{Fore.MAGENTA}we are excited for you!\n")
                break
            

def display_rules():
    print("""
    Rules Of The Game:
        A secret word will be given.
        The user needs to find out the word.
        The user will be given specifc chances.
        If the user lose all the chances the game will 
        be over.
        if the user was able to find out the correct letters 
        for the word before losing all the chances, he will
        win the game.
    """)
    print("Do you want to start the game? Y/N")
    y_n_answer = input("Y/N: ")
    if y_n_answer.upper() == "Y":
        print("Start game")
    elif y_n_answer.upper() == "N":
        welcome_msg()
    else:
        print("please enter y/n ")


def game_options():
    print("\n~~~~~~~~~~~~~")
    print("\n How you want to start? ")
    print("press 1 to start the game.")
    print("press 2 to read the rules.")
    chose = input(" ")
    if chose == "1":
        start(get_word())
    elif chose == "2":
        display_rules()
    else:
        print("you have only two options")
        game_options()
        

# this function will appear at the beginning of the game
def welcome_msg():
    print(
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
    print("Welcome to the game!")
    # ASk username
    while True:
        name = input("What should we call you? \n") 
        if name.isalpha():
            print("We are happy to have you " + name)
            print("Hope you have fun and learn!")
            break
        else:
            print("\n plese enter string \n")

    # Displaying game options
    game_options()    




    steps = [
      """
                  /`         \  
                 /'           \`
                /'              \
   __,. -- ~~ ~|                 |~ ~~ -- . __
               |                 |
               \                 /
                `._           _.'
                   ^~- . -  ~^

      """,
      """ 
       
             _\/                 \/_
              \\   {`------'}    //
               \\  /`---/',`\\  //
                \/'     | |\ \`//
                /'      | | \/ /\
   __,. -- ~~ ~|        `\|      |~ ~~ -- . __
               |                 |
               \                 /
                `._           _.'
                   ^~- . -  ~^

      """,
      """           
                   __________       
                  /          \        
                 ()          ()        
                  \          /          
             _\/   \        /    \/_
              \\   {`------'}    //
               \\  /`---/',`\\  //
                \/'     | |\ \`//
                /'      | | \/ /\
   __,. -- ~~ ~|        `\|      |~ ~~ -- . __
               |                 |
               \                 /
                `._           _.'
                   ^~- . -  ~^

      """,
      """ 
                    .------,
                    |______|
                   _|_Ll___|_
                  [__________]          
                  /          \        
                 ()          ()        
                  \          /          
             _\/   \        /    \/_
              \\   {`------'}    //
               \\  /`---/',`\\  //
                \/'     | |\ \`//
                /'      | | \/ /\
   __,. -- ~~ ~|        `\|      |~ ~~ -- . __
               |                 |
               \                 /
                `._           _.'
                   ^~- . -  ~^

      """,
      """ 
                    .------,
                    |______|
                   _|_Ll___|_
                  [__________]         
                  /          \        
                 ()  o  o    ()        
                  \          /          
             _\/   \        /    \/_
              \\   {`------'}    //
               \\  /`---/',`\\  //
                \/'  o  | |\ \`//
                /'      | | \/ /\
   __,. -- ~~ ~|    o   `\|      |~ ~~ -- . __
               |                 |
               \    o            /
                `._           _.'
                   ^~- . -  ~^

      """,
      """ 
                    .------,
      .\/.          |______|
    _\_}{_/_       _|_Ll___|_
     / }{ \       [__________]          .\/.
      '/\'        /          \        _\_\/_/_
                 ()  o  o    ()        / /\ \
                  \ ~~~   .  /          '/\'
             _\/   \ '...'  /    \/_
              \\   {`------'}    //
               \\  /`---/',`\\  //
                \/'  o  | |\ \`//
                /'      | | \/ /\
   __,. -- ~~ ~|    o   `\|      |~ ~~ -- . __
               |                 |
               \    o            /
                `._           _.'
                   ^~- . -  ~^

      """,
    ]


def display_snowman(lives):

    return snowman.steps[lives]

welcome_msg()
get_word()
