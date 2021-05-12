"""
    textobject.py
    DGTavo88

    Contains the TextObject class.

    TextObject is the object used to write things.
    The class contains functions for customizing color of elements, as well as modifying the text of the object.

    To do:
     - Customize font and text size.
"""

from tkinter import *
from tkinter import font
import tools

class TextObject():
    def __init__(self, window):
        tobject = Text(window, font = tools.GetFont("text")) #Create Text widget.
        tobject.pack(expand=True, fill=BOTH) #Display Text widget.
        self.instance = tobject #Save Text widget reference.
        self.loadedtext = ""

    #Change Background Color.
    def BGColor(self, scolor = "#FFFFFF"):
        self.instance.configure(bg = scolor)

    #Change Text Color.
    def TextColor(self, scolor = "#000000"):
        self.instance.configure(fg = scolor)

    #Change Cursor Color.
    def CursorColor(self, scolor = "#000000"):
        self.instance.configure(insertbackground = scolor)

    #Get the text from the TextObject.
    def GetText(self):
        return self.instance.get("1.0", "end")

    #Delete all text from TextObject.
    def DeleteText(self):
        self.instance.delete("1.0", "end")

    #Replace the text from the TextObject.
    def ReplaceText(self, rtext):
        self.DeleteText() #Delete text.
        self.instance.insert("end", rtext) #Insert text.
