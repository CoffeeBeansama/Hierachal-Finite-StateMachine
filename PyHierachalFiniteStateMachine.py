import PySimpleGUI as sg
from PyEmotions import *
from PyEmotionCache import StateCache


class PyHierachalFiniteStateMachine:

    def __init__(self,_sg):

        self.superStateButtonSize = (100, 100)
        self.subStateButtonSize =(80,80)
        self.windowSize = (350, 350)

        self.Emojis = {"Joyful": "Images/Joyful.png",
                       "Angry": "Images/Angry.png",
                       "Sad": "Images/Sad.png",
                       "Happy": "Images/Happy.png",
                       "Ecstatic": "Images/Ecstatic.png",
                       "Excited": "Images/Excited.png"

                       }

        self.backButton = "Images/backArrow.png"

        self.stateCache = StateCache(_sg)

        self.CreateWindow(_sg)





    def CreateSuperStateButton(self,_image,_key):
        return sg.Image(filename=_image,size=self.superStateButtonSize,key=_key,enable_events=True)

    def CreateSubStateButton(self,_image,_key):
        return sg.Image(filename=_image,size=self.subStateButtonSize,key=_key,enable_events=True,visible=False)
    def CreateWindow(self,_sg):
        _sg.theme("black")

        layout = [
            [_sg.Text("Choose your Emotion"),_sg.Push(),_sg.Image(self.backButton,size=(80,35),visible=False,key="-backButton-")],
            [self.CreateSuperStateButton(self.Emojis["Joyful"],"-joyful-"),self.CreateSuperStateButton(self.Emojis["Angry"],"-angry-"),self.CreateSuperStateButton(self.Emojis["Sad"],"-sad-")],
            [self.CreateSubStateButton(self.Emojis["Happy"],"Happy"),self.CreateSubStateButton(self.Emojis["Ecstatic"],"Ecstatic"),self.CreateSubStateButton(self.Emojis["Excited"],"Excited")],
        ]

        window = _sg.Window("HierachalFiniteStateMachine", layout, size=self.windowSize)

        while True:
            event, values = window.Read()

            if event == "-joyful-":
                window["-angry-"].Update(visible=False)
                window["-sad-"].Update(visible=False)
                window["-backButton-"].Update(visible=True)
                window["Happy"].Update(visible=True)
                window["Ecstatic"].Update(visible=True)
                window["Excited"].Update(visible=True)
                self.currentState = self.stateCache.JoyFulState()



            if event in ["Happy","Ecstatic","Excited"]:
                self.currentState.EnterState()


            if event == "-angry-":
                window["-joyful-"].Update(visible=False)
                window["-sad-"].Update(visible=False)
                window["-backButton-"].Update(visible=True)
                self.currentState = self.stateCache.AngryState()

                self.currentState.EnterState()

            if event == "-sad-":
                window["-joyful-"].Update(visible=False)
                window["-angry-"].Update(visible=False)
                window["-backButton-"].Update(visible=True)
                self.currentState = self.stateCache.SadState()
                self.currentState.EnterState()




            if event == _sg.WINDOW_CLOSED:
                break






humanEmotion = PyHierachalFiniteStateMachine(sg)















