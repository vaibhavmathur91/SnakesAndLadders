from game import SnakeLadder, Dice
from constants import BOARD_LENGTH, PLAYERS, THROW_DICE


class Main:
    def __init__(self):
        self.total_players = PLAYERS

    def execute_game(self):
        check = True
        while check:
            players_count = input("How many players between 2 and 5 ( Press q quit to exit !!)\n")
            if players_count.isdigit() and (1 < int(players_count) < 6):
                self.total_players = int(players_count)
                check = False
            elif players_count == "q" or players_count == "Q":
                break
            else:
                print("Please enter valid numbers !!")
        if self.total_players:
            snake_ladder = SnakeLadder(BOARD_LENGTH, self.total_players)
            dice = Dice()
            while True:
                input_key = input("Player"+str(snake_ladder.get_cur_player()) + THROW_DICE)
                if input_key == "q" or input_key == "Q":
                    break
                else:
                    cur_num = dice.throw()
                    print("Number on Dice is " + str(cur_num))
                    snake_ladder.mark_the_position(cur_num)
                    if snake_ladder.end_of_game():
                        break
            print("Positions of players are ", snake_ladder.get_winners())
