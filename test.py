X = "X"
O = "O"
EMPTY = None
board=[[X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY ]]
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
    for combination in wins:
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

    if winner(board)==X or winner(board)==O:
        return True
    for i,j in board:
        if board[i][j]!=EMPTY:
            return True

    return False
