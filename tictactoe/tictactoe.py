"""
Tic Tac Toe Player
"""

import math
from tkinter import Y

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x=0
    count_y=0
    for row in board:
        for cell in row:
            if board[row][cell]==X:
                count_x+=1
            if board[row][cell]==Y:
                count_y+=1
    if count_x==count_y:
        return Y
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions=set()
    for row in board:
        for cell in row:
            if board[row][cell]==EMPTY:
                actions.add(row,cell)
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn=player(board)
    if action not in actions(board):
        raise IndexError
    else: 
        fin_board=board[action]=turn
    return fin_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
