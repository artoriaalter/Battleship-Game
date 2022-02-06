from class_library import *

def start_screen():
    print("""
    Welcome to Artoria Alter's very first portfolio project! This program is a terminal battleship game that is played with 2 people,
    or against a super intelligent bot(just kidding)
    Please choose the game type you want!
    1- 2 players
    2- Against a bot
    """)
    choice = int(input())

    if choice == 1:
        player_1_name = input("Enter player 1's name")
        player_2_name = input("Enter player 2's name")

        player_1 = Player(player_1_name)
        player_2 = Player(player_2_name)
    elif choice == 2:
        player_1_name = input("Enter player 1's name")

        player_1 = Player(player_1_name)
        player_2 = Bot("Super Intelligent Bot")


    return Game(player_1, player_2)

def placement():
    for player in Game.turn_list:
        Game.input_placement(player)


Game = start_screen()

placement()
