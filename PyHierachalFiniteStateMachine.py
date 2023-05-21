import PySimpleGUI as sg
from PyEmotions import *
from PyEmotionCache import StateCache


class PyHierachalFiniteStateMachine:

    def __init__(self,_sg):

        self.Emojis = {"Joyful": "Images/Joyful.png","Angry":"Images/Angry.png","Sad":"Images/Sad.png"

                       }

        self.backButton = "Images/backArrow.png"
        self.superStateButtonSize = (100, 100)
        self.windowSize = (350, 350)

        self.CreateWindow(_sg)

        self.stateCache = StateCache()

        self.currentState = self.stateCache.JoyFulState()
        self.currentState.EnterState()

    def CreateSuperStateButton(self,_image,_key):
        return sg.Image(filename=_image,size=self.superStateButtonSize,key=_key,enable_events=True)

    def CreateSubStateButton(self,_image,_key):
        return sg.Image(filename=_image,size=self.buttonSize,key=_key,enable_events=True)
    def CreateWindow(self,_sg):
        _sg.theme("black")

        layout = [
            [_sg.Text("Choose your Emotion"),_sg.Push(),_sg.Image(self.backButton,size=(80,35),visible=False,key="-backButton-")],
            [self.CreateSuperStateButton(self.Emojis["Joyful"],"-joyful-"),self.CreateSuperStateButton(self.Emojis["Angry"],"-angry-"),self.CreateSuperStateButton(self.Emojis["Sad"],"-sad-")],
        ]

        window = _sg.Window("HierachalFiniteStateMachine", layout, size=self.windowSize)

        while True:
            event, values = window.Read()

            if event == "-joyful-":
                window["-angry-"].Update(visible=False)
                window["-sad-"].Update(visible=False)
                window["-backButton-"].Update(visible=True)



            if event == _sg.WINDOW_CLOSED:
                break






humanEmotion = PyHierachalFiniteStateMachine(sg)















