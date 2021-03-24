"""
    TextEditor.py
    DGTavo88

    Main file for the TextEditor.

    To execute, use "cd" to this directory, then use "python TextEditor.py"
"""
from tkinter import * #Import the tkinter module.
from tkinter import font
from textobject import TextObject #Import the TextObject class from textobject.py.
import tools #Import tools from tools.py.
from fmcommands import * #Import the fmcommands module from fcommands.py.
import ctypes #Import ctypes to fix text blur.

data = tools.LoadLanguageText() #Load the text from the JSON File.

ctypes.windll.shcore.SetProcessDpiAwareness(1) #Fix text blur.

#Create main window.
mainwindow = Tk()

for f in font.families():
    print(f)

#Create text object.
tobject = TextObject(mainwindow)

#Remove these to disable dark mode.
tobject.BGColor("#000000")
tobject.TextColor("#FFFFFF")
tobject.CursorColor("#FFFFFF")

#Create menu bar.
menubar = Menu(mainwindow)

#File Menu.
filemenu = Menu(menubar, tearoff = False, font = tools.GetFont("menu")) #Create File Menu.
filemenu.add_command(label = data["filemenu_newfile"], command = lambda: NewFileProcess(mainwindow, tobject)) #Add command "New File".
filemenu.add_command(label = data["filemenu_openfile"], command = lambda: LoadFileProcess(mainwindow, tobject)) #Add command "Open File".
filemenu.add_separator() #Add a separator
filemenu.add_command(label = data["filemenu_savefile"], command = lambda: SaveFileProcess(mainwindow, tobject)) #Add command "Save File".
filemenu.add_command(label = data["filemenu_savefileas"], command = lambda: SaveFileAsProcess(mainwindow, tobject)) #Add command "Save File As".
filemenu.add_separator() #Add a separator
filemenu.add_command(label = data["filemenu_exiteditor"], command = lambda: EndWorldProgram(mainwindow, tobject)) #Add command "Exit Editor".
menubar.add_cascade(label = data["filemenu_label"], menu = filemenu) #Add the file menu as a cascade menu with the label "File".

#Overwrite Closing Protocol
mainwindow.protocol("WM_DELETE_WINDOW", lambda: EndWorldProgram(mainwindow, tobject))

#Show menu bar.
mainwindow.config(menu = menubar)

#Set the title of the window.
mainwindow.title(data["window_name_untitled"])

#Start the window's main loop.
mainwindow.mainloop()
