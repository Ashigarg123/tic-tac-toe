"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_turn = 0
    o_turn = 0
    for i in board:
        for j in i:
            if j=="X":
                x_turn+=1
            elif j=="O":
                o_turn+=1
    if o_turn <= x_turn:
        return O
    else:
        return X


    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_1=set()
    #have an empty set
    #enumerate through the cells and row to check if they are empty
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                action_1.add((i,j))
    return action_1

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #check if action is valid or not
    if terminal(board):
        raise ValueError("Play again!")
    elif action not in actions(board):
        raise Exception("Invalid Action!!!")
    else:
        new_board = copy.deepcopy(board)
        #print(result)
        new_board[action[0]][action[1]]=player(new_board)
        (i, j) = action
        new_board[i][j] = player(board)
        #print(new_board)

    return new_board

    #create a new board copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #find all the possible ways a user can win the game
    ways_to_win=[[(0,0),(0,1),(0,2)],
                [(1,0),(1,1),(1,2)],
                [(2,0),(2,1),(2,2)],
                [(0,2),(1,1),(2,0)],
                [(0,0),(1,0),(2,0)],
                [(0,2),(1,2),(2,2)],
                [(0,1),(1,1),(2,1)],
                [(0, 0), (1, 1), (2, 2)],]
  #now check which user made 3 moves same as above combination
  #then declare the winner
    for combination in ways_to_win:
        x_turn = 0
        o_turn = 0
        for i, j in combination:
            if board[i][j] == X:
                x_turn += 1
            if board[i][j] == O:
                o_turn += 1
        if x_turn == 3:
            return X
        if o_turn == 3:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if winner(board) is not None or not actions(board):
       #return True
    #else:
        #return False
    if (winner(board) == X):
        return True
    elif (winner(board) == O):
        return True

    for i in range(3):
        for j in range(3):
            if  board[i][j] == None:
                return False
    return True


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
    #if terminal(board)==True:


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if board == [[EMPTY]*3]*3:
        return (0,0)
    if player(board)==X:
        v = float('-inf')
        final_action=None
        for action in actions(board):
            finalResult = minValue(result(board, action))
            if finalResult > v:
                v = finalResult
                final_action = action
    elif player(board)==O:
        v = float('inf')
        final_action=None
        for action in actions(board):
            finalResult = maxValue(result(board, action))
            if finalResult < v:
                v = finalResult
                final_action = action
    return final_action

def maxValue(board):

    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v=max(v, minValue(result(board,action)))

    return v

def minValue(board):

    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v=min(v, maxValue(result(board,action)))

    return v
