"""
    tools.py
    DGTavo88

    Contains several tools (functions) used throughout the program.
    
"""
from tkinter import font #From the tkinter module import font.
import os #Import os module.
import json #Import json module.
import sys #Import sys module.
import ntpath #Inport ntpath module.

def Error(serror):
    print(serror) #Show error message.
    sys.exit(1) #Exit program.

def LoadLanguageText():
    if os.path.exists("Language/lang_en.json"):
        with open("Language/lang_en.json") as lang_data: #Open the "lang" JSON file as "lang_data".
            data = json.load(lang_data) #Load the data from the "lang" file and save it as a dictionary.
            return data #Return dictionary.
    else:
        Error("Error!\nLanguage File doesn't exist.") #Show an error.

data = LoadLanguageText()

def GetFont(sfont = "text"):
    fonts = {
    "text": font.Font(family = "Consolas", size = 12),  #Font for text.
    "menu": font.Font(family = "Consolas", size = 10)   #Font for menu.
    }
    ffont = fonts.get(sfont, "-1")  #Get font.
    if ffont != -1:
        return ffont
    else:
        Error("Error!\nDesired font '%s' doesn't exist." %(sfont))

def GetFilename(filepath):
    tail, head = ntpath.split(filepath) #Split path.
    print("Tail: " + str(tail))
    print("Head: " + str(head))
    if head != "":
        return head #Return name.
    else:
        return filepath  #Return directory.

def UpdateTitle(mainwindow, fdir, floaded):
    if floaded == True:
        mainwindow.title(data["window_name"] %(GetFilename(fdir))) #Set window name to file name.
    else:
        mainwindow.title(data["window_name_untitled"])  #Set window name to default.
