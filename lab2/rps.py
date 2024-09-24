from random import randint
from time import sleep

while True:
    # 0 == Rock
    # 1 == Paper
    # 2 == Scissors
    comp_move = randint(0,2)
    plyr_move = str(input("Please enter an option [r/p/s]: ")).lower()
    allowed_moves = {"r", "p", "s"}

    if (plyr_move in allowed_moves):
        if comp_move == 0 and plyr_move == "r":
            print("It's a tie! ... :P")
        elif comp_move == 0 and plyr_move == "p":
            print("The human player wins!")
        elif comp_move == 0 and plyr_move == "s":
            print("The computer wins!")
            
        if comp_move == 1 and plyr_move == "r":
            print("The computer wins!")
        elif comp_move == 1 and plyr_move == "p":
            print("It's a tie! ... :P")
        elif comp_move == 1 and plyr_move == "s":
            print("The human player wins!")

        if comp_move == 2 and plyr_move == "r":
            print("The human player wins!")
        elif comp_move == 2 and plyr_move == "p":
            print("The computer wins!")
        elif comp_move == 2 and plyr_move == "s":
            print("It's a tie! ... :P")

    else:
        print("Please use R, P, or S.\n")
        sleep(0.025)