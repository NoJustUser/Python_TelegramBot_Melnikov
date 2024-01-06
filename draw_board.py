from colorama import Fore, Back, Style, init

init()

colors = {
    'X': Fore.RED + 'X' + Style.RESET_ALL,
    '0': Fore.BLUE + 'O' + Style.RESET_ALL,
    ' ': Back.YELLOW + ' ' + Style.RESET_ALL,
}


def draw_board(board):
    res = []
    for i in range(3):
        tmp = [colors.get(v) for v in board[i]]
        res.append(tmp)
    prnt = [' | '.join(v) for v in res]
    print(*prnt, sep='\n---------\n')
