theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def wincondition(board):
    vals = []
    for el in board.values():
        vals += str(el)

    if vals[0] == vals[1] == vals[2]:
        return vals[0]
    elif vals[3] == vals[4] == vals[5]:
        return vals[3]
    elif vals[6] == vals[7] == vals[8]:
        return vals[6]

    if vals[0] == vals[3] == vals[6]:
        return vals[0]
    elif vals[1] == vals[4] == vals[7]:
        return vals[1]
    elif vals[2] == vals[5] == vals[8]:
        return vals[2]

    if vals[0] == vals[4] == vals[8] or vals[2] == vals[4] == vals[6]:
        return vals[4]
    return ' '


turn = 'X'
for i in range(9):
    printboard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if move not in theBoard:
        print('Invalid place! Try again')
        while move not in theBoard:
            move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    win = wincondition(theBoard)
    if win != ' ':
        print(win + ' has won!')
        break
printboard(theBoard)
