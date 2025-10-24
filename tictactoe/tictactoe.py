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
    for row in board:
        x=0
        if(board[row][x]==board[row+1][x])&(board[row][x]==board[row+2][x]):
            return board[row][x]
    for col in board: 
        y=0
        if(board[y][col]==board[y][col+1])&(board[y][col]==board[y][col+2]):
            return board[y][col]
    if(board[0][0]==board[1][1])&(board[0][0]==board[2][2]):
        return board[0][0]
    if(board[0][2]==board[1][1])&(board[0][2]==board[2][0]):
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True
    else: 
        count=0
        for row in board:
            for cell in row:
                if board[row][cell]==EMPTY:
                    count+=1
        if count==0:
            return True
        else: 
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    play=player(board)
    action=actions(board)
    scores=set()
    opt_action=None
    for item in actions:
        min=float('inf')
        max=float('-inf')
        next=result(board,item)
        if terminal(next)==True:
            score=utility(next)
            if score>max:
                max=score
            if score<min:
                min=score
        else:
            steps=actions(next)
            for item in steps:
                next=result(next,item)
                if terminal(next)==True:
                    score=utility(next)
                if score>max:
                    max=score
                if score<min:
                    min=score
            else:
                steps=actions(next)
                for item in steps:
                    next=result(next,item)
                    if terminal(next)==True:
                        score=utility(next)
                    if score>max:
                        max=score
                    if score<min:
                        min=score
                    else:
                        steps=actions(next)
                        for item in steps:
                            next=result(next,item)
                            if terminal(next)==True:
                                score=utility(next)
                            if score>max:
                                max=score
                            if score<min:
                                min=score
                            else:
                                steps=actions(next)
                                for item in steps:
                                    next=result(next,item)
                                    if terminal(next)==True:
                                        score=utility(next)
                                    if score>max:
                                        max=score
                                    if score<min:
                                        min=score
                                    else:
                                        steps=actions(next)
                                        for item in steps:
                                            next=result(next,item)
                                            if terminal(next)==True:
                                                score=utility(next)
                                            if score>max:
                                                max=score
                                            if score<min:
                                                min=score
                                            else:
                                                steps=actions(next)
                                                for item in steps:
                                                    next=result(next,item)
                                                    if terminal(next)==True:
                                                        score=utility(next)
                                                    if score>max:
                                                        max=score
                                                    if score<min:
                                                        min=score         
                                                    else:
                                                        steps=actions(next)
                                                        for item in steps:
                                                            next=result(next,item)
                                                            if terminal(next)==True:
                                                                score=utility(next)
                                                            if score>max:
                                                                max=score
                                                            if score<min:
                                                                min=score  
                                                            else:
                                                                steps=actions(next)
                                                                for item in steps:
                                                                    next=result(next,item)
                                                                    if terminal(next)==True:
                                                                        score=utility(next)
                                                                    if score>max:
                                                                        max=score
                                                                    if score<min:
                                                                        min=score                
        if player==X:
            scores.add(min)
        elif player==Y:
            scores.add(max)
    list_act=list(actions(board))
    list_scores=list(scores)
    opt=scores[1]
    if player==X:
        for item in scores:
            if item>opt:
                opt_action=list_act[list_scores.index(item)]
    elif player==Y:
        for item in scores:
            if item>opt:
                opt_action=list_act[list_scores.index(item)]
    return opt_action
