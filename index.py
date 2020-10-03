"""
Ship of fools !

Ship of fools is a simple dice game. It is played with five standard 6-faced
dice by two or more players. The game goal is to gather a 6, a 5 and a 4
(Ship, Captain and Crew) in the mentioned order. The sum of the two remaining
dice (cargo) is preferred as high as possible. The player with the highest
cargo score wins the round.

In our customized version of this game, we let players play until one of the
players scores 21 or more in total.
"""

import random

__author__ = 'Sudipto Das'
__email__ = 'dev.sudipto.das@gmail.com'


class Die(object):
    """
    A single die
    """

    def __init__(self):
        self._value = None

    def get_value(self) -> int:
        """
        Get current rolled number
        """
        return self._value

    def roll(self):
        """
        Roles the die. Sets the value of _value to the rolled number.
        """
        rolled_value = random.randint(1, 6)
        self._value = rolled_value


class DiceCup(object):
    def __init__(self):
        self._dice = []

    def value(self, index: int) -> int:
        pass

    def bank(self, index: int) -> int:
        pass

    def is_banked(self, index: int) -> int:
        pass

    def release(self, index: int):
        pass

    def release_all(self):
        pass

    def roll(self):
        pass


class ShipOfFoolsGame(object):
    def __init__(self, winning_score: int):
        self.__cup = None
        self.__winning_score = winning_score

    def round(self) -> int:
        pass


class Player(object):
    def __init__(self, name: str, score=None):
        self._name = name
        self._score = score

    def set_name(self, name: str):
        pass

    def current_score(self) -> int:
        pass

    def reset_score(self):
        pass

    def play_round(self) -> ShipOfFoolsGame:
        pass


class PlayRoom(object):
    def __init__(self):
        self._game = None
        self._player = []

    def set_game(self, game: ShipOfFoolsGame):
        """
        Assigns a new game
        :param game: A new game
        """
        self._game = game

    def add_player(self, player: Player):
        self._player.append(player)

    def reset_scores(self):
        pass

    def play_round(self):
        pass

    def game_finished(self) -> bool:
        pass

    def print_scores(self):
        pass

    def print_winner(self):
        pass


# Winning score
current_winning_score = 21

# Main script, where program starts execution
if __name__ == '__main__':
    room = PlayRoom()
    room.set_game(ShipOfFoolsGame(current_winning_score))
    room.add_player(Player('John Snow'))
    room.add_player(Player('Khalessi'))
    room.reset_scores()

    while not room.game_finished():
        room.play_round()
        room.print_scores()

    room.print_winner()
