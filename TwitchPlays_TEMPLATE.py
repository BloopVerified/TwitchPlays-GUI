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

import TwitchPlays_Connection
from ScreenManageFile import ScreenManage
from ControlManageFile import ControlManage
from GreenScreenFile import GreenScreen
from MouseManageFile import MouseManage
from BackgroundInfoFile import backgroundInfo

moveMouseUp = MouseManage.moveMouseUp
moveMouseDown = MouseManage.moveMouseDown
moveMouseRight = MouseManage.moveMouseRight
moveMouseLeft = MouseManage.moveMouseLeft
textMouseUp = MouseManage.textMouseUp
textMouseDown = MouseManage.textMouseDown
textMouseRight = MouseManage.textMouseRight
textMouseLeft = MouseManage.textMouseLeft
rightClick = MouseManage.rightClick
rightClickValue = MouseManage.rightClickValue
leftClick = MouseManage.leftClick
leftClickValue = MouseManage.leftClickValue

startXGet = ScreenManage.startXGet
endXGet = ScreenManage.endXGet
startYGet = ScreenManage.startYGet
endYGet = ScreenManage.endYGet

upKeyCls = ControlManage.upKeyCls
downKeyCls = ControlManage.downKeyCls
rightKeyCls = ControlManage.rightKeyCls
leftKeyCls = ControlManage.leftKeyCls
oneKeyCls = ControlManage.oneKeyCls
twoKeyCls = ControlManage.twoKeyCls
threeKeyCls = ControlManage.threeKeyCls
fourKeyCls = ControlManage.fourKeyCls
fiveKeyCls = ControlManage.fiveKeyCls
sixKeyCls = ControlManage.sixKeyCls
sevenKeyCls = ControlManage.sevenKeyCls
eightKeyCls = ControlManage.eightKeyCls
nineKeyCls = ControlManage.nineKeyCls
zeroKeyCls = ControlManage.zeroKeyCls
shiftKeyCls = ControlManage.shiftKeyCls
controlKeyCls = ControlManage.controlKeyCls
macroOneKeyOneCls = ControlManage.macroOneKeyOneCls
macroOneKeyTwoCls = ControlManage.macroOneKeyTwoCls
macroTwoKeyOneCls = ControlManage.macroTwoKeyOneCls
macroTwoKeyTwoCls = ControlManage.macroTwoKeyTwoCls
macroThreeKeyOneCls = ControlManage.macroThreeKeyOneCls
macroThreeKeyTwoCls = ControlManage.macroThreeKeyTwoCls
macroFourKeyOneCls = ControlManage.macroFourKeyOneCls
macroFourKeyTwoCls = ControlManage.macroFourKeyTwoCls
actionOneKeyCls = ControlManage.actionOneKeyCls
actionTwoKeyCls = ControlManage.actionTwoKeyCls
actionThreeKeyCls = ControlManage.actionThreeKeyCls
actionFourKeyCls = ControlManage.actionFourKeyCls
actionFiveKeyCls = ControlManage.actionFiveKeyCls
actionSixKeyCls = ControlManage.actionSixKeyCls
actionSevenKeyCls = ControlManage.actionSevenKeyCls
actionEightKeyCls = ControlManage.actionEightKeyCls
macroOneTimerOneCls = ControlManage.macroOneTimerOneCls
macroTwoTimerOneCls = ControlManage.macroTwoTimerOneCls
macroThreeTimerOneCls = ControlManage.macroThreeTimerOneCls
macroFourTimerOneCls = ControlManage.macroFourTimerOneCls
macroOneTimerTwoCls = ControlManage.macroOneTimerTwoCls
macroTwoTimerTwoCls = ControlManage.macroTwoTimerTwoCls
macroThreeTimerTwoCls = ControlManage.macroThreeTimerTwoCls
macroFourTimerTwoCls = ControlManage.macroFourTimerTwoCls
enterKeyCls = ControlManage.enterKeyCls
spaceKeyCls = ControlManage.spaceKeyCls

greenScreenCls = GreenScreen.greenScreenCls

previousTab = backgroundInfo.previousTab
TWITCH_CHANNEL = backgroundInfo.TWITCH_CHANNEL
STREAMING_ON_TWITCH = backgroundInfo.STREAMING_ON_TWITCH
STREAMING_ON_YOUTUBE = backgroundInfo.STREAMING_ON_YOUTUBE
YOUTUBE_STREAM_URL = backgroundInfo.YOUTUBE_STREAM_URL
YOUTUBE_CHANNEL_ID = backgroundInfo.YOUTUBE_CHANNEL_ID
twitchActive = backgroundInfo.twitchActive
youtubeActive = backgroundInfo.youtubeActive
backMessageFour = backgroundInfo.backMessageFour
backMessageThree = backgroundInfo.backMessageThree
backMessageTwo = backgroundInfo.backMessageTwo
backMessageOne = backgroundInfo.backMessageOne
t = backgroundInfo.t
y = backgroundInfo.y
t1 = backgroundInfo.t1
gamesetting = backgroundInfo.gamesetting


class TextToAction():
    TTAOne = ''
    TTATwo = ''
    TTAThree = ''
    TTAFour = ''

    def handle_message(self, message):
        controller = ControlManage()
        mousemove = MouseManage()
        ScreenXStartEntry = 0
        ScreenXEndEntry = 0
        ScreenYStartEntry = 0
        ScreenYEndEntry = 0
        try:
            ScreenXStartEntry = int(ScreenManage.startXGet)
            ScreenXEndEntry = int(ScreenManage.endXGet)
            ScreenYStartEntry = int(ScreenManage.startYGet)
            ScreenYEndEntry = int(ScreenManage.endYGet)

        except Exception as e:
            ScreenXStartEntry = 0
            ScreenXEndEntry = 1920
            ScreenYStartEntry = 0
            ScreenYEndEntry = 1080

        try:
            msg = message['message'].lower()
            username = message['username'].lower()
            TextToAction.TTAFour = (backgroundInfo.backMessageThree)
            TextToAction.TTAThree = (backgroundInfo.backMessageTwo)
            TextToAction.TTATwo = (backgroundInfo.backMessageOne)
            TextToAction.TTAOne = "Got this message from " + username + ": " + msg
            sendUpdateMessage = partial(sendUpdateMessageFunc, messageRelayOne, messageRelayTwo, messageRelayThree,
                                        messageRelayFour, TextToAction.TTAOne, TextToAction.TTATwo,
                                        TextToAction.TTAThree, TextToAction.TTAFour)
            start.after(100, sendUpdateMessage)
            position = str(mouse.get_position())
            position = position.replace("(", "")
            position = position.replace(")", "")
            position = position.split(", ")
            positionX = position[0]
            positionY = position[1]

            # I've added some example videogame logic code below:
            ###################################
            # Example Minecraft Code Sample
            ###################################
            if (backgroundInfo.gamesetting == 0 and backgroundInfo.previousTab == 3):
                if (msg.lower() == 'right' and (
                        (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (
                        int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    RightButton['bg'] = 'red'
                    keyboard.press("d")
                    time.sleep(1)
                    keyboard.release("d")
                    RightButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'left' and (
                        (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (
                        int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    LeftButton['bg'] = 'red'
                    keyboard.press("a")
                    time.sleep(1)
                    keyboard.release("a")
                    LeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'forward' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    upButton['bg'] = 'red'
                    keyboard.press("w")
                    time.sleep(1)
                    keyboard.release("w")
                    upButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'back' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    DownButton['bg'] = 'red'
                    keyboard.press("s")
                    time.sleep(1)
                    keyboard.release("s")
                    DownButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'space' or msg.lower() == 'jump' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    spaceButton['bg'] = 'red'
                    pydirectinput.press('space')
                    time.sleep(0)
                    spaceButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'hop' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    upButton['bg'] = 'red'
                    spaceButton['bg'] = 'red'
                    pydirectinput.keyDown('space')
                    keyboard.press("w")
                    time.sleep(1)
                    pydirectinput.keyUp('space')
                    keyboard.release("w")
                    upButton['bg'] = '#f0f0f0'
                    spaceButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'shifton' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    pydirectinput.keyDown('shift')
                    shiftButton['bg'] = 'red'
                elif (msg.lower() == 'shiftoff' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    pydirectinput.keyUp('shift')
                    shiftButton['bg'] = '#f0f0f0'

                elif (msg.lower() == 'controlon' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    pydirectinput.keyDown('control')
                    controlButton['bg'] = 'red'
                elif (msg.lower() == 'controloff' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    pydirectinput.keyUp('control')
                    controlButton['bg'] = '#f0f0f0'

                elif (msg.lower() == '1' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    oneButton['bg'] = 'red'
                    keyboard.press("1")
                    keyboard.release("1")
                    time.sleep(1)
                    oneButton['bg'] = '#f0f0f0'
                elif (msg.lower() == '2' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    twoButton['bg'] = 'red'
                    keyboard.press("2")
                    keyboard.release("2")
                    time.sleep(1)
                    twoButton['bg'] = '#f0f0f0'
                elif (msg.lower() == '3' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    threeButton['bg'] = 'red'
                    keyboard.press("3")
                    keyboard.release("3")
                    time.sleep(1)
                    threeButton['bg'] = '#f0f0f0'
                elif (msg.lower() == '4' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    fourButton['bg'] = 'red'
                    keyboard.press("4")
                    keyboard.release("4")
                    time.sleep(1)
                    fourButton['bg'] = '#f0f0f0'
                elif (msg.lower() == '5' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    fiveButton['bg'] = 'red'
                    keyboard.press("5")
                    keyboard.release("5")
                    time.sleep(1)
                    fiveButton['bg'] = '#f0f0f0'
                elif (msg.lower() == '6' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    sixButton['bg'] = 'red'
                    keyboard.press("6")
                    keyboard.release("6")
                    time.sleep(1)
                    sixButton['bg'] = '#f0f0f0'
                elif (msg.lower() == '7' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    sevenButton['bg'] = 'red'
                    keyboard.press("7")
                    keyboard.release("7")
                    time.sleep(1)
                    sevenButton['bg'] = '#f0f0f0'
                elif (msg.lower() == '8' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    eightButton['bg'] = 'red'
                    keyboard.press("8")
                    keyboard.release("8")
                    time.sleep(1)
                    eightButton['bg'] = '#f0f0f0'
                elif (msg.lower() == '9' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    nineButton['bg'] = 'red'
                    keyboard.press("9")
                    keyboard.release("9")
                    time.sleep(1)
                    nineButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'h2' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    secHandButton['bg'] = 'red'
                    keyboard.press("f")
                    keyboard.release("f")
                    time.sleep(1)
                    secHandButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'inv' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    InvButton['bg'] = 'red'
                    keyboard.press("e")
                    keyboard.release("e")
                    time.sleep(1)
                    InvButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'drop' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    dropButton['bg'] = 'red'
                    keyboard.press("q")
                    keyboard.release("q")
                    time.sleep(1)
                    dropButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'rt' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveRightButton['bg'] = 'red'
                    mouse.move(45, 0, False, .1)
                    mouseMoveRightButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'lt' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveLeftButton['bg'] = 'red'
                    mouse.move(-45, 0, False, .1)
                    mouseMoveLeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'ut' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveUpButton['bg'] = 'red'
                    mouse.move(0, -45, False, .1)
                    mouseMoveUpButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'dt' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveDownButton['bg'] = 'red'
                    mouse.move(0, 45, False, .1)
                    mouseMoveDownButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'hit' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    mouse.release("left")
                    time.sleep(1)
                    mouseLeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'smine' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    mouse.release("left")
                    time.sleep(1)
                    mouseLeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'lmine' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    time.sleep(3)
                    mouse.release("left")
                    mouseLeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'place' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseRightButton['bg'] = 'red'
                    mouse.press("right")
                    mouse.release("right")
                    time.sleep(1)
                    mouseRightButton['bg'] = '#f0f0f0'

            if (backgroundInfo.gamesetting == 1 and backgroundInfo.previousTab == 3):
                if (msg.lower() == 'right' and (
                        (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (
                        int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    RightButton['bg'] = 'red'
                    keyboard.press("d")
                    time.sleep(1)
                    keyboard.release("d")
                    RightButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'left' and (
                        (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (
                        int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    LeftButton['bg'] = 'red'
                    keyboard.press("a")
                    time.sleep(1)
                    keyboard.release("a")
                    LeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'forward' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    upButton['bg'] = 'red'
                    keyboard.press("w")
                    time.sleep(1)
                    keyboard.release("w")
                    upButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'back' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    DownButton['bg'] = 'red'
                    keyboard.press("s")
                    time.sleep(1)
                    keyboard.release("s")
                    DownButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'accept' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    acceptButton['bg'] = 'red'
                    keyboard.press("z")
                    keyboard.release("z")
                    time.sleep(1)
                    acceptButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'skip' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    skipButton['bg'] = 'red'
                    keyboard.press("x")
                    keyboard.release("x")
                    time.sleep(1)
                    skipButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'mr' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveRightButton['bg'] = 'red'
                    mouse.move(45, 0, False, .1)
                    mouseMoveRightButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'ml' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveLeftButton['bg'] = 'red'
                    mouse.move(-45, 0, False, .1)
                    mouseMoveLeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'mu' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveUpButton['bg'] = 'red'
                    mouse.move(0, -45, False, .1)
                    mouseMoveUpButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'md' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveDownButton['bg'] = 'red'
                    mouse.move(0, 45, False, .1)
                    mouseMoveDownButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'lc' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    mouse.release("left")
                    time.sleep(1)
                    mouseLeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'rc' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseRightButton['bg'] = 'red'
                    mouse.press("right")
                    mouse.release("right")
                    time.sleep(1)
                    mouseRightButton['bg'] = '#f0f0f0'

            if (backgroundInfo.gamesetting == 1 and backgroundInfo.previousTab == 14):
                if (msg.lower() == 'right' and (
                        (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (
                        int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    RightButton['bg'] = 'red'
                    keyboard.press("right")
                    time.sleep(1)
                    keyboard.release("right")
                    RightButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'left' and (
                        (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (
                        int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    LeftButton['bg'] = 'red'
                    keyboard.press("left")
                    time.sleep(1)
                    keyboard.release("left")
                    LeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'up' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    upButton['bg'] = 'red'
                    keyboard.press("up")
                    time.sleep(1)
                    keyboard.release("up")
                    upButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'back' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    DownButton['bg'] = 'red'
                    keyboard.press("down")
                    time.sleep(1)
                    keyboard.release("down")
                    DownButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'x' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    confirmButton['bg'] = 'red'
                    keyboard.press("x")
                    keyboard.release("x")
                    time.sleep(1)
                    confirmButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'c' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    cancelButton['bg'] = 'red'
                    keyboard.press("c")
                    keyboard.release("c")
                    time.sleep(1)
                    cancelButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'b' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    miscButton['bg'] = 'red'
                    keyboard.press("b")
                    keyboard.release("b")
                    time.sleep(1)
                    miscButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'space' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    spaceButton['bg'] = 'red'
                    keyboard.press("space")
                    keyboard.release("space")
                    time.sleep(1)
                    spaceButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'mr' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveRightButton['bg'] = 'red'
                    mouse.move(45, 0, False, .1)
                    mouseMoveRightButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'ml' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveLeftButton['bg'] = 'red'
                    mouse.move(-45, 0, False, .1)
                    mouseMoveLeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'mu' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveUpButton['bg'] = 'red'
                    mouse.move(0, -45, False, .1)
                    mouseMoveUpButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'md' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveDownButton['bg'] = 'red'
                    mouse.move(0, 45, False, .1)
                    mouseMoveDownButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'lc' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    mouse.release("left")
                    time.sleep(1)
                    mouseLeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == 'rc' and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseRightButton['bg'] = 'red'
                    mouse.press("right")
                    mouse.release("right")
                    time.sleep(1)
                    mouseRightButton['bg'] = '#f0f0f0'

            if (backgroundInfo.gamesetting == 99 and backgroundInfo.previousTab == 3):
                if (msg.lower() == upButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                        int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    upButton['bg'] = 'red'
                    keyboard.press(controller.upKeyCls)
                    keyboard.release(controller.upKeyCls)
                    time.sleep(1)
                    upButton['bg'] = '#f0f0f0'

                elif (msg.lower() == downButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    downButton['bg'] = 'red'
                    keyboard.press(controller.downKeyCls)
                    keyboard.release(controller.downKeyCls)
                    time.sleep(1)
                    downButton['bg'] = '#f0f0f0'

                elif (msg.lower() == rightButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    rightButton['bg'] = 'red'
                    keyboard.press(controller.rightKeyCls)
                    keyboard.release(controller.rightKeyCls)
                    time.sleep(1)
                    rightButton['bg'] = '#f0f0f0'

                elif (msg.lower() == leftButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    leftButton['bg'] = 'red'
                    keyboard.press(controller.leftKeyCls)
                    keyboard.release(controller.leftKeyCls)
                    time.sleep(1)
                    leftButton['bg'] = '#f0f0f0'

                elif (msg.lower() == oneButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    oneButton['bg'] = 'red'
                    keyboard.press(controller.oneKeyCls)
                    keyboard.release(controller.oneKeyCls)
                    time.sleep(1)
                    oneButton['bg'] = '#f0f0f0'

                elif (msg.lower() == twoButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    twoButton['bg'] = 'red'
                    keyboard.press(controller.twoKeyCls)
                    keyboard.release(controller.twoKeyCls)
                    time.sleep(1)
                    twoButton['bg'] = '#f0f0f0'

                elif (msg.lower() == threeButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    threeButton['bg'] = 'red'
                    keyboard.press(controller.threeKeyCls)
                    keyboard.release(controller.threeKeyCls)
                    time.sleep(1)
                    threeButton['bg'] = '#f0f0f0'

                elif (msg.lower() == fourButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    fourButton['bg'] = 'red'
                    keyboard.press(controller.fourKeyCls)
                    keyboard.release(controller.fourKeyCls)
                    time.sleep(1)
                    fourButton['bg'] = '#f0f0f0'

                elif (msg.lower() == fiveButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    fiveButton['bg'] = 'red'
                    keyboard.press(controller.fiveKeyCls)
                    keyboard.release(controller.fiveKeyCls)
                    time.sleep(1)
                    fiveButton['bg'] = '#f0f0f0'

                elif (msg.lower() == sixButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    sixButton['bg'] = 'red'
                    keyboard.press(controller.sixKeyCls)
                    keyboard.release(controller.sixKeyCls)
                    time.sleep(1)
                    sixButton['bg'] = '#f0f0f0'

                elif (msg.lower() == sevenButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    sevenButton['bg'] = 'red'
                    keyboard.press(controller.sixKeyCls)
                    keyboard.release(controller.sixKeyCls)
                    time.sleep(1)
                    sevenButton['bg'] = '#f0f0f0'

                elif (msg.lower() == sevenButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    sevenButton['bg'] = 'red'
                    keyboard.press(controller.sevenKeyCls)
                    keyboard.release(controller.sevenKeyCls)
                    time.sleep(1)
                    sevenButton['bg'] = '#f0f0f0'

                elif (msg.lower() == eightButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    eightButton['bg'] = 'red'
                    keyboard.press(controller.eightKeyCls)
                    keyboard.release(controller.eightKeyCls)
                    time.sleep(1)
                    eightButton['bg'] = '#f0f0f0'

                elif (msg.lower() == nineButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    nineButton['bg'] = 'red'
                    keyboard.press(controller.nineKeyCls)
                    keyboard.release(controller.nineKeyCls)
                    time.sleep(1)
                    nineButton['bg'] = '#f0f0f0'

                elif (msg.lower() == zeroButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    zeroButton['bg'] = 'red'
                    keyboard.press(controller.zeroKeyCls)
                    keyboard.release(controller.zeroKeyCls)
                    time.sleep(1)
                    zeroButton['bg'] = '#f0f0f0'

                elif (msg.lower() == shiftButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    shiftButton['bg'] = 'red'
                    keyboard.press(controller.shiftKeyCls)
                    keyboard.release(controller.shiftKeyCls)
                    time.sleep(1)
                    shiftButton['bg'] = '#f0f0f0'

                elif (msg.lower() == controlButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    controlButton['bg'] = 'red'
                    keyboard.press(controller.controlKeyCls)
                    keyboard.release(controller.controlKeyCls)
                    time.sleep(1)
                    controlButton['bg'] = '#f0f0f0'

                elif (msg.lower() == enterButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    enterButton['bg'] = 'red'
                    keyboard.press(controller.enterKeyCls)
                    keyboard.release(controller.enterKeyCls)
                    time.sleep(1)
                    enterButton['bg'] = '#f0f0f0'

                elif (msg.lower() == spaceButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    spaceButton['bg'] = 'red'
                    keyboard.press(controller.spaceKeyCls)
                    keyboard.release(controller.spaceKeyCls)
                    time.sleep(1)
                    spaceButton['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonOne['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonOne['bg'] = 'red'
                    keyboard.press(controller.actionOneKeyCls)
                    keyboard.release(controller.actionOneKeyCls)
                    time.sleep(1)
                    actionButtonOne['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonTwo['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonTwo['bg'] = 'red'
                    keyboard.press(controller.actionTwoKeyCls)
                    keyboard.release(controller.actionTwoKeyCls)
                    time.sleep(1)
                    actionButtonTwo['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonThree['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonThree['bg'] = 'red'
                    keyboard.press(controller.actionThreeKeyCls)
                    keyboard.release(controller.actionThreeKeyCls)
                    time.sleep(1)
                    actionButtonThree['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonFour['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonFour['bg'] = 'red'
                    keyboard.press(controller.actionFourKeyCls)
                    keyboard.release(controller.actionFourKeyCls)
                    time.sleep(1)
                    actionButtonFour['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonFive['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonFive['bg'] = 'red'
                    keyboard.press(controller.actionFiveKeyCls)
                    keyboard.release(controller.actionFiveKeyCls)
                    time.sleep(1)
                    actionButtonFive['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonSix['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonSix['bg'] = 'red'
                    keyboard.press(controller.actionSixKeyCls)
                    keyboard.release(controller.actionSixKeyCls)
                    time.sleep(1)
                    actionButtonSix['bg'] = '#f0f0f0'

                if (msg.lower() == actionButtonSeven['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                        int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonSeven['bg'] = 'red'
                    keyboard.press(controller.actionSevenKeyCls)
                    keyboard.release(controller.actionSevenKeyCls)
                    time.sleep(1)
                    actionButtonSeven['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonEight['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonEight['bg'] = 'red'
                    keyboard.press(controller.actionEightKeyCls)
                    keyboard.release(controller.actionEightKeyCls)
                    time.sleep(1)
                    actionButtonEight['bg'] = '#f0f0f0'

                elif (msg.lower() == macroOneButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    macroOneButton['bg'] = 'red'
                    keyboard.press(controller.macroOneKeyOneCls)
                    time.sleep(int(controller.macroOneTimerOneCls))
                    keyboard.press(controller.macroOneKeyTwoCls)
                    keyboard.release(controller.macroOneKeyOneCls)
                    time.sleep(int(controller.macroOneTimerTwoCls))
                    keyboard.release(controller.macroOneKeyTwoCls)
                    macroOneButton['bg'] = '#f0f0f0'

                elif (msg.lower() == macroTwoButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    macroTwoButton['bg'] = 'red'
                    keyboard.press(controller.macroTwoKeyOneCls)
                    time.sleep(int(controller.macroTwoTimerOneCls))
                    keyboard.press(controller.macroTwoKeyTwoCls)
                    keyboard.release(controller.macroTwoKeyOneCls)
                    time.sleep(int(controller.macroTwoTimerTwoCls))
                    keyboard.release(controller.macroTwoKeyTwoCls)
                    macroTwoButton['bg'] = '#f0f0f0'

                elif (msg.lower() == macroThreeButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    macroThreeButton['bg'] = 'red'
                    keyboard.press(controller.macroThreeKeyOneCls)
                    time.sleep(int(controller.macroThreeTimerOneCls))
                    keyboard.press(controller.macroThreeKeyTwoCls)
                    keyboard.release(controller.macroThreeKeyOneCls)
                    time.sleep(int(controller.macroThreeTimerTwoCls))
                    keyboard.release(controller.macroThreeKeyTwoCls)
                    macroThreeButton['bg'] = '#f0f0f0'

                elif (msg.lower() == macroFourButton['text'].lower() and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    macroFourButton['bg'] = 'red'
                    keyboard.press(controller.macroFourKeyOneCls)
                    time.sleep(int(controller.macroFourTimerOneCls))
                    keyboard.press(controller.macroFourKeyTwoCls)
                    keyboard.release(controller.macroFourKeyOneCls)
                    time.sleep(int(controller.macroFourTimerTwoCls))
                    keyboard.release(controller.macroFourKeyTwoCls)
                    macroFourButton['bg'] = '#f0f0f0'

                elif (msg.lower() == MouseManage.textMouseRight and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveRightButton['bg'] = 'red'
                    mouse.move(int("" + str(mousemove.moveMouseRight)), 0, False, .1)
                    mouseMoveRightButton['bg'] = '#f0f0f0'
                elif (msg.lower() == MouseManage.textMouseLeft and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveLeftButton['bg'] = 'red'
                    mouse.move(int("-" + str(mousemove.moveMouseLeft)), 0, False, .1)
                    mouseMoveLeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == MouseManage.textMouseUp and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveUpButton['bg'] = 'red'
                    mouse.move(0, int("-" + str(mousemove.moveMouseUp)), False, .1)
                    mouseMoveUpButton['bg'] = '#f0f0f0'
                elif (msg.lower() == MouseManage.textMouseDown and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseMoveDownButton['bg'] = 'red'
                    mouse.move(0, int("" + str(mousemove.moveMouseDown)), False, .1)
                    mouseMoveDownButton['bg'] = '#f0f0f0'
                elif (msg.lower() == MouseManage.leftClick and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseLeftButton['bg'] = 'red'
                    mouse.press(MouseManage.leftClickValue)
                    mouse.release(MouseManage.leftClickValue)
                    time.sleep(1)
                    mouseLeftButton['bg'] = '#f0f0f0'
                elif (msg.lower() == MouseManage.rightClick and (
                        int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (
                              int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseRightButton['bg'] = 'red'
                    mouse.press(MouseManage.rightClickValue)
                    mouse.release(MouseManage.rightClickValue)
                    time.sleep(1)
                    mouseRightButton['bg'] = '#f0f0f0'

            ####################################
            ####################################

        except Exception as e:
            print("Encountered exception: " + str(e))


##################### GAME VARIABLES #####################

def thread():
    backgroundInfo.t1 = threading.Thread(target=Program, daemon=True)
    if (backgroundInfo.t1.is_alive() != True):
        startButton["state"] = DISABLED
        endButton["state"] = DISABLED
        startButton['bg'] = 'light yellow'
        backgroundInfo.t1.start()
    else:
        backgroundInfo.t1.join()


def Program(eventRun=None):
    TTA = TextToAction()
    handleMessaging = TTA.handle_message
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
    MAX_WORKERS = 100  # Maximum number of threads you can process at a time

    last_time = time.time()
    message_queue = []
    thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
    active_tasks = []
    alt_active_tasks = []
    pyautogui.FAILSAFE = False

    ##########################################################

    # Count down before starting, so you have time to load up the game
    countdown = 5
    while countdown > 0:
        messageRelayConnect.config(text=countdown)
        countdown -= 1
        time.sleep(1)

    try:
        if (
                backgroundInfo.twitchActive == True and backgroundInfo.youtubeActive != True and backgroundInfo.previousTab == 3):
            backgroundInfo.t = TwitchPlays_Connection.Twitch()
            backgroundInfo.t.twitch_connect(backgroundInfo.TWITCH_CHANNEL)
            messageRelayConnect.config(text='Connected To Twitch')
        elif (
                backgroundInfo.youtubeActive == True and backgroundInfo.twitchActive != True and backgroundInfo.previousTab == 3):
            backgroundInfo.t = TwitchPlays_Connection.YouTube()
            backgroundInfo.t.youtube_connect(backgroundInfo.YOUTUBE_CHANNEL_ID, backgroundInfo.YOUTUBE_STREAM_URL)
            messageRelayConnect.config(text='Connected To Youtube')
        elif (
                backgroundInfo.twitchActive == True and backgroundInfo.youtubeActive == True and backgroundInfo.previousTab == 3):
            backgroundInfo.t = TwitchPlays_Connection.Twitch()
            backgroundInfo.t.twitch_connect(backgroundInfo.TWITCH_CHANNEL)
            backgroundInfo.y = TwitchPlays_Connection.YouTube()
            backgroundInfo.y.youtube_connect(backgroundInfo.YOUTUBE_CHANNEL_ID, backgroundInfo.YOUTUBE_STREAM_URL)
            messageRelayConnect.config(text='Connected To Twitch and Youtube')
        endButton["state"] = ACTIVE
        startButton['bg'] = 'light green'
    except Exception as e:
        messageRelayConnect.config(text='Error: Unable to connect to a platform. Check login details...')
        endButton["state"] = ACTIVE
        startButton['bg'] = 'red'

    while (True and backgroundInfo.previousTab == 3):
        t = backgroundInfo.t
        y = backgroundInfo.y
        active_tasks = [t for t in active_tasks if not t.done()]
        alt_active_tasks = [y for y in alt_active_tasks if not y.done()]

        # Check for new messages
        new_messages = t.twitch_receive_messages()

        if (backgroundInfo.STREAMING_ON_TWITCH == True and backgroundInfo.STREAMING_ON_YOUTUBE == True):
            alt_new_messages = y.twitch_receive_messages()
        else:
            alt_new_messages = None
        if new_messages:
            message_queue += new_messages;  # New messages are added to the back of the queue
            message_queue = message_queue[-MAX_QUEUE_LENGTH:]  # Shorten the queue to only the most recent X messages
        if backgroundInfo.STREAMING_ON_TWITCH == True and backgroundInfo.STREAMING_ON_YOUTUBE == True and alt_new_messages != None:
            message_queue += alt_new_messages;
            message_queue = message_queue[-MAX_QUEUE_LENGTH:]

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
                    active_tasks.append(thread_pool.submit(handleMessaging, message))
                elif len(alt_active_tasks) <= MAX_WORKERS:
                    alt_active_tasks.append(thread_pool.submit(handleMessaging, message))
                else:
                    print(
                        f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')


sendInfo = backgroundInfo()
sendTwitchFunc = sendInfo.twitch_Button
sendYoutubeFunc = sendInfo.youtube_Button
sendTwitchAndYoutubeFunc = sendInfo.youtubeAndTwitch_Button
sendCloseFunc = sendInfo.web_close_window
sendWebSiteFunc = sendInfo.WebSite
sendBackTrackAccountFunc = sendInfo.backTrackAccount
sendBackTrackPlatformFunc = sendInfo.backTrackPlatform
sendPlatformCloseFunc = sendInfo.platform_close_window
sendMinecraftSettingFunc = sendInfo.minecraftSetting
sendCustomSettingFunc = sendInfo.customSetting
sendGameCloseFunc = sendInfo.game_close_window
sendThread = thread
sendProgramFunc = sendInfo.endProgram
sendStartCloseFunc = sendInfo.start_close_window
sendUpdateMessageFunc = sendInfo.updateMessage
greenScreenMode = GreenScreen()
GSModeFunc = greenScreenMode.greenScreenChange

sendHeartBoundSettingFunc = sendInfo.heartboundSetting
sendKnuckleSandwichSettingFunc = sendInfo.knuckleSandwichSetting


while (backgroundInfo.previousTab == 0):
    web = mtTkinter.Tk()
    web.lift()
    web.attributes('-topmost', True)
    web.grab_set()
    web.grab_release()
    web.focus_force()
    web.title("ContentPlays")
    web.iconbitmap("icon.ico")
    web.geometry("525x350+700+300")
    web.config(background="white")
    web.minsize(525, 350)
    web.maxsize(525, 350)
    youtubePhoto = PhotoImage(file="youtube.png")
    youtubeResize = youtubePhoto.subsample(3, 3)
    twitchPhoto = PhotoImage(file="twitch.png")
    twitchResize = twitchPhoto.subsample(3, 3)
    webText = Label(web, text="Select The Platform",
                    bg="white",
                    fg="black",
                    font=("Arial", 17))
    sendTwitch = partial(sendTwitchFunc, web)
    twitchButton = Button(web, height=1, width=10, text="Twitch", font=("Arial", 12), compound=TOP,
                          command=sendTwitch)  # , image= twitchResize, height = 140, width = 100)
    sendYoutube = partial(sendYoutubeFunc, web)
    youtubeButton = Button(web, height=1, width=10, text="Youtube", font=("Arial", 12), compound=TOP,
                           command=sendYoutube)  # , image= youtubeResize), height = 140, width = 100)
    sendTwitchAndYoutube = partial(sendTwitchAndYoutubeFunc, web)
    twitchAndYoutubeButton = Button(web, height=1, width=20, text="Both Twitch and Youtube", font=("Arial", 12),
                                    compound=TOP, command=sendTwitchAndYoutube)
    thanks = Label(web,
                   text="Original code by Wituz, updated by DDarknut, DougDoug, Ottomated. Further expanded by Bloop",
                   bg="white",
                   fg="black",
                   font=("Arial", 7))

    sendClose = partial(sendCloseFunc, web)
    web.protocol("WM_DELETE_WINDOW", sendClose)
    webText.place(x=155, y=50)
    twitchButton.place(x=120, y=100)
    youtubeButton.place(x=285, y=100)
    # twitchAndYoutubeButton.place(x=162, y=260)
    twitchAndYoutubeButton.place(x=162, y=160)
    thanks.place(x=0, y=330)
    web.mainloop()
    while (backgroundInfo.previousTab == 1):
        platform = mtTkinter.Tk()
        platform.lift()
        platform.attributes('-topmost', True)
        platform.grab_set()
        platform.grab_release()
        platform.focus_force()
        platform.title("ContentPlays")
        platform.iconbitmap("icon.ico")
        platform.geometry("525x350+700+300")
        platform.config(background="white")
        platform.minsize(525, 350)
        platform.maxsize(525, 350)
        username = None
        youtubeURL = None
        if (backgroundInfo.twitchActive == True and backgroundInfo.youtubeActive == True):
            webText = Label(platform, text="Enter Your Youtube Channel ID",
                            bg="white",
                            fg="black",
                            font=("Arial", 10))
            webURL = Label(platform, text="Enter Your Youtube Stream URL",
                           bg="white",
                           fg="black",
                           font=("Arial", 10))
            username = Entry(platform, text="Channel ID..", width=53)
            youtubeURL = Entry(platform, text="Channel URL..", width=53)
            username.place(x=25, y=50)
            webText.place(x=5, y=20)
            webURL.place(x=5, y=80)
            youtubeURL.place(x=25, y=110)

            webText = Label(platform, text="Enter Your Twitch Username",
                            bg="white",
                            fg="black",
                            font=("Arial", 10))
            username = Entry(platform, text="Username..", width=53)
            username.place(x=25, y=170)
            webText.place(x=5, y=140)

        if (backgroundInfo.twitchActive == True and backgroundInfo.youtubeActive == False):
            webText = Label(platform, text="Enter Your Twitch Username",
                            bg="white",
                            fg="black",
                            font=("Arial", 10))
            username = Entry(platform, text="Username..", width=53)
            username.place(x=25, y=50)
            webText.place(x=5, y=20)
        if (backgroundInfo.youtubeActive == True and backgroundInfo.twitchActive == False):
            webText = Label(platform, text="Enter Your Channel ID",
                            bg="white",
                            fg="black",
                            font=("Arial", 10))
            webURL = Label(platform, text="Enter Your Stream URL",
                           bg="white",
                           fg="black",
                           font=("Arial", 10))
            username = Entry(platform, text="Channel ID..", width=53)
            youtubeURL = Entry(platform, text="Channel URL..", width=53)
            username.place(x=25, y=50)
            webText.place(x=5, y=20)
            webURL.place(x=5, y=80)
            youtubeURL.place(x=25, y=110)
        sendWebSite = partial(sendWebSiteFunc, platform, username, youtubeURL)
        nextButton = Button(platform, text="Next", height=2, width=5, command=sendWebSite)
        nextButton.place(x=460, y=290)
        sendBackTrackAccount = partial(sendBackTrackAccountFunc, platform)
        backButton = Button(platform, text="Back", height=2, width=5, command=sendBackTrackAccount)
        backButton.place(x=15, y=290)
        sendPlatformClose = partial(sendPlatformCloseFunc, platform)
        platform.protocol("WM_DELETE_WINDOW", sendPlatformClose)
        platform.mainloop()
        while (backgroundInfo.previousTab == 2):
            game = mtTkinter.Tk()
            game.lift()
            game.attributes('-topmost', True)
            game.grab_set()
            game.grab_release()
            game.focus_force()
            game.title("ContentPlays")
            game.iconbitmap("icon.ico")
            game.geometry("525x350+700+300")
            game.config(background="white")
            game.minsize(525, 350)
            game.maxsize(525, 350)

            webText = Label(game, text="Select A Game",
                            bg="white",
                            fg="black",
                            font=("Arial", 15))
            webText.place(x=175, y=50)

            sendMinecraftSetting = partial(sendMinecraftSettingFunc, game)
            minecraftButton = Button(game, text="Minecraft", height=2, width=9, command=sendMinecraftSetting)
            minecraftButton.place(x=75, y=100)

            sendHeartBoundSetting = partial(sendHeartBoundSettingFunc, game)
            gameTwoButton = Button(game, text="HeartBound", height=2, width=9, command=sendHeartBoundSetting)
            gameTwoButton.place(x=150, y=100)

            gameThreeButton = Button(game, text="Game 3", height=2, width=9, command=None)
            gameThreeButton.place(x=225, y=100)

            gameFourButton = Button(game, text="Game 4", height=2, width=9, command=None)
            gameFourButton.place(x=300, y=100)

            gameFiveButton = Button(game, text="Game 5", height=2, width=9, command=None)
            gameFiveButton.place(x=375, y=100)

            gameSixButton = Button(game, text="Game 6", height=2, width=9, command=None)
            gameSixButton.place(x=75, y=150)

            gameSevenButton = Button(game, text="Game 7", height=2, width=9, command=None)
            gameSevenButton.place(x=150, y=150)

            gameEightButton = Button(game, text="Game 8", height=2, width=9, command=None)
            gameEightButton.place(x=225, y=150)

            gameNineButton = Button(game, text="Game 9", height=2, width=9, command=None)
            gameNineButton.place(x=300, y=150)

            gameTenButton = Button(game, text="Game 10", height=2, width=9, command=None)
            gameTenButton.place(x=375, y=150)

            gameElevenButton = Button(game, text="Game 11", height=2, width=9, command=None)
            gameElevenButton.place(x=75, y=200)

            gameTwelveButton = Button(game, text="Game 12", height=2, width=9, command=None)
            gameTwelveButton.place(x=150, y=200)

            gameThirteenButton = Button(game, text="Game 13", height=2, width=9, command=None)
            gameThirteenButton.place(x=225, y=200)

            sendKnuckleSandwichSetting = partial(sendKnuckleSandwichSettingFunc, game)
            gameFourteenButton = Button(game, text="Knuckle Sandwich", height=2, width=9, wraplength=52,
                                        command=sendKnuckleSandwichSetting)
            gameFourteenButton.place(x=300, y=200)

            sendCustomSetting = partial(sendCustomSettingFunc, game)
            customButton = Button(game, text="Custom", height=2, width=9, command=sendCustomSetting)
            customButton.place(x=375, y=200)

            sendBackTrackPlatform = partial(sendBackTrackPlatformFunc, game)
            backButton = Button(game, text="Back", height=2, width=5, command=sendBackTrackPlatform)
            backButton.place(x=15, y=290)
            sendGameClose = partial(sendGameCloseFunc, game)

            ScreenManage.startXGet = 0
            ScreenManage.endXGet = 1920
            ScreenManage.startYGet = 0
            ScreenManage.endYGet =1080

            game.protocol("WM_DELETE_WINDOW", sendGameClose)

            game.mainloop()
            while (backgroundInfo.previousTab == 3):
                start = mtTkinter.Tk()
                start.lift()
                start.attributes('-topmost', True)
                start.grab_set()
                start.grab_release()
                start.focus_force()
                start.title("ContentPlays")
                start.iconbitmap("icon.ico")
                start.geometry("525x350+700+300")
                start.config(background="white")
                start.minsize(525, 350)
                start.maxsize(525, 350)

                menubar = Menu(start)
                options = Menu(menubar, tearoff=0)
                menubar.add_cascade(label='Options', menu=options)
                screenManager = ScreenManage()
                screenFunction = partial(screenManager.screenOption, start)
                options.add_command(label='Screen', command=screenFunction)

                messageRelayOne = Label(start, text='',
                                        bg="white",
                                        fg="black",
                                        font=("Arial", 10))
                messageRelayTwo = Label(start, text='',
                                        bg="white",
                                        fg="black",
                                        font=("Arial", 10))
                messageRelayThree = Label(start, text='',
                                          bg="white",
                                          fg="black",
                                          font=("Arial", 10))
                messageRelayFour = Label(start, text='',
                                         bg="white",
                                         fg="black",
                                         font=("Arial", 10))

                messageRelayConnect = Label(start, text='',
                                            bg="white",
                                            fg="black",
                                            font=("Arial", 13),
                                            anchor="center")

                startButton = Button(start, text="Start", height=2, width=5, command=sendThread)
                startButton.place(x=225, y=280)
                sendProgram = partial(sendProgramFunc, start, startButton, messageRelayOne, messageRelayTwo,
                                      messageRelayThree, messageRelayFour)

                endButton = Button(start, text="End", height=2, width=5, command=sendProgram)
                endButton.place(x=275, y=280)

                if (backgroundInfo.gamesetting == 0):
                    shiftButton = Button(start, text="Shift", height=1, width=5, state=DISABLED)
                    shiftButton.place(x=20, y=145)

                    controlButton = Button(start, text="Control", height=1, width=6, state=DISABLED)
                    controlButton.place(x=20, y=175)

                    upButton = Button(start, text="Up", height=1, width=4, state=DISABLED)
                    DownButton = Button(start, text="Down", height=1, width=4, state=DISABLED)
                    LeftButton = Button(start, text="Left", height=1, width=4, state=DISABLED)
                    RightButton = Button(start, text="Right", height=1, width=4, state=DISABLED)
                    upButton.place(x=115, y=145)
                    DownButton.place(x=115, y=175)
                    LeftButton.place(x=75, y=175)
                    RightButton.place(x=155, y=175)

                    secHandButton = Button(start, text="Swap", height=1, width=4, state=DISABLED)
                    secHandButton.place(x=215, y=110)

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

                    spaceButton = Button(start, text="Space Bar", height=1, width=20, state=DISABLED)
                    spaceButton.place(x=221, y=175)

                    dropButton = Button(start, text="Drop", height=1, width=4, state=DISABLED)
                    dropButton.place(x=75, y=110)

                    InvButton = Button(start, text="Inv", height=1, width=4, state=DISABLED)
                    InvButton.place(x=155, y=110)

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

                if (backgroundInfo.gamesetting == 1):
                    upButton = Button(start, text="Up", height=1, width=4, state=DISABLED)
                    DownButton = Button(start, text="Down", height=1, width=4, state=DISABLED)
                    LeftButton = Button(start, text="Left", height=1, width=4, state=DISABLED)
                    RightButton = Button(start, text="Right", height=1, width=4, state=DISABLED)
                    upButton.place(x=115, y=145)
                    DownButton.place(x=115, y=175)
                    LeftButton.place(x=75, y=175)
                    RightButton.place(x=155, y=175)

                    acceptButton = Button(start, text="z", height=1, width=4, state=DISABLED)
                    acceptButton.place(x=75, y=110)

                    skipButton = Button(start, text="x", height=1, width=4, state=DISABLED)
                    skipButton.place(x=155, y=110)

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

                if (backgroundInfo.gamesetting == 14):
                    upButton = Button(start, text="Up", height=1, width=4, state=DISABLED)
                    DownButton = Button(start, text="Down", height=1, width=4, state=DISABLED)
                    LeftButton = Button(start, text="Left", height=1, width=4, state=DISABLED)
                    RightButton = Button(start, text="Right", height=1, width=4, state=DISABLED)
                    upButton.place(x=115, y=145)
                    DownButton.place(x=115, y=175)
                    LeftButton.place(x=75, y=175)
                    RightButton.place(x=155, y=175)

                    confirmButton = Button(start, text="x", height=1, width=4, state=DISABLED)
                    confirmButton.place(x=75, y=110)

                    cancelButton = Button(start, text="c", height=1, width=4, state=DISABLED)
                    cancelButton.place(x=115, y=110)

                    miscButton = Button(start, text="b", height=1, width=4, state=DISABLED)
                    miscButton.place(x=155, y=110)

                    spaceButton = Button(start, text="Space", height=1, width=20, state=DISABLED)
                    spaceButton.place(x=221, y=175)

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

                if (backgroundInfo.gamesetting == 99):
                    start.minsize(600, 350)
                    start.maxsize(600, 350)
                    # controlManager = ControlManage()
                    # controlFunction = partial(controlManager.controlOption, start, upButton, downButton, rightButton, leftButton, oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton, zeroButton, shiftButton, controlButton, enterButton, spaceButton, actionButtonOne, actionButtonTwo, actionButtonThree, actionButtonFour, actionButtonFive, actionButtonSix, actionButtonSeven, actionButtonEight, macroOneButton, macroTwoButton, macroThreeButton, macroFourButton, mouseMoveRightButton, mouseMoveLeftButton, mouseMoveUpButton, mouseMoveDownButton, mouseLeftButton, mouseRightButton)
                    # mouseManager = MouseManage()
                    # mouseFunction = partial(mouseManager.mouseOption, start, greenScreenCls)

                    # options.add_command(label='Keyboard', command= controlFunction)
                    # options.add_command(label='Mouse', command= mouseFunction)

                    upButton = Button(start, text="Up", height=1, width=4, state=DISABLED)
                    downButton = Button(start, text="Down", height=1, width=4, state=DISABLED)
                    leftButton = Button(start, text="Left", height=1, width=4, state=DISABLED)
                    rightButton = Button(start, text="Right", height=1, width=4, state=DISABLED)
                    upButton.place(x=100, y=140)
                    downButton.place(x=100, y=170)
                    leftButton.place(x=60, y=170)
                    rightButton.place(x=140, y=170)

                    oneButton = Button(start, text="1", height=1, width=4, state=DISABLED)
                    twoButton = Button(start, text="2", height=1, width=4, state=DISABLED)
                    threeButton = Button(start, text="3", height=1, width=4, state=DISABLED)
                    fourButton = Button(start, text="4", height=1, width=4, state=DISABLED)
                    fiveButton = Button(start, text="5", height=1, width=4, state=DISABLED)
                    sixButton = Button(start, text="6", height=1, width=4, state=DISABLED)
                    sevenButton = Button(start, text="7", height=1, width=4, state=DISABLED)
                    eightButton = Button(start, text="8", height=1, width=4, state=DISABLED)
                    nineButton = Button(start, text="9", height=1, width=4, state=DISABLED)
                    zeroButton = Button(start, text="0", height=1, width=4, state=DISABLED)
                    oneButton.place(x=20, y=30)
                    twoButton.place(x=65, y=30)
                    threeButton.place(x=110, y=30)
                    fourButton.place(x=155, y=30)
                    fiveButton.place(x=200, y=30)
                    sixButton.place(x=245, y=30)
                    sevenButton.place(x=290, y=30)
                    eightButton.place(x=335, y=30)
                    nineButton.place(x=380, y=30)
                    zeroButton.place(x=425, y=30)

                    spaceButton = Button(start, text="Space Bar", height=1, width=15, state=DISABLED)
                    spaceButton.place(x=185, y=170)

                    macroOneButton = Button(start, text="Macro 1", height=1, width=6, state=DISABLED)
                    macroOneButton.place(x=20, y=70)

                    macroTwoButton = Button(start, text="Macro 2", height=1, width=6, state=DISABLED)
                    macroTwoButton.place(x=20, y=100)

                    macroThreeButton = Button(start, text="Macro 3", height=1, width=6, state=DISABLED)
                    macroThreeButton.place(x=410, y=70)

                    macroFourButton = Button(start, text="Macro 4", height=1, width=6, state=DISABLED)
                    macroFourButton.place(x=410, y=100)

                    actionButtonOne = Button(start, text="Action 1", height=1, width=7, state=DISABLED)
                    actionButtonOne.place(x=115, y=70)

                    actionButtonTwo = Button(start, text="Action 2", height=1, width=7, state=DISABLED)
                    actionButtonTwo.place(x=180, y=70)

                    actionButtonThree = Button(start, text="Action 3", height=1, width=7, state=DISABLED)
                    actionButtonThree.place(x=245, y=70)

                    actionButtonFour = Button(start, text="Action 4", height=1, width=7, state=DISABLED)
                    actionButtonFour.place(x=310, y=70)

                    actionButtonFive = Button(start, text="Action 5", height=1, width=7, state=DISABLED)
                    actionButtonFive.place(x=115, y=100)

                    actionButtonSix = Button(start, text="Action 6", height=1, width=7, state=DISABLED)
                    actionButtonSix.place(x=180, y=100)

                    actionButtonSeven = Button(start, text="Action 7", height=1, width=7, state=DISABLED)
                    actionButtonSeven.place(x=245, y=100)

                    actionButtonEight = Button(start, text="Action 8", height=1, width=7, state=DISABLED)
                    actionButtonEight.place(x=310, y=100)

                    enterButton = Button(start, text="enter", height=1, width=7, state=DISABLED)
                    enterButton.place(x=403, y=140)

                    shiftButton = Button(start, text="Shift", height=1, width=7, state=DISABLED)
                    shiftButton.place(x=20, y=140)

                    controlButton = Button(start, text="CTRL", height=1, width=4, state=DISABLED)
                    controlButton.place(x=20, y=170)

                    mousePalmButton = Button(start, text="", height=2, width=5, state=DISABLED)
                    mouseLeftButton = Button(start, text="L", height=1, width=2, state=DISABLED)
                    mouseRightButton = Button(start, text="R", height=1, width=2, state=DISABLED)
                    mousePalmButton.place(x=510, y=125)
                    mouseLeftButton.place(x=510, y=100)
                    mouseRightButton.place(x=531, y=100)

                    mouseMoveUpButton = Button(start, text="↑", height=1, width=1, state=DISABLED)
                    mouseMoveDownButton = Button(start, text="↓", height=1, width=1, state=DISABLED)
                    mouseMoveLeftButton = Button(start, text="←", height=1, width=1, state=DISABLED)
                    mouseMoveRightButton = Button(start, text="→", height=1, width=1, state=DISABLED)
                    mouseMoveUpButton.place(x=525, y=70)
                    mouseMoveDownButton.place(x=525, y=170)
                    mouseMoveLeftButton.place(x=485, y=120)
                    mouseMoveRightButton.place(x=560, y=120)

                    startButton.place(x=250, y=280)
                    endButton.place(x=300, y=280)
                    controlManager = ControlManage()
                    controlFunction = partial(controlManager.controlOption,  start, upButton, downButton, rightButton,
                                              leftButton, oneButton, twoButton, threeButton, fourButton, fiveButton,
                                              sixButton, sevenButton, eightButton, nineButton, zeroButton, shiftButton,
                                              controlButton, enterButton, spaceButton, actionButtonOne, actionButtonTwo,
                                              actionButtonThree, actionButtonFour, actionButtonFive, actionButtonSix,
                                              actionButtonSeven, actionButtonEight, macroOneButton, macroTwoButton,
                                              macroThreeButton, macroFourButton, mouseMoveRightButton,
                                              mouseMoveLeftButton, mouseMoveUpButton, mouseMoveDownButton,
                                              mouseLeftButton, mouseRightButton)
                    mouseManager = MouseManage()
                    mouseFunction = partial(mouseManager.mouseOption, start, greenScreenCls)
                    options.add_command(label='Keyboard', command=controlFunction)
                    options.add_command(label='Mouse', command=mouseFunction)

                GSMode = partial(GSModeFunc, start, messageRelayOne, messageRelayTwo, messageRelayThree,
                                 messageRelayFour, messageRelayConnect)
                options.add_command(label='GS Mode', command=GSMode)
                messageRelayFour.place(x=5, y=200)
                messageRelayThree.place(x=5, y=220)
                messageRelayTwo.place(x=5, y=240)
                messageRelayOne.place(x=5, y=260)
                messageRelayConnect.place(x=20, y=5)
                sendStartClose = partial(sendStartCloseFunc, start)
                start.protocol("WM_DELETE_WINDOW", sendStartClose)
                start.config(menu=menubar)
                start.mainloop()

exit()
