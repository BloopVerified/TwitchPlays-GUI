import concurrent.futures
import ctypes
import threading as threading
import time
import tkinter
from functools import partial
from tkinter import *
from tkinter.ttk import Combobox
import keyboard
import mouse
import mttkinter as mtTkinter
import pyautogui
import pydirectinput
from mttkinter import *
from screeninfo import get_monitors, Monitor

import GreenScreenFile

class MouseManage():
    moveMouseUp = 45
    moveMouseDown = 45
    moveMouseRight = 45
    moveMouseLeft = 45
    textMouseUp = ''
    textMouseDown = ''
    textMouseRight = ''
    textMouseLeft = ''
    rightClick = ''
    rightClickValue = ''
    leftClick = ''
    leftClickValue = ''
    mouseOptBackUp = ''

    def __init__(self):
        self.upMouse = None
        self.downMouse = None
        self.leftMouse = None
        self.rightMouse = None

        self.mouseUpText = StringVar()
        self.mouseUpText.set('')
        self.mouseDownText = StringVar()
        self.mouseDownText.set('')
        self.mouseRightText = StringVar()
        self.mouseRightText.set('')
        self.mouseLeftText = StringVar()
        self.mouseLeftText.set('')
        self.keyOptions = ('none','left', 'right')

        self.leftClickText = StringVar()
        self.leftClickKey = StringVar()
        self.rightClickText = StringVar()
        self.rightClickKey = StringVar()
        self.leftClickText.set('')
        self.leftClickKey.set('0')
        self.rightClickText.set('')
        self.rightClickKey.set('0')
        self.upM = StringVar()
        self.upM.set('45')
        self.downM = StringVar()
        self.downM.set('45')
        self.leftM = StringVar()
        self.leftM.set('45')
        self.rightM = StringVar()
        self.rightM.set('45')

    def mouseOption(self, start, greenScreenCls):
        mouseOpt = mtTkinter.Toplevel(start)
        MouseManage.mouseOptBackUp = mouseOpt
        mouseOpt.lift()
        mouseOpt.attributes('-topmost', True)
        mouseOpt.grab_set()
        mouseOpt.grab_release()
        mouseOpt.focus_force()
        mouseOpt.title("ContentPlays")
        mouseOpt.iconbitmap("icon.ico")
        mouseOpt.geometry("500x500+700+300")
        mouseOpt.config(background="white")
        mouseOpt.minsize(500, 500)
        mouseOpt.maxsize(500, 500)

        mouseUp = Label(mouseOpt, text="Mouse:",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        mouseUp.place(x=40, y=35)

        mouseUp = Label(mouseOpt, text="Chat Text:",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        mouseUp.place(x=120, y=35)

        mouseUp = Label(mouseOpt, text="Movement:",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        mouseUp.place(x=200, y=35)


#Mouse Up
        mouseUp = Label(mouseOpt, text="Mouse Up:",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        mouseUp.place(x=40, y=60)

        mouseUpTextEntry = Entry(mouseOpt, width=12, textvariable=self.mouseUpText)
        mouseUpTextEntry.place(x=120, y=60)

        self.upMouse = IntVar(mouseOpt)
        self.upMouse.set(value=int(self.upM.get()))
        mouseUpEntry = Spinbox(mouseOpt, from_= 0, to = 180, textvariable=self.upMouse)
        mouseUpEntry.place(x=200, y=60)

#Mouse Down
        mouseDown = Label(mouseOpt, text="Mouse Down:",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        mouseDown.place(x=40, y=85)

        mouseDownTextEntry = Entry(mouseOpt, width=12, textvariable=self.mouseDownText)
        mouseDownTextEntry.place(x=120, y=85)

        self.downMouse = IntVar(mouseOpt)
        self.downMouse.set(value=int(self.downM.get()))
        mouseDownEntry = Spinbox(mouseOpt, from_= 0, to = 180, textvariable=self.downMouse)
        mouseDownEntry.place(x=200, y=85)
# Mouse Right
        mouseRight = Label(mouseOpt, text="Mouse Right:",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        mouseRight.place(x=40, y=110)

        mouseRightTextEntry = Entry(mouseOpt, width=12, textvariable=self.mouseRightText)
        mouseRightTextEntry.place(x=120, y=110)

        self.rightMouse = IntVar(mouseOpt)
        self.rightMouse.set(value=int(self.rightM.get()))
        mouseRightEntry = Spinbox(mouseOpt, from_= 0, to = 180, textvariable=self.rightMouse)
        mouseRightEntry.place(x=200, y=110)

# Mouse Left
        mouseLeft = Label(mouseOpt, text="Mouse Left :",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        mouseLeft.place(x=40, y=135)

        mouseLeftTextEntry = Entry(mouseOpt, width=12, textvariable=self.mouseLeftText)
        mouseLeftTextEntry.place(x=120, y=135)

        self.leftMouse = IntVar(mouseOpt)
        self.leftMouse.set(value=int(self.leftM.get()))
        mouseLeftEntry = Spinbox(mouseOpt, from_= 0, to = 180, textvariable=self.leftMouse)
        mouseLeftEntry.place(x=200, y=135)

#Left Click
        leftClick = Label(mouseOpt, text="Left Click:",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        leftClick.place(x=40, y=160)

        leftClickTextEntry = Entry(mouseOpt, width=12, textvariable=self.leftClickText)
        leftClickTextEntry.place(x=120, y=160)

        leftClickCombo = Combobox(mouseOpt, width=10, textvariable=self.leftClickKey, values=self.keyOptions)
        leftClickCombo.place(x=200, y=160)

# Right Click
        rightClick = Label(mouseOpt, text="Right Click:",
                          bg="white",
                          fg="black",
                          font=("Arial", 9))
        rightClick.place(x=40, y=185)

        rightClickTextEntry = Entry(mouseOpt, width=12, textvariable=self.rightClickText)
        rightClickTextEntry.place(x=120, y=185)

        rightClickCombo = Combobox(mouseOpt, width=10, textvariable=self.rightClickKey , values=self.keyOptions)
        rightClickCombo.place(x=200, y=185)



# Mouse Icon
        mousePalmButton = Button(mouseOpt, text="", height=2, width=5, state=DISABLED)
        mouseLeftButton = Button(mouseOpt, text="L", height=1, width=2, state=DISABLED)
        mouseRightButton = Button(mouseOpt, text="R", height=1, width=2, state=DISABLED)
        mousePalmButton.place(x=400, y=75)
        mouseLeftButton.place(x=400, y=50)
        mouseRightButton.place(x=421, y=50)

        mouseMoveUpButton = Button(mouseOpt, text="↑", height=1, width=1, state=DISABLED)
        mouseMoveDownButton = Button(mouseOpt, text="↓", height=1, width=1, state=DISABLED)
        mouseMoveLeftButton = Button(mouseOpt, text="←", height=1, width=1, state=DISABLED)
        mouseMoveRightButton = Button(mouseOpt, text="→", height=1, width=1, state=DISABLED)
        mouseMoveUpButton.place(x=415, y=20)
        mouseMoveDownButton.place(x=415, y=120)
        mouseMoveLeftButton.place(x=375, y=70)
        mouseMoveRightButton.place(x=450, y=70)

#Mouse Manage Functions
        submitControl = partial(MouseManage.submitMouse, self, mouseOpt, mouseUpEntry, mouseDownEntry, mouseRightEntry, mouseLeftEntry, mouseUpTextEntry, mouseDownTextEntry, mouseRightTextEntry, mouseLeftTextEntry,leftClickTextEntry,leftClickCombo,rightClickTextEntry,rightClickCombo)
        submitButton = Button(mouseOpt, text='Submit', command=submitControl)
        submitButton.place(x=195, y=450)
        clearControl = partial(MouseManage.clearMouse, self, mouseUpEntry, mouseDownEntry, mouseRightEntry, mouseLeftEntry, mouseUpTextEntry, mouseDownTextEntry, mouseRightTextEntry, mouseLeftTextEntry,leftClickTextEntry,leftClickCombo,rightClickTextEntry,rightClickCombo)
        clearButton = Button(mouseOpt, text='Clear', command=clearControl)
        clearButton.place(x=255, y=450)
        mouseOpt.after(1, MouseManage.updateMouse, self, mouseOpt, mouseUpTextEntry, mouseDownTextEntry, mouseRightTextEntry, mouseLeftTextEntry, leftClickTextEntry,leftClickCombo,rightClickTextEntry,rightClickCombo)
        closeMouse = partial(MouseManage.closeMouse_close_window, self, mouseOpt)
        mouseOpt.protocol("WM_DELETE_WINDOW", closeMouse)
        startcloseMouse = partial(MouseManage.alt_closeMouse_close_window, self, mouseOpt, start)
        start.protocol("WM_DELETE_WINDOW", startcloseMouse)

    def closeMouse_close_window(self, mouseOpt):
        mouseOpt.destroy()

    def alt_closeMouse_close_window(self, mouseOpt, start):
        try:
            mouseOpt.destroy()
            GreenScreenFile.GreenScreen.greenScreenCls = True
            start.destroy()
            exit()
        except Exception as e:
            GreenScreenFile.GreenScreen.greenScreenCls = True
            start.destroy()
            exit()

    def submitMouse(self, mouseOpt, mouseUpEntry, mouseDownEntry, mouseRightEntry, mouseLeftEntry, mouseUpTextEntry, mouseDownTextEntry, mouseRightTextEntry, mouseLeftTextEntry,leftClickTextEntry,leftClickCombo,rightClickTextEntry,rightClickCombo):
        if(mouseUpTextEntry.get() != ''):
            self.upM.set(self.upMouse.get())
            self.mouseUpText.set(mouseUpTextEntry.get())
            MouseManage.moveMouseUp = self.upMouse.get()
            MouseManage.textMouseUp = mouseUpTextEntry.get()
        else:
            self.upM.set('45')
            self.mouseUpText.set('')
            MouseManage.moveMouseUp = 45
            MouseManage.textMouseUp = ''

        if(mouseDownTextEntry.get() != ''):
            self.downM.set(self.downMouse.get())
            self.mouseDownText.set(mouseDownTextEntry.get())
            MouseManage.moveMouseDown = self.downMouse.get()
            MouseManage.textMouseDown = mouseDownTextEntry.get()
        else:
            self.downM.set('45')
            self.mouseDownText.set('')
            MouseManage.moveMouseDown = 45
            MouseManage.textMouseDown = ''

        if(mouseRightTextEntry.get() != ''):
            self.rightM.set(self.rightMouse.get())
            self.mouseRightText.set(mouseRightTextEntry.get())
            MouseManage.moveMouseRight = self.rightMouse.get()
            MouseManage.textMouseRight = mouseRightTextEntry.get()
        else:
            self.rightM.set('45')
            self.mouseRightText.set('')
            MouseManage.moveMouseRight = 45
            MouseManage.textMouseRight = ''

        if(mouseLeftTextEntry.get() != ''):
            self.leftM.set(self.leftMouse.get())
            self.mouseLeftText.set(mouseLeftTextEntry.get())
            MouseManage.moveMouseLeft = self.leftMouse.get()
            MouseManage.textMouseLeft = mouseLeftTextEntry.get()
        else:
            self.leftM.set('45')
            self.mouseLeftText.set('')
            MouseManage.moveMouseLeft = 45
            MouseManage.textMouseLeft = ''

        if(leftClickTextEntry.get() != ''):
            self.leftClickText.set(leftClickTextEntry.get())
            MouseManage.leftClick = leftClickTextEntry.get()
            MouseManage.leftClickValue = leftClickCombo.get()
            index = self.keyOptions.index(leftClickCombo.get())
            self.leftClickKey.set(str(index))
        else:
            self.leftClickText.set('')
            MouseManage.leftClick = ''
            MouseManage.leftClickValue = ''
            self.leftClickKey.set('0')
        if(rightClickTextEntry.get() != ''):
            self.rightClickText.set(rightClickTextEntry.get())
            MouseManage.rightClick = rightClickTextEntry.get()
            MouseManage.rightClickValue = rightClickCombo.get()
            index = self.keyOptions.index(rightClickCombo.get())
            self.rightClickKey.set(str(index))
        else:
            self.rightClickText.set('')
            MouseManage.rightClick = ''
            MouseManage.rightClickValue = ''
            self.rightClickKey.set('0')

        mouseOpt.destroy()

    def updateMouse(self, mouseOpt, mouseUpTextEntry, mouseDownTextEntry, mouseRightTextEntry, mouseLeftTextEntry,leftClickTextEntry,leftClickCombo,rightClickTextEntry,rightClickCombo):
        mouseUpTextEntry.config(text=self.mouseUpText.get())
        mouseDownTextEntry.config(text=self.mouseDownText.get())
        mouseRightTextEntry.config(text=self.mouseRightText.get())
        mouseLeftTextEntry.config(text=self.mouseLeftText.get())
        leftClickTextEntry.config(text=self.leftClickText.get())
        rightClickTextEntry.config(text=self.rightClickText.get())
        if self.leftClickKey.get() != 'none':
            leftClickCombo.current(self.leftClickKey.get())
        if self.rightClickKey.get() != 'none':
            rightClickCombo.current(self.rightClickKey.get())


    def clearMouse(self, mouseUpEntry, mouseDownEntry, mouseRightEntry, mouseLeftEntry, mouseUpTextEntry, mouseDownTextEntry, mouseRightTextEntry, mouseLeftTextEntry, leftClickTextEntry,leftClickCombo,rightClickTextEntry,rightClickCombo):
        self.upMouse.set(45)
        self.downMouse.set(45)
        self.rightMouse.set(45)
        self.leftMouse.set(45)
        leftClickCombo.current(0)
        rightClickCombo.current(0)
        mouseUpTextEntry.delete(0, END)
        mouseDownTextEntry.delete(0, END)
        mouseRightTextEntry.delete(0, END)
        mouseLeftTextEntry.delete(0, END)
        leftClickTextEntry.delete(0, END)
        rightClickTextEntry.delete(0, END)