from draw_board import *
from ask_and_make_move import *
from check_win import *

while True:
    board = [[" " for i in range(3)] for j in range(3)]
    player = 'X'
    draw_board(board)

    while True:
        ask_and_make_move(player, board)
        draw_board(board)
        if check_win(player, board):
            print(f'Игрок {player} - вы выиграли !')
            break
        # проверить, произошла ли ничья
        tie_game = False
        for row in board:
            for cell in row:
                if cell == " ":
                    tie_game = True
        # если произошла ничья, завершить цикл
        if not tie_game:
            print('Ничья !')
            break
        # Меняем игрока
        player = 'X' if player == '0' else '0'

    restart = input("Хотите сыграть еще раз? (y/n) ")
    if restart.lower() != "y":
        break
