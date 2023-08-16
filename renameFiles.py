from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, StringVar
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/renameFile")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def openHome():
    window.destroy()
    import HomeScreen


def openMerger():
    window.destroy()
    import pdfMerger


def openFiles():
    entry_3.config(state="normal")
    entry_3.delete("1.0", "end")
    filePath = filedialog.askopenfilenames()
    for fileDirectory in filePath:
        index = fileDirectory.rfind('/')
        fileName = fileDirectory[(index + 1):]
        entry_3.insert("1.0", (fileName + "\n"), "center")
    entry_3.config(state="disabled")
    return filePath


def renameFiles():
    global button_pressed
    
    def enter(self):
        button_pressed.set("button pressed")
        
    window.bind('<Return>', enter)
    button_pressed = StringVar()

    for fileDirectory in openFiles():
        entry_2.config(state="normal")
        entry_2.delete("1.0", "end")
        entry_1.delete(0, "end")
        
        index = fileDirectory.rfind('/')
        fileName = fileDirectory[(index + 1):]
        entry_2.insert("1.0", ("Rename file \"" + fileName + "\" to: "), "center")
        entry_2.config(state="disabled")
        
        button_3.wait_variable(button_pressed)
        
        renamedFile = entry_1.get()
        p_index = fileDirectory.rfind('.')
        renamedDir = fileDirectory[0:(index + 1)] + renamedFile + fileDirectory[p_index:]
        os.rename(fileDirectory, renamedDir)
        entry_2.config(state="disabled")
        


window = Tk()
window.title("File Renamer")
window.geometry("1280x720")
window.configure(bg = "#21222F")


canvas = Canvas(
    window,
    bg = "#21222F",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    58.0,
    360.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("merger.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("PDF Merger Button clicked"), openMerger()],
    relief="flat"
)
button_1.place(
    x=19.0,
    y=206.0,
    width=65.0,
    height=65.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("Home.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("Home Button clicked"), openHome()],
    relief="flat"
)
button_2.place(
    x=19.0,
    y=20.0,
    width=65.0,
    height=65.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("Rename.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("Rename Button clicked"), button_pressed.set("button pressed")],
    relief="flat"
)
button_3.place(
    x=846.0,
    y=601.0,
    width=250.0,
    height=53.0
)


button_image_5 = PhotoImage(
    file=relative_to_assets("SelectFiles.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("Select Files Button clicked"), renameFiles()],
    relief="flat"
)
button_5.place(
    x=846.0,
    y=310.0,
    width=250.0,
    height=53.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("Text.png"))
image_2 = canvas.create_image(
    405.0,
    307.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    971.0,
    530.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    971.0,
    530.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#252736",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=707.0,
    y=511.0,
    width=528.0,
    height=38.0
)
entry_1.configure(justify="center")

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    971.0,
    430.0,
    image=image_image_4
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    971.0,
    430.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#252736",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=707.0,
    y=411.0,
    width=528.0,
    height=38.0
)
entry_2.config(state="disabled")
entry_2.tag_configure("center", justify="center")

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    971.0,
    172.0,
    image=image_image_5
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    971.0,
    173.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#252736",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=707.0,
    y=79.0,
    width=528.0,
    height=186.0
)
entry_3.config(state="disabled")
entry_3.tag_configure("center", justify="center")

window.resizable(False, False)
window.mainloop()
