def ask_move(player):
    # дать игроку возможность сделать ход, то есть  ввести координаты
    x, y = input(f"{player}, Введите координаты ячейки (напр. 0 0): ").strip().split()
    # преобразовать координаты в целые числа
    x, y = int(x), int(y)
    return x, y


def make_move(x, y, player, board):
    # задать условие, которое проверяет,
    # находится ли координата в пределах поля и свободно ли место
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        # если свободно, записать значение игрока (Х или 0) в ячейку
        board[x][y] = player
    else:
        print("Клетка занята, попробуйте снова.")
        ask_move(player)


def ask_and_make_move(player, board):
    x, y = ask_move(player)
    make_move(x, y, player, board)