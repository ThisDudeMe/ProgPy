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

    returnDeck = shuffledCardStack * random.randrange(1, 5)

    random.shuffle(returnDeck)

    return returnDeck

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

    cardTypes = BlackJackCards()
    cards = BlackJackStartDeal()
    aiCards, playerCards, currentGameCards = cards
    playerCardValue = 0
    aiCardValue = 0
    isAiTurn = False

    if isAiTurn is False:

        playerCards.append(currentGameCards.pop(-1))

        for i in range(playerCards[-1]):

            if i in cardTypes:
                
                if "Ace" in playerCards:
                    
                    if cardTypes["Ace"] == 1:
                        
                        if (playerCardValue + cardTypes[i] + 10) <= 21:

                            cardTypes["Ace"] = 11
                            playerCardValue += cardTypes[i]

                    elif cardTypes["Ace"] == 11:

                        if (playerCardValue + cardTypes[i]) > 21:

                            cardTypes["Ace"] = 1
                            playerCardValue += cardTypes[i]

                    else:
                        cardTypes["Ace"] = 1
                        playerCardValue += cardTypes[i]      

                else:
            
                    playerCardValue += cardTypes[i]

    elif isAiTurn is True:
        
        aiCards.append(currentGameCards.pop(-1))

        for i in range(aiCards[-1]):

            if i in cardTypes:
                
                if "Ace" in aiCards:
                    
                    if cardTypes["Ace"] == 1:
                        
                        if (aiCardValue + cardTypes[i] + 10) <= 21:

                            cardTypes["Ace"] = 11
                            aiCardValue += cardTypes[i]

                    elif cardTypes["Ace"] == 11:

                        if (aiCardValue + cardTypes[i]) > 21:

                            cardTypes["Ace"] = 1
                            aiCardValue += cardTypes[i]

                    else:
                        cardTypes["Ace"] = 1
                        aiCardValue += cardTypes[i]      

                else:
            
                    aiCardValue += cardTypes[i]

    
        
       
    return isAiTurn, aiCardValue, playerCardValue
    
def AITrigger():
    aIcards = AddCard()
    isAITurn, aiCardValue, playerCardValue = aIcards

    while isAITurn == True:
        
        if aiCardValue > playerCardValue and aiCardValue <=21:

            return print("ai WIns")
            
        elif aiCardValue < 21

            


    pass

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

    

    
        


    




