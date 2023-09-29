#Imports
import requests
import time
import tkinter
from colorama import Fore, Style
from tkinter import filedialog

#function for starting the program
def StartProgram():
    #assigning variables
    resetStyle = Style.RESET_ALL
    constants = {
        
                    "B": "b", "C": "c", "D": "d", "F": "f", "G": "g",
                    "H": "h", "J": "j", "K": "k", "L": "l", "M": "m",
                    "N": "n", "P": "p", "Q": "q", "R": "r", "S": "s",
                    "T": "t", "V": "v", "W": "w", "X": "x", "Y": "y",
                    "Z": "z"
               
                }
    #thisHandlesthefileChoosingWIndowFunction
    def ChooseFile():
        root = tkinter.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        filePath = filedialog.askopenfilename()
        return filePath
    #this handles the decrypt function
    def DecryptText():
        print("Error: You are not authorized to use this function. ")
        print("If you want to decrypt a file subscribe to our VIP Pass for only 399.99 sek per month!")
        time.sleep(1)
        print("")
        UserOptions()
    #this handles the encrypt function
    def EncryptText():
        toEncrypt = []
        fileToEncrypt = ""

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
                time.sleep(0.2)

                print("Please enter URL ")
                print("Example:https://www.example.com ")
                url = input(Fore.BLUE + ": " + resetStyle)

                try:
            
                    response = requests.get(url)
                    
                    if response.status_code == 200:  
                        
                        fileToEncrypt = response.text
                        
                        for character in fileToEncrypt:
                        
                            if character in constants.keys():
                                toEncrypt.append(character + "o" + character.lower())
                            

                            elif character in constants.values():
                                toEncrypt.append(character + "o" + character.lower())

                            else:
                                toEncrypt.append(character)
                    
                        encryptedText = "".join(toEncrypt)
                        print("")
                        print("Text encrypted: ", encryptedText)
                        time.sleep(0.2)
                        break
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
                time.sleep(0.2)
                
                filePath = ChooseFile()
                try:
                    with open(filePath, "r") as file:
                        fileToEncrypt = file.read()
                        fileSelected = True
                        

                except FileNotFoundError:
                    fileSelected = False
                    print(f"File '{filePath}' not found.")
                    
                except Exception as e:
                    fileSelected = False
                    print(f"An error occurred: {str(e)}")
                
                if fileSelected:
        
                    for character in fileToEncrypt:
                        
                        if character in constants.keys():
                            toEncrypt.append(character + "o" + character.lower())
                            

                        elif character in constants.values():
                            toEncrypt.append(character + "o" + character.lower())

                        else:
                            toEncrypt.append(character)
                    
                    encryptedText = "".join(toEncrypt)
                    print("")
                    print("Text encrypted: ", encryptedText)
                    time.sleep(0.2)
                    break
                    
                else:
                    print(Fore.RED,"Error: No file was selected! ",resetStyle)                       
            elif choice == 3:
                print("Where is your text located?")
                print(Fore.RED, "Press (1) if you have a URL", resetStyle)
                print(Fore.RED, "Press (2) if you have a file on your computer", resetStyle)
                print(Fore.GREEN, "Press (3) if you want to input a text manually", resetStyle)
                print(Fore.RED, "Press (4) if you want to go back", resetStyle)
                time.sleep(0.2)
                
                fileToEncrypt = input("Please write the text you want to encrypt! ")
        
                for character in fileToEncrypt:
                    
                    if character in constants.keys():
                        toEncrypt.append(character + "o" + character.lower())
                        

                    elif character in constants.values():
                        toEncrypt.append(character + "o" + character.lower())

                    else:
                        toEncrypt.append(character)
                
                encryptedText = "".join(toEncrypt)
                print("")
                print("Text encrypted: ", encryptedText)
                time.sleep(0.2)
                break
            elif choice == 4:
                print("Where is your text located?")
                print(Fore.RED, "Press (1) if you have a URL", resetStyle)
                print(Fore.RED, "Press (2) if you have a file on your computer", resetStyle)
                print(Fore.RED, "Press (3) if you want to input a text manually", resetStyle)
                print(Fore.GREEN, "Press (4) if you want to go back", resetStyle)
                time.sleep(0.2)       
                UserOptions()
            else:
                print(Fore.RED,"Invalid Please choose a correct option! ",resetStyle) 
   #this handles what to do based on user input
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
                time.sleep(0.2)
                print("")
                EncryptText()
                break
                
            if choice == 2:
                print("What do you want to do?")
                print(Fore.RED, "Press (1) to encrypt text", resetStyle)
                print(Fore.GREEN, "Press (2) to decrypt text", resetStyle)
                time.sleep(0.2)
                print("")
                DecryptText()
            
                
            
            else:
                print("")
                print(Fore.RED,"Invalid Please choose a correct option! ",resetStyle)
    #thisTriggers user choices
    UserOptions()
#this triggers the program
StartProgram()