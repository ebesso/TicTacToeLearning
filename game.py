import os, math

def play_game(cpu, size,first):
    turn = 0

    board = []

    for i in range(0, size):
        board.append([])
        for j in range(0, size):
            board[i].append(0)


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

        if is_winnable(board) == False:
            print('Not winnable')

        if has_won(board):
            input('Someone won')
        elif is_draw(board):
            input('Draw')  
    


def get_move(board, mark):
    i = int(input('Move: '))
    board[math.floor(i / len(board))][i - len(board) * math.floor(i / len(board))] = mark
    return board     


def simulate_game(p1, p2, size, view):

    turn = 0

    board = []

    for i in range(0, size):
        board.append([])
        for j in range(0, size):
            board[i].append(0)

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
        


        if turn > size + 1:
            if is_winnable(board) == False:
                return None, None, None
            winner = has_won(board)

            if winner != 0:
                if view:
                    print(str(winner) + ' won')
                    input()

                if winner == 1:
                    return p1, p1_boards, p2_boards
                else:
                    return p2, p2_boards, p1_boards
            
        turn += 1

        if view:
            input()

def is_winnable(board):

    for i in range(0, len(board)):
        if 1 in board[i] and 2 not in board[i]:
            return True
        elif 1 not in board[i] and 2 in board[i]:
            return True
    
    verticals = []

    for x in range(0, len(board)):
        verticals.append([])
        for y in range(0, len(board)):
            verticals[x].append(board[x][y])
    
    for i in range(0, len(verticals)):
        if 1 in verticals[i] and 2 not in verticals[i]:
            return True
        elif 1 not in verticals[i] and 2 in verticals[i]:
            return True

    diagonal = []

    for x in range(0, len(board)):
        diagonal.append(board[x][x])

    if 1 in diagonal and 2 not in diagonal:
        return True
    elif 1 not in diagonal and 2 in diagonal:
        return True

    diagonal = []

    for x in range(0, len(board)):
        diagonal.append(board[len(board) - 1 - x][x])  

    if 1 in diagonal and 2 not in diagonal:
        return True
    elif 1 not in diagonal and 2 in diagonal:
        return True
    
    return False

def is_draw(board):

    for i in range(0, len(board)):
        if 0 in board[i]:
            return False
    
    return True

def has_won(board):

    #Check horizontal
    for i in range(0, len(board)):
        if 0 not in board[i]:

            #2 won
            if 1 not in board[i] and 2 in board[i]:
                return 2
            
            #1 Won
            if 2 not in board[i] and 1 in board[i]:
                return 1
    
    #Check vertical
    for p in range(1, 3):

        for x in range(0, len(board)):
            win = True
            for y in range(0, len(board)):
                if board[y][x] != p:
                    win = False
                    break
            
            if win == True:
                return p

    #Check diagonal
    for p in range(1, 3):
        won = True

        for x in range(0, len(board)):
            if board[x][x] != p:
                won = False
                break
        
        if won == True:
            return p

        won = True

        for x in range(0, len(board)):
            if board[len(board) - 1 - x][x] != p:
                won = False
                break
        
        if won == True:
            return p

    return 0

def render_board(board):

    clear = lambda : os.system('cls')
    clear()

    for a in range(0, len(board)):
        row = ''
        for b in range(0, len(board)):
            row += str(board[a][b])
        print(row)

def serialize_board():
    pass

def deserialize_board():
    pass

