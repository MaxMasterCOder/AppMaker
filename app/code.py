import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame,tkinter.filedialog
def createShortcut(target,destination=os.path.dirname(__file__),name='Shortcut',iconLocation=None):
    os.system('python -m pip install pywin32')
    import win32com.client
    path = os.path.join(destination,name + '.lnk')
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    if iconLocation != None:
        shortcut.IconLocation = iconLocation
    shortcut.save()
def pygame_width():
    info = pygame.display.Info()
    return info.current_w
def pygame_height():
    info = pygame.display.Info()
    return info.current_h
def pygame_screensize():
    return pygame.display.set_mode((pygame_width(),pygame_height()))
def pickFile():
    return tkinter.filedialog.askopenfilename()
def pickDir():
    return tkinter.filedialog.askdirectory()
def dirPath(path):
    if os.path.exists():
        return os.path.dirname(path)
    else:
        print('\nERROR. Path does not exist\n')