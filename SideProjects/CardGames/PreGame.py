import pygame as pg
import numpy as np
import random

class DeckContents:

    def CreateDeck(self):

        cardValues = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Joker", "Queen", "King", "Ace"]
        cardTypes = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.deck = []

        for i in cardTypes:
            
            for x in cardValues:

                self.deck.append(f"{x} of {i}")

        return self.deck
        
class BlackJack:
    def __init__(self):
        
        tempDeck = DeckContents().CreateDeck().copy()
        amountOfDecks = random.randrange(1,8)
        gameDeck = {}
        
        for _ in range(amountOfDecks):
            gameDeck.update(tempDeck)
        
        random.shuffle(gameDeck)

            
            
        

        pass
class Poker:
    pass
class AskUser:

    def UserAnswer(self):

        while True:

            try:
                print("What do you want to play? ")
                print("Type (1) for Poker! ")
                print("Type (2) for BlackJack! ")
                print("Type (3) to EXIT ! ")
                userInput = int(input(" : "))

                if userInput == 1:
                    BlackJack()
                elif userInput == 2:
                    Poker()
                elif userInput == 3:
                    break
                else:
                    raise ValueError("Invalid please enter a correct choice!")
                

            except ValueError as e:
                print(e)