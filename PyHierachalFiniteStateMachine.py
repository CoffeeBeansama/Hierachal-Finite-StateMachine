import asyncio

import PySimpleGUI as sg
from PyEmotions import *
from PyEmotionCache import StateCache


class PyHierachalFiniteStateMachine:

    def __init__(self):



        self.stateCache = StateCache(self)

        self.currentState = self.stateCache.JoyFulState()

        self.ChangeSuperState = False
        self.ReadEmotion = True
        self.currentState.ChooseSuperState()
        self.UpdateState()

    def UpdateState(self):
        while self.ReadEmotion:
            self.currentState.UpdateState()















humanEmotion = PyHierachalFiniteStateMachine()















