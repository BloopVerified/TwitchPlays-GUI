import concurrent.futures
import ctypes
import threading as threading
import time
from functools import partial
from tkinter import *
import keyboard
import mouse
import mttkinter as mtTkinter
import pyautogui
import pydirectinput
from mttkinter import *
from screeninfo import get_monitors, Monitor
import TwitchPlays_Connection


class ScreenManage():
    def __init__(self):
        self.startX = StringVar()
        self.endX = StringVar()
        self.startY = StringVar()
        self.endY = StringVar()

        self.startX.set('0')
        self.endX.set('0')
        self.startY.set('0')
        self.endY.set('0')


    def screenOption(self):
        screenRes = mtTkinter.Tk()
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
        ScreenXStartEntry = Entry(screenRes, width=25, textvariable=self.startX)
        ScreenXEndEntry = Entry(screenRes, width=25, textvariable=self.endX)

        ScreenYStart = Label(screenRes, text="Enter Screen Y Start Variable",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        ScreenYEnd = Label(screenRes, text="Enter Screen Y End Variable",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        ScreenYStartEntry = Entry(screenRes, width=25, textvariable=self.startY)
        ScreenYEndEntry = Entry(screenRes, width=25, textvariable=self.endY)
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
        global startX, endX, startY, endY
        self.startX.set(ScreenXStartEntry.get())
        startX = (ScreenXStartEntry.get())
        self.endX.set(ScreenXEndEntry.get())
        endX = (ScreenXEndEntry.get())
        self.startY.set(ScreenYStartEntry.get())
        startY = (ScreenYStartEntry.get())
        self.endY.set(ScreenYEndEntry.get())
        endY = (ScreenYEndEntry.get())
        screenRes.destroy()

    def updateScreenEntry(self,ScreenXStartEntry, ScreenXEndEntry, ScreenYStartEntry, ScreenYEndEntry):
        ScreenXStartEntry.insert(END, self.startX.get())
        ScreenXEndEntry.insert(END, self.endX.get())
        ScreenYStartEntry.insert(END, self.startY.get())
        ScreenYEndEntry.insert(END, self.endY.get())


def backTrackAccount():
    platform.destroy()
    global previousTab
    previousTab -= 1
    global TWITCH_CHANNEL
    TWITCH_CHANNEL = ''
    global STREAMING_ON_TWITCH
    STREAMING_ON_TWITCH =  False
    global YOUTUBE_CHANNEL_ID
    YOUTUBE_CHANNEL_ID = ''
    global YOUTUBE_STREAM_URL
    YOUTUBE_STREAM_URL = None
    global twitchActive
    twitchActive = False
    global youtubeActive
    youtubeActive = False


def updateMessage():
    messageRelayOne.config(text=backMessageFour)
    messageRelayTwo.config(text=backMessageThree)
    messageRelayThree.config(text=backMessageTwo)
    messageRelayFour.config(text=backMessageOne)
    start.after(1, updateMessage)


def updateClear():
    global backMessageFour, backMessageThree, backMessageTwo, backMessageOne
    backMessageFour = ''
    backMessageThree = ''
    backMessageTwo = ''
    backMessageOne = ''
    start.after(1, updateClear)


def backTrackPlatform():
    game.destroy()
    global previousTab
    previousTab -= 1


def minecraftSetting():
    global gamesetting
    gamesetting = 0
    global previousTab
    previousTab = 3
    game.destroy()

def customSetting():
    global gamesetting
    gamesetting = 99
    global previousTab
    previousTab = 3
    game.destroy()

def endProgram():
    global previousTab
    global t
    t=''
    if(t == ''):
        updateClear()
    previousTab -= 1
    startButton["state"] = ACTIVE
    start.destroy()

def twitch_Button():
    global twitchActive
    global previousTab
    previousTab = 1
    twitchActive = True
    web.destroy()

def youtube_Button():
    global previousTab
    global youtubeActive
    previousTab = 1
    youtubeActive = True
    web.destroy()

def start_close_window():
    thread()
    start.destroy()
    exit()

def platform_close_window():
    platform.destroy()
    exit()

def game_close_window():
    game.destroy()
    exit()

def web_close_window():
    web.destroy()
    exit()

def handle_message(message):
    ScreenXStartEntry = 0
    ScreenXEndEntry = 0
    ScreenYStartEntry = 0
    ScreenYEndEntry = 0
    try:
        ScreenXStartEntry = int(startX)
        ScreenXEndEntry = int(endX)
        ScreenYStartEntry = int(startY)
        ScreenYEndEntry = int(endY)

    except Exception as e:
        ScreenXStartEntry = 0
        ScreenXEndEntry = 1920
        ScreenYStartEntry = 0
        ScreenYEndEntry = 1080

    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        global backMessageFour,backMessageThree,backMessageTwo,backMessageOne
        backMessageFour= backMessageThree
        backMessageThree= backMessageTwo
        backMessageTwo= backMessageOne
        backMessageOne = "Got this message from " + username + ": " + msg

        position = str(mouse.get_position())
        position = position.replace("(","")
        position = position.replace(")","")
        position = position.split(", ")
        positionX = position[0]
        positionY = position[1]

        # I've added some example videogame logic code below:
        ###################################
        # Example Minecraft Code Sample
        ###################################
        print(positionX, ScreenXEndEntry, positionX, ScreenXStartEntry, positionY, ScreenYEndEntry, positionY, ScreenYStartEntry)
        if(gamesetting == 0 and previousTab == 3):
            if(msg.lower() == 'right' and ((int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                RightButton['bg'] = 'red'
                keyboard.press("d")
                time.sleep(1)
                keyboard.release("d")
                RightButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'left' and ((int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                LeftButton['bg'] = 'red'
                keyboard.press("a")
                time.sleep(1)
                keyboard.release("a")
                LeftButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'forward' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                upButton['bg'] = 'red'
                keyboard.press("w")
                time.sleep(1)
                keyboard.release("w")
                upButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'back' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                DownButton['bg'] = 'red'
                keyboard.press("s")
                time.sleep(1)
                keyboard.release("s")
                DownButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'space' or msg.lower() == 'jump' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                spaceButton['bg'] = 'red'
                pydirectinput.press('space')
                time.sleep(0)
                spaceButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'hop' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                upButton['bg'] = 'red'
                spaceButton['bg'] = 'red'
                pydirectinput.keyDown('space')
                keyboard.press("w")
                time.sleep(1)
                pydirectinput.keyUp('space')
                keyboard.release("w")
                upButton['bg'] = '#f0f0f0'
                spaceButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'shifton' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                pydirectinput.keyDown('shift')
                shiftButton['bg'] = 'red'
            elif(msg.lower() == 'shiftoff' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                pydirectinput.keyUp('shift')
                shiftButton['bg'] = '#f0f0f0'
            elif(msg.lower() == '1' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                oneButton['bg'] = 'red'
                keyboard.press("1")
                keyboard.release("1")
                time.sleep(1)
                oneButton['bg'] = '#f0f0f0'
            elif(msg.lower() == '2' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                twoButton['bg'] = 'red'
                keyboard.press("2")
                keyboard.release("2")
                time.sleep(1)
                twoButton['bg'] = '#f0f0f0'
            elif(msg.lower() == '3' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                threeButton['bg'] = 'red'
                keyboard.press("3")
                keyboard.release("3")
                time.sleep(1)
                threeButton['bg'] = '#f0f0f0'
            elif(msg.lower() == '4' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                fourButton['bg'] = 'red'
                keyboard.press("4")
                keyboard.release("4")
                time.sleep(1)
                fourButton['bg'] = '#f0f0f0'
            elif(msg.lower() == '5' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                fiveButton['bg'] = 'red'
                keyboard.press("5")
                keyboard.release("5")
                time.sleep(1)
                fiveButton['bg'] = '#f0f0f0'
            elif(msg.lower() == '6' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                sixButton['bg'] = 'red'
                keyboard.press("6")
                keyboard.release("6")
                time.sleep(1)
                sixButton['bg'] = '#f0f0f0'
            elif(msg.lower() == '7' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                sevenButton['bg'] = 'red'
                keyboard.press("7")
                keyboard.release("7")
                time.sleep(1)
                sevenButton['bg'] = '#f0f0f0'
            elif(msg.lower() == '8' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                eightButton['bg'] = 'red'
                keyboard.press("8")
                keyboard.release("8")
                time.sleep(1)
                eightButton['bg'] = '#f0f0f0'
            elif(msg.lower() == '9' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                nineButton['bg'] = 'red'
                keyboard.press("9")
                keyboard.release("9")
                time.sleep(1)
                nineButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'h2' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                secHandButton['bg'] = 'red'
                keyboard.press("f")
                keyboard.release("f")
                time.sleep(1)
                secHandButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'inv' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                InvButton['bg'] = 'red'
                keyboard.press("e")
                keyboard.release("e")
                time.sleep(1)
                InvButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'drop' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                dropButton['bg'] = 'red'
                keyboard.press("q")
                keyboard.release("q")
                time.sleep(1)
                dropButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'rt' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                mouseMoveRightButton['bg'] = 'red'
                mouse.move(45, 0, False, .1)
                mouseMoveRightButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'lt' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                mouseMoveLeftButton['bg'] = 'red'
                mouse.move(-45, 0, False, .1)
                mouseMoveLeftButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'ut' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                mouseMoveUpButton['bg'] = 'red'
                mouse.move(0, -45, False, .1)
                mouseMoveUpButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'dt'and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                mouseMoveDownButton['bg'] = 'red'
                mouse.move(0, 45, False, .1)
                mouseMoveDownButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'hit' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                mouseLeftButton['bg'] = 'red'
                mouse.press("left")
                mouse.release("left")
                time.sleep(1)
                mouseLeftButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'smine' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                mouseLeftButton['bg'] = 'red'
                mouse.press("left")
                mouse.release("left")
                time.sleep(1)
                mouseLeftButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'lmine' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                mouseLeftButton['bg'] = 'red'
                mouse.press("left")
                time.sleep(3)
                mouse.release("left")
                mouseLeftButton['bg'] = '#f0f0f0'
            elif(msg.lower() == 'place' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                mouseRightButton['bg'] = 'red'
                mouse.press("right")
                mouse.release("right")
                time.sleep(1)
                mouseRightButton['bg'] = '#f0f0f0'

            if (gamesetting == 99 and previousTab == 3):
                print('working')

        ####################################
        ####################################

    except Exception as e:
        print("Encountered exception: " + str(e))







##################### GAME VARIABLES #####################
def WebSite():
    # Replace this with your Twitch username. Must be all lowercase.
    global TWITCH_CHANNEL
    TWITCH_CHANNEL = ''
    global STREAMING_ON_TWITCH
    STREAMING_ON_TWITCH =  False
    global YOUTUBE_CHANNEL_ID
    YOUTUBE_CHANNEL_ID = ''
    global YOUTUBE_STREAM_URL
    YOUTUBE_STREAM_URL = None
    global previousTab
    if(youtubeActive == True):
        usernameAccess = username.get()
        channelURL = youtubeURL.get()
    if(twitchActive == True):
        usernameAccess = username.get()
    if(twitchActive == True):
        TWITCH_CHANNEL = usernameAccess

        # If streaming on Youtube, set this to False
        STREAMING_ON_TWITCH = twitchActive

    # If you're streaming on Youtube, replace this with your Youtube's Channel ID
    # Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
    if(youtubeActive == True):
        YOUTUBE_CHANNEL_ID = usernameAccess

        # If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
        # Otherwise you can leave this as "None"
        YOUTUBE_STREAM_URL = channelURL
    if(YOUTUBE_CHANNEL_ID != None and youtubeActive == True):
        if(usernameAccess != '' and channelURL !=  ''):
            previousTab = 2
            platform.destroy()
    if(STREAMING_ON_TWITCH == True and twitchActive == True):
        if(usernameAccess != ''):
            previousTab = 2
            platform.destroy()

    ##################### MESSAGE QUEUE VARIABLES #####################

def thread():
    global t1
    t1 = threading.Thread(target=Program)
    if (t1.is_alive() != True):
        startButton["state"] = DISABLED
        endButton["state"] = DISABLED
        startButton['bg'] = 'light yellow'
        t1.start()
    else:
        t1.join()


def Program(eventRun=None):
    global previousTab
    global t
    # MESSAGE_RATE controls how fast we process incoming Twitch Chat messages. It's the number of seconds it will take to handle all messages in the queue.
    # This is used because Twitch delivers messages in "batches", rather than one at a time. So we process the messages over MESSAGE_RATE duration, rather than processing the entire batch at once.
    # A smaller number means we go through the message queue faster, but we will run out of messages faster and activity might "stagnate" while waiting for a new batch. 
    # A higher number means we go through the queue slower, and messages are more evenly spread out, but delay from the viewers' perspective is higher.
    # You can set this to 0 to disable the queue and handle all messages immediately. However, then the wait before another "batch" of messages is more noticeable.
    MESSAGE_RATE = 0.5
    # MAX_QUEUE_LENGTH limits the number of commands that will be processed in a given "batch" of messages. 
    # e.g. if you get a batch of 50 messages, you can choose to only process the first 10 of them and ignore the others.
    # This is helpful for games where too many inputs at once can actually hinder the gameplay.
    # Setting to ~50 is good for total chaos, ~5-10 is good for 2D platformers
    MAX_QUEUE_LENGTH = 20
    MAX_WORKERS = 100 # Maximum number of threads you can process at a time

    last_time = time.time()
    message_queue = []
    thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
    active_tasks = []
    pyautogui.FAILSAFE = False

    ##########################################################

    # Count down before starting, so you have time to load up the game
    countdown = 5
    while countdown > 0:
        messageRelayConnect.config(text=countdown)
        countdown -= 1
        time.sleep(1)

    try:
        if (STREAMING_ON_TWITCH and previousTab == 3):
            t = TwitchPlays_Connection.Twitch()
            t.twitch_connect(TWITCH_CHANNEL)
            messageRelayConnect.config(text='Connected To Twitch')
        elif(previousTab == 3):
            t = TwitchPlays_Connection.YouTube()
            t.youtube_connect(YOUTUBE_CHANNEL_ID, YOUTUBE_STREAM_URL)
            messageRelayConnect.config(text='Connected To Youtube')
        endButton["state"] = ACTIVE
        startButton['bg'] = 'light green'
    except Exception as e:
        messageRelayConnect.config(text='Error: Unable to connect to a platform. Check login details...')
        endButton["state"] = ACTIVE
        startButton['bg'] = 'red'

    while(True):

        active_tasks = [t for t in active_tasks if not t.done()]

        #Check for new messages
        new_messages = t.twitch_receive_messages();
        if new_messages:
            message_queue += new_messages; # New messages are added to the back of the queue
            message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

        messages_to_handle = []
        if not message_queue:
            # No messages in the queue
            last_time = time.time()
        else:
            # Determine how many messages we should handle now
            r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
            n = int(r * len(message_queue))
            if n > 0:
                # Pop the messages we want off the front of the queue
                messages_to_handle = message_queue[0:n]
                del message_queue[0:n]
                last_time = time.time();

        # If user presses Shift+Backspace, automatically end the program
        if keyboard.is_pressed('shift+backspace'):
            exit()

        if not messages_to_handle:
            continue
        else:
            for message in messages_to_handle:
                if len(active_tasks) <= MAX_WORKERS:
                    active_tasks.append(thread_pool.submit(handle_message, message))
                else:
                    print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')



backMessageFour = ''
backMessageThree = ''
backMessageTwo = ''
backMessageOne = ''
youtubeURL = None
twitchActive = False
youtubeActive = False
previousTab = 0
while(previousTab == 0):
    web = mtTkinter.Tk()
    web.lift()
    web.attributes('-topmost', True)
    web.grab_set()
    web.grab_release()
    web.focus_force()
    web.title("ContentPlays")
    web.iconbitmap("icon.ico")
    web.geometry("525x350+700+300")
    web.config(background = "white")
    web.minsize(525,350)
    web.maxsize(525,350)
    youtubePhoto = PhotoImage(file = "youtube.png")
    youtubeResize = youtubePhoto.subsample(3,3)
    twitchPhoto = PhotoImage(file = "twitch.png")
    twitchResize = twitchPhoto.subsample(3,3)
    webText = Label(web, text="Select The Platform",
                        bg = "white",
                        fg = "black",
                        font = ("Arial", 17))
    twitchButton = Button(web,height = 140, width = 100, text="Twitch",font = ("Arial", 12), image= twitchResize,compound = TOP, command = twitch_Button)
    youtubeButton = Button(web,height = 140, width = 100, text="Youtube",font = ("Arial", 12), image= youtubeResize,compound = TOP, command= youtube_Button)
    thanks = Label(web, text="Original code by Wituz, updated by DDarknut, DougDoug, Ottomated. Further expanded by Bloop",
                        bg = "white",
                        fg = "black",
                        font = ("Arial", 7))


    web.protocol("WM_DELETE_WINDOW", web_close_window)
    webText.place(x=155, y=50)
    twitchButton.place(x=120, y=100)
    youtubeButton.place(x=285, y=100)
    thanks.place(x=0, y=330)
    web.mainloop()
    while(previousTab == 1):
        platform = mtTkinter.Tk()
        platform.lift()
        platform.attributes('-topmost', True)
        platform.grab_set()
        platform.grab_release()
        platform.focus_force()
        platform.title("ContentPlays")
        platform.iconbitmap("icon.ico")
        platform.geometry("525x350+700+300")
        platform.config(background = "white")
        platform.minsize(525,350)
        platform.maxsize(525,350)
        if(twitchActive == True):
            webText = Label(platform, text="Enter Your Twitch Username",
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
            username = Entry(platform, text = "Username..", width = 53)
            username.place(x=25, y=50)
            webText.place(x=5, y=20)
        if(youtubeActive == True):
            webText = Label(platform, text="Enter Your Channel ID",
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
            webURL = Label(platform, text="Enter Your Stream URL",
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
            username = Entry(platform, text = "Channel ID..", width = 53)
            youtubeURL = Entry(platform, text = "Channel URL..", width = 53)
            username.place(x=25, y=50)
            webText.place(x=5, y=20)
            webURL.place(x=5, y=80)
            youtubeURL.place(x=25, y=110)
        nextButton = Button(platform, text="Next",height = 2, width = 5, command = WebSite)
        nextButton.place(x=460, y = 290)
        backButton = Button(platform, text="Back",height = 2, width = 5, command = backTrackAccount)
        backButton.place(x=15, y = 290)
        platform.protocol("WM_DELETE_WINDOW", platform_close_window)
        platform.mainloop()
        while(previousTab == 2):
            game = mtTkinter.Tk()
            game.lift()
            game.attributes('-topmost', True)
            game.grab_set()
            game.grab_release()
            game.focus_force()
            game.title("ContentPlays")
            game.iconbitmap("icon.ico")
            game.geometry("525x350+700+300")
            game.config(background = "white")
            game.minsize(525,350)
            game.maxsize(525,350)

            webText = Label(game, text="Select A Game",
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 15))
            webText.place(x=175, y=50)

            minecraftButton = Button(game, text="Minecraft",height = 2, width = 7, command = minecraftSetting)
            minecraftButton.place(x=75, y = 100)

            gameTwoButton = Button(game, text="Game 2",height = 2, width = 7, command = None)
            gameTwoButton.place(x=150, y = 100)

            gameThreeButton = Button(game, text="Game 3",height = 2, width = 7, command = None)
            gameThreeButton.place(x=225, y = 100)

            gameFourButton = Button(game, text="Game 4",height = 2, width = 7, command = None)
            gameFourButton.place(x=300, y = 100)

            gameFiveButton = Button(game, text="Game 5",height = 2, width = 7, command = None)
            gameFiveButton.place(x=375, y = 100)

            gameSixButton = Button(game, text="Game 6",height = 2, width = 7, command = None)
            gameSixButton.place(x=75, y = 150)

            gameSevenButton = Button(game, text="Game 7",height = 2, width = 7, command = None)
            gameSevenButton.place(x=150, y = 150)

            gameEightButton = Button(game, text="Game 8",height = 2, width = 7, command = None)
            gameEightButton.place(x=225, y = 150)

            gameNineButton = Button(game, text="Game 9",height = 2, width = 7, command = None)
            gameNineButton.place(x=300, y = 150)

            gameTenButton = Button(game, text="Game 10",height = 2, width = 7, command = None)
            gameTenButton.place(x=375, y = 150)

            gameElevenButton = Button(game, text="Game 11",height = 2, width = 7, command = None)
            gameElevenButton.place(x=75, y = 200)

            gameTwelveButton = Button(game, text="Game 12",height = 2, width = 7, command = None)
            gameTwelveButton.place(x=150, y = 200)

            gameThirteenButton = Button(game, text="Game 13",height = 2, width = 7, command = None)
            gameThirteenButton.place(x=225, y = 200)

            gameFourteenButton = Button(game, text="Game 14",height = 2, width = 7, command = None)
            gameFourteenButton.place(x=300, y = 200)

            customButton = Button(game, text="Custom",height = 2, width = 7, command = None)#customSetting
            customButton.place(x=375, y = 200)

            backButton = Button(game, text="Back",height = 2, width = 5, command = backTrackPlatform)
            backButton.place(x=15, y = 290)

            game.protocol("WM_DELETE_WINDOW", game_close_window)
            game.mainloop()

            while(previousTab == 3):
                start = mtTkinter.Tk()
                start.lift()
                start.attributes('-topmost', True)
                start.grab_set()
                start.grab_release()
                start.focus_force()
                start.title("ContentPlays")
                start.iconbitmap("icon.ico")
                start.geometry("525x350+700+300")
                start.config(background = "white")
                start.minsize(525,350)
                start.maxsize(525,350)

                menubar = Menu(start)
                options = Menu(menubar, tearoff = 0)
                menubar.add_cascade(label='Options', menu=options)
                screenManager = ScreenManage()
                options.add_command(label='Screen', command= screenManager.screenOption)


                messageRelayOne = Label(start, text=backMessageOne,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
                messageRelayTwo = Label(start, text=backMessageTwo,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
                messageRelayThree = Label(start, text=backMessageThree,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
                messageRelayFour = Label(start, text=backMessageFour,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))

                messageRelayConnect = Label(start, text='',
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 13),
                    anchor="center")


                startButton = Button(start, text="Start",height = 2, width = 5, command = thread)
                startButton.place(x=225, y = 280)
                endButton = Button(start, text="End",height = 2, width = 5, command = endProgram)

                if(gamesetting == 0):
                    upButton = Button(start, text="Up", height=1, width=4, state=DISABLED)
                    DownButton = Button(start, text="Down", height=1, width=4, state=DISABLED)
                    LeftButton = Button(start, text="Left", height=1, width=4, state=DISABLED)
                    RightButton = Button(start, text="Right", height=1, width=4, state=DISABLED)
                    upButton.place(x=60, y=115)
                    DownButton.place(x=60, y=175)
                    LeftButton.place(x=20, y=145)
                    RightButton.place(x=100, y=145)

                    secHandButton = Button(start, text="Swap", height=1, width=4, state=DISABLED)
                    secHandButton.place(x=160, y=115)

                    oneButton = Button(start, text="1", height=1, width=3, state=DISABLED)
                    twoButton = Button(start, text="2", height=1, width=3, state=DISABLED)
                    threeButton = Button(start, text="3", height=1, width=3, state=DISABLED)
                    fourButton = Button(start, text="4", height=1, width=3, state=DISABLED)
                    fiveButton = Button(start, text="5", height=1, width=3, state=DISABLED)
                    sixButton = Button(start, text="6", height=1, width=3, state=DISABLED)
                    sevenButton = Button(start, text="7", height=1, width=3, state=DISABLED)
                    eightButton = Button(start, text="8", height=1, width=3, state=DISABLED)
                    nineButton = Button(start, text="9", height=1, width=3, state=DISABLED)
                    oneButton.place(x=20, y=50)
                    twoButton.place(x=60, y=50)
                    threeButton.place(x=100, y=50)
                    fourButton.place(x=140, y=50)
                    fiveButton.place(x=180, y=50)
                    sixButton.place(x=220, y=50)
                    sevenButton.place(x=260, y=50)
                    eightButton.place(x=300, y=50)
                    nineButton.place(x=340, y=50)

                    spaceButton = Button(start, text="Space Bar", height=1, width=10, state=DISABLED)
                    spaceButton.place(x=160, y=175)

                    shiftButton = Button(start, text="Shift", height=1, width=5, state=DISABLED)
                    shiftButton.place(x=260, y=175)

                    dropButton = Button(start, text="Drop", height=1, width=4, state=DISABLED)
                    dropButton.place(x=20, y=90)

                    InvButton = Button(start, text="Inv", height=1, width=4, state=DISABLED)
                    InvButton.place(x=100, y=90)

                    mousePalmButton = Button(start, text="", height=2, width=5, state=DISABLED)
                    mouseLeftButton = Button(start, text="L", height=1, width=2, state=DISABLED)
                    mouseRightButton = Button(start, text="R", height=1, width=2, state=DISABLED)
                    mousePalmButton.place(x=430, y=125)
                    mouseLeftButton.place(x=430, y=100)
                    mouseRightButton.place(x=451, y=100)

                    mouseMoveUpButton = Button(start, text="↑", height=1, width=1, state=DISABLED)
                    mouseMoveDownButton = Button(start, text="↓", height=1, width=1, state=DISABLED)
                    mouseMoveLeftButton = Button(start, text="←", height=1, width=1, state=DISABLED)
                    mouseMoveRightButton = Button(start, text="→", height=1, width=1, state=DISABLED)
                    mouseMoveUpButton.place(x=445, y=70)
                    mouseMoveDownButton.place(x=445, y=170)
                    mouseMoveLeftButton.place(x=405, y=120)
                    mouseMoveRightButton.place(x=480, y=120)

                #if(gamesetting == 99):


                endButton.place(x=275, y = 280)
                messageRelayOne.place(x= 5, y=200)
                messageRelayTwo.place(x= 5, y=220)
                messageRelayThree.place(x= 5, y=240)
                messageRelayFour.place(x= 5, y=260)
                messageRelayConnect.place(x=10, y=5)
                start.protocol("WM_DELETE_WINDOW", start_close_window)
                start.after(1000, updateMessage)
                start.config(menu=menubar)
                start.mainloop()
exit()
