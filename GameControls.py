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

import TwitchPlays_TEMPLATE

class TextToAction():
    def handle_message(self, message):
        ScreenXStartEntry = 0
        ScreenXEndEntry = 0
        ScreenYStartEntry = 0
        ScreenYEndEntry = 0
        try:
            ScreenXStartEntry = int(TwitchPlays_TEMPLATE.startXGet)
            ScreenXEndEntry = int(TwitchPlays_TEMPLATE.endXGet)
            ScreenYStartEntry = int(TwitchPlays_TEMPLATE.startYGet)
            ScreenYEndEntry = int(TwitchPlays_TEMPLATE.endYGet)

        except Exception as e:
            ScreenXStartEntry = 0
            ScreenXEndEntry = 1920
            ScreenYStartEntry = 0
            ScreenYEndEntry = 1080

        try:
            msg = message['message'].lower()
            username = message['username'].lower()
            TwitchPlays_TEMPLATE.TTAFour = (TwitchPlays_TEMPLATE.TTAThree)
            TwitchPlays_TEMPLATE.TTAThree = (TwitchPlays_TEMPLATE.TTATwo)
            TwitchPlays_TEMPLATE.TTATwo = (TwitchPlays_TEMPLATE.TTAOne)
            TwitchPlays_TEMPLATE.TTAOne = "Got this message from " + username + ": " + msg
            TwitchPlays_TEMPLATE.start.after(1000, TwitchPlays_TEMPLATE.sendUpdateMessage)
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
            if(TwitchPlays_TEMPLATE.gamesetting == 0 and TwitchPlays_TEMPLATE.previousTab == 3):
                if(msg.lower() == 'right' and ((int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    TwitchPlays_TEMPLATE.rightButton['bg'] = 'red'
                    keyboard.press("d")
                    time.sleep(1)
                    keyboard.release("d")
                    TwitchPlays_TEMPLATE.rightButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'left' and ((int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    TwitchPlays_TEMPLATE.leftButton['bg'] = 'red'
                    keyboard.press("a")
                    time.sleep(1)
                    keyboard.release("a")
                    TwitchPlays_TEMPLATE.leftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'forward' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.upButton['bg'] = 'red'
                    keyboard.press("w")
                    time.sleep(1)
                    keyboard.release("w")
                    TwitchPlays_TEMPLATE.upButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'back' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.downButton['bg'] = 'red'
                    keyboard.press("s")
                    time.sleep(1)
                    keyboard.release("s")
                    TwitchPlays_TEMPLATE.downButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'space' or msg.lower() == 'jump' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.spaceButton['bg'] = 'red'
                    pydirectinput.press('space')
                    time.sleep(0)
                    TwitchPlays_TEMPLATE.spaceButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'hop' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.upButton['bg'] = 'red'
                    TwitchPlays_TEMPLATE.spaceButton['bg'] = 'red'
                    pydirectinput.keyDown('space')
                    keyboard.press("w")
                    time.sleep(1)
                    pydirectinput.keyUp('space')
                    keyboard.release("w")
                    TwitchPlays_TEMPLATE.upButton['bg'] = '#f0f0f0'
                    TwitchPlays_TEMPLATE.spaceButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'shifton' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    pydirectinput.keyDown('shift')
                    TwitchPlays_TEMPLATE.shiftButton['bg'] = 'red'
                elif(msg.lower() == 'shiftoff' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    pydirectinput.keyUp('shift')
                    TwitchPlays_TEMPLATE.shiftButton['bg'] = '#f0f0f0'

                elif(msg.lower() == 'controlon' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    pydirectinput.keyDown('control')
                    TwitchPlays_TEMPLATE.controlButton['bg'] = 'red'
                elif(msg.lower() == 'controloff' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    pydirectinput.keyUp('control')
                    TwitchPlays_TEMPLATE.controlButton['bg'] = '#f0f0f0'

                elif(msg.lower() == '1' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.oneButton['bg'] = 'red'
                    keyboard.press("1")
                    keyboard.release("1")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.oneButton['bg'] = '#f0f0f0'
                elif(msg.lower() == '2' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.twoButton['bg'] = 'red'
                    keyboard.press("2")
                    keyboard.release("2")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.twoButton['bg'] = '#f0f0f0'
                elif(msg.lower() == '3' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.threeButton['bg'] = 'red'
                    keyboard.press("3")
                    keyboard.release("3")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.threeButton['bg'] = '#f0f0f0'
                elif(msg.lower() == '4' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.fourButton['bg'] = 'red'
                    keyboard.press("4")
                    keyboard.release("4")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.fourButton['bg'] = '#f0f0f0'
                elif(msg.lower() == '5' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.fiveButton['bg'] = 'red'
                    keyboard.press("5")
                    keyboard.release("5")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.fiveButton['bg'] = '#f0f0f0'
                elif(msg.lower() == '6' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.sixButton['bg'] = 'red'
                    keyboard.press("6")
                    keyboard.release("6")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.sixButton['bg'] = '#f0f0f0'
                elif(msg.lower() == '7' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.sevenButton['bg'] = 'red'
                    keyboard.press("7")
                    keyboard.release("7")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.sevenButton['bg'] = '#f0f0f0'
                elif(msg.lower() == '8' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.eightButton['bg'] = 'red'
                    keyboard.press("8")
                    keyboard.release("8")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.eightButton['bg'] = '#f0f0f0'
                elif(msg.lower() == '9' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.nineButton['bg'] = 'red'
                    keyboard.press("9")
                    keyboard.release("9")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.nineButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'h2' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.secHandButton['bg'] = 'red'
                    keyboard.press("f")
                    keyboard.release("f")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.secHandButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'inv' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.InvButton['bg'] = 'red'
                    keyboard.press("e")
                    keyboard.release("e")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.InvButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'drop' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.dropButton['bg'] = 'red'
                    keyboard.press("q")
                    keyboard.release("q")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.dropButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'rt' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveRightButton['bg'] = 'red'
                    mouse.move(45, 0, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveRightButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'lt' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveLeftButton['bg'] = 'red'
                    mouse.move(-45, 0, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'ut' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveUpButton['bg'] = 'red'
                    mouse.move(0, -45, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveUpButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'dt'and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveDownButton['bg'] = 'red'
                    mouse.move(0, 45, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveDownButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'hit' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    mouse.release("left")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'smine' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    mouse.release("left")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'lmine' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    time.sleep(3)
                    mouse.release("left")
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'place' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseRightButton['bg'] = 'red'
                    mouse.press("right")
                    mouse.release("right")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.mouseRightButton['bg'] = '#f0f0f0'

            if(TwitchPlays_TEMPLATE.gamesetting == 1 and TwitchPlays_TEMPLATE.previousTab == 3):
                if(msg.lower() == 'right' and ((int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    TwitchPlays_TEMPLATE.rightButton['bg'] = 'red'
                    keyboard.press("d")
                    time.sleep(1)
                    keyboard.release("d")
                    TwitchPlays_TEMPLATE.rightButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'left' and ((int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    TwitchPlays_TEMPLATE.leftButton['bg'] = 'red'
                    keyboard.press("a")
                    time.sleep(1)
                    keyboard.release("a")
                    TwitchPlays_TEMPLATE.leftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'forward' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.upButton['bg'] = 'red'
                    keyboard.press("w")
                    time.sleep(1)
                    keyboard.release("w")
                    TwitchPlays_TEMPLATE.upButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'back' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.downButton['bg'] = 'red'
                    keyboard.press("s")
                    time.sleep(1)
                    keyboard.release("s")
                    TwitchPlays_TEMPLATE.downButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'accept' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.acceptButton['bg'] = 'red'
                    keyboard.press("z")
                    keyboard.release("z")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.acceptButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'skip' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.skipButton['bg'] = 'red'
                    keyboard.press("x")
                    keyboard.release("x")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.skipButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'mr' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveRightButton['bg'] = 'red'
                    mouse.move(45, 0, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveRightButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'ml' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveLeftButton['bg'] = 'red'
                    mouse.move(-45, 0, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'mu' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveUpButton['bg'] = 'red'
                    mouse.move(0, -45, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveUpButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'md'and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveDownButton['bg'] = 'red'
                    mouse.move(0, 45, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveDownButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'lc' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    mouse.release("left")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'rc' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseRightButton['bg'] = 'red'
                    mouse.press("right")
                    mouse.release("right")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.mouseRightButton['bg'] = '#f0f0f0'

            if(TwitchPlays_TEMPLATE.gamesetting == 1 and TwitchPlays_TEMPLATE.previousTab == 14):
                if(msg.lower() == 'right' and ((int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    TwitchPlays_TEMPLATE.rightButton['bg'] = 'red'
                    keyboard.press("right")
                    time.sleep(1)
                    keyboard.release("right")
                    TwitchPlays_TEMPLATE.rightButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'left' and ((int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) or (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry))):
                    TwitchPlays_TEMPLATE.leftButton['bg'] = 'red'
                    keyboard.press("left")
                    time.sleep(1)
                    keyboard.release("left")
                    TwitchPlays_TEMPLATE.leftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'up' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.upButton['bg'] = 'red'
                    keyboard.press("up")
                    time.sleep(1)
                    keyboard.release("up")
                    TwitchPlays_TEMPLATE.upButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'back' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.downButton['bg'] = 'red'
                    keyboard.press("down")
                    time.sleep(1)
                    keyboard.release("down")
                    TwitchPlays_TEMPLATE.downButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'x' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.confirmButton['bg'] = 'red'
                    keyboard.press("x")
                    keyboard.release("x")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.confirmButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'c' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.cancelButton['bg'] = 'red'
                    keyboard.press("c")
                    keyboard.release("c")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.cancelButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'b' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.miscButton['bg'] = 'red'
                    keyboard.press("b")
                    keyboard.release("b")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.miscButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'space' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.spaceButton['bg'] = 'red'
                    keyboard.press("space")
                    keyboard.release("space")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.spaceButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'mr' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveRightButton['bg'] = 'red'
                    mouse.move(45, 0, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveRightButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'ml' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveLeftButton['bg'] = 'red'
                    mouse.move(-45, 0, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'mu' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveUpButton['bg'] = 'red'
                    mouse.move(0, -45, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveUpButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'md'and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveDownButton['bg'] = 'red'
                    mouse.move(0, 45, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveDownButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'lc' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = 'red'
                    mouse.press("left")
                    mouse.release("left")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == 'rc' and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseRightButton['bg'] = 'red'
                    mouse.press("right")
                    mouse.release("right")
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.mouseRightButton['bg'] = '#f0f0f0'

            if (TwitchPlays_TEMPLATE.gamesetting == 99 and TwitchPlays_TEMPLATE.previousTab == 3):
                if(msg.lower() == TwitchPlays_TEMPLATE.upButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.upButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.upKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.upKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.upButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.downButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.downButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.downKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.downKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.downButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.rightButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.rightButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.rightKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.rightKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.rightButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.leftButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.leftButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.leftKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.leftKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.leftButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.oneButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.oneButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.oneKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.oneKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.oneButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.twoButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.twoButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.twoKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.twoKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.twoButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.threeButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.threeButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.threeKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.threeKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.threeButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.fourButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.fourButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.fourKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.fourKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.fourButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.fiveButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.fiveButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.fiveKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.fiveKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.fiveButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.sixButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.sixButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.sixKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.sixKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.sixButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.sevenButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.sevenButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.sixKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.sixKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.sevenButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.sevenButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.sevenButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.sevenKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.sevenKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.sevenButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.eightButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.eightButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.eightKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.eightKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.eightButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.nineButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.nineButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.nineKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.nineKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.nineButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.zeroButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.zeroButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.zeroKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.zeroKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.zeroButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.shiftButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.shiftButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.shiftKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.shiftKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.shiftButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.controlButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.controlButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.controlKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.controlKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.controlButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.enterButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.enterButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.enterKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.enterKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.enterButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.spaceButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.spaceButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.spaceKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.spaceKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.spaceButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.actionButtonOne['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.actionButtonOne['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.actionOneKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.actionOneKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.actionButtonOne['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.actionButtonTwo['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.actionButtonTwo['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.actionTwoKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.actionTwoKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.actionButtonTwo['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.actionButtonThree['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.actionButtonThree['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.actionThreeKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.actionThreeKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.actionButtonThree['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.actionButtonFour['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.actionButtonFour['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.actionFourKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.actionFourKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.actionButtonFour['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.actionButtonFive['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.actionButtonFive['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.actionFiveKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.actionFiveKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.actionButtonFive['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.actionButtonSix['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.actionButtonSix['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.actionSixKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.actionSixKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.actionButtonSix['bg'] = '#f0f0f0'

                if (msg.lower() == TwitchPlays_TEMPLATE.actionButtonSeven['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.actionButtonSeven['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.actionSevenKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.actionSevenKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.actionButtonSeven['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.actionButtonEight['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.actionButtonEight['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.actionEightKeyCls)
                    keyboard.release(TwitchPlays_TEMPLATE.actionEightKeyCls)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.actionButtonEight['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.macroOneButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.macroOneButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.macroOneKeyOneCls)
                    time.sleep(int(TwitchPlays_TEMPLATE.macroOneTimerOneCls))
                    keyboard.press(TwitchPlays_TEMPLATE.macroOneKeyTwoCls)
                    keyboard.release(TwitchPlays_TEMPLATE.macroOneKeyOneCls)
                    time.sleep(int(TwitchPlays_TEMPLATE.macroOneTimerTwoCls))
                    keyboard.release(TwitchPlays_TEMPLATE.macroOneKeyTwoCls)
                    TwitchPlays_TEMPLATE.macroOneButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.macroTwoButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.macroTwoButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.macroTwoKeyOneCls)
                    time.sleep(int(TwitchPlays_TEMPLATE.macroTwoTimerOneCls))
                    keyboard.press(TwitchPlays_TEMPLATE.macroTwoKeyTwoCls)
                    keyboard.release(TwitchPlays_TEMPLATE.macroTwoKeyOneCls)
                    time.sleep(int(TwitchPlays_TEMPLATE.macroTwoTimerTwoCls))
                    keyboard.release(TwitchPlays_TEMPLATE.macroTwoKeyTwoCls)
                    TwitchPlays_TEMPLATE.macroTwoButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.macroThreeButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.macroThreeButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.macroThreeKeyOneCls)
                    time.sleep(int(TwitchPlays_TEMPLATE.macroThreeTimerOneCls))
                    keyboard.press(TwitchPlays_TEMPLATE.macroThreeKeyTwoCls)
                    keyboard.release(TwitchPlays_TEMPLATE.macroThreeKeyOneCls)
                    time.sleep(int(TwitchPlays_TEMPLATE.macroThreeTimerTwoCls))
                    keyboard.release(TwitchPlays_TEMPLATE.macroThreeKeyTwoCls)
                    TwitchPlays_TEMPLATE.macroThreeButton['bg'] = '#f0f0f0'

                elif (msg.lower() == TwitchPlays_TEMPLATE.macroFourButton['text'].lower() and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.macroFourButton['bg'] = 'red'
                    keyboard.press(TwitchPlays_TEMPLATE.macroFourKeyOneCls)
                    time.sleep(int(TwitchPlays_TEMPLATE.macroFourTimerOneCls))
                    keyboard.press(TwitchPlays_TEMPLATE.macroFourKeyTwoCls)
                    keyboard.release(TwitchPlays_TEMPLATE.macroFourKeyOneCls)
                    time.sleep(int(TwitchPlays_TEMPLATE.macroFourTimerTwoCls))
                    keyboard.release(TwitchPlays_TEMPLATE.macroFourKeyTwoCls)
                    TwitchPlays_TEMPLATE.macroFourButton['bg'] = '#f0f0f0'

                elif(msg.lower() == TwitchPlays_TEMPLATE.textMouseRight and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveRightButton['bg'] = 'red'
                    mouse.move(int("" + str(TwitchPlays_TEMPLATE.moveMouseRight)), 0, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveRightButton['bg'] = '#f0f0f0'
                elif(msg.lower() == TwitchPlays_TEMPLATE.textMouseLeft and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveLeftButton['bg'] = 'red'
                    mouse.move(int("-" + str(TwitchPlays_TEMPLATE.moveMouseLeft)), 0, False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == TwitchPlays_TEMPLATE.textMouseUp and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveUpButton['bg'] = 'red'
                    mouse.move(0, int("-" + str(TwitchPlays_TEMPLATE.moveMouseUp)), False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveUpButton['bg'] = '#f0f0f0'
                elif(msg.lower() == TwitchPlays_TEMPLATE.textMouseDown and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseMoveDownButton['bg'] = 'red'
                    mouse.move(0, int("" + str(TwitchPlays_TEMPLATE.moveMouseDown)), False, .1)
                    TwitchPlays_TEMPLATE.mouseMoveDownButton['bg'] = '#f0f0f0'
                elif(msg.lower() == TwitchPlays_TEMPLATE.leftClick and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = 'red'
                    mouse.press(TwitchPlays_TEMPLATE.leftClickValue)
                    mouse.release(TwitchPlays_TEMPLATE.leftClickValue)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.mouseLeftButton['bg'] = '#f0f0f0'
                elif(msg.lower() == TwitchPlays_TEMPLATE.rightClick and (int(positionX) <= ScreenXEndEntry and int(positionX) >= ScreenXStartEntry) and (int(positionY) <= ScreenYEndEntry and int(positionY) >= ScreenYStartEntry)):
                    TwitchPlays_TEMPLATE.mouseRightButton['bg'] = 'red'
                    mouse.press(TwitchPlays_TEMPLATE.rightClickValue)
                    mouse.release(TwitchPlays_TEMPLATE.rightClickValue)
                    time.sleep(1)
                    TwitchPlays_TEMPLATE.mouseRightButton['bg'] = '#f0f0f0'


            ####################################
            ####################################

        except Exception as e:
            print("Encountered exception: " + str(e))