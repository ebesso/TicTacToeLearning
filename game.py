import os, math

def play_game(cpu, first):
    turn = 0

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    render_board(board)

    while True:
        if turn % 2 == 0:
            if first == True:
                board = get_move(board, 1)
            else:
                board = cpu.play(board, 1)
        else:
            if first == False:
                board = get_move(board, 2)
            else:
                board = cpu.play(board, 2)
        
        turn += 1
        render_board(board)

        if has_won(board):
            input('Someone won')
        elif is_draw(board):
            input('Draw')  
    


def get_move(board, mark):
    i = int(input('Move: '))
    board[math.floor(i / 3)][i - 3 * math.floor(i / 3)] = mark
    return board     


def simulate_game(p1, p2, view):

    turn = 0

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    p1_boards = []
    p2_boards = []

    # Game Loop
    while True:
        if turn % 2 == 0:
            board = p1.play(board, 1)
            p1_boards.append(p1.serialize(board))
        else:
            board = p2.play(board, 2)
            p2_boards.append(p2.serialize(board))
        
        if view:
            render_board(board)

        if turn > 3:
            winner = has_won(board)

            if winner != 0:
                if view:
                    print(str(winner) + ' won')
                    input()

                if winner == 1:
                    return p1, p1_boards, p2_boards
                else:
                    return p2, p2_boards, p1_boards
            
            if is_draw(board):
                if view:
                    print('Draw')
                    input()
                return None, None, None

        turn += 1

        if view:
            input()

def is_draw(board):
    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return True
    else:
        return False

def has_won(board):

    #Check horizontal
    for i in range(0, 3):
        if 0 not in board[i]:

            #2 won
            if 1 not in board[i] and 2 in board[i]:
                return 2
            
            #1 Won
            if 2 not in board[i] and 1 in board[i]:
                return 1
    
    #Check vertical
    for p in range(1, 3):
        for x in range(0, 3):
            win = True
            for y in range(0, 3):
                if board[y][x] != p:
                    win = False
                    break
            
            if win:
                return p

    #Check diagonal
    if board[1][1] != 0:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        
        if board[2][0] == board[1][1] == board[0][2]:
            return board[1][1]
    
    return 0



def render_board(board):

    clear = lambda : os.system('cls')
    clear()

    for a in range(0, 3):
        row = ''
        for b in range(0, 3):
            row += str(board[a][b])
        print(row)

def serialize_board():
    pass

def deserialize_board():
    pass

