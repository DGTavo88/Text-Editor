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
import globals #Import Global Variables.

def Error(serror):
    print(serror) #Show error message.
    sys.exit(1) #Exit program.

def LoadLanguageText():
    if os.path.exists("Language/lang_en.json"):
        with open("Language/lang_en.json") as lang_data: #Open the "lang" JSON file as "lang_globals.data".
            globals.data = json.load(lang_data) #Load the globals.data from the "lang" file and save it as a dictionary.
            return globals.data #Return dictionary.
    else:
        Error("Error!\nLanguage File doesn't exist.") #Show an error.

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

def GetFilename():
    tail, head = ntpath.split(globals.loadedDirectory) #Split path.
    print("Tail: " + str(tail))
    print("Head: " + str(head))
    if head != "":
        return head #Return name.
    else:
        return tail  #Return directory.

def UpdateTitle():
    window_text = globals.data["window_name_untitled"]
    if globals.loadedFile == True:
        window_text = globals.data["window_name"] %(GetFilename()) #Set window name to file name.

    globals.mainwindow.title(window_text)  #Set window name to default.

def CheckForTextChanges():
    if globals.tobject.GetText() != globals.tobject.loadedtext:
        window_title = globals.mainwindow.title()
        if not globals.checked_text:
            globals.mainwindow.title("*" + window_title)
            globals.checked_text = True
