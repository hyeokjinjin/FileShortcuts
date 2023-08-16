from pathlib import Path
import PyPDF2
import os

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/appendPDF")

merge = PyPDF2.PdfMerger()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def openRenamer():
    window.destroy()
    import renameFiles


def openHome():
    window.destroy()
    import HomeScreen


def pushNameToBox():
    filePath = filedialog.askopenfilenames()
    entry_1.config(state="normal")
    for fileDirectory in filePath:
        if fileDirectory.endswith(".pdf"):
            index = fileDirectory.rfind('/')
            file = fileDirectory[(index + 1):]
            entry_1.insert("1.0", (file + "\n"), "center")
            merge.append(fileDirectory)
    entry_1.config(state="disabled")


def saveNewPDF():
    folderPath = filedialog.askdirectory()
    os.chdir(folderPath)
    merge.write("combinedPDF.pdf")
    


#Makes the window for the shortcut page
window = Tk()
window.title("PDF Merger")
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


#Rename button on the side
button_image_1 = PhotoImage(
    file=relative_to_assets("Rename.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("Rename Button clicked"), openRenamer()],
    relief="flat"
)
button_1.place(
    x=19.0,
    y=113.0,
    width=65.0,
    height=65.0
)


#Home button on the side
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


#Save PDF button
button_image_3 = PhotoImage(
    file=relative_to_assets("SavePDF.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("Save Button clicked"), saveNewPDF()],
    relief="flat"
)
button_3.place(
    x=803.0,
    y=533.0,
    width=343.0,
    height=53.0
)


#Select Files button
button_image_4 = PhotoImage(
    file=relative_to_assets("SelectFiles.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("Select Files Button clicked"), pushNameToBox()],
    relief="flat"
)
button_4.place(
    x=803.0,
    y=452.0,
    width=343.0,
    height=53.0
)


#TextBox Images and Entry Widget
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    974.0,
    272.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    405.0,
    307.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    974.0,
    271.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#252736",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=709.0,
    y=125.0,
    width=530.0,
    height=291.0
)
entry_1.config(state="disabled")
entry_1.tag_configure("center", justify="center")

window.resizable(False, False)
window.mainloop()
