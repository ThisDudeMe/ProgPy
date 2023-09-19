# importing tkinter to handle the select file function

import tkinter as tk
from tkinter import filedialog

# defining a list of constants for reusability

constants = [
              "B", "C", "D", "F", "G", "H", "J",
              "K","L", "M", "N", "P", "Q", "R",
              "S","T","V", "W", "X", "Z"
             ]

# function for handling the popup window for selecting a file
def SelectFile():


        root = tk.Tk()
        root.withdraw()
        filePath = filedialog.askopenfilename()
        root.destroy()

        return filePath

# function that gets the contents of the file based on the filepath variable that was saved and returned in the function above: SelectFile()
# then saves the contents of the file into a variable(fileToEncrypt)
def GetFileContents():
        
        filePath = SelectFile()

        with open(filePath, "r", encoding = "utf-8") as file:
                fileToEncryptReturn = file.read()

                return fileToEncryptReturn      

# this function handles the encryption logic. it encrypts the contents of the returned variable(fileToEncryptReturn) from 
# the function above GetFileContents():
#then loops trough each letter in the contents and adds them to a list and if the letter is a constant then it adds an o 
# and the same letter but in lower case
def EncryptFile():
        
        fileToEncrypt = GetFileContents()
        encryptingFile = []

        for letter in fileToEncrypt:
                
                if letter.upper() in constants:
                    
                    encryptingFile.append(letter + "o" + letter.lower())
                
                else: 
                    
                    encryptingFile.append(letter)
                
        
        encryptedFile = "".join(encryptingFile)

        return encryptedFile
#this function is started first then it, starts the function above EncryptFile() and when everything is executed 
# it prints the results
def StartProgram():
       
        encryptedtext = EncryptFile()
        print(" This is the encrypted text: ", encryptedtext)

        return

#this starts the StartProgram()- function
StartProgram()
