import PySimpleGUI as sg
from PyEmotions import *
from PyEmotionCache import StateCache
import sys
sys.setrecursionlimit(1500)

class HumanMood:



    def __init__(self):


        self.stateCache = StateCache()



        self.currentState = self.stateCache.JoyFulState()
        self.currentState.EnterState()



humanEmotion = HumanMood()












