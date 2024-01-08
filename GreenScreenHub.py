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

class GreenScreen():
    def greenScreenChange(self):
        if(TwitchPlays_TEMPLATE.greenScreenCls == False):
            TwitchPlays_TEMPLATE.greenScreenCls = True
            TwitchPlays_TEMPLATE.start['bg'] = 'lime'
            TwitchPlays_TEMPLATE.messageRelayConnect['bg'] = 'lime'
            TwitchPlays_TEMPLATE.messageRelayOne['bg'] = 'lime'
            TwitchPlays_TEMPLATE.messageRelayTwo['bg'] = 'lime'
            TwitchPlays_TEMPLATE.messageRelayThree['bg'] = 'lime'
            TwitchPlays_TEMPLATE.messageRelayFour['bg'] = 'lime'

        else:
            TwitchPlays_TEMPLATE.greenScreenCls = False
            TwitchPlays_TEMPLATE.start['bg'] = 'white'
            TwitchPlays_TEMPLATE.messageRelayConnect['bg'] = 'white'
            TwitchPlays_TEMPLATE.messageRelayOne['bg'] = 'white'
            TwitchPlays_TEMPLATE.messageRelayTwo['bg'] = 'white'
            TwitchPlays_TEMPLATE.messageRelayThree['bg'] = 'white'
            TwitchPlays_TEMPLATE.messageRelayFour['bg'] = 'white'