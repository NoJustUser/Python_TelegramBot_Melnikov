from draw_board import *
from ask_and_make_move import *
from check_win import *

board = [[" " for i in range(3)] for j in range(3)]
player = 'X'
draw_board(board)


while True:
    ask_and_make_move(player, board)
    draw_board(board)
    if check_win(player, board):
        flag = input('Хотите играть снова ? y/n')
        if flag == 'n':
            break
    # Меняем игрока
    player = 'X' if player == '0' else '0'



