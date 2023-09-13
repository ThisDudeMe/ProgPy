import random

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
def BlackJackRules():

    currentgameCards = BlackJackShuffle()
    aiCards = []
    playerCards = []
    isAiTurn = True
    cantAddMoreAi = False
    cantAddMorePlayer = False
    dealFinnished = False

    while dealFinnished == False:  
        
        if cantAddMoreAi == True and cantAddMorePlayer == True:

            dealFinnished = True
            
        else:

            if cantAddMoreAi == False:

                if isAiTurn == True:
                            
                    if len(aiCards) < 2:
                                
                        aiCards.append(currentgameCards.pop())
                    

                    else:
                        cantAddMoreAi = True
                isAiTurn = False   


            if cantAddMorePlayer == False:

                if isAiTurn == False:

                    if len(playerCards) < 2:

                        playerCards.append(currentgameCards.pop())
                
                            
                    else:
                        cantAddMorePlayer = True

                isAiTurn = True

    return aiCards,playerCards,currentgameCards

afterDeal = BlackJackRules()

pCards,aCards,cDeck = afterDeal


print(f"playercards: {pCards}", f"aiCards: {aCards}", f"deckremain: {cDeck}")

