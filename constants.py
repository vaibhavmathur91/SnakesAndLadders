PLAYERS = 0
BOARD_LENGTH = 10

LADDER_LIST = [(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (51, 67), (72, 91), (80, 96)]
SNAKES_LIST = [
    (36, 6), (32, 10), (17, 7), (62, 18), (48, 26), (54, 34),
    (95, 56), (62, 19), (64, 60), (97, 78), (92, 73), (98, 79)
]

HOW_TO_PLAY = """
    How to play:

        1) Each player puts their token on the start of board.
        2) Take it in turns to roll the dice. Move your token forward the number of spaces shown on the dice.
        3) If your token lands at the bottom of a ladder, you can move up to the top of the ladder.
        4) If your token lands on the head of a snake, you must slide down to the bottom of the snake.
        5) The first player to get to end of board is the winner.
"""
THROW_DICE = " Press any key to roll dice ( Press q quit to exit !!)"
