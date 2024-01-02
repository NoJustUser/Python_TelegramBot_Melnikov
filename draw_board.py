def draw_board(board):
    res = [' | '.join(v) for v in board]
    print(*res, sep='\n---------\n')