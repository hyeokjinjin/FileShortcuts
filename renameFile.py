from tkinter import *
from tkinter import filedialog
import sys
import os


def openFiles():
    global filePath
    filePath = filedialog.askopenfilenames()
    for fileDirectory in filePath:
        index = fileDirectory.rfind('/')
        fileName = fileDirectory[(index + 1):]
        txtBox.insert(INSERT, (fileName + "\n"))
    txtBox.config(state=DISABLED)
        
def renameFiles():
    def enter(self):
        button_pressed.set("button pressed")
    window.bind('<Return>', enter)
    
    renameFileWindow.pack()
    userRenameInput.pack()
    
    renameFileButton = Button(text="Rename", command=lambda: button_pressed.set("button pressed"))
    renameFileButton.pack()
    
    button_pressed = StringVar()
    for fileDirectory in filePath:
        renameFileWindow.delete("1.0", "end")
        userRenameInput.delete(0, END)
        
        #button_pressed = StringVar()
        
        index = fileDirectory.rfind('/')
        fileName = fileDirectory[(index + 1):]
        renameFileWindow.insert(INSERT, ("Rename file \"" + fileName + "\" to: "))
        
        renameFileButton.wait_variable(button_pressed)
        
        renamedFile = userRenameInput.get()
        p_index = fileDirectory.rfind('.')
        renamedDir = fileDirectory[0:(index + 1)] + renamedFile + fileDirectory[p_index:]
        os.rename(fileDirectory, renamedDir) 
    

window = Tk(className=" File Renaming Tool")
window.geometry("600x400")


txtBox = Text(window, height=15, width=25)
openFileButton = Button(text="Open Files to Rename", command=openFiles)
startRenameButton = Button(text="Start Rename Each File", command=renameFiles)
renameFileWindow = Text(window, height=3, width=40)
userRenameInput = Entry()


openFileButton.pack()
txtBox.pack()
startRenameButton.pack()



window.mainloop()
