from __future__ import division
import math

STARTING_ELO = 1000
K_FACTOR = 32

class Environment:
    """The environment to initialize. Implements create_player() and find().

    :Example:
    >>> 
    """

    def __init__(self, starting_elo=STARTING_ELO, k_factor=K_FACTOR):
        self.starting_elo = starting_elo
        self.k_factor = k_factor
        self._players = {}
        self._games = []

    @property
    def players(self):
        return self._players

    @property
    def games(self):
        return self._games

    def create_player(self, key, value=None):
        """Creates a new entity in the environment (called players) and
        initializes it with the default elo and k-factor. Also injects this
        environment into the player, so it can access the games it's played.

        :param key: key that we can locate the player by.
        :param value: 
        :return: a Player entity
        """
        new_player = _Player(key, value, env, self.starting_elo, self.k_factor)
        self._players[key] = new_player
        return new_player

    def find_player(self, key):
        """Finds a player by key."""
        return self._players[key]

    def log_game(winner, loser):
        self._games.append(Game(winner, loser))


class _Game:
    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser


class _Player:
    # TODO: add logging and recalculate from the logging (dirty checking?)
    def __init__(self, id, value, env, starting_elo, k_factor):
        self_id = id
        self.value = value
        self._env = env
        self._starting_elo = starting_elo
        self._k_factor = K_FACTOR

    @property
    def rating(self):
        # recalculate ratings from games here
        pass

    def _q(self):
        # TODO: give explanation of this
        return math.pow(10, self.rating / 400)

    def _beat(self, opponent):
        # TODO: give explanation of this
        my_expected_score = self._q() / (self._q() + opponent._q())
        opponent_expected_score = opponent._q() / (self._q() + opponent._q())

        my_new_score = self.rating + (self._k_factor * (1 - my_expected_score))
        opponent_new_score = opponent.rating + (self._k_factor * (0 - opponent_expected_score))

        self.rating = my_new_score
        opponent.rating = opponent_new_score

    def beat(self, opponent):
        self._beat(opponent)

    def lost_to(self, opponent):
        opponent._beat(self)

# how to export this properly?
eduardo = Environment
