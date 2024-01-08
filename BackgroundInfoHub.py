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

class backgroundInfo():
    def backTrackAccount(self):

        TwitchPlays_TEMPLATE.previousTab -= 1
        TwitchPlays_TEMPLATE.TWITCH_CHANNEL = ''
        TwitchPlays_TEMPLATE.STREAMING_ON_TWITCH = False
        TwitchPlays_TEMPLATE.YOUTUBE_CHANNEL_ID = ''
        TwitchPlays_TEMPLATE.YOUTUBE_STREAM_URL = None
        TwitchPlays_TEMPLATE.STREAMING_ON_YOUTUBE = False
        TwitchPlays_TEMPLATE.twitchActive = False
        TwitchPlays_TEMPLATE.youtubeActive = False
        TwitchPlays_TEMPLATE.gamesetting = 0
        TwitchPlays_TEMPLATE.platform.destroy()


    def updateMessage(self):
        TwitchPlays_TEMPLATE.messageRelayOne.config(text=TwitchPlays_TEMPLATE.TTAFour)
        TwitchPlays_TEMPLATE.messageRelayTwo.config(text=TwitchPlays_TEMPLATE.TTAThree)
        TwitchPlays_TEMPLATE.messageRelayThree.config(text=TwitchPlays_TEMPLATE.TTATwo)
        TwitchPlays_TEMPLATE.messageRelayFour.config(text=TwitchPlays_TEMPLATE.TTAOne)
        #start.after(1, updateMessage)


    def updateClear(self):
        TwitchPlays_TEMPLATE.TTAFour = ''
        TwitchPlays_TEMPLATE.TTAThree = ''
        TwitchPlays_TEMPLATE.TTATwo = ''
        TwitchPlays_TEMPLATE.TTAOne = ''
        #start.after(1, updateClear)


    def backTrackPlatform(self):

        TwitchPlays_TEMPLATE.previousTab -= 1
        TwitchPlays_TEMPLATE.game.destroy()


    def minecraftSetting(self):

        TwitchPlays_TEMPLATE.gamesetting = 0
        TwitchPlays_TEMPLATE.previousTab = 3
        TwitchPlays_TEMPLATE.game.destroy()

    def heartboundSetting(self):

        TwitchPlays_TEMPLATE.gamesetting = 1
        TwitchPlays_TEMPLATE.previousTab = 3
        TwitchPlays_TEMPLATE.game.destroy()

    def knuckleSandwichSetting(self):

        TwitchPlays_TEMPLATE.gamesetting = 14
        TwitchPlays_TEMPLATE.previousTab = 3
        TwitchPlays_TEMPLATE.game.destroy()

    def customSetting(self):

        TwitchPlays_TEMPLATE.gamesetting = 99
        TwitchPlays_TEMPLATE.previousTab = 3
        TwitchPlays_TEMPLATE.game.destroy()


    def endProgram(self):
        TwitchPlays_TEMPLATE.t = ''
        TwitchPlays_TEMPLATE.y = ''
        if(TwitchPlays_TEMPLATE.t == '' or TwitchPlays_TEMPLATE.y == ''):
            backgroundInfo.updateClear(self)
        TwitchPlays_TEMPLATE.previousTab -= 1
        TwitchPlays_TEMPLATE.startButton["state"] = ACTIVE
        TwitchPlays_TEMPLATE.greenScreenCls = False
        try:
            TwitchPlays_TEMPLATE.mimicMouseBox.destroy()
        except Exception as e:
            None
        try:
            TwitchPlays_TEMPLATE.mimicControlBox.destroy()
        except Exception as e:
            None
        try:
            TwitchPlays_TEMPLATE.mimicScreenBox.destroy()
        except Exception as e:
            None
        TwitchPlays_TEMPLATE.start.destroy()

    def twitch_Button(self):
        TwitchPlays_TEMPLATE.previousTab = 1
        TwitchPlays_TEMPLATE.twitchActive = True
        TwitchPlays_TEMPLATE.web.destroy()

    def youtube_Button(self):
        TwitchPlays_TEMPLATE.previousTab = 1
        TwitchPlays_TEMPLATE.youtubeActive = True
        TwitchPlays_TEMPLATE.web.destroy()

    def youtubeAndTwitch_Button(self):
        TwitchPlays_TEMPLATE.previousTab = 1
        TwitchPlays_TEMPLATE.youtubeActive = True
        TwitchPlays_TEMPLATE.twitchActive = True
        TwitchPlays_TEMPLATE.web.destroy()

    def start_close_window(self):
        #thread()
        TwitchPlays_TEMPLATE.greenScreenCls = False
        TwitchPlays_TEMPLATE.start.destroy()
        exit()

    def platform_close_window(self):
        TwitchPlays_TEMPLATE.platform.destroy()
        exit()

    def game_close_window(self):
        TwitchPlays_TEMPLATE.game.destroy()
        exit()

    def web_close_window(self):
        TwitchPlays_TEMPLATE.web.destroy()
        exit()

    def WebSite(self):

        # Replace this with your Twitch username. Must be all lowercase.
        TwitchPlays_TEMPLATE.TWITCH_CHANNEL = ''
        TwitchPlays_TEMPLATE.STREAMING_ON_TWITCH = False
        TwitchPlays_TEMPLATE.YOUTUBE_CHANNEL_ID = ''
        TwitchPlays_TEMPLATE.YOUTUBE_STREAM_URL = None
        TwitchPlays_TEMPLATE.STREAMING_ON_YOUTUBE = False
        if(TwitchPlays_TEMPLATE.youtubeActive == True and TwitchPlays_TEMPLATE.twitchActive == False):
            usernameAccess = TwitchPlays_TEMPLATE.username.get()
            channelURL = TwitchPlays_TEMPLATE.youtubeURL.get()
        if(TwitchPlays_TEMPLATE.twitchActive == True and TwitchPlays_TEMPLATE.youtubeActive == False):
            usernameAccess = TwitchPlays_TEMPLATE.username.get()
        if(TwitchPlays_TEMPLATE.twitchActive == True and TwitchPlays_TEMPLATE.youtubeActive == False):
            TwitchPlays_TEMPLATE.TWITCH_CHANNEL = usernameAccess

            # If streaming on Youtube, set this to False
            TwitchPlays_TEMPLATE.STREAMING_ON_TWITCH = TwitchPlays_TEMPLATE.twitchActive

        # If you're streaming on Youtube, replace this with your Youtube's Channel ID
        # Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
        if(TwitchPlays_TEMPLATE.youtubeActive == True and TwitchPlays_TEMPLATE.twitchActive == False):
            TwitchPlays_TEMPLATE.YOUTUBE_CHANNEL_ID = usernameAccess

            # If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
            # Otherwise you can leave this as "None"
            TwitchPlays_TEMPLATE.YOUTUBE_STREAM_URL = channelURL

        if(TwitchPlays_TEMPLATE.youtubeActive == True and TwitchPlays_TEMPLATE.twitchActive == True):
            TwitchPlays_TEMPLATE.STREAMING_ON_TWITCH = TwitchPlays_TEMPLATE.twitchActive
            TwitchPlays_TEMPLATE.STREAMING_ON_YOUTUBE = TwitchPlays_TEMPLATE.youtubeActive

            youtubeUsernameAccess = TwitchPlays_TEMPLATE.username.get()
            youtubeChannelURL = TwitchPlays_TEMPLATE.youtubeURL.get()

            twitchUsernameAccess = TwitchPlays_TEMPLATE.username.get()

            TwitchPlays_TEMPLATE.YOUTUBE_STREAM_URL = youtubeChannelURL
            TwitchPlays_TEMPLATE.YOUTUBE_CHANNEL_ID = youtubeUsernameAccess
            TwitchPlays_TEMPLATE.TWITCH_CHANNEL = twitchUsernameAccess

        if(TwitchPlays_TEMPLATE.YOUTUBE_CHANNEL_ID != None and TwitchPlays_TEMPLATE.youtubeActive == True and TwitchPlays_TEMPLATE.twitchActive == True):
            if(youtubeUsernameAccess != '' and youtubeChannelURL !=  '' and twitchUsernameAccess != ''):
                TwitchPlays_TEMPLATE.previousTab = 2
                TwitchPlays_TEMPLATE.platform.destroy()
        if(TwitchPlays_TEMPLATE.YOUTUBE_CHANNEL_ID != None and TwitchPlays_TEMPLATE.youtubeActive == True and TwitchPlays_TEMPLATE.twitchActive == False):
            if(usernameAccess != '' and channelURL !=  ''):
                TwitchPlays_TEMPLATE.previousTab = 2
                TwitchPlays_TEMPLATE.platform.destroy()
        if(TwitchPlays_TEMPLATE.STREAMING_ON_TWITCH == True and TwitchPlays_TEMPLATE.twitchActive == True and TwitchPlays_TEMPLATE.youtubeActive == False):
            if(usernameAccess != ''):
                TwitchPlays_TEMPLATE.previousTab = 2
                TwitchPlays_TEMPLATE.platform.destroy()

        ##################### MESSAGE QUEUE VARIABLES #####################

    def thread(self):

        TwitchPlays_TEMPLATE.t1 = threading.Thread(target=TwitchPlays_TEMPLATE.Program)
        if (TwitchPlays_TEMPLATE.t1.is_alive() != True):
            TwitchPlays_TEMPLATE.startButton["state"] = DISABLED
            TwitchPlays_TEMPLATE.endButton["state"] = DISABLED
            TwitchPlays_TEMPLATE.startButton['bg'] = 'light yellow'
            TwitchPlays_TEMPLATE.t1.start()
        else:
            TwitchPlays_TEMPLATE.t1.join()