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

import MouseHub
import GameControls
import BackgroundInfoHub
import ScreenHub
import ControlHub
import GreenScreenHub
import TwitchPlays_Connection

##################### GAME VARIABLES #####################

#GreenScreen Values
greenScreenCls = False

#ControlHub Values
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

#MouseHub Values
mimicMouseBox = ''
moveMouseUp = 45
moveMouseDown = 45
moveMouseRight = 45
moveMouseLeft = 45
textMouseUp = ''
textMouseDown = ''
textMouseRight = ''
textMouseLeft = ''
rightClick = ''
rightClickValue = ''
leftClick = ''
leftClickValue = ''

#ScreenHub Values
startXGet = ''
endXGet = ''
startYGet = ''
endYGet = ''
mimicScreenBox = ''

#BackGround Values
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
t = None
y = None
t1 = None
gamesetting = 0
username = ''
youtubeURL = ''

#GameControl Values
TTAOne = ''
TTATwo = ''
TTAThree = ''
TTAFour = ''

#Program Values
TTA = GameControls.TextToAction()
sendInfo = BackgroundInfoHub.backgroundInfo()
sendTwitch = sendInfo.twitch_Button
sendYoutube = sendInfo.youtube_Button
sendTwitchAndYoutube = sendInfo.youtubeAndTwitch_Button
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
greenScreenMode = GreenScreenHub.GreenScreen()
GSMode = greenScreenMode.greenScreenChange
sendHeartBoundSetting = sendInfo.heartboundSetting
sendKnuckleSandwichSetting = sendInfo.knuckleSandwichSetting
messageRelayConnect = ''
messageRelayOne = ''
messageRelayTwo = ''
messageRelayThree = ''
messageRelayFour = ''
startButton = ''
endButton = ''

def Program(eventRun=None):
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
        if (twitchActive == True and youtubeActive != True and previousTab == 3):
            t = TwitchPlays_Connection.Twitch()
            t.twitch_connect(TWITCH_CHANNEL)
            messageRelayConnect.config(text='Connected To Twitch')
        elif(youtubeActive == True and twitchActive != True and previousTab == 3):
            t = TwitchPlays_Connection.YouTube()
            t.youtube_connect(YOUTUBE_CHANNEL_ID, YOUTUBE_STREAM_URL)
            messageRelayConnect.config(text='Connected To Youtube')
        elif(twitchActive == True and youtubeActive == True and previousTab == 3):
            t = TwitchPlays_Connection.Twitch()
            t.twitch_connect(TWITCH_CHANNEL)
            y = TwitchPlays_Connection.YouTube()
            y.youtube_connect(YOUTUBE_CHANNEL_ID, YOUTUBE_STREAM_URL)
            messageRelayConnect.config(text='Connected To Twitch and Youtube')
        endButton["state"] = ACTIVE
        startButton['bg'] = 'light green'
    except Exception as e:
        messageRelayConnect.config(text='Error: Unable to connect to a platform. Check login details...')
        endButton["state"] = ACTIVE
        startButton['bg'] = 'red'

    while(True and previousTab == 3):
        try:
            t = t
        except Exception as e:
            t = t
            y = y
        active_tasks = [t for t in active_tasks if not t.done()]
        alt_active_tasks = [y for y in alt_active_tasks if not y.done()]

        #Check for new messages
        new_messages = t.twitch_receive_messages()

        if(STREAMING_ON_TWITCH == True and STREAMING_ON_YOUTUBE == True):
            alt_new_messages = y.twitch_receive_messages()
        else:
            alt_new_messages = None
        if new_messages:
            message_queue += new_messages; # New messages are added to the back of the queue
            message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages
        if STREAMING_ON_TWITCH == True and STREAMING_ON_YOUTUBE == True and alt_new_messages != None:
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
                    print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

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
    twitchButton = Button(web,height = 1, width = 10, text="Twitch",font = ("Arial", 12),compound = TOP, command = sendTwitch)#, image= twitchResize, height = 140, width = 100)
    youtubeButton = Button(web,height = 1, width = 10, text="Youtube",font = ("Arial", 12),compound = TOP, command= sendYoutube)#, image= youtubeResize), height = 140, width = 100)
    twitchAndYoutubeButton = Button(web,height = 1, width = 20, text="Both Twitch and Youtube",font = ("Arial", 12),compound = TOP, command= sendTwitchAndYoutube)
    thanks = Label(web, text="Original code by Wituz, updated by DDarknut, DougDoug, Ottomated. Further expanded by Bloop",
                        bg = "white",
                        fg = "black",
                        font = ("Arial", 7))


    web.protocol("WM_DELETE_WINDOW", sendClose)
    webText.place(x=155, y=50)
    twitchButton.place(x=120, y=100)
    youtubeButton.place(x=285, y=100)
    #twitchAndYoutubeButton.place(x=162, y=260)
    twitchAndYoutubeButton.place(x=162, y=160)
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
        if(twitchActive == True and youtubeActive == True):
            webText = Label(platform, text="Enter Your Youtube Channel ID",
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
            webURL = Label(platform, text="Enter Your Youtube Stream URL",
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
            username = Entry(platform, text = "Channel ID..", width = 53)
            youtubeURL = Entry(platform, text = "Channel URL..", width = 53)
            username.place(x=25, y=50)
            webText.place(x=5, y=20)
            webURL.place(x=5, y=80)
            youtubeURL.place(x=25, y=110)


            webText = Label(platform, text="Enter Your Twitch Username",
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
            username = Entry(platform, text = "Username..", width = 53)
            username.place(x=25, y=170)
            webText.place(x=5, y=140)

        if(twitchActive == True and youtubeActive == False):
            webText = Label(platform, text="Enter Your Twitch Username",
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
            username = Entry(platform, text = "Username..", width = 53)
            username.place(x=25, y=50)
            webText.place(x=5, y=20)
        if(youtubeActive == True and twitchActive == False):
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

            minecraftButton = Button(game, text="Minecraft",height = 2, width = 9, command = sendMinecraftSetting)
            minecraftButton.place(x=75, y = 100)

            gameTwoButton = Button(game, text="HeartBound",height = 2, width = 9, command = sendHeartBoundSetting)
            gameTwoButton.place(x=150, y = 100)

            gameThreeButton = Button(game, text="Game 3",height = 2, width = 9, command = None)
            gameThreeButton.place(x=225, y = 100)

            gameFourButton = Button(game, text="Game 4",height = 2, width = 9, command = None)
            gameFourButton.place(x=300, y = 100)

            gameFiveButton = Button(game, text="Game 5",height = 2, width = 9, command = None)
            gameFiveButton.place(x=375, y = 100)

            gameSixButton = Button(game, text="Game 6",height = 2, width = 9, command = None)
            gameSixButton.place(x=75, y = 150)

            gameSevenButton = Button(game, text="Game 7",height = 2, width = 9, command = None)
            gameSevenButton.place(x=150, y = 150)

            gameEightButton = Button(game, text="Game 8",height = 2, width = 9, command = None)
            gameEightButton.place(x=225, y = 150)

            gameNineButton = Button(game, text="Game 9",height = 2, width = 9, command = None)
            gameNineButton.place(x=300, y = 150)

            gameTenButton = Button(game, text="Game 10",height = 2, width = 9, command = None)
            gameTenButton.place(x=375, y = 150)

            gameElevenButton = Button(game, text="Game 11",height = 2, width = 9, command = None)
            gameElevenButton.place(x=75, y = 200)

            gameTwelveButton = Button(game, text="Game 12",height = 2, width = 9, command = None)
            gameTwelveButton.place(x=150, y = 200)

            gameThirteenButton = Button(game, text="Game 13",height = 2, width = 9, command = None)
            gameThirteenButton.place(x=225, y = 200)

            gameFourteenButton = Button(game, text="Knuckle Sandwich",height = 2, width = 9,wraplength=52, command = sendKnuckleSandwichSetting)
            gameFourteenButton.place(x=300, y = 200)

            customButton = Button(game, text="Custom",height = 2, width = 9, command = sendCustomSetting)
            customButton.place(x=375, y = 200)

            backButton = Button(game, text="Back",height = 2, width = 5, command = sendBackTrackPlatform)
            backButton.place(x=15, y = 290)

            game.protocol("WM_DELETE_WINDOW", sendGameClose)
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
                screenManager = ScreenHub.ScreenManage()
                options.add_command(label='Screen', command= screenManager.screenOption)


                messageRelayOne = Label(start, text=TTAOne,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
                messageRelayTwo = Label(start, text=TTATwo,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
                messageRelayThree = Label(start, text=TTAThree,
                    bg = "white",
                    fg = "black",
                    font = ("Arial", 10))
                messageRelayFour = Label(start, text=TTAFour,
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

                if(gamesetting == 0):
                    shiftButton = Button(start, text="Shift", height=1, width=5, state=DISABLED)
                    shiftButton.place(x=20, y=145)

                    controlButton = Button(start, text="Control", height=1, width=6, state=DISABLED)
                    controlButton.place(x=20, y=175)

                    upButton = Button(start, text="Up", height=1, width=4, state=DISABLED)
                    downButton = Button(start, text="Down", height=1, width=4, state=DISABLED)
                    leftButton = Button(start, text="Left", height=1, width=4, state=DISABLED)
                    rightButton = Button(start, text="Right", height=1, width=4, state=DISABLED)
                    upButton.place(x=115, y=145)
                    downButton.place(x=115, y=175)
                    leftButton.place(x=75, y=175)
                    rightButton.place(x=155, y=175)

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

                if(gamesetting == 1):
                    upButton = Button(start, text="Up", height=1, width=4, state=DISABLED)
                    downButton = Button(start, text="Down", height=1, width=4, state=DISABLED)
                    leftButton = Button(start, text="Left", height=1, width=4, state=DISABLED)
                    rightButton = Button(start, text="Right", height=1, width=4, state=DISABLED)
                    upButton.place(x=115, y=145)
                    downButton.place(x=115, y=175)
                    leftButton.place(x=75, y=175)
                    rightButton.place(x=155, y=175)

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

                if (gamesetting == 14):
                    upButton = Button(start, text="Up", height=1, width=4, state=DISABLED)
                    downButton = Button(start, text="Down", height=1, width=4, state=DISABLED)
                    leftButton = Button(start, text="Left", height=1, width=4, state=DISABLED)
                    rightButton = Button(start, text="Right", height=1, width=4, state=DISABLED)
                    upButton.place(x=115, y=145)
                    downButton.place(x=115, y=175)
                    leftButton.place(x=75, y=175)
                    rightButton.place(x=155, y=175)

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


                if(gamesetting == 99):
                    start.minsize(600, 350)
                    start.maxsize(600, 350)
                    controlManager = ControlHub.ControlManage()
                    controlFunction = partial(controlManager.controlOption, start)
                    mouseManager = MouseHub.MouseManage()
                    mouseFunction = partial(mouseManager.mouseOption, start)

                    options.add_command(label='Keyboard', command= controlFunction)
                    options.add_command(label='Mouse', command= mouseFunction)

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
