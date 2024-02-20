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

from GreenScreenFile import GreenScreen

class backgroundInfo():
    previousTab = 0
    TWITCH_CHANNEL = ''
    STREAMING_ON_TWITCH = False
    STREAMING_ON_YOUTUBE = False
    YOUTUBE_STREAM_URL = None
    YOUTUBE_CHANNEL_ID = ''
    twitchActive = False
    youtubeActive = False
    backMessageFour = ''
    backMessageThree = ''
    backMessageTwo = ''
    backMessageOne = ''
    t = ''
    y = ''
    t1 = None
    gamesetting = 0
    def backTrackAccount(self, platform):
        backgroundInfo.previousTab -= 1
        backgroundInfo.TWITCH_CHANNEL = ''
        backgroundInfo.STREAMING_ON_TWITCH = False
        backgroundInfo.YOUTUBE_CHANNEL_ID = ''
        backgroundInfo.YOUTUBE_STREAM_URL = None
        backgroundInfo.STREAMING_ON_YOUTUBE = False
        backgroundInfo.twitchActive = False
        backgroundInfo.youtubeActive = False
        backgroundInfo.gamesetting = 0
        platform.destroy()


    def updateMessage(self, messageRelayOne, messageRelayTwo,messageRelayThree,messageRelayFour, TTAOne, TTATwo, TTAThree, TTAFour):
        backgroundInfo.backMessageFour = TTAFour
        backgroundInfo.backMessageThree = TTAThree
        backgroundInfo.backMessageTwo = TTATwo
        backgroundInfo.backMessageOne = TTAOne
        messageRelayOne.config(text=backgroundInfo.backMessageOne)
        messageRelayTwo.config(text=backgroundInfo.backMessageTwo)
        messageRelayThree.config(text=backgroundInfo.backMessageThree)
        messageRelayFour.config(text=backgroundInfo.backMessageFour)
        #start.after(1, updateMessage)


    def updateClear(self, messageRelayOne, messageRelayTwo, messageRelayThree, messageRelayFour):
        backgroundInfo.backMessageFour = ''
        backgroundInfo.backMessageThree = ''
        backgroundInfo.backMessageTwo = ''
        backgroundInfo.backMessageOne = ''
        messageRelayFour.config(text=backgroundInfo.backMessageFour)
        messageRelayThree.config(text=backgroundInfo.backMessageThree)
        messageRelayTwo.config(text=backgroundInfo.backMessageTwo)
        messageRelayOne.config(text=backgroundInfo.backMessageOne)
        #start.after(1, updateClear)


    def backTrackPlatform(self, game):
        backgroundInfo.previousTab -= 1
        game.destroy()


    def minecraftSetting(self, game): #I got to right here
        backgroundInfo.gamesetting = 0
        backgroundInfo.previousTab = 3
        game.destroy()

    def heartboundSetting(self, game):
        backgroundInfo.gamesetting = 1
        backgroundInfo.previousTab = 3
        game.destroy()

    def knuckleSandwichSetting(self, game):
        backgroundInfo.gamesetting = 14
        backgroundInfo.previousTab = 3
        game.destroy()

    def customSetting(self, game):
        backgroundInfo.gamesetting = 99
        backgroundInfo.previousTab = 3
        game.destroy()


    def endProgram(self, start, startButton, messageRelayOne, messageRelayTwo, messageRelayThree, messageRelayFour):
        backgroundInfo.t = ''
        backgroundInfo.y = ''
        if(backgroundInfo.t == '' or backgroundInfo.y == ''):
            backgroundInfo.updateClear(self, messageRelayOne, messageRelayTwo, messageRelayThree, messageRelayFour)
        backgroundInfo.previousTab -= 1
        startButton["state"] = ACTIVE
        GreenScreen.greenScreenCls = False
        start.destroy()

    def twitch_Button(self, web):
        backgroundInfo.previousTab = 1
        backgroundInfo.twitchActive = True
        web.destroy()

    def youtube_Button(self,web):
        backgroundInfo.previousTab = 1
        backgroundInfo.youtubeActive = True
        web.destroy()

    def youtubeAndTwitch_Button(self, web):
        backgroundInfo.previousTab = 1
        backgroundInfo.youtubeActive = True
        backgroundInfo.twitchActive = True
        web.destroy()

    def start_close_window(self, start):
        #thread()
        GreenScreen.greenScreenCls = False
        start.destroy()
        exit()

    def platform_close_window(self, platform):
        platform.destroy()
        exit()

    def game_close_window(self, game):
        game.destroy()
        exit()

    def web_close_window(self, web):
        web.destroy()
        exit()

    def WebSite(self,platform ,username, youtubeURL):
        # Replace this with your Twitch username. Must be all lowercase.
        backgroundInfo.TWITCH_CHANNEL = ''
        backgroundInfo.STREAMING_ON_TWITCH = False
        backgroundInfo.YOUTUBE_CHANNEL_ID = ''
        backgroundInfo.YOUTUBE_STREAM_URL = None
        backgroundInfo.STREAMING_ON_YOUTUBE = False

        if(backgroundInfo.youtubeActive == True and backgroundInfo.twitchActive == False):
            usernameAccess = username.get()
            channelURL = youtubeURL.get()
        if(backgroundInfo.twitchActive == True and backgroundInfo.youtubeActive == False):
            usernameAccess = username.get()
        if(backgroundInfo.twitchActive == True and backgroundInfo.youtubeActive == False):
            backgroundInfo.TWITCH_CHANNEL = usernameAccess

            # If streaming on Youtube, set this to False
            backgroundInfo.STREAMING_ON_TWITCH = backgroundInfo.twitchActive

        # If you're streaming on Youtube, replace this with your Youtube's Channel ID
        # Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
        if(backgroundInfo.youtubeActive == True and backgroundInfo.twitchActive == False):
            backgroundInfo.YOUTUBE_CHANNEL_ID = usernameAccess

            # If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
            # Otherwise you can leave this as "None"
            backgroundInfo.YOUTUBE_STREAM_URL = channelURL

        if(backgroundInfo.youtubeActive == True and backgroundInfo.twitchActive == True):
            backgroundInfo.STREAMING_ON_TWITCH = backgroundInfo.twitchActive
            backgroundInfo.STREAMING_ON_YOUTUBE = backgroundInfo.youtubeActive

            youtubeUsernameAccess = username.get()
            youtubeChannelURL = youtubeURL.get()

            twitchUsernameAccess = username.get()

            backgroundInfo.YOUTUBE_STREAM_URL = youtubeChannelURL
            backgroundInfo.YOUTUBE_CHANNEL_ID = youtubeUsernameAccess
            backgroundInfo.TWITCH_CHANNEL = twitchUsernameAccess

        if(backgroundInfo.YOUTUBE_CHANNEL_ID != None and backgroundInfo.youtubeActive == True and backgroundInfo.twitchActive == True):
            if(youtubeUsernameAccess != '' and youtubeChannelURL !=  '' and twitchUsernameAccess != ''):
                backgroundInfo.previousTab = 2
                platform.destroy()
        if(backgroundInfo.YOUTUBE_CHANNEL_ID != None and backgroundInfo.youtubeActive == True and backgroundInfo.twitchActive == False):
            if(usernameAccess != '' and channelURL !=  ''):
                backgroundInfo.previousTab = 2
                platform.destroy()
        if(backgroundInfo.STREAMING_ON_TWITCH == True and backgroundInfo.twitchActive == True and backgroundInfo.youtubeActive == False):
            if(usernameAccess != ''):
                backgroundInfo.previousTab = 2
                platform.destroy()

        ##################### MESSAGE QUEUE VARIABLES #####################