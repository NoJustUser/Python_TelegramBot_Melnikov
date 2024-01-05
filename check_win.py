def check_win(player, board):
    board_zip = list(map(list, zip(board[0], board[1], board[2])))
    # две возможные диагонали
    rd1 = [board[0][0], board[1][1], board[2][2]]
    rd2 = [board[0][2], board[1][1], board[2][0]]
    collection = [
        board[0], board[1], board[2],
        board_zip[0], board_zip[1], board_zip[2],
        rd1, rd2
    ]

    # проверяет совпадение символов в коллекции со
    # значением player
    def check_list(lst):
        tmp = 0
        for value in lst:
            if value == player and value is not ' ':
                tmp += 1
        return tmp == 3

    for v in collection:
        if check_list(v):
            print(f'Игрок {player} - вы выиграли !')
            return True
    return False
