import PySimpleGUI as sg
from PyEmotions import *
from PyEmotionCache import StateCache


class PyHierachalFiniteStateMachine:

    def __init__(self,_sg):

        self.Emojis = {"Joyful": "Images/Joyful.png","Angry":"Images/Angry.png","Sad":"Images/Sad.png"

                       }

        self.windowSize = (350, 350)

        self.CreateWindow(_sg)

        self.stateCache = StateCache()

        self.currentState = self.stateCache.JoyFulState()
        self.currentState.EnterState()

    def CreateWindow(self,_sg):

        _sg.theme("black")

        layout = [
            [sg.Text("Choose your Emotion")],
            [sg.Image(self.Emojis["Joyful"],size=(100,100)),sg.Image(self.Emojis["Angry"],size=(100,100)),sg.Image(self.Emojis["Sad"],size=(100,100))]
        ]

        window = _sg.Window("HierachalFiniteStateMachine", layout, size=self.windowSize)

        while True:
            event, values = window.Read()

            if event == _sg.WINDOW_CLOSED:
                break


humanEmotion = PyHierachalFiniteStateMachine(sg)















