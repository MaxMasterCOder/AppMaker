from tkinter import Tk
from PyQt5.QtWidgets import QFileDialog
import tkinter.filedialog
import os
Tk().withdraw()
def pickFile():
    return tkinter.filedialog.askopenfilename()
def pickDir():
    return tkinter.filedialog.askdirectory()
def dirPath(path):
    if os.path.exists():
        os.path.dirname(path)
    else:
        print('\nERROR. Path does not exist\n')