
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
    print("How you want to start? ")
    print("press 1 to start the game.")
    print("press 2 to read the rules.")
    chose = input(" ")
    if chose == "1":
        print("staring game..")
    elif chose == "2":
        display_rules()
    else:
        print("you have only two options")


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


welcome_msg()