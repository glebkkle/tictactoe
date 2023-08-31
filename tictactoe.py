"""
Tic Tac Toe Player
"""
import copy
import math

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

    xcounter=0
    ocounter=0
    for i in range(0,len((board))):
        for j in range(0,len(board[0])):
            if board[i][j]==X:
                xcounter+=1
            elif board[i][j]==O:
                ocounter+=1
    if xcounter > ocounter:
        return O
    else:
        return X
    
    




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    
    moves=set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==EMPTY:
                tup=(i,j)
                moves.add(tup)
    return moves




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


    
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
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
    if terminal(board)==True:
        return None
    else:
        if player(board)==X:
            value,move=max_value(board)
            return move
        else:
            value,move=min_value(board)
            return move
    
def max_value(board):
    if terminal(board):
        return utility(board),None
    v=float('-inf')
    move=None
    for action in actions(board):
        val,act=min_value(result(board,action))
        if val > v:
            v=val
            move=action
            if v==1:
                return v,move
    return v,move
def min_value(board):
    if terminal(board):
        return utility(board),None
    v=float('inf')
    move=None
    for action in actions(board):
        val,act=max_value(result(board,action))
        if val < v:
            v=val
            move=action
            if v==-1:
                return v,move
    return v,move



