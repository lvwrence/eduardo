Eduardo
=======

![](https://45.media.tumblr.com/b3d6a7ef75e2bf2f64dfd9171b207d81/tumblr_mk8vcuNso71qhd14co1_500.gif)

Eduardo is an implementation of the Elo rating system. The expected scores of
players are calculated using the logistic curve, and the k-factor can be
parameterized.

Installation
============
    pip install eduardo

Testing
=======
    python eduardo/tests/test.py

Usage
=====
```python
# default elo is 1000 and default k-factor is 32
chess_world = Elo()

# pass a unique, immutable value to register the player
names = ['magnus', 'garry', 'bobby', 'lawrence']
chess_players = [chess_world.create_player(name) for name in names]

# register results of games using player objects
magnus, garry, bobby, lawrence = chess_players
magnus.beat(bobby)
lawrence.lost_to(garry)

assert lawrence.rating == 984.0
assert garry.rating == 1016.0

# find players by id
assert chess_world.find_player('lawrence') == lawrence

# get all players as a dict
assert chess_world.players == {'bobby': bobby, 'garry': garry, 'lawrence': lawrence, 'magnus': magnus}


# modify defaults: higher k-factor means higher sensitivity
photo_world = Elo(starting_elo=1400, k_factor=16)

# use log_game to record batches of games
with open('data/players.txt', 'r') as players, open('data/games.txt', 'r') as games:
    urls = [line.rstrip() for line in players.readlines()]
    photo_players = [photo_world.create_player(url) for url in urls]

    games = [line.rstrip() for line in games.readlines()]
    for winner, loser in [game.split('>') for game in games]:
        photo_world.log_game(winner, loser)
```
