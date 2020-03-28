import random, math, copy

class Bot:

    def __init__(self, knowledge, identity):
        self.knowledge = knowledge
        self.id = identity

    def update_knowledge(self, board, delta):
        known, r_board, turns = self.is_board_known(self.deserialize(board))
        self.knowledge[self.serialize(r_board)] += delta

    def generate_knowledge(self, board, mark):

        for a in range(0, 9):
            x = math.floor(a / 3)
            y = a - 3 * math.floor(a /   3)
            
            if board[x][y] == 0:
                board[x][y] = mark

                known, r_board, turns = self.is_board_known(board)

                if known == False:
                    self.knowledge[self.serialize(board)] = 0
                
                if mark == 1:
                    self.generate_knowledge(board, 2)
                else:
                    self.generate_knowledge(board, 1)

                board[x][y] = 0

    def play(self, board, mark):

        best_board = None
        rating = 0

        for i in range(0, 9):
            a = math.floor(i / 3)
            b = i - 3 * math.floor(i / 3)

            if board[a][b] == 0:
                board[a][b] = mark

                known, r_board, r = self.is_board_known(board)

                if best_board == None:
                    best_board = copy.deepcopy(board)
                    rating = copy.deepcopy(self.knowledge[self.serialize(r_board)])
                
                else:
                    if self.knowledge[self.serialize(r_board)] > rating:
                        best_board = copy.deepcopy(board)
                        rating = copy.deepcopy(self.knowledge[self.serialize(r_board)])
                
                board[a][b] = 0
        
        return best_board

    def is_board_known(self, board):

        if(self.serialize(board) in self.knowledge):
            return True, board, 0

        for i in range(1, 4):
            board = self.rotate_board(board)
            if(self.serialize(board) in self.knowledge):
                return True, board, i
        
        return False, board, 0

    def rotate_board(self, board):

        top_row = [board[0][2], board[1][2], board[2][2]]
        mid_row = [board[0][1], board[1][1], board[2][1]]
        bot_row = [board[0][0], board[1][0], board[2][0]]
        
        return [top_row, mid_row, bot_row]

    def add(self, board, solution):
        self.knowledge[self.serialize(board)] = solution

    def mutate_knowledge(self, percentage):

        for i in range(0, math.floor(len(self.knowledge) * percentage)):
            board = random.choice(list(self.knowledge.keys()))
            
            self.knowledge[board] = random.randint(-10, 10)


    def serialize(self, board):
        data = ''

        for a in range(0, 3):
            for b in range(0, 3):
                data += str(board[a][b])
        
        return data

    def deserialize(self, board):
        data = []

        for a in range(0, 3):
            row = []
            for b in range(0, 3):
                row.append(int(board[a * 3 + b]))

            data.append(row)

        return data 