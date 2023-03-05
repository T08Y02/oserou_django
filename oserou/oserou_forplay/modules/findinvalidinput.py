import os
import time
import random
import math

from oserou_forplay.modules import placestone, calcscore

def bestScore(board_state, color):
    bestscore = 0
    for i in range(8):
        for j in range(8):
            if board_state[i][j] == 0:
                bestscore = max([bestscore, calcscore.score_count(board_state, i, j, color)])
    return bestscore

def checkValid(board_state, selected_row, selected_collumn, color):
    valid = 0
    bestscore = bestScore(board_state, color)
    if board_state[selected_row][selected_collumn] != 0 or \
        calcscore.score_count(board_state, selected_row, selected_collumn, color) <= 0:
        if bestscore <= 0:
            valid = 2
        else:
            valid = 1
    return valid
    
