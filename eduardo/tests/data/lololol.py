import random

with open('players.txt', 'r') as f:
    players = [line.rstrip() for line in f.readlines()]

    for _ in range(500):
        player1 = random.choice(players)
        player2 = player1
        while player1 == player2:
            player2 = random.choice(players)

        print player1 + ">" + player2
