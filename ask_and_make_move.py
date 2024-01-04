def ask_move(player, board):
    # дать игроку возможность сделать ход, то есть  ввести координаты
    x, y = map(int, input(f"{player}, Введите координаты ячейки (напр. 0 0): ").strip().split())
    # находится ли координата в пределах поля и свободно ли место
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        return x, y
    print('Клетка занята. Введите координаты еще раз.')
    ask_move(player, board)


def make_move(x, y, player, board):
    board[x][y] = player


def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    make_move(x, y, player, board)
    return board
