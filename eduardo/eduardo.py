from __future__ import division
import math

K_FACTOR = 32

class Elo:
    def __init__(self):
        self.players = []

    def create_player(self, key, value):
        new_player = _Player(key, value)
        self.players.append(new_player)

        return new_player

    def find(self):
        raise NotImplementedError


class _Player:
    # TODO: add logging and recalculate from the logging (dirty checking?)
    def __init__(self, id, value):
        self_id = id
        self.value = value
        self.rating = 1000
        self._k_factor = K_FACTOR

    def _q(self):
        # TODO: give explanation of this
        return math.pow(10, self.rating / 400)

    def _beat(self, opponent):
        # TODO: give explanation of this
        my_expected_score = self._q() / (self._q() + opponent._q())
        opponent_expected_score = opponent._q() / (self._q() + opponent._q())

        my_new_score = self.rating + (K_FACTOR * (1 - my_expected_score))
        opponent_new_score = opponent.rating + (K_FACTOR * (0 - opponent_expected_score))

        self.rating = my_new_score
        opponent.rating = opponent_new_score

    def beat(self, opponent):
        self._beat(opponent)

    def lost_to(self, opponent):
        opponent._beat(self)
