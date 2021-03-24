"""
    fmcommands.py
    DGTavo88
    
    Contains the functions used by the "File" menu options.
"""

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tools
import traceback
import sys

data = tools.LoadLanguageText() #Load strings from file.
loadedFile = False #Used for checking if a file has been loaded into the text editor.
loadedDirectory = "-1" #Used for storing the directory of the loaded file.
nf = False #Flag for new file.

#User decides to save file.
def EPYes(popup, window, textobject):
    SaveFileProcess(window, textobject) #Save file.
    popup.destroy() #Destroy the pop-up.
    sys.exit(0) #End the program.

#User desides to not save file.
def EPNo(popup):
    popup.destroy() #Destroy the pop-up.
    sys.exit(0) #End the program.

#User decides to not end the program.
def EPCancel(popup):
    popup.destroy() #Destroy the pop-up.

def EndWorldProgram(window, textobject):
    global loadedFile, loadedDirectory
    dtext = textobject.GetText()    #Get the text from the TextObject.
    if dtext != "" or dtext != " ": #Check that the text isn't empty or just a space.
        popup = Tk()    #Create pop-up.
        popup.title(data["newfile_saveprompt"]) #Change title of pop-up.
        prompt = Label(popup, text = data["newfile_saveprompt"], font = tools.GetFont("text"))  #Create label on pop-up.
        prompt.grid(row = 0, column = 0)    #Display label.
        style = ttk.Style() #Create style.
        style.map("TButton", background = [("pressed", "white"), ("active", "green")])  #Set new style.
        byes = ttk.Button(popup, text = data["option_yes"], command = lambda: EPYes(popup, window, textobject), style = "TButton")  #Create yes button.
        bno = ttk.Button(popup, text = data["option_no"], command = lambda: EPNo(popup)) #Create "no" button.
        bcancel = ttk.Button(popup, text = data["option_cancel"], command = lambda: EPCancel(popup)) #Create "cancel" button.
        #byes.pack()
        byes.grid(row = 2, column = 0) #Display "yes" button.
        #bno.pack()
        bno.grid(row = 2, column = 1) #Display "no" button.
        #bcancel.pack()
        bcancel.grid(row = 2, column = 2) #Display "cancel" button.

#Update window title + some variables once the user has created a new file.
def NFYUpdate(window):
    global loadedFile, loadedDirectory, nf
    loadedFile = False
    loadedDirectory = "-1"
    tools.UpdateTitle(window, GetSaveDir(), CheckFileLoaded()) #Update title.
    nf = False

#User decides to create new file.
def NFYes(popup, window, textobject):
    global nf
    nf = True
    SaveFileProcess(window, textobject) #Save file content.
    popup.destroy() #Destroy pop-up.
    textobject.DeleteText() #Delete the text from the TextObject.
    loadedFile = False
    loadedDirectory = "-1"
    tools.UpdateTitle(window, GetSaveDir(), CheckFileLoaded())  #Update title.

def NFNo(popup, textobject):
    popup.destroy() #Destroy pop-up-
    textobject.DeleteText() #Delete text from TextObject.
    loadedFile = False
    loadedDirectory = "-1"

def NFCancel(popup):
    popup.destroy() #Destroy pop-up.

def NewFileProcess(window, textobject):
    global loadedFile, loadedDirectory
    dtext = textobject.GetText() #Get text from TextObject.
    if dtext != "" or dtext != " ": #Check that text isn't empty or just a space.
        popup = Tk() #Create new tkinter window.
        popup.title(data["newfile_saveprompt"]) #Set pop-up title.
        prompt = Label(popup, text = data["newfile_saveprompt"], font = tools.GetFont("text")) #Create label on pop-up.
        prompt.grid(row = 0, column = 0) #Display label.
        style = ttk.Style() #Create new style.
        style.map("TButton", background = [("pressed", "white"), ("active", "green")]) #Set new style.
        byes = ttk.Button(popup, text = data["option_yes"], command = lambda: NFYes(popup, window, textobject), style = "TButton") #Create "yes" button.
        bno = ttk.Button(popup, text = data["option_no"], command = lambda: NFNo(popup, textobject)) #Create "no" button.
        bcancel = ttk.Button(popup, text = data["option_cancel"], command = lambda: NFCancel(popup)) #Create "cancel" button.
        #byes.pack()
        byes.grid(row = 2, column = 0) #Display "yes" button.
        #bno.pack()
        bno.grid(row = 2, column = 1) #Display "no" button.
        #bcancel.pack()
        bcancel.grid(row = 2, column = 2) #Display "cancel" button.
    else:
        textobject.DeleteText() #Delete text from TextObject.
        loadedFile = False
        loadedDirectory = "-1"

def SaveFileProcess(window, textobject):
    global loadedFile, loadedDirectory, nf
    if loadedFile == True and loadedDirectory != "-1": #If file loaded and directory is not "-1".
        print("Saving file...")
        with open(loadedDirectory, "w", encoding = "utf-8") as savefile:   #Open file for writing with "utf-8" encoding.
            print(textobject.GetText())
            savefile.write(textobject.GetText()) #Write TextObject text to file.
        print("File saved successfully.")
        if nf == True:
            NFYUpdate(window) #Update window.
    else:
        SaveFileAsProcess(window, textobject) #Go to SaveFileAsProcess.

def SaveFileAsProcess(window, textobject):
    global loadedFile, loadedDirectory, nf
    print("Saving file as...")
    try:
        loadedDirectory = filedialog.asksaveasfilename(initialdir = "%desktop%", title = data["savemenu_savetitle"], filetypes = ((data["savemenu_texttype"], "*.txt"), (data["savemenu_alltypes"], "*.*"))) #Ask user for file path.
        loadedFile = True
        if loadedDirectory != "":   #If we have a path.
            with open(loadedDirectory, "w", encoding = "utf-8") as savefile:    #Open file for writing with "utf-8" encoding.
                print(textobject.GetText())
                savefile.write(textobject.GetText())    #Write TextObject text to the file.
            print("File saved successfully.")
            tools.UpdateTitle(window, GetSaveDir(), CheckFileLoaded())  #Update window title.
            if nf == True:
                NFYUpdate(window) #Update window title.
        else:
            loadedFile = False
            loadedDirectory = "-1"
            print("File was not saved.")
    except:
        print("Failed to save file.")
        print(traceback.format_exc())

def LoadFileProcess(window, textobject):
    global loadedFile, loadedDirectory
    print("Loading file...")
    try:
        loadedDirectory = filedialog.askopenfilename(initialdir = "%desktop%", title = data["savemenu_savetitle"], filetypes = ((data["savemenu_texttype"], "*.txt"), (data["savemenu_alltypes"], "*.*"))) #Get file path.
        if loadedDirectory != "":   #If we have a file path.
            loadedFile = True
            with open(loadedDirectory, "r", encoding = "utf-8") as savefile:    #Open file for reading with "utf-8" encoding.
                textobject.ReplaceText(savefile.read()) #Read text from file and set it as the TextObject text.
            tools.UpdateTitle(window, GetSaveDir(), CheckFileLoaded())  #Update window title.
            print("File loaded successfully.")
        else:
            loadedFile = False
            loadedDirectory = "-1"
            print("File wasn't loaded.")
    except:
        print("Failed to load file.")
        print(traceback.format_exc())

def GetSaveDir():
    global loadedDirectory
    return loadedDirectory

def CheckFileLoaded():
    global loadedFile
    return loadedFile
