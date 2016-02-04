from __future__ import division
import math

q = lambda rating: math.pow(10, rating / 400)

def new_score(winner_rating, loser_rating, k_factor):
    winner_expected_score = q(winner_rating) / (q(winner_rating) + q(loser_rating))
    loser_expected_score = q(loser_rating) / (q(winner_rating) + q(loser_rating))

    winner_new_score = winner_rating + (k_factor * (1 - winner_expected_score))
    loser_new_score = loser_rating + (k_factor * (0 - loser_expected_score))

    return winner_new_score, loser_new_score
