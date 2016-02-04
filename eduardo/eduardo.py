from collections import defaultdict
from utils import new_score

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
        self.players = {}
        self._games = []

    @property
    def gamestate(self):
        return _Gamestate(self._games, self.starting_elo, self.k_factor)

    def create_player(self, id):
        """Creates a new entity in the environment (called players) and
        initializes it with the default elo and k-factor. Also injects this
        environment into the player, so it can access the games it's played.

        :param id: key that we can locate the player by.
        :return: a Player entity
        """
        new_player = _Player(id, self)
        self.players[id] = new_player
        return new_player

    def find_player(self, id):
        """Finds a player by id."""
        return self.players[id]

    def log_game(self, winner, loser):
        self._games.append(_Game(winner, loser))


class _Game:
    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser


class _Gamestate:
    def __init__(self, games, starting_elo, k_factor):
        self.state = self.calculate_state(games, starting_elo, k_factor)

    def calculate_state(self, games, starting_elo, k_factor):
        if not games:
            return defaultdict(lambda: starting_elo)

        # can we use a generator here?
        prev_state = self.calculate_state(games[:-1], starting_elo, k_factor)
        return self._new_state(prev_state, games[-1], k_factor)

    def _new_state(self, prev_state, game, k_factor):
        winner = game.winner
        loser = game.loser

        new_state = prev_state.copy()
        new_state[winner], new_state[loser] = new_score(prev_state[winner], prev_state[loser], k_factor)
        return new_state


class _Player:
    def __init__(self, id, env):
        self._id = id
        self._env = env

    def __repr__(self):
        return str(self.rating)

    @property
    def rating(self):
        return self._env.gamestate.state[self._id]

    def _beat(self, opponent):
        self._env.log_game(self._id, opponent._id)

    def beat(self, opponent):
        self._beat(opponent)

    def lost_to(self, opponent):
        opponent._beat(self)


Elo = Environment
