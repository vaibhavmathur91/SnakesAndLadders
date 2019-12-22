from play import Main
from constants import HOW_TO_PLAY


if __name__ == "__main__":
    print()
    while True:
        inp = int(input("""
        1) How to play
        2) Start game
        3) Quit
        """))
        if 1 == inp:
            print(HOW_TO_PLAY)
        elif 2 == inp:
            Main().execute_game()
        elif 3 == inp:
            break
        else:
            print("Wrong choices, Try Again !!")
