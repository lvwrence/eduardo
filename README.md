Eduardo
=======

> Eduardo Saverin: Are you all right?

> Mark Zuckerberg: I need you.

> Eduardo Saverin: I'm here for you.

> Mark Zuckerberg: No, I need the algorithm you used to rank chess players.

Eduardo is an implementation of the Elo rating system. The expected scores of
players are calculated using the logistic curve, and the k-factor can be
parameterized.

Installation
============

    pip install eduardo

Usage
=====
    from eduardo import Elo
    elo = Elo()
    # TODO: add option for default starting elo

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
    print(lawrence.rating)
    print(garry.rating)
