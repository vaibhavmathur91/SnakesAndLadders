import random
from constants import SNAKES_LIST, LADDER_LIST


class Dice:
    def __init__(self):
        self.dice = [1, 2, 3, 4, 5, 6]

    def throw(self):
        return random.choice(self.dice)


class Position(object):
    def __init__(self, pos):
        self.pos = pos
        self.snake = False
        self.ladder = False
        self.end_of_snake = None
        self.end_of_ladder = None

    def __lt__(self, other):
        return self.pos < other.pos

    def __repr__(self):
        return str(self.pos)

    def is_ladder(self):
        return self.ladder

    def is_snake(self):
        return self.snake

    def mark_as_ladder(self, new_pos):
        self.ladder = True
        self.end_of_ladder = new_pos

    def mark_as_snake(self, new_pos):
        self.snake = True
        self.end_of_snake = new_pos

    def get_pos(self):
        return int(self.pos)


class Players:
    def __init__(self, id_number):
        self.id_number = id_number
        self.cur_pos = None
        self.has_completed = False

    def __repr__(self):
        return "player"+str(self.id_number)

    def get_id(self):
        return self.id_number

    def set_pos(self, new_id):
        self.cur_pos = new_id

    def __lt__(self, other):
        return self.id_number < other.id_number


class SnakeLadder:
    def __init__(self, size, total_players):
        self.size = size
        self.total_players = total_players
        self.board = [Position(i*10+j) for j in range(self.size) for i in range(self.size)]
        self.board.sort()
        self.players = [Players(i) for i in range(self.total_players)]
        self.players.sort()
        self.winners = []
        self.turn_index = 0
        self._add_snake()
        self._add_ladder()

    def get_winner_rank(self):
        return len(self.winners)

    def make_winner(self, player):
        print("Hurray !!  Player" + str(player.get_id()) + " comes " + str(self.get_winner_rank()+1))
        self.winners.append(player)
        player.has_completed = True

    def check_winner(self, player, cur_num):
        if cur_num > 98:
            self.make_winner(player)
            return True
        return False

    def get_winners(self):
        return self.winners

    def change_players_turn(self):
        if self.end_of_game():
            return
        self.turn_index = (self.turn_index + 1) % self.total_players
        if self.players[self.turn_index].has_completed:
            self.change_players_turn()

    def get_cur_player(self):
        return self.players[self.turn_index].get_id()

    def which_player_turn(self):
        return self.players[self.turn_index]

    def _add_snake(self):
        snake_list = random.sample(SNAKES_LIST, 5)
        for start, end in snake_list:
            self.board[start-1].mark_as_snake(self.board[end-1])

    def _add_ladder(self):
        for start, end in LADDER_LIST:
            self.board[start].mark_as_ladder(self.board[end])

    @staticmethod
    def _get_new_position(cur_pos, new_pos):
        print("enter get_new_position", cur_pos, new_pos)
        if new_pos.is_snake():
            if cur_pos == "-1":
                print("Snake bite, dropped from Start to " + str(new_pos.end_of_snake))
            else:
                print("Snake bite, dropped from " + str(cur_pos.get_pos()) + " to " + str(new_pos.end_of_snake))
            return new_pos.end_of_snake
        elif new_pos.is_ladder():
            if cur_pos == "-1":
                print("Climbed ladder from Start to " + str(new_pos.end_of_ladder))
            else:
                print("Climbed ladder from " + str(cur_pos.get_pos()) + " to " + str(new_pos.end_of_ladder))
            return new_pos.end_of_ladder
        else:
            return new_pos

    def _set_player_token_to_position(self, cur_player, cur_num):
        if cur_player.cur_pos == "-1":
            cur_player.set_pos(self._get_new_position(cur_player.cur_pos, self.board[cur_num]))
        else:
            prev_num = cur_player.cur_pos.get_pos()
            if not self.check_winner(cur_player, prev_num+cur_num):
                cur_player.set_pos(self._get_new_position(cur_player.cur_pos, self.board[prev_num+cur_num]))
        self.change_players_turn()

    def mark_the_position(self, cur_num):
        cur_player = self.which_player_turn()
        if cur_player.cur_pos is None and cur_num != 6:
            print("Try Again!! Get 6 to start\n")
            self.change_players_turn()
        elif cur_player.cur_pos is None and cur_num == 6:
            cur_player.set_pos("-1")
        else:
            self._set_player_token_to_position(cur_player, cur_num)

    def end_of_game(self):
        if self.total_players == len(self.winners):
            return True
        return False
