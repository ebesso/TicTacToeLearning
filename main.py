import os, operator, pickle, copy

from game import simulate_game, play_game
from bot import Bot

def start():
    parent = Bot({}, -1)

    filename = 'parent_knowledge.pkl'

    if os.path.exists(filename):
        if input('Load saved knowledge? ') == 'y':
        
            with open(filename, 'rb') as f:
                parent.knowledge = pickle.load(f)
            
            print('Loaded start data (' + str(len(parent.knowledge)) + ')')

    while True:
        
        size = int(input('Board size: '))
        population = int(input('Populations: '))
        generations = int(input('Generations: '))

        for g in range(0, generations):
            children = []

            for i in range(0, population):
                child = Bot(copy.deepcopy(parent.knowledge), i)
                child.mutate_knowledge(0.5)

                children.append(Child(child))

            for a in range(0, population):
                for b in range(0, population):
                    winner, winner_boards, loser_boards = simulate_game(children[a].bot, children[b].bot, size, False)

                    #Not draw
                    if winner != None:
                        if winner.id == children[a].bot.id:
                            for i in range(0, len(winner_boards)):
                                parent.update_knowledge(winner_boards[i], 1)
                            for i in range(0, len(loser_boards)):
                                parent.update_knowledge(loser_boards[i], -1)

                        else:
                            for i in range(0, len(winner_boards)):
                                parent.update_knowledge(winner_boards[i], 1)

                            for i in range(0, len(loser_boards)):
                                parent.update_knowledge(loser_boards[i], -1)
            
            print('[' + str(g) + '] Done (' + str(len(parent.knowledge)) + ')')


        if input('Play against current generation? ') ==  'y':
            if input('Go first? ') == 'y':
                play_game(parent, size, True)
            else:
                play_game(parent, size, False)

        if input('View current generation? ') == 'y':
            simulate_game(parent, parent, size, True)

        if input('Save knowledge? ') == 'y':
            with open(filename, 'wb') as f:
                pickle.dump(parent.knowledge, f, pickle.HIGHEST_PROTOCOL)
            
            print('Saved knowledge')

class Child:
    def __init__(self, bot):
        self.bot = bot
        self.wins = 0


if __name__ == '__main__':
    start()