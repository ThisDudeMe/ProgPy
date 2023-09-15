import random

from colorama import Fore, Back, Style, init
from sympy import false


def BlackJackCards():

    cardTypes = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Joker": 10, "Queen": 10, "King": 10}


    return cardTypes
def BlackJackShuffle():
    
    cards = BlackJackCards()
    shuffledCardStack = []

    for i in cards.keys():
        shuffledCardStack.extend([i] * 4)

    random.shuffle(shuffledCardStack)

    return shuffledCardStack
def BlackJackStartDeal():

    currentGameCards = BlackJackShuffle()
    aiCards = []
    playerCards = []
    isAiTurn = True
    cantAddMoreAi = False
    cantAddMorePlayer = False
    dealFinnished = False
    aiAllowShowFirsCard = True

    while dealFinnished == False:  
        
        if cantAddMoreAi == True and cantAddMorePlayer == True:

            dealFinnished = True
            
        else:

            if cantAddMoreAi == False:

                if isAiTurn == True:
                    
                            
                    if len(aiCards) < 2:
                                
                        aiCards.append(currentGameCards.pop())

                        if aiAllowShowFirsCard == False:
                            print("AI: ","Card")
                        
                        if aiAllowShowFirsCard == True:
                            print("AI: ",len(aiCards[-1]))
                            aiAllowShowFirsCard = False
                    

                    else:
                        cantAddMoreAi = True
                isAiTurn = False   


            if cantAddMorePlayer == False:

                if isAiTurn == False:

                    if len(playerCards) < 2:

                        playerCards.append(currentGameCards.pop())
                        print("Player: ", playerCards[-1])

                
                            
                    else:
                        cantAddMorePlayer = True

                isAiTurn = True

    return aiCards,playerCards,currentGameCards
def AddCard():
    #SWITCH DYNAMIC TO PLAYER AND AI //// CURRENTLY DOES NOT ADD CARDS FROM DECK AND REMOVE FROM DECK!!
    cardTypes = BlackJackCards()
    cards = BlackJackStartDeal()
    aiCards, playerCards,currentGameCards = cards
    dynamicCards = []
    dynamicCardsValue = 00
    playerCardValue = 0
    aiCardValue = 0
    isAiTurn = False

    if isAiTurn is False:

        dynamicCards = playerCards
        dynamicCardsValue = playerCardValue

    if isAiTurn is True:
        
        dynamicCards = aiCards
        dynamicCardsValue = aiCardValue

    for i in range(dynamicCards[-1]):

        if i in cardTypes:
            
            if "Ace" in dynamicCards:
                
                if cardTypes["Ace"] == 1:
                    
                    if (dynamicCardsValue + cardTypes[i] + 10) <= 21:

                        cardTypes["Ace"] = 11
                        dynamicCardsValue += cardTypes[i]

                if cardTypes["Ace"] == 11:

                    if (dynamicCardsValue + cardTypes[i]) > 21:

                        cardTypes["Ace"] = 1
                        dynamicCardsValue += cardTypes[i]

                else:
                    cardTypes["Ace"] = 1
                    dynamicCardsValue += cardTypes[i]      

            else:
        
                dynamicCardsValue += cardTypes[i]                
    
    if isAiTurn == False:

        playerCardValue = dynamicCardsValue
        
        return isAiTurn, playerCardValue, aiCardValue
    
    if isAiTurn == True:
        
        aiCardValue = dynamicCardsValue
        return isAiTurn, aiCardValue
def AITrigger():
    aIcards = AddCard()
    isAITurn, aiCardValue = aIcards
def StartGame():
    while True:
        
        userInput = input((Fore.GREEN,"Press: C for CONTINUE! ",Fore.RED,"Press: S for STOP! ", Fore.WHITE ))

        if userInput == "C":
            playercards = AddCard()
            isaiTurn, playerCardValue = playercards
            AddCard()

        if userInput == "S":
            
            AITrigger()
            break
            
        else:
            print("Unknown command! Please presss the correct key! ")

    

    
        


    




