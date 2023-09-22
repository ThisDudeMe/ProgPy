'''# https://youtu.be/L8ypSXwyBds?t=3879


import torch
import random
import numpy as np
from collections import deque
from game import SnakeGameAI, Direction, Point

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.nGames = 0
        self.epsilon = 0 #randomness
        self.gamma = 0#discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft()
        self.model = None # TODO
        self.Trainer = None # TODO
    



    def GetState(self, game):
        head = game.snake[0]
        pointL = Point(head.x - 20, head.y)
        pointR = Point(head.x + 20, head.y)
        pointU = Point(head.x, head.y - 20)
        pointD = Point(head.x, head.y + 20)

        dirL = game.direction == Direction.LEFT
        dirR = game.direction == Direction.RIGHT
        dirU = game.direction == Direction.UP
        dirD = game.direction == Direction.DOWN

        state = [   #dangerStrait
                    (dirR and game.is_collision(pointR)) or
                    (dirL and game.is_collision(pointL)) or
                    (dirU and game.is_collision(pointU)) or
                    (dirD and game.is_collision(pointD)),

                    # danger right
                    (dirU and game.is_collision(pointR)) or
                    (dirD and game.is_collision(pointL)) or
                    (dirL and game.is_collision(pointU)) or
                    (dirR and game.is_collision(pointD)),

                    #danger left

                    (dirD and game.is_collision(pointR)) or
                    (dirU and game.is_collision(pointL)) or
                    (dirR and game.is_collision(pointU)) or
                    (dirL and game.is_collision(pointD)),

                    #move direction
                    dirL,
                    dirR,
                    dirU,
                    dirD,

                    #food location 
                    game.food.x < game.head.x, # food left
                    game.food.x > game.head.x, #food right
                    game.food.y < game.head.y, #food up
                    game.food.y > game.head.y  # food down
                ]
        return np.array(state, dtype=int)

    def Remember(self, state, action, reward, nextState, gameOver):
        self.memory.append((state, action, reward, nextState, gameOver)) # pop left if max_memory is reachd
    
    def trainLongMemory(self):
        if len(self.memory) > BATCH_SIZE:
            miniSample = random.sample(self.memory, BATCH_SIZE) # list of tuples

        else:
            miniSample = self.memory

        self.Trainer.TrainStep(states, actions, rewards, nextStates, gameOvers)


    def trainShortMemory(self, state, action, reward, nextState, gameOver):
        self.Trainer.TrainStep(state, action, reward, nextState, gameOver)
    
    def GetAction(self, state):
        pass


def Train():
    plotScores = []
    plotAvgScore = []
    totalScore = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True:
        #get old state
        stateOld = agent.GetState(game)

        #get move
        finalMove = agent.GetAction(stateOld)

        #perform move get new state
        reward, done, score = game.play_step(finalMove)
        stateNew = agent.GetState(game)

        agent.trainShortMemory(stateOld, finalMove, reward, stateNew, gameOver)

        #remeber
        agent.Remember(stateOld, finalMove, reward, stateNew, gameOver)

        if GameOver:
            #train long memory, plot result
            game.Reset()
            agent.nGames += 1
            agent.trainLongMemory()

            if score > record:
                record = score
                #agent.model.save()

            print("Game ", agent.nGames,"Score ", score, "Record ", record)

            #TODO: plot


if __name__ == "__main__":
    Train()'''