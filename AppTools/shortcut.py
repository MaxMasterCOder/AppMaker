import os


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