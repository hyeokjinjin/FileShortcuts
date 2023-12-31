from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/HomeScreen")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def openRenamer():
    window.destroy()
    import renameFiles
    
    
def openMerger():
    window.destroy()
    import pdfMerger


window = Tk()
window.title("Shortcut App Home Screen")
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
    file=relative_to_assets("button_1.png"))
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
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("Rename Button clicked"), openRenamer()],
    relief="flat"
)
button_2.place(
    x=19.0,
    y=113.0,
    width=65.0,
    height=65.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    640.0,
    359.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
