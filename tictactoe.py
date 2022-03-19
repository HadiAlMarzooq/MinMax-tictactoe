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
    counter = 0
    for i in range(3):  # [0,1,2]
        for j in range(3):  # [0,1,2]
            # if it wasn't empty
            if board[i][j] != EMPTY:
                counter += 1
    # X Starts first.
    if board == initial_state():
        return X
    # since X starts first, his turn during the game is basically the odd turn counter, for example:
    # If X starts the  game, his turn index is 1, then O plays for 2, then X takes 3 and etc, which concludes
    # the theory.
    if counter % 2 == 1:
        return O
    # if counter wasn't odd, then it was O's turn, so now its X's turn.
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # empty set
    possibleActions = set()
    for i in range(3):
        for j in range(3):
            # If empty, then add index (i, j) to the possible actions.
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making possibleMove (i, j) on the board.
    """
    # if action not in actions(board):
    #     raise Exception("Invalid action :(")
    # # copy library to make a deepcopy as documented.
    # board2 = copy.deepcopy(board)
    # # returning the result in a new board, so that the original board isn't modified.
    # board2[action[0]][action[1]] = player(board)
    # return board2
    if action not in actions(board):
        raise Exception("Invalid Action!!!")

    b2 = copy.deepcopy(board)
    b2[action[0]][action[1]] = player(board)
    
    return b2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # As the documentation says, One can win the game with three of their possibleMoves in a row horizontally, vertically, or diagonally.
    # So, we'll consider the three cases.
    # Horizontally:
    for i in range(3):  # [0,1,2]
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != EMPTY:
                return board[i][0]

   # Vertically:
    for j in range(3):  # [0,1,2]
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] != EMPTY:
                return board[0][j]
         

    # Diagionally:

    #[  x][2,2]
    #[ x ][1,1]
    #[x  ][0,0]

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != EMPTY:
            return board[0][0]
        

    # [x
    #   x
    #    x]
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] != EMPTY:
            return board[2][0]


    # if none of the requirements was met, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != None):
        return True
    # we'll have to check for the draw case, and to do that, we need to check
    # weather the board still has EMPTY states or not
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    # otherwise, return True [draw]
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == X):
        return 1
    elif(winner(board) == O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float('-inf')
    Min = float('inf')

    if player(board) == X:
        return Max_Value(board,Max,Min)[1]
    else:
        return Min_Value(board,Max,Min)[1]

# Max_value function as described in CS50:
def Max_Value(board, Max, Min):
    possibleMove = None
    if terminal(board):
        return [utility(board), None]
    vMin = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > vMin:
            vMin = test
            possibleMove = action
        if Max >= Min:
            break
    return [vMin, possibleMove]
# Min_value function as described in CS50:

def Min_Value(board, Max, Min):
    possibleMove = None
    if terminal(board):
        return [utility(board), None]
    vMax = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < vMax:
            vMax = test
            possibleMove = action
        if Max >= Min:
            break
    return [vMax, possibleMove]
