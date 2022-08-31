#!/usr/bin/env python3.8

from itertools import permutations


'''
The game has 6 available colors:
    1. Blue.
    2. White Blue.
    3. Green.
    4. Red.
    5. Orange.
    6. Yellow.

'''

SIZE = 4  # number of guessing colors.
COLORS = 6  # number of possible colors.

class GameMove():

    '''
    represent every move in the game.
    '''

    def __init__(self, guess, result):
        self.guess = guess
        self.result = result


def init_options():
    psb = permutations(range(COLORS), SIZE)
    return psb

def sub_option(options, move):
    pass 


class Board():

    '''
    board class for represent the board game.
    '''

    def __init__(self):
        self.moves = []
        self.option = init_options()

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def add_result(self):
        '''
        Add the last action result.
        '''

    def calculate_solution(self):
        '''
        Calculate Solution for the next move in the board.
        '''

    def next_move(self):
        '''
        Calculte what the best option for the next move.
        '''
