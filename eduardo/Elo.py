K_FACTOR = 30

class Elo:
    def __init__(self):
        self.players = []

    def create_player(self, value):
        new_player = _Player(value)
        self.players.append(new_player)

        return new_player

    def find(self):
        raise NotImplementedError


class _Player:
    def __init__(self, kvalue):
        self.value = value
        self.rating = 1000
        self._k_factor = K_FACTOR

    def beat(self, other_player):
        pass

    def lost_to(self, other_player):
        pass
