from tkinter import *
from tkinter import filedialog
import PyPDF2
import os


merge = PyPDF2.PdfMerger()


def openPDF():
    filePath = filedialog.askopenfilenames()
    txtBox.config(state=NORMAL)
    for file in filePath:
        if file.endswith(".pdf"):
            txtBox.insert(INSERT, (file + "\n"))
            merge.append(file)
    txtBox.config(state=DISABLED)


def savePDF():
    folderPath = filedialog.askdirectory()
    os.chdir(folderPath)
    merge.write("combindedPDF.pdf")
    createdBox.insert(INSERT, "Created")
    createdBox.config(state=DISABLED)
    createdBox.pack()


window = Tk(className=' PDF Appending Tool')
window.geometry("450x350")


txtBox = Text(window, height=15, width=45)
createdBox = Text(window, height=1, width=9)
PDFopenButton = Button(text="Open Files", command=openPDF)
PDFsaveButton = Button(text="Select Folder to Save New PDF", command=savePDF)


txtBox.pack()
PDFopenButton.pack()
PDFsaveButton.pack()
txtBox.config(state=DISABLED)

window.mainloop()
