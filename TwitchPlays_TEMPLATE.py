import concurrent.futures
import ctypes
import threading as threading
import time
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

class GreenScreen():
    greenScreenCls = False
    def greenScreenChange(self):
        if(GreenScreen.greenScreenCls == False):
            GreenScreen.greenScreenCls = True
            start['bg'] = 'lime'
            messageRelayConnect['bg'] = 'lime'
            messageRelayOne['bg'] = 'lime'
            messageRelayTwo['bg'] = 'lime'
            messageRelayThree['bg'] = 'lime'
            messageRelayFour['bg'] = 'lime'

        else:
            GreenScreen.greenScreenCls = False
            start['bg'] = 'white'
            messageRelayConnect['bg'] = 'white'
            messageRelayOne['bg'] = 'white'
            messageRelayTwo['bg'] = 'white'
            messageRelayThree['bg'] = 'white'
            messageRelayFour['bg'] = 'white'


class ControlManage():
    upKeyCls = ''
    downKeyCls = ''
    rightKeyCls = ''
    leftKeyCls = ''
    oneKeyCls = ''
    twoKeyCls = ''
    threeKeyCls = ''
    fourKeyCls = ''
    fiveKeyCls = ''
    sixKeyCls = ''
    sevenKeyCls = ''
    eightKeyCls = ''
    nineKeyCls = ''
    zeroKeyCls = ''
    shiftKeyCls = ''
    controlKeyCls = ''
    macroOneKeyOneCls = ''
    macroOneKeyTwoCls = ''
    macroTwoKeyOneCls = ''
    macroTwoKeyTwoCls = ''
    macroThreeKeyOneCls = ''
    macroThreeKeyTwoCls = ''
    macroFourKeyOneCls = ''
    macroFourKeyTwoCls = ''
    actionOneKeyCls = ''
    actionTwoKeyCls = ''
    actionThreeKeyCls = ''
    actionFourKeyCls = ''
    actionFiveKeyCls = ''
    actionSixKeyCls = ''
    actionSevenKeyCls = ''
    actionEightKeyCls = ''
    macroOneTimerOneCls = ''
    macroTwoTimerOneCls = ''
    macroThreeTimerOneCls = ''
    macroFourTimerOneCls = ''
    macroOneTimerTwoCls = ''
    macroTwoTimerTwoCls = ''
    macroThreeTimerTwoCls = ''
    macroFourTimerTwoCls = ''
    enterKeyCls = ''
    spaceKeyCls = ''
    def __init__(self):
        self.upText = StringVar()
        self.downText = StringVar()
        self.rightText = StringVar()
        self.leftText = StringVar()
        self.oneText = StringVar()
        self.twoText = StringVar()
        self.threeText = StringVar()
        self.fourText = StringVar()
        self.fiveText = StringVar()
        self.sixText = StringVar()
        self.sevenText = StringVar()
        self.eightText = StringVar()
        self.nineText = StringVar()
        self.zeroText = StringVar()
        self.shiftText = StringVar()
        self.controlText = StringVar()
        self.macroOneText = StringVar()
        self.macroTwoText = StringVar()
        self.macroThreeText = StringVar()
        self.macroFourText = StringVar()
        self.actionOneText = StringVar()
        self.actionTwoText = StringVar()
        self.actionThreeText = StringVar()
        self.actionFourText = StringVar()
        self.actionFiveText = StringVar()
        self.actionSixText = StringVar()
        self.actionSevenText = StringVar()
        self.actionEightText = StringVar()
        self.macroOneTimerOne = StringVar()
        self.macroTwoTimerOne = StringVar()
        self.macroThreeTimerOne = StringVar()
        self.macroFourTimerOne = StringVar()
        self.macroOneTimerTwo = StringVar()
        self.macroTwoTimerTwo = StringVar()
        self.macroThreeTimerTwo = StringVar()
        self.macroFourTimerTwo = StringVar()
        self.enterText = StringVar()
        self.spaceText = StringVar()

        self.enterText.set('')
        self.spaceText.set('')
        self.upText.set('')
        self.downText.set('')
        self.rightText.set('')
        self.leftText.set('')
        self.oneText.set('')
        self.twoText.set('')
        self.threeText.set('')
        self.fourText.set('')
        self.fiveText.set('')
        self.sixText.set('')
        self.sevenText.set('')
        self.eightText.set('')
        self.nineText.set('')
        self.zeroText.set('')
        self.shiftText.set('')
        self.controlText.set('')
        self.macroOneText.set('')
        self.macroTwoText.set('')
        self.macroThreeText.set('')
        self.macroFourText.set('')
        self.actionOneText.set('')
        self.actionTwoText.set('')
        self.actionThreeText.set('')
        self.actionFourText.set('')
        self.actionFiveText.set('')
        self.actionSixText.set('')
        self.actionSevenText.set('')
        self.actionEightText.set('')
        self.macroOneTimerOne.set('0')
        self.macroTwoTimerOne.set('0')
        self.macroThreeTimerOne.set('0')
        self.macroFourTimerOne.set('0')
        self.macroOneTimerTwo.set('0')
        self.macroTwoTimerTwo.set('0')
        self.macroThreeTimerTwo.set('0')
        self.macroFourTimerTwo.set('0')
        self.keyOptions = ('none','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0','[', ']','\\','-','+',';','\'','`',',','.','/','Backspace','Control','Alt','Spacebar','Enter','Shift','Up Arrow','Down Arrow','Right Button','Left Arrow')

        self.upKeyValue = StringVar()
        self.downKeyValue = StringVar()
        self.leftKeyValue = StringVar()
        self.rightKeyValue = StringVar()
        self.enterKeyValue = StringVar()
        self.controlKeyValue = StringVar()
        self.spaceKeyValue = StringVar()
        self.shiftKeyValue = StringVar()
        self.oneKeyValue = StringVar()
        self.twoKeyValue = StringVar()
        self.threeKeyValue = StringVar()
        self.fourKeyValue = StringVar()
        self.fiveKeyValue = StringVar()
        self.sixKeyValue = StringVar()
        self.sevenKeyValue = StringVar()
        self.eightKeyValue = StringVar()
        self.nineKeyValue = StringVar()
        self.zeroKeyValue = StringVar()
        self.actionOneKeyValue = StringVar()
        self.actionTwoKeyValue = StringVar()
        self.actionThreeKeyValue = StringVar()
        self.actionFourKeyValue = StringVar()
        self.actionFiveKeyValue = StringVar()
        self.actionSixKeyValue = StringVar()
        self.actionSevenKeyValue = StringVar()
        self.actionEightKeyValue = StringVar()
        self.macroOneKeyValueOne = StringVar()
        self.macroTwoKeyValueOne = StringVar()
        self.macroThreeKeyValueOne = StringVar()
        self.macroFourKeyValueOne = StringVar()
        self.macroOneKeyValueTwo = StringVar()
        self.macroTwoKeyValueTwo = StringVar()
        self.macroThreeKeyValueTwo = StringVar()
        self.macroFourKeyValueTwo = StringVar()

        self.upKeyValue.set('0')
        self.downKeyValue.set('0')
        self.leftKeyValue.set('0')
        self.rightKeyValue.set('0')
        self.enterKeyValue.set('0')
        self.controlKeyValue.set('0')
        self.spaceKeyValue.set('0')
        self.shiftKeyValue.set('0')
        self.oneKeyValue.set('0')
        self.twoKeyValue.set('0')
        self.threeKeyValue.set('0')
        self.fourKeyValue.set('0')
        self.fiveKeyValue.set('0')
        self.sixKeyValue.set('0')
        self.sevenKeyValue.set('0')
        self.eightKeyValue.set('0')
        self.nineKeyValue.set('0')
        self.zeroKeyValue.set('0')
        self.actionOneKeyValue.set('0')
        self.actionTwoKeyValue.set('0')
        self.actionThreeKeyValue.set('0')
        self.actionFourKeyValue.set('0')
        self.actionFiveKeyValue.set('0')
        self.actionSixKeyValue.set('0')
        self.actionSevenKeyValue.set('0')
        self.actionEightKeyValue.set('0')
        self.macroOneKeyValueOne.set('0')
        self.macroTwoKeyValueOne.set('0')
        self.macroThreeKeyValueOne.set('0')
        self.macroFourKeyValueOne.set('0')
        self.macroOneKeyValueTwo.set('0')
        self.macroTwoKeyValueTwo.set('0')
        self.macroThreeKeyValueTwo.set('0')
        self.macroFourKeyValueTwo.set('0')


    def controlOption(self, start):
        controlOpt = mtTkinter.Tk()
        controlOpt.lift()
        controlOpt.attributes('-topmost', True)
        controlOpt.grab_set()
        controlOpt.grab_release()
        controlOpt.focus_force()
        controlOpt.title("ContentPlays")
        controlOpt.iconbitmap("icon.ico")
        controlOpt.geometry("600x650+700+300")
        controlOpt.config(background="white")
        controlOpt.minsize(600, 650)
        controlOpt.maxsize(600, 650)
        youtubePhoto = PhotoImage(file="youtube.png")
        youtubeResize = youtubePhoto.subsample(3, 3)
        twitchPhoto = PhotoImage(file="twitch.png")
        twitchResize = twitchPhoto.subsample(3, 3)

        movementText = Label(controlOpt, text="Movement Keys",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        movementText.place(x=15, y=10)

        keyText = Label(controlOpt, text="Key",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        keyText.place(x=40, y=35)

        chatText = Label(controlOpt, text="Chat Text",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        chatText.place(x=100, y=35)

        bindingText = Label(controlOpt, text="Binding",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        bindingText.place(x=210, y=35)

#Up Key
        displayUp = Label(controlOpt, text="up:",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        displayUp.place(x=40, y=60)
        displayUpEntry = Entry(controlOpt, width=12, textvariable=self.upText)
        displayUpEntry.place(x=95, y=60)
        upKey = Combobox(controlOpt, width= 10, textvariable=self.upKeyValue , values = self.keyOptions)
        upKey.place(x=195, y=60)

#Down Key
        displayDown = Label(controlOpt, text="down:",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        displayDown.place(x=310, y=60)
        displayDownEntry = Entry(controlOpt, width=12, textvariable=self.downText)
        displayDownEntry.place(x=365, y=60)
        downKey = Combobox(controlOpt, width=10, textvariable=self.downKeyValue , values=self.keyOptions)
        downKey.place(x=465, y=60)

# Left Key
        displayLeft = Label(controlOpt, text="left:",
                            bg="white",
                            fg="black",
                            font=("Arial", 9))
        displayLeft.place(x=40, y=85)
        displayLeftEntry = Entry(controlOpt, width=12, textvariable=self.leftText)
        displayLeftEntry.place(x=95, y=85)
        leftKey = Combobox(controlOpt, width=10,textvariable=self.leftKeyValue , values=self.keyOptions)
        leftKey.place(x=195, y=85)

# Right Key
        displayRight = Label(controlOpt, text="right:",
                             bg="white",
                             fg="black",
                             font=("Arial", 9))
        displayRight.place(x=310, y=85)
        displayRightEntry = Entry(controlOpt, width=12, textvariable=self.rightText)
        displayRightEntry.place(x=365, y=85)
        rightKey = Combobox(controlOpt, width=10, textvariable=self.rightKeyValue , values=self.keyOptions)
        rightKey.place(x=465, y=85)

# Shift Key
        displayShift = Label(controlOpt, text="shift:",
                             bg="white",
                             fg="black",
                             font=("Arial", 9))
        displayShift.place(x=40, y=110)
        displayShiftEntry = Entry(controlOpt, width=12, textvariable=self.shiftText)
        displayShiftEntry.place(x=95, y=110)
        shiftKey = Combobox(controlOpt, width=10, textvariable=self.shiftKeyValue , values=self.keyOptions)
        shiftKey.place(x=195, y=110)

# Control Key
        displayControl = Label(controlOpt, text="control:",
                               bg="white",
                               fg="black",
                               font=("Arial", 9))
        displayControl.place(x=310, y=110)
        displayControlEntry = Entry(controlOpt, width=12, textvariable=self.controlText)
        displayControlEntry.place(x=365, y=110)
        controlKey = Combobox(controlOpt, width=10, textvariable=self.controlKeyValue ,values=self.keyOptions)
        controlKey.place(x=465, y=110)

# Space Key
        displaySpace = Label(controlOpt, text="space:",
                               bg="white",
                               fg="black",
                               font=("Arial", 9))
        displaySpace.place(x=40, y=135)
        displaySpaceEntry = Entry(controlOpt, width=12, textvariable=self.spaceText)
        displaySpaceEntry.place(x=95, y=135)
        spaceKey = Combobox(controlOpt, width=10, textvariable=self.spaceKeyValue ,values=self.keyOptions)
        spaceKey.place(x=195, y=135)

# Enter Key
        displayEnter = Label(controlOpt, text="enter:",
                               bg="white",
                               fg="black",
                               font=("Arial", 9))
        displayEnter.place(x=310, y=135)
        displayEnterEntry = Entry(controlOpt, width=12, textvariable=self.enterText)
        displayEnterEntry.place(x=365, y=135)
        enterKey = Combobox(controlOpt, width=10, textvariable=self.enterKeyValue ,values=self.keyOptions)
        enterKey.place(x=465, y=135)

        actionText = Label(controlOpt, text="Action Keys",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        actionText.place(x=15, y=165)

# Action One Key
        displayActionOne = Label(controlOpt, text="Action 1:",
                                 bg="white",
                                 fg="black",
                                 font=("Arial", 9))
        displayActionOne.place(x=40, y=190)
        displayActionOneEntry = Entry(controlOpt, width=12, textvariable=self.actionOneText)
        displayActionOneEntry.place(x=95, y=190)
        actionOneKey = Combobox(controlOpt, width=10, textvariable=self.actionOneKeyValue ,values=self.keyOptions)
        actionOneKey.place(x=195, y=190)

# Action Two Key
        displayActionTwo = Label(controlOpt, text="Action 2:",
                                 bg="white",
                                 fg="black",
                                 font=("Arial", 9))
        displayActionTwo.place(x=40, y=215)
        displayActionTwoEntry = Entry(controlOpt, width=12, textvariable=self.actionTwoText)
        displayActionTwoEntry.place(x=95, y=215)
        actionTwoKey = Combobox(controlOpt, width=10, textvariable=self.actionTwoKeyValue ,values=self.keyOptions)
        actionTwoKey.place(x=195, y=215)

# Action Three Key
        displayActionThree = Label(controlOpt, text="Action 3:",
                                   bg="white",
                                   fg="black",
                                   font=("Arial", 9))
        displayActionThree.place(x=40, y=240)
        displayActionThreeEntry = Entry(controlOpt, width=12, textvariable=self.actionThreeText)
        displayActionThreeEntry.place(x=95, y=240)
        actionThreeKey = Combobox(controlOpt, width=10, textvariable=self.actionThreeKeyValue ,values=self.keyOptions)
        actionThreeKey.place(x=195, y=240)

# Action Four Key
        displayActionFour = Label(controlOpt, text="Action 4:",
                                  bg="white",
                                  fg="black",
                                  font=("Arial", 9))
        displayActionFour.place(x=40, y=265)
        displayActionFourEntry = Entry(controlOpt, width=12, textvariable=self.actionFourText)
        displayActionFourEntry.place(x=95, y=265)
        actionFourKey = Combobox(controlOpt, width=10, textvariable=self.actionFourKeyValue ,values=self.keyOptions)
        actionFourKey.place(x=195, y=265)

# Action Five Key
        displayActionFive = Label(controlOpt, text="Action 5:",
                                  bg="white",
                                  fg="black",
                                  font=("Arial", 9))
        displayActionFive.place(x=310, y=190)
        displayActionFiveEntry = Entry(controlOpt, width=12, textvariable=self.actionFiveText)
        displayActionFiveEntry.place(x=365, y=190)
        actionFiveKey = Combobox(controlOpt, width=10, textvariable=self.actionFiveKeyValue ,values=self.keyOptions)
        actionFiveKey.place(x=465, y=190)

# Action Six Key
        displayActionSix = Label(controlOpt, text="Action 6:",
                                 bg="white",
                                 fg="black",
                                 font=("Arial", 9))
        displayActionSix.place(x=310, y=215)
        displayActionSixEntry = Entry(controlOpt, width=12, textvariable=self.actionSixText)
        displayActionSixEntry.place(x=365, y=215)
        actionSixKey = Combobox(controlOpt, width=10, textvariable=self.actionSixKeyValue ,values=self.keyOptions)
        actionSixKey.place(x=465, y=215)

# Action Seven Key
        displayActionSeven = Label(controlOpt, text="Action 7:",
                                   bg="white",
                                   fg="black",
                                   font=("Arial", 9))
        displayActionSeven.place(x=310, y=240)
        displayActionSevenEntry = Entry(controlOpt, width=12, textvariable=self.actionSevenText)
        displayActionSevenEntry.place(x=365, y=240)
        actionSevenKey = Combobox(controlOpt, width=10, textvariable=self.actionSevenKeyValue , values=self.keyOptions)
        actionSevenKey.place(x=465, y=240)

# Action Eight Key
        displayActionEight = Label(controlOpt, text="Action 8:",
                                   bg="white",
                                   fg="black",
                                   font=("Arial", 9))
        displayActionEight.place(x=310, y=265)
        displayActionEightEntry = Entry(controlOpt, width=12, textvariable=self.actionEightText)
        displayActionEightEntry.place(x=365, y=265)
        actionEightKey = Combobox(controlOpt, width=10, textvariable=self.actionEightKeyValue ,values=self.keyOptions)
        actionEightKey.place(x=465, y=265)

        numberText = Label(controlOpt, text="Number Keys",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        numberText.place(x=15, y=290)

# One Key
        displayOne = Label(controlOpt, text="one:",
                           bg="white",
                           fg="black",
                           font=("Arial", 9))
        displayOne.place(x=40, y=315)
        displayOneEntry = Entry(controlOpt, width=12, textvariable=self.oneText)
        displayOneEntry.place(x=95, y=315)
        oneKey = Combobox(controlOpt, width=10, textvariable=self.oneKeyValue ,values=self.keyOptions)
        oneKey.place(x=195, y=315)

# Two Key
        displayTwo = Label(controlOpt, text="two:",
                           bg="white",
                           fg="black",
                           font=("Arial", 9))
        displayTwo.place(x=40, y=340)
        displayTwoEntry = Entry(controlOpt, width=12, textvariable=self.twoText)
        displayTwoEntry.place(x=95, y=340)
        twoKey = Combobox(controlOpt, width=10, textvariable=self.twoKeyValue ,values=self.keyOptions)
        twoKey.place(x=195, y=340)

# Three Key
        displayThree = Label(controlOpt, text="three:",
                             bg="white",
                             fg="black",
                             font=("Arial", 9))
        displayThree.place(x=40, y=365)
        displayThreeEntry = Entry(controlOpt, width=12, textvariable=self.threeText)
        displayThreeEntry.place(x=95, y=365)
        threeKey = Combobox(controlOpt, width=10, textvariable=self.threeKeyValue ,values=self.keyOptions)
        threeKey.place(x=195, y=365)

# Four Key
        displayFour = Label(controlOpt, text="four:",
                            bg="white",
                            fg="black",
                            font=("Arial", 9))
        displayFour.place(x=40, y=390)
        displayFourEntry = Entry(controlOpt, width=12, textvariable=self.fourText)
        displayFourEntry.place(x=95, y=390)
        fourKey = Combobox(controlOpt, width=10, textvariable=self.fourKeyValue ,values=self.keyOptions)
        fourKey.place(x=195, y=390)

# Five Key
        displayFive = Label(controlOpt, text="five:",
                            bg="white",
                            fg="black",
                            font=("Arial", 9))
        displayFive.place(x=40, y=415)
        displayFiveEntry = Entry(controlOpt, width=12, textvariable=self.fiveText)
        displayFiveEntry.place(x=95, y=415)
        fiveKey = Combobox(controlOpt, width=10, textvariable=self.fiveKeyValue ,values=self.keyOptions)
        fiveKey.place(x=195, y=415)

# Six Key
        displaySix = Label(controlOpt, text="six:",
                           bg="white",
                           fg="black",
                           font=("Arial", 9))
        displaySix.place(x=310, y=315)
        displaySixEntry = Entry(controlOpt, width=12, textvariable=self.sixText)
        displaySixEntry.place(x=365, y=315)
        sixKey = Combobox(controlOpt, width=10, textvariable=self.sixKeyValue ,values=self.keyOptions)
        sixKey.place(x=465, y=315)

# Seven Key
        displaySeven = Label(controlOpt, text="seven:",
                             bg="white",
                             fg="black",
                             font=("Arial", 9))
        displaySeven.place(x=310, y=340)
        displaySevenEntry = Entry(controlOpt, width=12, textvariable=self.sevenText)
        displaySevenEntry.place(x=365, y=340)
        sevenKey = Combobox(controlOpt, width=10, textvariable=self.sevenKeyValue ,values=self.keyOptions)
        sevenKey.place(x=465, y=340)

# Eight Key
        displayEight = Label(controlOpt, text="eight:",
                             bg="white",
                             fg="black",
                             font=("Arial", 9))
        displayEight.place(x=310, y=365)
        displayEightEntry = Entry(controlOpt, width=12, textvariable=self.eightText)
        displayEightEntry.place(x=365, y=365)
        eightKey = Combobox(controlOpt, width=10, textvariable=self.eightKeyValue ,values=self.keyOptions)
        eightKey.place(x=465, y=365)

# Nine Key
        displayNine = Label(controlOpt, text="nine:",
                            bg="white",
                            fg="black",
                            font=("Arial", 9))
        displayNine.place(x=310, y=390)
        displayNineEntry = Entry(controlOpt, width=12, textvariable=self.nineText)
        displayNineEntry.place(x=365, y=390)
        nineKey = Combobox(controlOpt, width=10, textvariable=self.nineKeyValue ,values=self.keyOptions)
        nineKey.place(x=465, y=390)

# Zero Key
        displayZero = Label(controlOpt, text="zero:",
                            bg="white",
                            fg="black",
                            font=("Arial", 9))
        displayZero.place(x=310, y=415)
        displayZeroEntry = Entry(controlOpt, width=12, textvariable=self.zeroText)
        displayZeroEntry.place(x=365, y=415)
        zeroKey = Combobox(controlOpt, width=10, textvariable=self.zeroKeyValue ,values=self.keyOptions)
        zeroKey.place(x=465, y=415)

        MacroText = Label(controlOpt, text="Macro Keys",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        MacroText.place(x=15, y=440)

        keyText = Label(controlOpt, text="Key",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        keyText.place(x=40, y=465)

        chatText = Label(controlOpt, text="Chat Text",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        chatText.place(x=100, y=465)

        bindingText = Label(controlOpt, text="Binding",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        bindingText.place(x=210, y=465)

        bindingText = Label(controlOpt, text="Interval",
                        bg="white",
                        fg="black",
                        font=("Arial", 10))
        bindingText.place(x=290, y=465)


# MacroOne Key
        displayMacroOne = Label(controlOpt, text="Macro 1:",
                                bg="white",
                                fg="black",
                                font=("Arial", 9))
        displayMacroOne.place(x=40, y=490)
        displayMacroOneEntry = Entry(controlOpt, width=12, textvariable=self.macroOneText)
        displayMacroOneEntry.place(x=95, y=490)
        macroOneKeyOne = Combobox(controlOpt, width=10, textvariable=self.macroOneKeyValueOne ,values=self.keyOptions)
        macroOneKeyOne.place(x=195, y=490)

        displayMacroOneEntryTimerOne = Entry(controlOpt, width=6, textvariable=self.macroOneTimerOne)
        displayMacroOneEntryTimerOne.place(x=295, y=490)
        macroOneKeyTwo = Combobox(controlOpt, width=10, textvariable=self.macroOneKeyValueTwo ,values=self.keyOptions)
        macroOneKeyTwo.place(x=355, y=490)
        displayMacroOneEntryTimerTwo = Entry(controlOpt, width=6, textvariable=self.macroOneTimerTwo)
        displayMacroOneEntryTimerTwo.place(x=455, y=490)

# MacroTwo Key
        displayMacroTwo = Label(controlOpt, text="Macro 2:",
                                bg="white",
                                fg="black",
                                font=("Arial", 9))
        displayMacroTwo.place(x=40, y=515)
        displayMacroTwoEntry = Entry(controlOpt, width=12, textvariable=self.macroTwoText)
        displayMacroTwoEntry.place(x=95, y=515)
        macroTwoKeyOne = Combobox(controlOpt, width=10, textvariable=self.macroTwoKeyValueOne ,values=self.keyOptions)
        macroTwoKeyOne.place(x=195, y=515)

        displayMacroTwoEntryTimerOne = Entry(controlOpt, width=6, textvariable=self.macroTwoTimerOne)
        displayMacroTwoEntryTimerOne.place(x=295, y=515)
        macroTwoKeyTwo = Combobox(controlOpt, width=10, textvariable=self.macroTwoKeyValueTwo ,values=self.keyOptions)
        macroTwoKeyTwo.place(x=355, y=515)
        displayMacroTwoEntryTimerTwo = Entry(controlOpt, width=6, textvariable=self.macroTwoTimerTwo)
        displayMacroTwoEntryTimerTwo.place(x=455, y=515)

# MacroThree Key
        displayMacroThree = Label(controlOpt, text="Macro 3:",
                                  bg="white",
                                  fg="black",
                                  font=("Arial", 9))
        displayMacroThree.place(x=40, y=540)
        displayMacroThreeEntry = Entry(controlOpt, width=12, textvariable=self.macroThreeText)
        displayMacroThreeEntry.place(x=95, y=540)
        macroThreeKeyOne = Combobox(controlOpt, width=10, textvariable=self.macroThreeKeyValueOne , values=self.keyOptions)
        macroThreeKeyOne.place(x=195, y=540)

        displayMacroThreeEntryTimerOne = Entry(controlOpt, width=6, textvariable=self.macroThreeTimerOne)
        displayMacroThreeEntryTimerOne.place(x=295, y=540)
        macroThreeKeyTwo = Combobox(controlOpt, width=10, textvariable=self.macroThreeKeyValueTwo ,values=self.keyOptions)
        macroThreeKeyTwo.place(x=355, y=540)
        displayMacroThreeEntryTimerTwo = Entry(controlOpt, width=6, textvariable=self.macroThreeTimerTwo)
        displayMacroThreeEntryTimerTwo.place(x=455, y=540)

# MacroFour Key
        displayMacroFour = Label(controlOpt, text="Macro 4:",
                                 bg="white",
                                 fg="black",
                                 font=("Arial", 9))
        displayMacroFour.place(x=40, y=565)
        displayMacroFourEntry = Entry(controlOpt, width=12, textvariable=self.macroFourText)
        displayMacroFourEntry.place(x=95, y=565)
        macroFourKeyOne = Combobox(controlOpt, width=10, textvariable=self.macroFourKeyValueOne , values=self.keyOptions)
        macroFourKeyOne.place(x=195, y=565)

        displayMacroFourEntryTimerOne = Entry(controlOpt, width=6, textvariable=self.macroFourTimerOne)
        displayMacroFourEntryTimerOne.place(x=295, y=565)
        macroFourKeyTwo = Combobox(controlOpt, width=10, textvariable=self.macroFourKeyValueTwo ,values=self.keyOptions)
        macroFourKeyTwo.place(x=355, y=565)
        displayMacroFourEntryTimerTwo = Entry(controlOpt, width=6, textvariable=self.macroFourTimerTwo)
        displayMacroFourEntryTimerTwo.place(x=455, y=565)


        submitControl = partial(ControlManage.on_press, self, controlOpt, start, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo)
        submitButton = Button(controlOpt, text='Submit', command=submitControl)
        submitButton.place(x=250, y=610)
        clearControl = partial(ControlManage.clearKeyBinding, self, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo)
        clearButton = Button(controlOpt, text='Clear', command=clearControl)
        clearButton.place(x=310, y=610)
        controlOpt.after(1, self.updateKeyEntry, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo)
        closeControl = partial(ControlManage.closeControl_close_window, self, controlOpt)
        controlOpt.protocol("WM_DELETE_WINDOW", closeControl)
        startcloseControl = partial(ControlManage.alt_closeControl_close_window, self, controlOpt)
        start.protocol("WM_DELETE_WINDOW", startcloseControl)

    def updateKeyEntry(self, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo):
        displayUpEntry.insert(END, self.upText.get())
        displayDownEntry.insert(END, self.downText.get())
        displayRightEntry.insert(END, self.rightText.get())
        displayLeftEntry.insert(END, self.leftText.get())
        displayShiftEntry.insert(END, self.shiftText.get())
        displayControlEntry.insert(END, self.controlText.get())
        displaySpaceEntry.insert(END, self.spaceText.get())
        displayEnterEntry.insert(END, self.enterText.get())
        displayActionOneEntry.insert(END, self.actionOneText.get())
        displayActionTwoEntry.insert(END, self.actionTwoText.get())
        displayActionThreeEntry.insert(END, self.actionThreeText.get())
        displayActionFourEntry.insert(END, self.actionFourText.get())
        displayActionFiveEntry.insert(END, self.actionFiveText.get())
        displayActionSixEntry.insert(END, self.actionSixText.get())
        displayActionSevenEntry.insert(END, self.actionSevenText.get())
        displayActionEightEntry.insert(END, self.actionEightText.get())
        displayOneEntry.insert(END, self.oneText.get())
        displayTwoEntry.insert(END, self.twoText.get())
        displayThreeEntry.insert(END, self.threeText.get())
        displayFourEntry.insert(END, self.fourText.get())
        displayFiveEntry.insert(END, self.fiveText.get())
        displaySixEntry.insert(END, self.sixText.get())
        displaySevenEntry.insert(END, self.sevenText.get())
        displayEightEntry.insert(END, self.eightText.get())
        displayNineEntry.insert(END, self.nineText.get())
        displayZeroEntry.insert(END, self.zeroText.get())
        displayMacroOneEntry.insert(END, self.macroOneText.get())
        displayMacroOneEntryTimerOne.insert(END, self.macroOneTimerOne.get())
        displayMacroOneEntryTimerTwo.insert(END, self.macroOneTimerTwo.get())
        displayMacroTwoEntry.insert(END, self.macroTwoText.get())
        displayMacroTwoEntryTimerOne.insert(END, self.macroTwoTimerOne.get())
        displayMacroTwoEntryTimerTwo.insert(END, self.macroTwoTimerTwo.get())
        displayMacroThreeEntry.insert(END, self.macroThreeText.get())
        displayMacroThreeEntryTimerOne.insert(END, self.macroThreeTimerOne.get())
        displayMacroThreeEntryTimerTwo.insert(END, self.macroThreeTimerTwo.get())
        displayMacroFourEntry.insert(END, self.macroFourText.get())
        displayMacroFourEntryTimerOne.insert(END, self.macroFourTimerOne.get())
        displayMacroFourEntryTimerTwo.insert(END, self.macroFourTimerTwo.get())
        upKey.current(int(self.upKeyValue.get()))
        downKey.current(int(self.downKeyValue.get()))
        leftKey.current(int(self.leftKeyValue.get()))
        rightKey.current(int(self.rightKeyValue.get()))
        shiftKey.current(int(self.shiftKeyValue.get()))
        controlKey.current(int(self.controlKeyValue.get()))
        spaceKey.current(int(self.spaceKeyValue.get()))
        enterKey.current(int(self.enterKeyValue.get()))
        actionOneKey.current(int(self.actionOneKeyValue.get()))
        actionTwoKey.current(int(self.actionTwoKeyValue.get()))
        actionThreeKey.current(int(self.actionThreeKeyValue.get()))
        actionFourKey.current(int(self.actionFourKeyValue.get()))
        actionFiveKey.current(int(self.actionFiveKeyValue.get()))
        actionSixKey.current(int(self.actionSixKeyValue.get()))
        actionSevenKey.current(int(self.actionSevenKeyValue.get()))
        actionEightKey.current(int(self.actionEightKeyValue.get()))
        oneKey.current(int(self.oneKeyValue.get()))
        twoKey.current(int(self.twoKeyValue.get()))
        threeKey.current(int(self.threeKeyValue.get()))
        fourKey.current(int(self.fourKeyValue.get()))
        fiveKey.current(int(self.fiveKeyValue.get()))
        sixKey.current(int(self.sixKeyValue.get()))
        sevenKey.current(int(self.sevenKeyValue.get()))
        eightKey.current(int(self.eightKeyValue.get()))
        nineKey.current(int(self.nineKeyValue.get()))
        zeroKey.current(int(self.zeroKeyValue.get()))
        macroOneKeyOne.current(int(self.macroOneKeyValueOne.get()))
        macroOneKeyTwo.current(int(self.macroOneKeyValueTwo.get()))
        macroTwoKeyOne.current(int(self.macroTwoKeyValueOne.get()))
        macroTwoKeyTwo.current(int(self.macroTwoKeyValueTwo.get()))
        macroThreeKeyOne.current(int(self.macroThreeKeyValueOne.get()))
        macroThreeKeyTwo.current(int(self.macroThreeKeyValueTwo.get()))
        macroFourKeyOne.current(int(self.macroFourKeyValueTwo.get()))
        macroFourKeyTwo.current(int(self.macroFourKeyValueTwo.get()))


    def closeControl_close_window(self, controlOpt):
        controlOpt.destroy()

    def alt_closeControl_close_window(self, controlOpt):
        try:
            controlOpt.destroy()
            GreenScreen.greenScreenCls = False
            start.destroy()
            exit()
        except Exception as e:
            GreenScreen.greenScreenCls = False
            start.destroy()
            exit()


    def on_press(self, controlOpt, start, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo):
        if(displayUpEntry.get() == '' or displayUpEntry.get() == None or upKey.get() == 'none'):
            upButton.config(text='')
        else:
            upButton.config(text=displayUpEntry.get())
            self.upText.set(displayUpEntry.get())
            index = self.keyOptions.index(upKey.get())
            self.upKeyValue.set(str(index))
            ControlManage.upKeyCls = upKey.get()


        if(displayDownEntry.get() == '' or displayDownEntry.get() == None or displayDownEntry.get() == 'none'):
            downButton.config(text='')
        else:
            downButton.config(text=displayDownEntry.get())
            self.downText.set(displayDownEntry.get())
            index = self.keyOptions.index(downKey.get())
            self.downKeyValue.set(str(index))
            ControlManage.downKeyCls = downKey.get()

        if (displayLeftEntry.get() == '' or displayLeftEntry.get() == None or displayLeftEntry.get() == 'none'):
            leftButton.config(text='')
        else:
            leftButton.config(text=displayLeftEntry.get())
            self.leftText.set(displayLeftEntry.get())
            index = self.keyOptions.index(leftKey.get())
            self.leftKeyValue.set(str(index))
            ControlManage.leftKeyCls = leftKey.get()

        if (displayRightEntry.get() == '' or displayRightEntry.get() == None or displayRightEntry.get() == 'none'):
            rightButton.config(text='')
        else:
            rightButton.config(text=displayRightEntry.get())
            self.rightText.set(displayRightEntry.get())
            index = self.keyOptions.index(rightKey.get())
            self.rightKeyValue.set(str(index))
            ControlManage.rightKeyCls = rightKey.get()

        if (displayOneEntry.get() == '' or displayOneEntry.get() == None or displayOneEntry.get() == 'none'):
            oneButton.config(text='')
        else:
            oneButton.config(text=displayOneEntry.get())
            self.oneText.set(displayOneEntry.get())
            index = self.keyOptions.index(oneKey.get())
            self.oneKeyValue.set(str(index))
            ControlManage.oneKeyCls = oneKey.get()

        if (displayTwoEntry.get() == '' or displayTwoEntry.get() == None or displayTwoEntry.get() == 'none'):
            twoButton.config(text='')
        else:
            twoButton.config(text=displayTwoEntry.get())
            self.twoText.set(displayTwoEntry.get())
            index = self.keyOptions.index(twoKey.get())
            self.twoKeyValue.set(str(index))
            ControlManage.twoKeyCls = twoKey.get()

        if (displayThreeEntry.get() == '' or displayThreeEntry.get() == None or displayThreeEntry.get() == 'none'):
            threeButton.config(text='')
        else:
            threeButton.config(text=displayThreeEntry.get())
            self.threeText.set(displayThreeEntry.get())
            index = self.keyOptions.index(threeKey.get())
            self.threeKeyValue.set(str(index))
            ControlManage.threeKeyCls = threeKey.get()

        if (displayFourEntry.get() == '' or displayFourEntry.get() == None or displayFourEntry.get() == 'none'):
            fourButton.config(text='')
        else:
            fourButton.config(text=displayFourEntry.get())
            self.fourText.set(displayFourEntry.get())
            index = self.keyOptions.index(fourKey.get())
            self.fourKeyValue.set(str(index))
            ControlManage.fourKeyCls = fourKey.get()

        if (displayFiveEntry.get() == '' or displayFiveEntry.get() == None or displayFiveEntry.get() == 'none'):
            fiveButton.config(text='')
        else:
            fiveButton.config(text=displayFiveEntry.get())
            self.fiveText.set(displayFiveEntry.get())
            index = self.keyOptions.index(fiveKey.get())
            self.fiveKeyValue.set(str(index))
            ControlManage.fiveKeyCls = fiveKey.get()

        if (displaySixEntry.get() == '' or displaySixEntry.get() == None or displaySixEntry.get() == 'none'):
            sixButton.config(text='')
        else:
            sixButton.config(text=displaySixEntry.get())
            self.sixText.set(displaySixEntry.get())
            index = self.keyOptions.index(sixKey.get())
            self.sixKeyValue.set(str(index))
            ControlManage.sixKeyCls = sixKey.get()

        if (displaySevenEntry.get() == '' or displaySevenEntry.get() == None or displaySevenEntry.get() == 'none'):
            sevenButton.config(text='')
        else:
            sevenButton.config(text=displaySevenEntry.get())
            self.sevenText.set(displaySevenEntry.get())
            index = self.keyOptions.index(sevenKey.get())
            self.sevenKeyValue.set(str(index))
            ControlManage.sevenKeyCls = sevenKey.get()

        if (displayEightEntry.get() == '' or displayEightEntry.get() == None or displayEightEntry.get() == 'none'):
            eightButton.config(text='')
        else:
            eightButton.config(text=displayEightEntry.get())
            self.eightText.set(displayEightEntry.get())
            index = self.keyOptions.index(eightKey.get())
            self.eightKeyValue.set(str(index))
            ControlManage.eightKeyCls = eightKey.get()

        if (displayNineEntry.get() == '' or displayNineEntry.get() == None or displayNineEntry.get() == 'none'):
            nineButton.config(text='')
        else:
            nineButton.config(text=displayNineEntry.get())
            self.nineText.set(displayNineEntry.get())
            index = self.keyOptions.index(nineKey.get())
            self.nineKeyValue.set(str(index))
            ControlManage.nineKeyCls = nineKey.get()

        if (displayZeroEntry.get() == '' or displayZeroEntry.get() == None or displayZeroEntry.get() == 'none'):
            zeroButton.config(text='')
        else:
            zeroButton.config(text=displayZeroEntry.get())
            self.zeroText.set(displayZeroEntry.get())
            index = self.keyOptions.index(zeroKey.get())
            self.zeroKeyValue.set(str(index))
            ControlManage.zeroKeyCls = zeroKey.get()

        if (displaySpaceEntry.get() == '' or displaySpaceEntry.get() == None or displaySpaceEntry.get() == 'none'):
            spaceButton.config(text='')
        else:
            spaceButton.config(text=displaySpaceEntry.get())
            self.spaceText.set(displaySpaceEntry.get())
            index = self.keyOptions.index(spaceKey.get())
            self.spaceKeyValue.set(str(index))
            ControlManage.spaceKeyCls = spaceKey.get()

        if (displayMacroOneEntry.get() == '' or displayMacroOneEntry.get() == None or displayMacroOneEntry.get() == 'none'):
            macroOneButton.config(text='')
        else:
            macroOneButton.config(text=displayMacroOneEntry.get())
            self.macroOneText.set(displayMacroOneEntry.get())
            index = self.keyOptions.index(macroOneKeyOne.get())
            self.macroOneKeyValueOne.set(str(index))
            index = self.keyOptions.index(macroOneKeyTwo.get())
            self.macroOneKeyValueTwo.set(str(index))
            ControlManage.macroOneKeyOneCls = macroOneKeyOne.get()
            ControlManage.macroOneKeyTwoCls = macroOneKeyTwo.get()

        if (displayMacroTwoEntry.get() == '' or displayMacroTwoEntry.get() == None or displayMacroTwoEntry.get() == 'none'):
            macroTwoButton.config(text='')
        else:
            macroTwoButton.config(text=displayMacroTwoEntry.get())
            self.macroTwoText.set(displayMacroTwoEntry.get())
            index = self.keyOptions.index(macroTwoKeyOne.get())
            self.macroTwoKeyValueOne.set(str(index))
            index = self.keyOptions.index(macroTwoKeyTwo.get())
            self.macroTwoKeyValueTwo.set(str(index))
            ControlManage.macroTwoKeyOneCls = macroTwoKeyOne.get()
            ControlManage.macroTwoKeyTwoCls = macroTwoKeyTwo.get()

        if (displayMacroThreeEntry.get() == '' or displayMacroThreeEntry.get() == None or displayMacroThreeEntry.get() == 'none'):
            macroThreeButton.config(text='')
        else:
            macroThreeButton.config(text=displayMacroThreeEntry.get())
            self.macroThreeText.set(displayMacroThreeEntry.get())
            index = self.keyOptions.index(macroThreeKeyOne.get())
            self.macroThreeKeyValueOne.set(str(index))
            index = self.keyOptions.index(macroThreeKeyTwo.get())
            self.macroThreeKeyValueTwo.set(str(index))
            ControlManage.macroThreeKeyOneCls = macroThreeKeyOne.get()
            ControlManage.macroThreeKeyTwoCls = macroThreeKeyTwo.get()

        if (displayMacroFourEntry.get() == '' or displayMacroFourEntry.get() == None or displayMacroFourEntry.get() == 'none'):
            macroFourButton.config(text='')
        else:
            macroFourButton.config(text=displayMacroFourEntry.get())
            self.macroFourText.set(displayMacroFourEntry.get())
            index = self.keyOptions.index(macroFourKeyOne.get())
            self.macroFourKeyValueOne.set(str(index))
            index = self.keyOptions.index(macroFourKeyTwo.get())
            self.macroFourKeyValueTwo.set(str(index))
            ControlManage.macroFourKeyOneCls = macroFourKeyOne.get()
            ControlManage.macroFourKeyTwoCls = macroFourKeyTwo.get()

        if (displayActionOneEntry.get() == '' or displayActionOneEntry.get() == None or displayActionOneEntry.get() == 'none'):
            actionButtonOne.config(text='')
        else:
            actionButtonOne.config(text=displayActionOneEntry.get())
            self.actionOneText.set(displayActionOneEntry.get())
            index = self.keyOptions.index(actionOneKey.get())
            self.actionOneKeyValue.set(str(index))
            ControlManage.actionOneKeyCls = actionOneKey.get()

        if (displayActionTwoEntry.get() == '' or displayActionTwoEntry.get() == None or displayActionTwoEntry.get() == 'none'):
            actionButtonTwo.config(text='')
        else:
            actionButtonTwo.config(text=displayActionTwoEntry.get())
            self.actionTwoText.set(displayActionTwoEntry.get())
            index = self.keyOptions.index(actionTwoKey.get())
            self.actionTwoKeyValue.set(str(index))
            ControlManage.actionTwoKeyCls = actionTwoKey.get()

        if (displayActionThreeEntry.get() == '' or displayActionThreeEntry.get() == None or displayActionThreeEntry.get() == 'none'):
            actionButtonThree.config(text='')
        else:
            actionButtonThree.config(text=displayActionThreeEntry.get())
            self.actionThreeText.set(displayActionThreeEntry.get())
            index = self.keyOptions.index(actionThreeKey.get())
            self.actionThreeKeyValue.set(str(index))
            ControlManage.actionThreeKeyCls = actionThreeKey.get()

        if (displayActionFourEntry.get() == '' or displayActionFourEntry.get() == None or displayActionFourEntry.get() == 'none'):
            actionButtonFour.config(text='')
        else:
            actionButtonFour.config(text=displayActionFourEntry.get())
            self.actionFourText.set(displayActionFourEntry.get())
            index = self.keyOptions.index(actionFourKey.get())
            self.actionFourKeyValue.set(str(index))
            ControlManage.actionFourKeyCls = actionFourKey.get()

        if (displayActionFiveEntry.get() == '' or displayActionFiveEntry.get() == None or displayActionFiveEntry.get() == 'none'):
            actionButtonFive.config(text='')
        else:
            actionButtonFive.config(text=displayActionFiveEntry.get())
            self.actionFiveText.set(displayActionFiveEntry.get())
            index = self.keyOptions.index(actionFiveKey.get())
            self.actionFiveKeyValue.set(str(index))
            ControlManage.actionFiveKeyCls = actionFiveKey.get()

        if (displayActionSixEntry.get() == '' or displayActionSixEntry.get() == None or displayActionSixEntry.get() == 'none'):
            actionButtonSix.config(text='')
        else:
            actionButtonSix.config(text=displayActionSixEntry.get())
            self.actionSixText.set(displayActionSixEntry.get())
            index = self.keyOptions.index(actionSixKey.get())
            self.actionSixKeyValue.set(str(index))
            ControlManage.actionSixKeyCls = actionSixKey.get()

        if (displayActionSevenEntry.get() == '' or displayActionSevenEntry.get() == None or displayActionSevenEntry.get() == 'none'):
            actionButtonSeven.config(text='')
        else:
            actionButtonSeven.config(text=displayActionSevenEntry.get())
            self.actionSevenText.set(displayActionSevenEntry.get())
            index = self.keyOptions.index(actionSevenKey.get())
            self.actionSevenKeyValue.set(str(index))
            ControlManage.actionSevenKeyCls = actionSevenKey.get()

        if (displayActionEightEntry.get() == '' or displayActionEightEntry.get() == None or displayActionEightEntry.get() == 'none'):
            actionButtonEight.config(text='')
        else:
            actionButtonEight.config(text=displayActionEightEntry.get())
            self.actionEightText.set(displayActionEightEntry.get())
            index = self.keyOptions.index(actionEightKey.get())
            self.actionEightKeyValue.set(str(index))
            ControlManage.actionEightKeyCls = actionEightKey.get()

        if (displayEnterEntry.get() == '' or displayEnterEntry.get() == None or displayEnterEntry.get() == 'none'):
            enterButton.config(text='')
        else:
            enterButton.config(text=displayEnterEntry.get())
            self.enterText.set(displayEnterEntry.get())
            index = self.keyOptions.index(enterKey.get())
            self.enterKeyValue.set(str(index))
            ControlManage.enterKeyCls = enterKey.get()

        if (displayShiftEntry.get() == '' or displayShiftEntry.get() == None or displayShiftEntry.get() == 'none'):
            shiftButton.config(text='')
        else:
            shiftButton.config(text=displayShiftEntry.get())
            self.shiftText.set(displayShiftEntry.get())
            index = self.keyOptions.index(shiftKey.get())
            self.shiftKeyValue.set(str(index))
            ControlManage.shiftKeyCls = shiftKey.get()

        if (displayControlEntry.get() == '' or displayControlEntry.get() == None or displayControlEntry.get() == 'none'):
            controlButton.config(text='')
        else:
            controlButton.config(text=displayControlEntry.get())
            self.controlText.set(displayControlEntry.get())
            index = self.keyOptions.index(controlKey.get())
            self.controlKeyValue.set(str(index))
            ControlManage.controlKeyCls = controlKey.get()

        if (displayMacroOneEntryTimerOne.get() == '' or displayMacroOneEntryTimerOne.get() == None):
            self.macroOneTimerOne.set('0')
        else:
            self.macroOneTimerOne.set(displayMacroOneEntryTimerOne.get())
            ControlManage.macroOneTimerOneCls = displayMacroOneEntryTimerOne.get()

        if (displayMacroTwoEntryTimerOne.get() == '' or displayMacroTwoEntryTimerOne.get() == None):
            self.macroTwoTimerOne.set('0')
        else:
            self.macroTwoTimerOne.set(displayMacroTwoEntryTimerOne.get())
            ControlManage.macroOneTimerTwoCls = displayMacroTwoEntryTimerOne.get()

        if (displayMacroThreeEntryTimerOne.get() == '' or displayMacroThreeEntryTimerOne.get() == None):
            self.macroThreeTimerOne.set('0')
        else:
            self.macroThreeTimerOne.set(displayMacroThreeEntryTimerOne.get())
            ControlManage.macroTwoTimerOneCls = displayMacroThreeEntryTimerOne.get()


        if (displayMacroFourEntryTimerOne.get() == '' or displayMacroFourEntryTimerOne.get() == None):
            self.macroFourTimerOne.set('0')
        else:
            self.macroFourTimerOne.set(displayMacroFourEntryTimerOne.get())
            ControlManage.macroTwoTimerTwoCls = displayMacroFourEntryTimerOne.get()


        if (displayMacroOneEntryTimerTwo.get() == '' or displayMacroOneEntryTimerTwo.get() == None):
            self.macroOneTimerTwo.set('0')
        else:
            self.macroOneTimerTwo.set(displayMacroOneEntryTimerTwo.get())
            ControlManage.macroThreeTimerOneCls = displayMacroOneEntryTimerTwo.get()


        if (displayMacroTwoEntryTimerTwo.get() == '' or displayMacroTwoEntryTimerTwo.get() == None):
            self.macroTwoTimerTwo.set('0')
        else:
            self.macroTwoTimerTwo.set(displayMacroTwoEntryTimerTwo.get())
            ControlManage.macroThreeTimerTwoCls = displayMacroTwoEntryTimerTwo.get()


        if (displayMacroThreeEntryTimerTwo.get() == '' or displayMacroThreeEntryTimerTwo.get() == None):
            self.macroThreeTimerTwo.set('0')
        else:
            self.macroThreeTimerTwo.set(displayMacroThreeEntryTimerTwo.get())
            ControlManage.macroFourTimerOneCls = displayMacroThreeEntryTimerTwo.get()


        if (displayMacroFourEntryTimerTwo.get() == '' or displayMacroFourEntryTimerTwo.get() == None):
            self.macroFourTimerTwo.set('0')
        else:
            self.macroFourTimerTwo.set(displayMacroFourEntryTimerTwo.get())
            ControlManage.macroFourTimerTwoCls = displayMacroFourEntryTimerTwo.get()

        controlOpt.destroy()

    def clearKeyBinding(self, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo):
        self.enterText.set('')
        self.spaceText.set('')
        self.upText.set('')
        self.downText.set('')
        self.rightText.set('')
        self.leftText.set('')
        self.oneText.set('')
        self.twoText.set('')
        self.threeText.set('')
        self.fourText.set('')
        self.fiveText.set('')
        self.sixText.set('')
        self.sevenText.set('')
        self.eightText.set('')
        self.nineText.set('')
        self.zeroText.set('')
        self.shiftText.set('')
        self.controlText.set('')
        self.macroOneText.set('')
        self.macroTwoText.set('')
        self.macroThreeText.set('')
        self.macroFourText.set('')
        self.actionOneText.set('')
        self.actionTwoText.set('')
        self.actionThreeText.set('')
        self.actionFourText.set('')
        self.actionFiveText.set('')
        self.actionSixText.set('')
        self.actionSevenText.set('')
        self.actionEightText.set('')
        self.macroOneTimerOne.set('0')
        self.macroTwoTimerOne.set('0')
        self.macroThreeTimerOne.set('0')
        self.macroFourTimerOne.set('0')
        self.macroOneTimerTwo.set('0')
        self.macroTwoTimerTwo.set('0')
        self.macroThreeTimerTwo.set('0')
        self.macroFourTimerTwo.set('0')
        self.upKeyValue.set('0')
        self.downKeyValue.set('0')
        self.leftKeyValue.set('0')
        self.rightKeyValue.set('0')
        self.enterKeyValue.set('0')
        self.controlKeyValue.set('0')
        self.spaceKeyValue.set('0')
        self.shiftKeyValue.set('0')
        self.oneKeyValue.set('0')
        self.twoKeyValue.set('0')
        self.threeKeyValue.set('0')
        self.fourKeyValue.set('0')
        self.fiveKeyValue.set('0')
        self.sixKeyValue.set('0')
        self.sevenKeyValue.set('0')
        self.eightKeyValue.set('0')
        self.nineKeyValue.set('0')
        self.zeroKeyValue.set('0')
        self.actionOneKeyValue.set('0')
        self.actionTwoKeyValue.set('0')
        self.actionThreeKeyValue.set('0')
        self.actionFourKeyValue.set('0')
        self.actionFiveKeyValue.set('0')
        self.actionSixKeyValue.set('0')
        self.actionSevenKeyValue.set('0')
        self.actionEightKeyValue.set('0')
        self.macroOneKeyValueOne.set('0')
        self.macroTwoKeyValueOne.set('0')
        self.macroThreeKeyValueOne.set('0')
        self.macroFourKeyValueOne.set('0')
        self.macroOneKeyValueTwo.set('0')
        self.macroTwoKeyValueTwo.set('0')
        self.macroThreeKeyValueTwo.set('0')
        self.macroFourKeyValueTwo.set('0')
        displayUpEntry.delete(0, END)
        displayDownEntry.delete(0, END)
        displayRightEntry.delete(0, END)
        displayLeftEntry.delete(0, END)
        displayShiftEntry.delete(0, END)
        displayControlEntry.delete(0, END)
        displaySpaceEntry.delete(0, END)
        displayEnterEntry.delete(0, END)
        displayActionOneEntry.delete(0, END)
        displayActionTwoEntry.delete(0, END)
        displayActionThreeEntry.delete(0, END)
        displayActionFourEntry.delete(0, END)
        displayActionFiveEntry.delete(0, END)
        displayActionSixEntry.delete(0, END)
        displayActionSevenEntry.delete(0, END)
        displayActionEightEntry.delete(0, END)
        displayOneEntry.delete(0, END)
        displayTwoEntry.delete(0, END)
        displayThreeEntry.delete(0, END)
        displayFourEntry.delete(0, END)
        displayFiveEntry.delete(0, END)
        displaySixEntry.delete(0, END)
        displaySevenEntry.delete(0, END)
        displayEightEntry.delete(0, END)
        displayNineEntry.delete(0, END)
        displayZeroEntry.delete(0, END)
        displayMacroOneEntry.delete(0, END)
        displayMacroOneEntryTimerOne.delete(0, END)
        displayMacroOneEntryTimerTwo.delete(0, END)
        displayMacroOneEntryTimerOne.insert(END, '0')
        displayMacroOneEntryTimerTwo.insert(END, '0')
        displayMacroTwoEntry.delete(0, END)
        displayMacroTwoEntryTimerOne.delete(0, END)
        displayMacroTwoEntryTimerTwo.delete(0, END)
        displayMacroTwoEntryTimerOne.insert(END, '0')
        displayMacroTwoEntryTimerTwo.insert(END, '0')
        displayMacroThreeEntry.delete(0, END)
        displayMacroThreeEntryTimerOne.delete(0, END)
        displayMacroThreeEntryTimerTwo.delete(0, END)
        displayMacroThreeEntryTimerOne.insert(END, '0')
        displayMacroThreeEntryTimerTwo.insert(END, '0')
        displayMacroFourEntry.delete(0, END)
        displayMacroFourEntryTimerOne.delete(0, END)
        displayMacroFourEntryTimerTwo.delete(0, END)
        displayMacroFourEntryTimerOne.insert(END, '0')
        displayMacroFourEntryTimerTwo.insert(END, '0')
        upKey.current(0)
        downKey.current(0)
        leftKey.current(0)
        rightKey.current(0)
        enterKey.current(0)
        controlKey.current(0)
        spaceKey.current(0)
        shiftKey.current(0)
        oneKey.current(0)
        twoKey.current(0)
        threeKey.current(0)
        fourKey.current(0)
        fiveKey.current(0)
        sixKey.current(0)
        sevenKey.current(0)
        eightKey.current(0)
        nineKey.current(0)
        zeroKey.current(0)
        actionOneKey.current(0)
        actionTwoKey.current(0)
        actionThreeKey.current(0)
        actionFourKey.current(0)
        actionFiveKey.current(0)
        actionSixKey.current(0)
        actionSevenKey.current(0)
        actionEightKey.current(0)
        macroOneKeyOne.current(0)
        macroTwoKeyOne.current(0)
        macroThreeKeyOne.current(0)
        macroFourKeyOne.current(0)
        macroOneKeyTwo.current(0)
        macroTwoKeyTwo.current(0)
        macroThreeKeyTwo.current(0)
        macroFourKeyTwo.current(0)





class ScreenManage():
    startXGet = ''
    endXGet = ''
    startYGet = ''
    endYGet = ''
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
        ScreenXStartEntry.insert(END, self.startX.get())
        ScreenXEndEntry.insert(END, self.endX.get())
        ScreenYStartEntry.insert(END, self.startY.get())
        ScreenYEndEntry.insert(END, self.endY.get())

class backgroundInfo():
    previousTab = 0
    TWITCH_CHANNEL = ''
    STREAMING_ON_TWITCH = False
    YOUTUBE_STREAM_URL = None
    YOUTUBE_CHANNEL_ID = ''
    twitchActive = False
    youtubeActive = False
    backMessageFour = ''
    backMessageThree = ''
    backMessageTwo = ''
    backMessageOne = ''
    t = ''
    t1 = None
    gamesetting = 0
    def backTrackAccount(self):
        backgroundInfo.previousTab -= 1
        backgroundInfo.TWITCH_CHANNEL = ''
        backgroundInfo.STREAMING_ON_TWITCH = False
        backgroundInfo.YOUTUBE_CHANNEL_ID = ''
        backgroundInfo.YOUTUBE_STREAM_URL = None
        backgroundInfo.twitchActive = False
        backgroundInfo.youtubeActive = False
        backgroundInfo.gamesetting = 0
        platform.destroy()


    def updateMessage(self):
        messageRelayOne.config(text=TextToAction.TTAFour)
        messageRelayTwo.config(text=TextToAction.TTAThree)
        messageRelayThree.config(text=TextToAction.TTATwo)
        messageRelayFour.config(text=TextToAction.TTAOne)
        #start.after(1, updateMessage)


    def updateClear(self):
        TextToAction.TTAFour = ''
        TextToAction.TTAThree = ''
        TextToAction.TTATwo = ''
        TextToAction.TTAOne = ''
        #start.after(1, updateClear)


    def backTrackPlatform(self):
        backgroundInfo.previousTab -= 1
        game.destroy()


    def minecraftSetting(self):
        backgroundInfo.gamesetting = 0
        backgroundInfo.previousTab = 3
        game.destroy()

    def customSetting(self):
        backgroundInfo.gamesetting = 99
        backgroundInfo.previousTab = 3
        game.destroy()


    def endProgram(self):
        backgroundInfo.t=''
        if(backgroundInfo.t == ''):
            backgroundInfo.updateClear(self)
        backgroundInfo.previousTab -= 1
        startButton["state"] = ACTIVE
        GreenScreen.greenScreenCls = False
        start.destroy()

    def twitch_Button(self):
        backgroundInfo.previousTab = 1
        backgroundInfo.twitchActive = True
        web.destroy()

    def youtube_Button(self):
        backgroundInfo.previousTab = 1
        backgroundInfo.youtubeActive = True
        web.destroy()

    def start_close_window(self):
        #thread()
        GreenScreen.greenScreenCls = False
        start.destroy()
        exit()

    def platform_close_window(self):
        platform.destroy()
        exit()

    def game_close_window(self):
        game.destroy()
        exit()

    def web_close_window(self):
        web.destroy()
        exit()

    def WebSite(self):
        # Replace this with your Twitch username. Must be all lowercase.
        backgroundInfo.TWITCH_CHANNEL = ''
        backgroundInfo.STREAMING_ON_TWITCH =  False
        backgroundInfo.YOUTUBE_CHANNEL_ID = ''
        backgroundInfo.YOUTUBE_STREAM_URL = None
        if(backgroundInfo.youtubeActive == True):
            usernameAccess = username.get()
            channelURL = youtubeURL.get()
        if(backgroundInfo.twitchActive == True):
            usernameAccess = username.get()
        if(backgroundInfo.twitchActive == True):
            backgroundInfo.TWITCH_CHANNEL = usernameAccess

            # If streaming on Youtube, set this to False
            backgroundInfo.STREAMING_ON_TWITCH = backgroundInfo.twitchActive

        # If you're streaming on Youtube, replace this with your Youtube's Channel ID
        # Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
        if(backgroundInfo.youtubeActive == True):
            backgroundInfo.YOUTUBE_CHANNEL_ID = usernameAccess

            # If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
            # Otherwise you can leave this as "None"
            backgroundInfo.YOUTUBE_STREAM_URL = channelURL
        if(backgroundInfo.YOUTUBE_CHANNEL_ID != None and backgroundInfo.youtubeActive == True):
            if(usernameAccess != '' and channelURL !=  ''):
                backgroundInfo.previousTab = 2
                platform.destroy()
        if(backgroundInfo.STREAMING_ON_TWITCH == True and backgroundInfo.twitchActive == True):
            if(usernameAccess != ''):
                backgroundInfo.previousTab = 2
                platform.destroy()

        ##################### MESSAGE QUEUE VARIABLES #####################

    def thread(self):
        backgroundInfo.t1 = threading.Thread(target=Program)
        if (backgroundInfo.t1.is_alive() != True):
            startButton["state"] = DISABLED
            endButton["state"] = DISABLED
            startButton['bg'] = 'light yellow'
            backgroundInfo.t1.start()
        else:
            backgroundInfo.t1.join()

class TextToAction():
    TTAOne = ''
    TTATwo = ''
    TTAThree = ''
    TTAFour = ''
    def handle_message(self, message):
        controller = ControlManage()

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
            TextToAction.TTAFour = (TextToAction.TTAThree)
            TextToAction.TTAThree = (TextToAction.TTATwo)
            TextToAction.TTATwo = (TextToAction.TTAOne)
            TextToAction.TTAOne = "Got this message from " + username + ": " + msg
            start.after(1000, sendUpdateMessage)
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
            if(backgroundInfo.gamesetting == 0 and backgroundInfo.previousTab == 3):
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

            if (backgroundInfo.gamesetting == 99 and backgroundInfo.previousTab == 3):
                if(msg.lower() == upButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    upButton['bg'] = 'red'
                    keyboard.press(controller.upKeyCls)
                    keyboard.release(controller.upKeyCls)
                    time.sleep(1)
                    upButton['bg'] = '#f0f0f0'

                elif (msg.lower() == downButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    downButton['bg'] = 'red'
                    keyboard.press(controller.downKeyCls)
                    keyboard.release(controller.downKeyCls)
                    time.sleep(1)
                    downButton['bg'] = '#f0f0f0'

                elif (msg.lower() == rightButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    rightButton['bg'] = 'red'
                    keyboard.press(controller.rightKeyCls)
                    keyboard.release(controller.rightKeyCls)
                    time.sleep(1)
                    rightButton['bg'] = '#f0f0f0'

                elif (msg.lower() == leftButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    leftButton['bg'] = 'red'
                    keyboard.press(controller.leftKeyCls)
                    keyboard.release(controller.leftKeyCls)
                    time.sleep(1)
                    leftButton['bg'] = '#f0f0f0'

                elif (msg.lower() == oneButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    oneButton['bg'] = 'red'
                    keyboard.press(controller.oneKeyCls)
                    keyboard.release(controller.oneKeyCls)
                    time.sleep(1)
                    oneButton['bg'] = '#f0f0f0'

                elif (msg.lower() == twoButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    twoButton['bg'] = 'red'
                    keyboard.press(controller.twoKeyCls)
                    keyboard.release(controller.twoKeyCls)
                    time.sleep(1)
                    twoButton['bg'] = '#f0f0f0'

                elif (msg.lower() == threeButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    threeButton['bg'] = 'red'
                    keyboard.press(controller.threeKeyCls)
                    keyboard.release(controller.threeKeyCls)
                    time.sleep(1)
                    threeButton['bg'] = '#f0f0f0'

                elif (msg.lower() == fourButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    fourButton['bg'] = 'red'
                    keyboard.press(controller.fourKeyCls)
                    keyboard.release(controller.fourKeyCls)
                    time.sleep(1)
                    fourButton['bg'] = '#f0f0f0'

                elif (msg.lower() == fiveButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    fiveButton['bg'] = 'red'
                    keyboard.press(controller.fiveKeyCls)
                    keyboard.release(controller.fiveKeyCls)
                    time.sleep(1)
                    fiveButton['bg'] = '#f0f0f0'

                elif (msg.lower() == sixButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    sixButton['bg'] = 'red'
                    keyboard.press(controller.sixKeyCls)
                    keyboard.release(controller.sixKeyCls)
                    time.sleep(1)
                    sixButton['bg'] = '#f0f0f0'

                elif (msg.lower() == sevenButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    sevenButton['bg'] = 'red'
                    keyboard.press(controller.sixKeyCls)
                    keyboard.release(controller.sixKeyCls)
                    time.sleep(1)
                    sevenButton['bg'] = '#f0f0f0'

                elif (msg.lower() == sevenButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    sevenButton['bg'] = 'red'
                    keyboard.press(controller.sevenKeyCls)
                    keyboard.release(controller.sevenKeyCls)
                    time.sleep(1)
                    sevenButton['bg'] = '#f0f0f0'

                elif (msg.lower() == eightButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    eightButton['bg'] = 'red'
                    keyboard.press(controller.eightKeyCls)
                    keyboard.release(controller.eightKeyCls)
                    time.sleep(1)
                    eightButton['bg'] = '#f0f0f0'

                elif (msg.lower() == nineButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    nineButton['bg'] = 'red'
                    keyboard.press(controller.nineKeyCls)
                    keyboard.release(controller.nineKeyCls)
                    time.sleep(1)
                    nineButton['bg'] = '#f0f0f0'

                elif (msg.lower() == zeroButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    zeroButton['bg'] = 'red'
                    keyboard.press(controller.zeroKeyCls)
                    keyboard.release(controller.zeroKeyCls)
                    time.sleep(1)
                    zeroButton['bg'] = '#f0f0f0'

                elif (msg.lower() == shiftButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    shiftButton['bg'] = 'red'
                    keyboard.press(controller.shiftKeyCls)
                    keyboard.release(controller.shiftKeyCls)
                    time.sleep(1)
                    shiftButton['bg'] = '#f0f0f0'

                elif (msg.lower() == controlButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    controlButton['bg'] = 'red'
                    keyboard.press(controller.controlKeyCls)
                    keyboard.release(controller.controlKeyCls)
                    time.sleep(1)
                    controlButton['bg'] = '#f0f0f0'

                elif (msg.lower() == enterButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    enterButton['bg'] = 'red'
                    keyboard.press(controller.enterKeyCls)
                    keyboard.release(controller.enterKeyCls)
                    time.sleep(1)
                    enterButton['bg'] = '#f0f0f0'

                elif (msg.lower() == spaceButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    spaceButton['bg'] = 'red'
                    keyboard.press(controller.spaceKeyCls)
                    keyboard.release(controller.spaceKeyCls)
                    time.sleep(1)
                    spaceButton['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonOne['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonOne['bg'] = 'red'
                    keyboard.press(controller.actionOneKeyCls)
                    keyboard.release(controller.actionOneKeyCls)
                    time.sleep(1)
                    actionButtonOne['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonTwo['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonTwo['bg'] = 'red'
                    keyboard.press(controller.actionTwoKeyCls)
                    keyboard.release(controller.actionTwoKeyCls)
                    time.sleep(1)
                    actionButtonTwo['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonThree['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonThree['bg'] = 'red'
                    keyboard.press(controller.actionThreeKeyCls)
                    keyboard.release(controller.actionThreeKeyCls)
                    time.sleep(1)
                    actionButtonThree['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonFour['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonFour['bg'] = 'red'
                    keyboard.press(controller.actionFourKeyCls)
                    keyboard.release(controller.actionFourKeyCls)
                    time.sleep(1)
                    actionButtonFour['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonFive['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonFive['bg'] = 'red'
                    keyboard.press(controller.actionFiveKeyCls)
                    keyboard.release(controller.actionFiveKeyCls)
                    time.sleep(1)
                    actionButtonFive['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonSix['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonSix['bg'] = 'red'
                    keyboard.press(controller.actionSixKeyCls)
                    keyboard.release(controller.actionSixKeyCls)
                    time.sleep(1)
                    actionButtonSix['bg'] = '#f0f0f0'

                if (msg.lower() == actionButtonSeven['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonSeven['bg'] = 'red'
                    keyboard.press(controller.actionSevenKeyCls)
                    keyboard.release(controller.actionSevenKeyCls)
                    time.sleep(1)
                    actionButtonSeven['bg'] = '#f0f0f0'

                elif (msg.lower() == actionButtonEight['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    actionButtonEight['bg'] = 'red'
                    keyboard.press(controller.actionEightKeyCls)
                    keyboard.release(controller.actionEightKeyCls)
                    time.sleep(1)
                    actionButtonEight['bg'] = '#f0f0f0'

                elif (msg.lower() == macroOneButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    macroOneButton['bg'] = 'red'
                    keyboard.press(controller.macroOneKeyOneCls)
                    time.sleep(int(controller.macroOneTimerOneCls))
                    keyboard.press(controller.macroOneKeyTwoCls)
                    keyboard.release(controller.macroOneKeyOneCls)
                    time.sleep(int(controller.macroOneTimerTwoCls))
                    keyboard.release(controller.macroOneKeyTwoCls)
                    macroOneButton['bg'] = '#f0f0f0'

                elif (msg.lower() == macroTwoButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    macroTwoButton['bg'] = 'red'
                    keyboard.press(controller.macroTwoKeyOneCls)
                    time.sleep(int(controller.macroTwoTimerOneCls))
                    keyboard.press(controller.macroTwoKeyTwoCls)
                    keyboard.release(controller.macroTwoKeyOneCls)
                    time.sleep(int(controller.macroTwoTimerTwoCls))
                    keyboard.release(controller.macroTwoKeyTwoCls)
                    macroTwoButton['bg'] = '#f0f0f0'

                elif (msg.lower() == macroThreeButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    macroThreeButton['bg'] = 'red'
                    keyboard.press(controller.macroThreeKeyOneCls)
                    time.sleep(int(controller.macroThreeTimerOneCls))
                    keyboard.press(controller.macroThreeKeyTwoCls)
                    keyboard.release(controller.macroThreeKeyOneCls)
                    time.sleep(int(controller.macroThreeTimerTwoCls))
                    keyboard.release(controller.macroThreeKeyTwoCls)
                    macroThreeButton['bg'] = '#f0f0f0'

                elif (msg.lower() == macroFourButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    macroFourButton['bg'] = 'red'
                    keyboard.press(controller.macroFourKeyOneCls)
                    time.sleep(int(controller.macroFourTimerOneCls))
                    keyboard.press(controller.macroFourKeyTwoCls)
                    keyboard.release(controller.macroFourKeyOneCls)
                    time.sleep(int(controller.macroFourTimerTwoCls))
                    keyboard.release(controller.macroFourKeyTwoCls)
                    macroFourButton['bg'] = '#f0f0f0'

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
                elif(msg.lower() == 'lc' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    mouse.release("left")
                    time.sleep(1)
                    mouseLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'rc' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    mouseRightButton['bg'] = 'red'
                    mouse.press("right")
                    mouse.release("right")
                    time.sleep(1)
                    mouseRightButton['bg'] = '#f0f0f0'


            ####################################
            ####################################

        except Exception as e:
            print("Encountered exception: " + str(e))







##################### GAME VARIABLES #####################

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
        if (backgroundInfo.STREAMING_ON_TWITCH and backgroundInfo.previousTab == 3):
            backgroundInfo.t = TwitchPlays_Connection.Twitch()
            backgroundInfo.t.twitch_connect(backgroundInfo.TWITCH_CHANNEL)
            messageRelayConnect.config(text='Connected To Twitch')
        elif(backgroundInfo.previousTab == 3):
            backgroundInfo.t = TwitchPlays_Connection.YouTube()
            backgroundInfo.t.youtube_connect(backgroundInfo.YOUTUBE_CHANNEL_ID, backgroundInfo.YOUTUBE_STREAM_URL)
            messageRelayConnect.config(text='Connected To Youtube')
        endButton["state"] = ACTIVE
        startButton['bg'] = 'light green'
    except Exception as e:
        messageRelayConnect.config(text='Error: Unable to connect to a platform. Check login details...')
        endButton["state"] = ACTIVE
        startButton['bg'] = 'red'

    while(True):
        t = backgroundInfo.t
        active_tasks = [t for t in active_tasks if not t.done()]

        #Check for new messages
        new_messages = t.twitch_receive_messages()
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
                    active_tasks.append(thread_pool.submit(handleMessaging, message))
                else:
                    print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')



sendInfo = backgroundInfo()
sendTwitch = sendInfo.twitch_Button
sendYoutube = sendInfo.youtube_Button
sendClose = sendInfo.web_close_window
sendWebSite = sendInfo.WebSite
sendBackTrackAccount = sendInfo.backTrackAccount
sendBackTrackPlatform = sendInfo.backTrackPlatform
sendPlatformClose = sendInfo.platform_close_window
sendMinecraftSetting = sendInfo.minecraftSetting
sendCustomSetting = sendInfo.customSetting
sendGameClose = sendInfo.game_close_window
sendThread = sendInfo.thread
sendProgram = sendInfo.endProgram
sendStartClose = sendInfo.start_close_window
sendUpdateMessage = sendInfo.updateMessage
greenScreenMode = GreenScreen()
GSMode = greenScreenMode.greenScreenChange
while(backgroundInfo.previousTab == 0):
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
    twitchButton = Button(web,height = 140, width = 100, text="Twitch",font = ("Arial", 12), image= twitchResize,compound = TOP, command = sendTwitch)
    youtubeButton = Button(web,height = 140, width = 100, text="Youtube",font = ("Arial", 12), image= youtubeResize,compound = TOP, command= sendYoutube)
    thanks = Label(web, text="Original code by Wituz, updated by DDarknut, DougDoug, Ottomated. Further expanded by Bloop",
                        bg = "white",
                        fg = "black",
                        font = ("Arial", 7))


    web.protocol("WM_DELETE_WINDOW", sendClose)
    webText.place(x=155, y=50)
    twitchButton.place(x=120, y=100)
    youtubeButton.place(x=285, y=100)
    thanks.place(x=0, y=330)
    web.mainloop()
    while(backgroundInfo.previousTab == 1):
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
        if(backgroundInfo.twitchActive == True):
            webText = Label(platform, text="Enter Your Twitch Username",
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
            username = Entry(platform, text = "Username..", width = 53)
            username.place(x=25, y=50)
            webText.place(x=5, y=20)
        if(backgroundInfo.youtubeActive == True):
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
        nextButton = Button(platform, text="Next",height = 2, width = 5, command = sendWebSite)
        nextButton.place(x=460, y = 290)
        backButton = Button(platform, text="Back",height = 2, width = 5, command = sendBackTrackAccount)
        backButton.place(x=15, y = 290)
        platform.protocol("WM_DELETE_WINDOW", sendPlatformClose)
        platform.mainloop()
        while(backgroundInfo.previousTab == 2):
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

            minecraftButton = Button(game, text="Minecraft",height = 2, width = 7, command = sendMinecraftSetting)
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

            customButton = Button(game, text="Custom",height = 2, width = 7, command = sendCustomSetting)
            customButton.place(x=375, y = 200)

            backButton = Button(game, text="Back",height = 2, width = 5, command = sendBackTrackPlatform)
            backButton.place(x=15, y = 290)

            game.protocol("WM_DELETE_WINDOW", sendGameClose)
            game.mainloop()

            while(backgroundInfo.previousTab == 3):
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


                messageRelayOne = Label(start, text=TextToAction.TTAOne,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
                messageRelayTwo = Label(start, text=TextToAction.TTATwo,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
                messageRelayThree = Label(start, text=TextToAction.TTAThree,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
                messageRelayFour = Label(start, text=TextToAction.TTAFour,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))

                messageRelayConnect = Label(start, text='',
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 13),
                    anchor="center")


                startButton = Button(start, text="Start",height = 2, width = 5, command = sendThread)
                startButton.place(x=225, y = 280)
                endButton = Button(start, text="End",height = 2, width = 5, command = sendProgram)
                endButton.place(x=275, y = 280)

                if(backgroundInfo.gamesetting == 0):
                    upButton = Button(start, text="Up", height=1, width=4, state=DISABLED)
                    DownButton = Button(start, text="Down", height=1, width=4, state=DISABLED)
                    LeftButton = Button(start, text="Left", height=1, width=4, state=DISABLED)
                    RightButton = Button(start, text="Right", height=1, width=4, state=DISABLED)
                    upButton.place(x=60, y=145)
                    DownButton.place(x=60, y=175)
                    LeftButton.place(x=20, y=175)
                    RightButton.place(x=100, y=175)

                    secHandButton = Button(start, text="Swap", height=1, width=4, state=DISABLED)
                    secHandButton.place(x=160, y=110)

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
                    spaceButton.place(x=160, y=175)

                    shiftButton = Button(start, text="Shift", height=1, width=5, state=DISABLED)
                    shiftButton.place(x=327, y=175)

                    dropButton = Button(start, text="Drop", height=1, width=4, state=DISABLED)
                    dropButton.place(x=20, y=110)

                    InvButton = Button(start, text="Inv", height=1, width=4, state=DISABLED)
                    InvButton.place(x=100, y=110)

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

                if(backgroundInfo.gamesetting == 99):
                    start.minsize(600, 350)
                    start.maxsize(600, 350)
                    controlManager = ControlManage()
                    controlFunction = partial(controlManager.controlOption, start)

                    options.add_command(label='Controls', command= controlFunction)

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

                options.add_command(label='GS Mode', command=GSMode)
                messageRelayOne.place(x= 5, y=200)
                messageRelayTwo.place(x= 5, y=220)
                messageRelayThree.place(x= 5, y=240)
                messageRelayFour.place(x= 5, y=260)
                messageRelayConnect.place(x=20, y=5)
                start.protocol("WM_DELETE_WINDOW", sendStartClose)
                start.config(menu=menubar)
                start.mainloop()
exit()
