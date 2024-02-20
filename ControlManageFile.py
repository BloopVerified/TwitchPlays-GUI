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
    mimicControlBox = ''
    controlOptBackUp = None
    switchControl = False
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
        self.keyOptions = ('none','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0','[', ']','\\','-','+',';','\'','`',',','.','/','del','ctrl','alt','spacebar','enter','shift','up','down','right','left')

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


    def controlOption(self, start, upButton, downButton, rightButton, leftButton, oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton, zeroButton, shiftButton, controlButton, enterButton, spaceButton, actionButtonOne, actionButtonTwo, actionButtonThree, actionButtonFour, actionButtonFive, actionButtonSix, actionButtonSeven, actionButtonEight, macroOneButton, macroTwoButton, macroThreeButton, macroFourButton, mouseMoveRightButton, mouseMoveLeftButton, mouseMoveUpButton, mouseMoveDownButton, mouseLeftButton, mouseRightButton):
        controlOpt = mtTkinter.Toplevel(start)
        ControlManage.controlOptBackUp = controlOpt
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
        displayUpEntry = Entry(controlOpt, width=12)
        displayUpEntry.place(x=95, y=60)
        upKey = Combobox(controlOpt, width= 10, values = self.keyOptions)
        upKey.place(x=195, y=60)

#Down Key
        displayDown = Label(controlOpt, text="down:",
                        bg="white",
                        fg="black",
                        font=("Arial", 9))
        displayDown.place(x=310, y=60)
        displayDownEntry = Entry(controlOpt, width=12)
        displayDownEntry.place(x=365, y=60)
        downKey = Combobox(controlOpt, width=10, values=self.keyOptions)
        downKey.place(x=465, y=60)

# Left Key
        displayLeft = Label(controlOpt, text="left:",
                            bg="white",
                            fg="black",
                            font=("Arial", 9))
        displayLeft.place(x=40, y=85)
        displayLeftEntry = Entry(controlOpt, width=12)
        displayLeftEntry.place(x=95, y=85)
        leftKey = Combobox(controlOpt, width=10, values=self.keyOptions)
        leftKey.place(x=195, y=85)

# Right Key
        displayRight = Label(controlOpt, text="right:",
                             bg="white",
                             fg="black",
                             font=("Arial", 9))
        displayRight.place(x=310, y=85)
        displayRightEntry = Entry(controlOpt, width=12)
        displayRightEntry.place(x=365, y=85)
        rightKey = Combobox(controlOpt, width=10, values=self.keyOptions)
        rightKey.place(x=465, y=85)

# Shift Key
        displayShift = Label(controlOpt, text="shift:",
                             bg="white",
                             fg="black",
                             font=("Arial", 9))
        displayShift.place(x=40, y=110)
        displayShiftEntry = Entry(controlOpt, width=12)
        displayShiftEntry.place(x=95, y=110)
        shiftKey = Combobox(controlOpt, width=10, values=self.keyOptions)
        shiftKey.place(x=195, y=110)

# Control Key
        displayControl = Label(controlOpt, text="control:",
                               bg="white",
                               fg="black",
                               font=("Arial", 9))
        displayControl.place(x=310, y=110)
        displayControlEntry = Entry(controlOpt, width=12)
        displayControlEntry.place(x=365, y=110)
        controlKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        controlKey.place(x=465, y=110)

# Space Key
        displaySpace = Label(controlOpt, text="space:",
                               bg="white",
                               fg="black",
                               font=("Arial", 9))
        displaySpace.place(x=40, y=135)
        displaySpaceEntry = Entry(controlOpt, width=12)
        displaySpaceEntry.place(x=95, y=135)
        spaceKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        spaceKey.place(x=195, y=135)

# Enter Key
        displayEnter = Label(controlOpt, text="enter:",
                               bg="white",
                               fg="black",
                               font=("Arial", 9))
        displayEnter.place(x=310, y=135)
        displayEnterEntry = Entry(controlOpt, width=12)
        displayEnterEntry.place(x=365, y=135)
        enterKey = Combobox(controlOpt, width=10,values=self.keyOptions)
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
        displayActionOneEntry = Entry(controlOpt, width=12)
        displayActionOneEntry.place(x=95, y=190)
        actionOneKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        actionOneKey.place(x=195, y=190)

# Action Two Key
        displayActionTwo = Label(controlOpt, text="Action 2:",
                                 bg="white",
                                 fg="black",
                                 font=("Arial", 9))
        displayActionTwo.place(x=40, y=215)
        displayActionTwoEntry = Entry(controlOpt, width=12)
        displayActionTwoEntry.place(x=95, y=215)
        actionTwoKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        actionTwoKey.place(x=195, y=215)

# Action Three Key
        displayActionThree = Label(controlOpt, text="Action 3:",
                                   bg="white",
                                   fg="black",
                                   font=("Arial", 9))
        displayActionThree.place(x=40, y=240)
        displayActionThreeEntry = Entry(controlOpt, width=12)
        displayActionThreeEntry.place(x=95, y=240)
        actionThreeKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        actionThreeKey.place(x=195, y=240)

# Action Four Key
        displayActionFour = Label(controlOpt, text="Action 4:",
                                  bg="white",
                                  fg="black",
                                  font=("Arial", 9))
        displayActionFour.place(x=40, y=265)
        displayActionFourEntry = Entry(controlOpt, width=12)
        displayActionFourEntry.place(x=95, y=265)
        actionFourKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        actionFourKey.place(x=195, y=265)

# Action Five Key
        displayActionFive = Label(controlOpt, text="Action 5:",
                                  bg="white",
                                  fg="black",
                                  font=("Arial", 9))
        displayActionFive.place(x=310, y=190)
        displayActionFiveEntry = Entry(controlOpt, width=12)
        displayActionFiveEntry.place(x=365, y=190)
        actionFiveKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        actionFiveKey.place(x=465, y=190)

# Action Six Key
        displayActionSix = Label(controlOpt, text="Action 6:",
                                 bg="white",
                                 fg="black",
                                 font=("Arial", 9))
        displayActionSix.place(x=310, y=215)
        displayActionSixEntry = Entry(controlOpt, width=12)
        displayActionSixEntry.place(x=365, y=215)
        actionSixKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        actionSixKey.place(x=465, y=215)

# Action Seven Key
        displayActionSeven = Label(controlOpt, text="Action 7:",
                                   bg="white",
                                   fg="black",
                                   font=("Arial", 9))
        displayActionSeven.place(x=310, y=240)
        displayActionSevenEntry = Entry(controlOpt, width=12)
        displayActionSevenEntry.place(x=365, y=240)
        actionSevenKey = Combobox(controlOpt, width=10, values=self.keyOptions)
        actionSevenKey.place(x=465, y=240)

# Action Eight Key
        displayActionEight = Label(controlOpt, text="Action 8:",
                                   bg="white",
                                   fg="black",
                                   font=("Arial", 9))
        displayActionEight.place(x=310, y=265)
        displayActionEightEntry = Entry(controlOpt, width=12)
        displayActionEightEntry.place(x=365, y=265)
        actionEightKey = Combobox(controlOpt, width=10,values=self.keyOptions)
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
        displayOneEntry = Entry(controlOpt, width=12)
        displayOneEntry.place(x=95, y=315)
        oneKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        oneKey.place(x=195, y=315)

# Two Key
        displayTwo = Label(controlOpt, text="two:",
                           bg="white",
                           fg="black",
                           font=("Arial", 9))
        displayTwo.place(x=40, y=340)
        displayTwoEntry = Entry(controlOpt, width=12)
        displayTwoEntry.place(x=95, y=340)
        twoKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        twoKey.place(x=195, y=340)

# Three Key
        displayThree = Label(controlOpt, text="three:",
                             bg="white",
                             fg="black",
                             font=("Arial", 9))
        displayThree.place(x=40, y=365)
        displayThreeEntry = Entry(controlOpt, width=12)
        displayThreeEntry.place(x=95, y=365)
        threeKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        threeKey.place(x=195, y=365)

# Four Key
        displayFour = Label(controlOpt, text="four:",
                            bg="white",
                            fg="black",
                            font=("Arial", 9))
        displayFour.place(x=40, y=390)
        displayFourEntry = Entry(controlOpt, width=12)
        displayFourEntry.place(x=95, y=390)
        fourKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        fourKey.place(x=195, y=390)

# Five Key
        displayFive = Label(controlOpt, text="five:",
                            bg="white",
                            fg="black",
                            font=("Arial", 9))
        displayFive.place(x=40, y=415)
        displayFiveEntry = Entry(controlOpt, width=12)
        displayFiveEntry.place(x=95, y=415)
        fiveKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        fiveKey.place(x=195, y=415)

# Six Key
        displaySix = Label(controlOpt, text="six:",
                           bg="white",
                           fg="black",
                           font=("Arial", 9))
        displaySix.place(x=310, y=315)
        displaySixEntry = Entry(controlOpt, width=12)
        displaySixEntry.place(x=365, y=315)
        sixKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        sixKey.place(x=465, y=315)

# Seven Key
        displaySeven = Label(controlOpt, text="seven:",
                             bg="white",
                             fg="black",
                             font=("Arial", 9))
        displaySeven.place(x=310, y=340)
        displaySevenEntry = Entry(controlOpt, width=12)
        displaySevenEntry.place(x=365, y=340)
        sevenKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        sevenKey.place(x=465, y=340)

# Eight Key
        displayEight = Label(controlOpt, text="eight:",
                             bg="white",
                             fg="black",
                             font=("Arial", 9))
        displayEight.place(x=310, y=365)
        displayEightEntry = Entry(controlOpt, width=12)
        displayEightEntry.place(x=365, y=365)
        eightKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        eightKey.place(x=465, y=365)

# Nine Key
        displayNine = Label(controlOpt, text="nine:",
                            bg="white",
                            fg="black",
                            font=("Arial", 9))
        displayNine.place(x=310, y=390)
        displayNineEntry = Entry(controlOpt, width=12)
        displayNineEntry.place(x=365, y=390)
        nineKey = Combobox(controlOpt, width=10,values=self.keyOptions)
        nineKey.place(x=465, y=390)

# Zero Key
        displayZero = Label(controlOpt, text="zero:",
                            bg="white",
                            fg="black",
                            font=("Arial", 9))
        displayZero.place(x=310, y=415)
        displayZeroEntry = Entry(controlOpt, width=12)
        displayZeroEntry.place(x=365, y=415)
        zeroKey = Combobox(controlOpt, width=10,values=self.keyOptions)
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
        displayMacroOneEntry = Entry(controlOpt, width=12)
        displayMacroOneEntry.place(x=95, y=490)
        macroOneKeyOne = Combobox(controlOpt, width=10,values=self.keyOptions)
        macroOneKeyOne.place(x=195, y=490)

        displayMacroOneEntryTimerOne = Entry(controlOpt, width=6)
        displayMacroOneEntryTimerOne.place(x=295, y=490)
        macroOneKeyTwo = Combobox(controlOpt, width=10,values=self.keyOptions)
        macroOneKeyTwo.place(x=355, y=490)
        displayMacroOneEntryTimerTwo = Entry(controlOpt, width=6)
        displayMacroOneEntryTimerTwo.place(x=455, y=490)

# MacroTwo Key
        displayMacroTwo = Label(controlOpt, text="Macro 2:",
                                bg="white",
                                fg="black",
                                font=("Arial", 9))
        displayMacroTwo.place(x=40, y=515)
        displayMacroTwoEntry = Entry(controlOpt, width=12)
        displayMacroTwoEntry.place(x=95, y=515)
        macroTwoKeyOne = Combobox(controlOpt, width=10,values=self.keyOptions)
        macroTwoKeyOne.place(x=195, y=515)

        displayMacroTwoEntryTimerOne = Entry(controlOpt, width=6)
        displayMacroTwoEntryTimerOne.place(x=295, y=515)
        macroTwoKeyTwo = Combobox(controlOpt, width=10,values=self.keyOptions)
        macroTwoKeyTwo.place(x=355, y=515)
        displayMacroTwoEntryTimerTwo = Entry(controlOpt, width=6)
        displayMacroTwoEntryTimerTwo.place(x=455, y=515)

# MacroThree Key
        displayMacroThree = Label(controlOpt, text="Macro 3:",
                                  bg="white",
                                  fg="black",
                                  font=("Arial", 9))
        displayMacroThree.place(x=40, y=540)
        displayMacroThreeEntry = Entry(controlOpt, width=12)
        displayMacroThreeEntry.place(x=95, y=540)
        macroThreeKeyOne = Combobox(controlOpt, width=10, values=self.keyOptions)
        macroThreeKeyOne.place(x=195, y=540)

        displayMacroThreeEntryTimerOne = Entry(controlOpt, width=6)
        displayMacroThreeEntryTimerOne.place(x=295, y=540)
        macroThreeKeyTwo = Combobox(controlOpt, width=10,values=self.keyOptions)
        macroThreeKeyTwo.place(x=355, y=540)
        displayMacroThreeEntryTimerTwo = Entry(controlOpt, width=6)
        displayMacroThreeEntryTimerTwo.place(x=455, y=540)

# MacroFour Key
        displayMacroFour = Label(controlOpt, text="Macro 4:",
                                 bg="white",
                                 fg="black",
                                 font=("Arial", 9))
        displayMacroFour.place(x=40, y=565)
        displayMacroFourEntry = Entry(controlOpt, width=12)
        displayMacroFourEntry.place(x=95, y=565)
        macroFourKeyOne = Combobox(controlOpt, width=10, values=self.keyOptions)
        macroFourKeyOne.place(x=195, y=565)

        displayMacroFourEntryTimerOne = Entry(controlOpt, width=6)
        displayMacroFourEntryTimerOne.place(x=295, y=565)
        macroFourKeyTwo = Combobox(controlOpt, width=10 ,values=self.keyOptions)
        macroFourKeyTwo.place(x=355, y=565)
        displayMacroFourEntryTimerTwo = Entry(controlOpt, width=6)
        displayMacroFourEntryTimerTwo.place(x=455, y=565)


        submitControl = partial(ControlManage.on_press, self, controlOpt, start, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo, upButton, downButton, rightButton, leftButton, oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton, zeroButton, shiftButton, controlButton, enterButton, spaceButton, actionButtonOne, actionButtonTwo, actionButtonThree, actionButtonFour, actionButtonFive, actionButtonSix, actionButtonSeven, actionButtonEight, macroOneButton, macroTwoButton, macroThreeButton, macroFourButton, mouseMoveRightButton, mouseMoveLeftButton, mouseMoveUpButton, mouseMoveDownButton, mouseLeftButton, mouseRightButton)
        submitButton = Button(controlOpt, text='Submit', command=submitControl)
        submitButton.place(x=250, y=610)
        clearControl = partial(ControlManage.clearKeyBinding, self, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo)
        clearButton = Button(controlOpt, text='Clear', command=clearControl)
        clearButton.place(x=310, y=610)
        controlOpt.after(1, self.updateKeyEntry, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo)
        closeControl = partial(ControlManage.closeControl_close_window, self, controlOpt)
        controlOpt.protocol("WM_DELETE_WINDOW", closeControl)
        startcloseControl = partial(ControlManage.alt_closeControl_close_window, self, controlOpt, start)
        start.protocol("WM_DELETE_WINDOW", startcloseControl)

    def updateKeyEntry(self, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo):
        displayUpEntry.delete(0, END)
        displayUpEntry.insert(END, self.upText.get())
        displayDownEntry.delete(0, END)
        displayDownEntry.insert(END, self.downText.get())
        displayRightEntry.delete(0, END)
        displayRightEntry.insert(END, self.rightText.get())
        displayLeftEntry.delete(0, END)
        displayLeftEntry.insert(END, self.leftText.get())
        displayShiftEntry.delete(0, END)
        displayShiftEntry.insert(END, self.shiftText.get())
        displayControlEntry.delete(0, END)
        displayControlEntry.insert(END, self.controlText.get())
        displaySpaceEntry.delete(0, END)
        displaySpaceEntry.insert(END, self.spaceText.get())
        displayEnterEntry.delete(0, END)
        displayEnterEntry.insert(END, self.enterText.get())
        displayActionOneEntry.delete(0, END)
        displayActionOneEntry.insert(END, self.actionOneText.get())
        displayActionTwoEntry.delete(0, END)
        displayActionTwoEntry.insert(END, self.actionTwoText.get())
        displayActionThreeEntry.delete(0, END)
        displayActionThreeEntry.insert(END, self.actionThreeText.get())
        displayActionFourEntry.delete(0, END)
        displayActionFourEntry.insert(END, self.actionFourText.get())
        displayActionFiveEntry.delete(0, END)
        displayActionFiveEntry.insert(END, self.actionFiveText.get())
        displayActionSixEntry.delete(0, END)
        displayActionSixEntry.insert(END, self.actionSixText.get())
        displayActionSevenEntry.delete(0, END)
        displayActionSevenEntry.insert(END, self.actionSevenText.get())
        displayActionEightEntry.delete(0, END)
        displayActionEightEntry.insert(END, self.actionEightText.get())
        displayOneEntry.delete(0, END)
        displayOneEntry.insert(END, self.oneText.get())
        displayTwoEntry.delete(0, END)
        displayTwoEntry.insert(END, self.twoText.get())
        displayThreeEntry.delete(0, END)
        displayThreeEntry.insert(END, self.threeText.get())
        displayFourEntry.delete(0, END)
        displayFourEntry.insert(END, self.fourText.get())
        displayFiveEntry.delete(0, END)
        displayFiveEntry.insert(END, self.fiveText.get())
        displaySixEntry.delete(0, END)
        displaySixEntry.insert(END, self.sixText.get())
        displaySevenEntry.delete(0, END)
        displaySevenEntry.insert(END, self.sevenText.get())
        displayEightEntry.delete(0, END)
        displayEightEntry.insert(END, self.eightText.get())
        displayNineEntry.delete(0, END)
        displayNineEntry.insert(END, self.nineText.get())
        displayZeroEntry.delete(0, END)
        displayZeroEntry.insert(END, self.zeroText.get())
        displayMacroOneEntry.delete(0, END)
        displayMacroOneEntry.insert(END, self.macroOneText.get())
        displayMacroOneEntryTimerOne.delete(0, END)
        displayMacroOneEntryTimerOne.insert(END, self.macroOneTimerOne.get())
        displayMacroOneEntryTimerTwo.delete(0, END)
        displayMacroOneEntryTimerTwo.insert(END, self.macroOneTimerTwo.get())
        displayMacroTwoEntry.delete(0, END)
        displayMacroTwoEntry.insert(END, self.macroTwoText.get())
        displayMacroTwoEntryTimerOne.delete(0, END)
        displayMacroTwoEntryTimerOne.insert(END, self.macroTwoTimerOne.get())
        displayMacroTwoEntryTimerTwo.delete(0, END)
        displayMacroTwoEntryTimerTwo.insert(END, self.macroTwoTimerTwo.get())
        displayMacroThreeEntry.delete(0, END)
        displayMacroThreeEntry.insert(END, self.macroThreeText.get())
        displayMacroThreeEntryTimerOne.delete(0, END)
        displayMacroThreeEntryTimerOne.insert(END, self.macroThreeTimerOne.get())
        displayMacroThreeEntryTimerTwo.delete(0, END)
        displayMacroThreeEntryTimerTwo.insert(END, self.macroThreeTimerTwo.get())
        displayMacroFourEntry.delete(0, END)
        displayMacroFourEntry.insert(END, self.macroFourText.get())
        displayMacroFourEntryTimerOne.delete(0, END)
        displayMacroFourEntryTimerOne.insert(END, self.macroFourTimerOne.get())
        displayMacroFourEntryTimerTwo.delete(0, END)
        displayMacroFourEntryTimerTwo.insert(END, self.macroFourTimerTwo.get())
        if self.upKeyValue.get() != 'none':
            upKey.current(self.upKeyValue.get())
        if self.downKeyValue.get() != 'none':
            downKey.current(self.downKeyValue.get())
        if self.leftKeyValue.get() != 'none':
            leftKey.current(self.leftKeyValue.get())
        if self.rightKeyValue.get() != 'none':
            rightKey.current(self.rightKeyValue.get())
        if self.shiftKeyValue.get() != 'none':
            shiftKey.current(self.shiftKeyValue.get())
        if self.controlKeyValue.get() != 'none':
            controlKey.current(self.controlKeyValue.get())
        if self.spaceKeyValue.get() != 'none':
            spaceKey.current(self.spaceKeyValue.get())
        if self.enterKeyValue.get() != 'none':
            enterKey.current(self.enterKeyValue.get())
        if self.actionOneKeyValue.get() != 'none':
            actionOneKey.current(self.actionOneKeyValue.get())
        if self.actionTwoKeyValue.get() != 'none':
            actionTwoKey.current(self.actionTwoKeyValue.get())
        if self.actionThreeKeyValue.get() != 'none':
            actionThreeKey.current(self.actionThreeKeyValue.get())
        if self.actionFourKeyValue.get() != 'none':
            actionFourKey.current(self.actionFourKeyValue.get())
        if self.actionFiveKeyValue.get() != 'none':
            actionFiveKey.current(self.actionFiveKeyValue.get())
        if self.actionSixKeyValue.get() != 'none':
            actionSixKey.current(self.actionSixKeyValue.get())
        if self.actionSevenKeyValue.get() != 'none':
            actionSevenKey.current(self.actionSevenKeyValue.get())
        if self.actionEightKeyValue.get() != 'none':
            actionEightKey.current(self.actionEightKeyValue.get())
        if self.oneKeyValue.get() != 'none':
            oneKey.current(self.oneKeyValue.get())
        if self.twoKeyValue.get() != 'none':
            twoKey.current(self.twoKeyValue.get())
        if self.threeKeyValue.get() != 'none':
            threeKey.current(self.threeKeyValue.get())
        if self.fourKeyValue.get() != 'none':
            fourKey.current(self.fourKeyValue.get())
        if self.fiveKeyValue.get() != 'none':
            fiveKey.current(self.fiveKeyValue.get())
        if self.sixKeyValue.get() != 'none':
            sixKey.current(self.sixKeyValue.get())
        if self.sevenKeyValue.get() != 'none':
            sevenKey.current(self.sevenKeyValue.get())
        if self.eightKeyValue.get() != 'none':
            eightKey.current(self.eightKeyValue.get())
        if self.nineKeyValue.get() != 'none':
            nineKey.current(self.nineKeyValue.get())
        if self.zeroKeyValue.get() != 'none':
            zeroKey.current(self.zeroKeyValue.get())
        if self.macroOneKeyValueOne.get() != 'none':
            macroOneKeyOne.current(self.macroOneKeyValueOne.get())
        if self.macroOneKeyValueTwo.get() != 'none':
            macroOneKeyTwo.current(self.macroOneKeyValueTwo.get())
        if self.macroTwoKeyValueOne.get() != 'none':
            macroTwoKeyOne.current(self.macroTwoKeyValueOne.get())
        if self.macroTwoKeyValueTwo.get() != 'none':
            macroTwoKeyTwo.current(self.macroTwoKeyValueTwo.get())
        if self.macroThreeKeyValueOne.get() != 'none':
            macroThreeKeyOne.current(self.macroThreeKeyValueOne.get())
        if self.macroThreeKeyValueTwo.get() != 'none':
            macroThreeKeyTwo.current(self.macroThreeKeyValueTwo.get())
        if self.macroFourKeyValueTwo.get() != 'none':
            macroFourKeyOne.current(self.macroFourKeyValueTwo.get())
        if self.macroFourKeyValueTwo.get() != 'none':
            macroFourKeyTwo.current(self.macroFourKeyValueTwo.get())


    def closeControl_close_window(self, controlOpt):
        controlOpt.destroy()


    def alt_closeControl_close_window(self, controlOpt, start):
        try:
            controlOpt.destroy()
            GreenScreenFile.GreenScreen.greenScreenCls = False
            start.destroy()
            exit()
        except Exception as e:
            GreenScreenFile.GreenScreen.greenScreenCls = False
            start.destroy()
            exit()


    def on_press(self, controlOpt, start, upKey, downKey, leftKey, rightKey, enterKey, controlKey, spaceKey, shiftKey, oneKey, twoKey, threeKey, fourKey, fiveKey, sixKey, sevenKey, eightKey, nineKey, zeroKey, actionOneKey, actionTwoKey, actionThreeKey, actionFourKey, actionFiveKey, actionSixKey, actionSevenKey, actionEightKey, macroOneKeyOne, macroTwoKeyOne, macroThreeKeyOne, macroFourKeyOne, macroOneKeyTwo, macroTwoKeyTwo, macroThreeKeyTwo, macroFourKeyTwo, displayUpEntry, displayDownEntry, displayRightEntry, displayLeftEntry, displayShiftEntry, displayControlEntry, displaySpaceEntry, displayEnterEntry, displayActionOneEntry, displayActionTwoEntry, displayActionThreeEntry, displayActionFourEntry, displayActionFiveEntry, displayActionSixEntry, displayActionSevenEntry, displayActionEightEntry, displayOneEntry, displayTwoEntry, displayThreeEntry, displayFourEntry, displayFiveEntry, displaySixEntry, displaySevenEntry, displayEightEntry, displayNineEntry, displayZeroEntry, displayMacroOneEntry, displayMacroOneEntryTimerOne, displayMacroOneEntryTimerTwo, displayMacroTwoEntry, displayMacroTwoEntryTimerOne, displayMacroTwoEntryTimerTwo, displayMacroThreeEntry, displayMacroThreeEntryTimerOne, displayMacroThreeEntryTimerTwo, displayMacroFourEntry, displayMacroFourEntryTimerOne, displayMacroFourEntryTimerTwo, upButton, downButton, rightButton, leftButton, oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton, zeroButton, shiftButton, controlButton, enterButton, spaceButton, actionButtonOne, actionButtonTwo, actionButtonThree, actionButtonFour, actionButtonFive, actionButtonSix, actionButtonSeven, actionButtonEight, macroOneButton, macroTwoButton, macroThreeButton, macroFourButton, mouseMoveRightButton, mouseMoveLeftButton, mouseMoveUpButton, mouseMoveDownButton, mouseLeftButton, mouseRightButton):
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