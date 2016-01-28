Eduardo
=======

> Eduardo Saverin: Are you all right?

> Mark Zuckerberg: I need you.

> Eduardo Saverin: I'm here for you.

> Mark Zuckerberg: No, I need the algorithm you used to rank chess players.

Eduardo is an implementation of the Elo rating system. The expected scores of
players are calculated using the logistic curve, and the k-factor can be
parameterized.

Usage
=====
    from eduardo import Elo
    # TODO: add option for default starting elo
    elo = Elo()

    # players can be any type
    users = [1, 'hello', [5], {name: 'lawrence'}]

    # pass a unique id to register the player
    # TODO: add optional k-factors, starting elo params
    players = map(elo.create_player(id, user) for user in enumerate(users))

    # now you can register results of games using player objects
    magnus = players[0]
    garry = players[1]
    bobby = players[2]
    lawrence = players[3]

    magnus.beat(bobby)
    lawrence.lost_to(garry)

    # you can also find players by id
    elo.find(1)

    # see a player's rating
    lawrence.rating # 960
