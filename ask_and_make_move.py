def ask_move(player, board):
    # дать игроку возможность сделать ход, то есть  ввести координаты
    x, y = input(f" Игрок {player}, Введите координаты ячейки (напр. 0 0): ").strip().split()
    x, y = int(x), int(y)
    # находится ли координата в пределах поля и свободно ли место
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        return x, y
    else:
        print('Клетка занята. Введите координаты еще раз.')
        return ask_move(player, board)


def make_move(x, y, player, board):
    board[x][y] = player


def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    make_move(x, y, player, board)

