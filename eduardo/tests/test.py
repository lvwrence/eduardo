#from __future__ import absolute_import


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from eduardo import Elo
    else:
        from ..Elo import Elo

    # TODO: add option for default starting elo
    elo = Elo()

    # players can be of any type
    users = [1, 'hello', [5], {'name': 'lawrence'}]

    # pass a unique id to register the player
    # TODO: add optional k-factors, starting elo params
    players = [elo.create_player(id, user) for id, user in enumerate(users)]

    # now you can register results of games using player objects
    magnus = players[0]
    garry = players[1]
    bobby = players[2]
    lawrence = players[3]

    magnus.beat(bobby)
    lawrence.lost_to(garry)

    # you can also find players by id
    # elo.find(1)

    # see a player's rating
    assert(lawrence.rating == 984.0)
    assert(garry.rating == 1016.0)
