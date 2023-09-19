#Imports
import requests
import time
import os
import colorama
import tkinter

from colorama import Fore, Back, Style
from tkinter import filedialog

#function for starting the program
def StartProgram():

    #assigning variables
    resetStyle = Style.RESET_ALL
    constants = {"B": "b", "C": "c", "D": "d", "F": "f", "G": "g",
                "H": "h", "J": "j", "K": "k", "L": "l", "M": "m",
                "N": "n", "P": "p", "Q": "q", "R": "r", "S": "s",
                "T": "t", "V": "v", "W": "w", "X": "x", "Y": "y",
                "Z": "z"
                }
    
    def chooseFile():
        root = tkinter.Tk()
        root.withdraw()
        filePath = filedialog.askopenfilename()
        return filePath
    def DecryptText():
        
        print("Error: You are not authorized to use this function. ")
        print("If you want to decrypt a file subscribe to our VIP Pass for only 399.99 sek per month!")
        time.sleep(2)
        return     
    def EncryptText():

        toEncrypt = []

        while True:
            print("Where is your text located?")
            print("Press (", Fore.RED, "1", resetStyle, ") if you have a URL")
            print("Press (", Fore.RED, "2", resetStyle, ") if you have a file on your computer")
            print("Press (", Fore.RED, "3", resetStyle, ") if you want to input a text manually")
            print("Press (", Fore.RED, "4", resetStyle, ") if you want to go back")

            choice = int(input(Fore.BLUE + ": " + resetStyle))
            
            if choice == 1:
                print("Where is your text located?")
                print(Fore.GREEN, "Press (1) if you have a URL", resetStyle)
                print(Fore.RED, "Press (2) if you have a file on your computer", resetStyle)
                print(Fore.RED, "Press (3) if you want to input a text manually", resetStyle)
                print(Fore.RED, "Press (4) if you want to go back", resetStyle)
                time.sleep(0.5)

                print("Please enter URL ")
                print("Example:https://www.example.com ")
                url = input(Fore.BLUE + ": " + resetStyle)

                try:
            
                    response = requests.get(url)
                    
                    if response.status_code == 200:  
                        
                        content = response.text
                        
                        for character in content:
                            if character in constants.keys():
                                toEncrypt.append(character + "o" + character.lower())
                            elif character in constants.values():
                                toEncrypt.append(character + "o" + character.lower())
                            else:
                                toEncrypt.append(character)
                    else:
                        print(Fore.RED, "Error: Unable to fetch content from the URL.", resetStyle)
                
                except Exception as error:
                    print(Fore.RED, "Error: ",error, resetStyle)              
            elif choice == 2:
                print("Where is your text located?")
                print(Fore.RED, "Press (1) if you have a URL", resetStyle)
                print(Fore.GREEN, "Press (2) if you have a file on your computer", resetStyle)
                print(Fore.RED, "Press (3) if you want to input a text manually", resetStyle)
                print(Fore.RED, "Press (4) if you want to go back", resetStyle)
                time.sleep(0.5)
                
                fileSelected = chooseFile()

                if fileSelected:
        
                    for character in fileSelected:
                        
                        if character in constants.keys():
                            toEncrypt.append(character + "o" + constants[character])
                            

                        elif character in constants.values():
                            toEncrypt.append(character + "o" + constants[character])

                        else:
                            toEncrypt.append(character)
                    
                    encryptedText = "".join(toEncrypt)
                    return encryptedText
                    
                else:
                    print(Fore.RED,"Error: No file was selected! ",resetStyle)                       
            elif choice == 3:
                print("Where is your text located?")
                print(Fore.RED, "Press (1) if you have a URL", resetStyle)
                print(Fore.RED, "Press (2) if you have a file on your computer", resetStyle)
                print(Fore.GREEN, "Press (3) if you want to input a text manually", resetStyle)
                print(Fore.RED, "Press (4) if you want to go back", resetStyle)
                time.sleep(0.5)
                
                userInput = input("Please write the text you want to encrypt! ")
        
                for character in userInput:
                    
                    if character in constants.keys():
                        toEncrypt.append(character + "o" + constants[character])
                        

                    elif character in constants.values():
                        toEncrypt.append(character + "o" + constants[character])

                    else:
                        toEncrypt.append(character)
                
                encryptedText = "".join(toEncrypt)
                return encryptedText
            elif choice == 4:
                print("Where is your text located?")
                print(Fore.RED, "Press (1) if you have a URL", resetStyle)
                print(Fore.RED, "Press (2) if you have a file on your computer", resetStyle)
                print(Fore.RED, "Press (3) if you want to input a text manually", resetStyle)
                print(Fore.GREEN, "Press (4) if you want to go back", resetStyle)
                time.sleep(0.5)
                return            
            else:
                print(Fore.RED,"Invalid Please choose a correct option! ",resetStyle) 
    def UserOptions():

        while True:
            
            print("What do you want to do?")
            print("Press (", Fore.RED, "1", resetStyle, ") to encrypt text")
            print("Press (", Fore.RED, "2", resetStyle, ") to decrypt text")

            choice = int(input(Fore.BLUE + ": " + resetStyle))

            if choice == 1:

                print("What do you want to do?")
                print(Fore.GREEN, "Press (1) to encrypt text", resetStyle)
                print(Fore.RED, "Press (2) to decrypt text", resetStyle)
                time.sleep(0.5)
                EncryptText()
                break
                
            if choice == 2:
                print("What do you want to do?")
                print(Fore.RED, "Press (1) to encrypt text", resetStyle)
                print(Fore.GREEN, "Press (2) to decrypt text", resetStyle)
                time.sleep(0.5)
                DecryptText()
                break
                
            
            else:
                
                print(Fore.RED,"Invalid Please choose a correct option! ",resetStyle)

    UserOptions()

StartProgram()