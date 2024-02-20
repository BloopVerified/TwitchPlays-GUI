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

class GreenScreen():
    greenScreenCls = False
    def greenScreenChange(self, start, messageRelayOne, messageRelayTwo, messageRelayThree, messageRelayFour, messageRelayConnect):
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