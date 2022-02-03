import random
from operator import *

from common.common_global import *

is_play_again = True


def mechanics():
    choices = ["rock", "paper", "scissors"]
    resultMsg = ""
    computer = ""
    player = None

    def check_patter_win():
        nonlocal player, choices, resultMsg, computer

        def checker(guess1, guess2):

            validatation_win = {
                # Computer First | Player Second
                "rock_lose_scissors": [guess2, guess1],
                "rock_win_paper": [guess2, guess1],
                "rock_tie_rock": [guess2, guess1],

                "paper_lost_rock": [guess2, guess1],
                "paper_win_scissors": [guess2, guess1],
                "paper_tie_paper": [guess2, guess1],

                "scissors_lost_paper": [guess2, guess1],
                "scissors_win_rock": [guess2, guess1],
                "scissors_tie_scissors": [guess2, guess1],

            }

            for key, value in validatation_win.items():
                get_res = key.split("_")[1]
                get_ops_1 = key.split("_")[0]
                get_ops_2 = key.split("_")[2]

                if (value[0] == get_ops_1 and value[1] == get_ops_2):
                    #  my_logger(f'{get_ops_1} {get_ops_2} {get_res}')
                    return f'You are {get_res}'

        computer = random.choice(choices)
        my_logger(f'Player Guess : {player}')
        my_logger(f'Computer Guess : {computer}')

        resultMsg = checker(player, computer)
        my_logger(f'{resultMsg}')

    def input_handler():
        nonlocal player, choices, resultMsg
        while player not in choices:
            player = input("Rock, Paper, Scissors : ").lower()
        check_patter_win()

    input_handler()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mechanics()
    while is_play_again:
        play_again = input("You want to play again ? Y/N : ").lower()
        if ["yes", "y"].__contains__(play_again):
            mechanics()
            is_play_again = True
        else:
            is_play_again = False
            my_logger(f'Thanks!')
            break
