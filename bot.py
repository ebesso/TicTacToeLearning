import random, math, copy

class Bot:

    def __init__(self, knowledge, identity):
        self.knowledge = knowledge
        self.id = identity

    def update_knowledge(self, board, delta):
        known, r_board, turns = self.is_board_known(self.deserialize(board))
        
        if known == True:
            self.knowledge[self.serialize(r_board)] += delta

        else:
            self.knowledge[self.serialize(r_board)] = delta

    def generate_knowledge(self, board, mark):

        for a in range(0, len(board)):
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

        boards = []

        best_board = None
        rating = 0

        size = int(math.pow(len(board), 2))
        
        for i in range(0, size):
            a = math.floor(i / len(board))
            b = i - len(board) * math.floor(i / len(board))

            if board[a][b] == 0:
                board[a][b] = mark

                known, r_board, r = self.is_board_known(board)

                if known == True:
                    if best_board == None:
                        best_board = copy.deepcopy(board)
                        rating = copy.deepcopy(self.knowledge[self.serialize(r_board)])
                    
                    elif self.knowledge[self.serialize(r_board)] > rating:
                        best_board = copy.deepcopy(board)
                        rating = copy.deepcopy(self.knowledge[self.serialize(r_board)])
                
                elif known == False:
                    boards.append(copy.deepcopy(board))
                
                board[a][b] = 0

        if len(boards) > 0:
            if best_board == None or rating < 1:
                best_board = random.choice(boards)

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
        return list(zip(*reversed(board)))

    def add(self, board, solution):
        self.knowledge[self.serialize(board)] = solution

    def mutate_knowledge(self, percentage):

        for i in range(0, math.floor(len(self.knowledge) * percentage)):
            board = random.choice(list(self.knowledge.keys()))
            
            self.knowledge[board] = random.randint(-10, 10)

    def serialize(self, board):
        data = ''

        for a in range(0, len(board)):
            for b in range(0, len(board)):
                data += str(board[a][b])
        
        return data

    def deserialize(self, board):
        data = []

        for a in range(0, int(math.pow(len(board), 0.5))):
            row = []
            for b in range(0, int(math.pow(len(board), 0.5))):
                row.append(int(board[a * int(math.pow(len(board), 0.5)) + b]))

            data.append(row)

        return data 