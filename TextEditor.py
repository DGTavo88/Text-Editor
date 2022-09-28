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
from emcommands import *
import ctypes #Import ctypes to fix text blur.
import globals #Global Variables to be used all throughout the place.

globals.Init()

globals.data = tools.LoadLanguageText() #Load the text from the JSON File.

ctypes.windll.shcore.SetProcessDpiAwareness(1) #Fix text blur.

#Create main window.
globals.mainwindow = Tk()

for f in font.families():
    print(f)

#Create text object.
globals.tobject = TextObject(globals.mainwindow)

#Remove these to disable dark mode.
globals.tobject.BGColor("#000000")
globals.tobject.TextColor("#FFFFFF")
globals.tobject.CursorColor("#FFFFFF")

#Create menu bar.
globals.menubar = Menu(globals.mainwindow)

#File Menu.
globals.filemenu = Menu(globals.menubar, tearoff = False, font = tools.GetFont("menu")) #Create File Menu.
globals.filemenu.add_command(label = globals.data["filemenu_newfile"], command = NewFileProcess, accelerator = "Ctrl + N") #Add command "New File".
globals.filemenu.add_command(label = globals.data["filemenu_openfile"], command = LoadFileProcess, accelerator = "Ctrl + O") #Add command "Open File".
globals.filemenu.add_separator() #Add a separator
globals.filemenu.add_command(label = globals.data["filemenu_savefile"], command = SaveFileProcess, accelerator = "Ctrl + S") #Add command "Save File".
globals.filemenu.add_command(label = globals.data["filemenu_savefileas"], command = SaveFileAsProcess, accelerator = "Ctrl + Shift + S") #Add command "Save File As".
globals.filemenu.add_separator() #Add a separator
globals.filemenu.add_command(label = globals.data["filemenu_exiteditor"], command = EndWorldProgram, accelerator = "Ctrl + E") #Add command "Exit Editor".

globals.editmenu = Menu(globals.menubar, tearoff = False, font = tools.GetFont("menu"))

#Edit Menu.
globals.viewmenu = Menu(globals.menubar, tearoff = False, font = tools.GetFont("menu"))
globals.viewmenu.add_command(label = globals.data["editmenu_edittext_current"], command = CurrentTextSettings)
globals.viewmenu.add_separator()
globals.viewmenu.add_command(label = globals.data["editmenu_edittext_global"])
globals.viewmenu.add_command(label = globals.data["editmenu_editsettings"])

globals.menubar.add_cascade(label = globals.data["filemenu_label"], menu = globals.filemenu) #Add the file menu as a cascade menu with the label "File".
globals.menubar.add_cascade(label = globals.data["editmenu_label"], menu = globals.viewmenu)
globals.menubar.add_cascade(label = "View", menu = globals.viewmenu)

globals.mainwindow.bind_all("<Control-n>", lambda x: NewFileProcess())
globals.mainwindow.bind_all("<Control-o>", lambda x: LoadFileProcess())
globals.mainwindow.bind_all("<Control-s>", lambda x: SaveFileProcess())
globals.mainwindow.bind_all("<Control-Shift-S>", lambda x: SaveFileAsProcess())
globals.mainwindow.bind_all("<Control-e>", lambda x: EndWorldProgram())
globals.mainwindow.bind_all("<Key>", lambda x: tools.CheckForTextChanges())

#Overwrite Closing Protocol
globals.mainwindow.protocol("WM_DELETE_WINDOW", lambda: EndWorldProgram())

#Show menu bar.
globals.mainwindow.config(menu = globals.menubar)

#Set the title of the window.
globals.mainwindow.title(globals.data["window_name_untitled"])

#Start the window's main loop.
globals.mainwindow.mainloop()
