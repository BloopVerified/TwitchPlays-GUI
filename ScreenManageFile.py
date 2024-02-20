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

class ScreenManage():
    startXGet = ''
    endXGet = ''
    startYGet = ''
    endYGet = ''
    screenOptBackUp = ''
    switchScreen = 0
    def __init__(self):
        self.startX = StringVar()
        self.endX = StringVar()
        self.startY = StringVar()
        self.endY = StringVar()

        self.startX.set('0')
        self.endX.set('0')
        self.startY.set('0')
        self.endY.set('0')


    def screenOption(self, start):
        screenRes = mtTkinter.Toplevel(start)
        ScreenManage.screenOptBackUp = screenRes
        screenRes.lift()
        screenRes.attributes('-topmost', True)
        screenRes.grab_set()
        screenRes.grab_release()
        screenRes.focus_force()
        screenRes.title("ContentPlays")
        screenRes.iconbitmap("icon.ico")
        screenRes.geometry("300x300+700+300")
        screenRes.config(background="white")
        screenRes.minsize(300, 400)
        screenRes.maxsize(300, 400)
        youtubePhoto = PhotoImage(file="youtube.png")
        youtubeResize = youtubePhoto.subsample(3, 3)
        twitchPhoto = PhotoImage(file="twitch.png")
        twitchResize = twitchPhoto.subsample(3, 3)
        separatorText = Label(screenRes, text="- or -",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        separatorText.place(x=135, y=100)
        ScreenXStart = Label(screenRes, text="Enter Screen X Start Variable",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        ScreenXEnd = Label(screenRes, text="Enter Screen X End Variable",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        ScreenXStartEntry = Entry(screenRes, width=25)
        ScreenXEndEntry = Entry(screenRes, width=25)

        ScreenYStart = Label(screenRes, text="Enter Screen Y Start Variable",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        ScreenYEnd = Label(screenRes, text="Enter Screen Y End Variable",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        ScreenYStartEntry = Entry(screenRes, width=25)
        ScreenYEndEntry = Entry(screenRes, width=25)
        monitorOneFunc = partial(ScreenManage.monitorDecisionOne, self, ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry)
        monitorTwoFunc = partial(ScreenManage.monitorDecisionTwo, self, ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry)
        monitorThreeFunc = partial(ScreenManage.monitorDecisionThree, self, ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry)
        monitorOne = Button(screenRes, text="Screen 1",height = 2, width = 6, command = monitorOneFunc)
        monitorTwo = Button(screenRes, text="Screen 2",height = 2, width = 6, command = monitorTwoFunc)
        monitorThree = Button(screenRes, text="Screen 3",height = 2, width = 6, command = monitorThreeFunc)
        monitorOne.place(x=25, y=25)
        monitorTwo.place(x=125, y=25)
        monitorThree.place(x=225, y=25)
        ScreenXStart.place(x=25, y=150)
        ScreenXStartEntry.place(x=25, y=175)
        ScreenXEnd.place(x=25, y=200)
        ScreenXEndEntry.place(x=25, y=225)
        ScreenYStart.place(x=25, y=250)
        ScreenYStartEntry.place(x=25, y=275)
        ScreenYEnd.place(x=25, y=300)
        ScreenYEndEntry.place(x=25, y=325)
        screenLimitFunc = partial(ScreenManage.ScreenGet, self,screenRes, ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry)
        SubmitScreenButton = Button(screenRes, height = 1, width = 5, text="Submit", font = ("Arial", 12), command= screenLimitFunc)
        SubmitScreenButton.place(x=125, y=360)
        screenRes.after(1, self.updateScreenEntry, ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry)
        closeRes = partial(ScreenManage.screenRes_close_window, self, screenRes)
        screenRes.protocol("WM_DELETE_WINDOW", closeRes)

    def monitorDecisionOne(self, ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry):
        try:
            testing = [''] *3
            z = 0
            for m in get_monitors():
                testing[z] = str(m)
                z+= 1
            monitorOne = testing[0].split()

            monitorStartHeight = monitorOne[1]
            monitorStartHeight = monitorStartHeight.replace('y=','')
            monitorStartHeight = monitorStartHeight.replace(',','')

            monitorEndHeight = monitorOne[3]
            monitorEndHeight = monitorEndHeight.replace('height=','')
            monitorEndHeight = monitorEndHeight.replace(',','')

            monitorStartWidth = monitorOne[0]
            monitorStartWidth = monitorStartWidth.replace('Monitor(x=','')
            monitorStartWidth = monitorStartWidth.replace(',','')

            monitorEndWidth = monitorOne[2]
            monitorEndWidth = monitorEndWidth.replace('width=','')
            monitorEndWidth = monitorEndWidth.replace(',','')


            startX = monitorStartWidth
            endX = int(monitorEndWidth) + int(monitorStartWidth)
            startY = monitorStartHeight
            endY = int(monitorEndHeight) + int(monitorStartHeight)
        except Exception as e:
            startX = 0
            endX = 0
            startY = 0
            endY = 0

        ScreenXStartEntry.delete(0, END)
        ScreenXStartEntry.insert(END, startX)
        ScreenXEndEntry.delete(0, END)
        ScreenXEndEntry.insert(END, endX)
        ScreenYStartEntry.delete(0, END)
        ScreenYStartEntry.insert(END, startY)
        ScreenYEndEntry.delete(0, END)
        ScreenYEndEntry.insert(END, endY)

    def monitorDecisionTwo(self, ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry):
        try:
            testing = [''] *3
            z = 0
            for m in get_monitors():
                testing[z] = str(m)
                z+= 1
            monitorOne = testing[1].split()

            monitorStartHeight = monitorOne[1]
            monitorStartHeight = monitorStartHeight.replace('y=','')
            monitorStartHeight = monitorStartHeight.replace(',','')

            monitorEndHeight = monitorOne[3]
            monitorEndHeight = monitorEndHeight.replace('height=','')
            monitorEndHeight = monitorEndHeight.replace(',','')

            monitorStartWidth = monitorOne[0]
            monitorStartWidth = monitorStartWidth.replace('Monitor(x=','')
            monitorStartWidth = monitorStartWidth.replace(',','')

            monitorEndWidth = monitorOne[2]
            monitorEndWidth = monitorEndWidth.replace('width=','')
            monitorEndWidth = monitorEndWidth.replace(',','')


            startX = monitorStartWidth
            endX = int(monitorEndWidth) + int(monitorStartWidth)
            startY = monitorStartHeight
            endY = int(monitorEndHeight) + int(monitorStartHeight)

        except Exception as e:
            startX = 0
            endX = 0
            startY = 0
            endY = 0

        ScreenXStartEntry.delete(0, END)
        ScreenXStartEntry.insert(END, startX)
        ScreenXEndEntry.delete(0, END)
        ScreenXEndEntry.insert(END, endX)
        ScreenYStartEntry.delete(0, END)
        ScreenYStartEntry.insert(END, startY)
        ScreenYEndEntry.delete(0, END)
        ScreenYEndEntry.insert(END, endY)

    def monitorDecisionThree(self, ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry):
        try:
            testing = [''] *3
            z = 0
            for m in get_monitors():
                testing[z] = str(m)
                z+= 1
            monitorOne = testing[2].split()

            monitorStartHeight = monitorOne[1]
            monitorStartHeight = monitorStartHeight.replace('y=','')
            monitorStartHeight = monitorStartHeight.replace(',','')

            monitorEndHeight = monitorOne[3]
            monitorEndHeight = monitorEndHeight.replace('height=','')
            monitorEndHeight = monitorEndHeight.replace(',','')

            monitorStartWidth = monitorOne[0]
            monitorStartWidth = monitorStartWidth.replace('Monitor(x=','')
            monitorStartWidth = monitorStartWidth.replace(',','')

            monitorEndWidth = monitorOne[2]
            monitorEndWidth = monitorEndWidth.replace('width=','')
            monitorEndWidth = monitorEndWidth.replace(',','')


            startX = monitorStartWidth
            endX = int(monitorEndWidth) + int(monitorStartWidth)
            startY = monitorStartHeight
            endY = int(monitorEndHeight) + int(monitorStartHeight)
        except Exception as e:
            startX = 0
            endX = 0
            startY = 0
            endY = 0

        ScreenXStartEntry.delete(0, END)
        ScreenXStartEntry.insert(END, startX)
        ScreenXEndEntry.delete(0, END)
        ScreenXEndEntry.insert(END, endX)
        ScreenYStartEntry.delete(0, END)
        ScreenYStartEntry.insert(END, startY)
        ScreenYEndEntry.delete(0, END)
        ScreenYEndEntry.insert(END, endY)


    def screenRes_close_window(self, screenRes):
        screenRes.destroy()
    def ScreenGet(self, screenRes, ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry):
        self.startX.set(ScreenXStartEntry.get())
        ScreenManage.startXGet = (ScreenXStartEntry.get())
        self.endX.set(ScreenXEndEntry.get())
        ScreenManage.endXGet = (ScreenXEndEntry.get())
        self.startY.set(ScreenYStartEntry.get())
        ScreenManage.startYGet = (ScreenYStartEntry.get())
        self.endY.set(ScreenYEndEntry.get())
        ScreenManage.endYGet = (ScreenYEndEntry.get())
        screenRes.destroy()

    def updateScreenEntry(self,ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry):
        ScreenXStartEntry.delete(END, 0)
        ScreenXStartEntry.insert(0, self.startX.get())
        ScreenXEndEntry.insert(0, self.endX.get())
        ScreenYStartEntry.insert(0, self.startY.get())
        ScreenYEndEntry.insert(0, self.endY.get())
