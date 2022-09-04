#!/usr/bin/env python3

import bac
import sys

WELLCOME_MESSAGE = \
'''Wellcome to HIT THE GOAL game solver.
Please follow the Rules:
    Each input colors represent as Character:
        b = Blue.
        l = Light Blue.
        r = Red.
        g = Green.
        o = Orange.
        y = Yellow.
    
    Each result represent as Character:
        w = White (missed).
        b = Black (Hit).

    Please enter the colors as Order.'''

def main():
    print(WELLCOME_MESSAGE)

    #test()

def test():
    
    board = bac.Board()
    while True:
        colors = input('Enter the colors {}: '.format(bac.LEGAL_COLORS.keys()))
        if colors == 'q' or colors == '':
            print(board)
            sys.exit()
        result = input('Enter the result for the move {}: '.format(bac.LEGAL_RESULT.keys()))
        board.add_move(bac.GameMove(colors, result))


def receive_colors():
    colors = input('Enter the colors (format: {}): '.format(''.join(bac.LEGAL_COLORS.keys())))
    colors = ''.join(colors.split(' '))  # get rid of white space character.
    if len(colors) != 4:
        print ('Wrong number of input colors.\nPlease Reneter again.')
        return receive_colors()

    # NEED TO FINISH!

def receive_result():
    pass

def main1():
    print('hello world!')
    
    while True:
        move = bac.GameMove(input('Enter the colors {}: '.format(bac.LEGAL_COLORS.keys())), 'bwbw')
        print (move)

    board = bac.Board()




if __name__ == '__main__':
    main()
