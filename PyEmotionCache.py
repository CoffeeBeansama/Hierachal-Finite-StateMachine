from enum import Enum


from PyEmotions import *

class Mood(Enum):
    Joyful = 1
    Sad = 2
    Angry = 3

    Happy = 4
    Ecstatic = 5
    Excited = 6

    Frustrated = 7
    Annoyed = 8
    Mad = 9

    Depressed = 10
    Sorrow = 11
    Pain = 12


class StateCache:




    def __init__(self,_main):

        self.main = _main


        self.states = {
                       "Joyful": JoyfulState(self,self.main),
                       "Sad": SadState(self,self.main), "Angry": AngryState(self,self.main),
                       "Happy": Happy(self,self.main),
                       "Ecstatic": Ecstatic(self,self.main),
                       "Excited": Excited(self,self.main),
                       "Frustrated": Frustrated(self,self.main),
                       "Annoyed": Annoyed(self,self.main),
                       "Mad": Mad(self,self.main),
                       "Depressed": Depressed(self,self.main),
                       "Sorrow": Sorrow(self,self.main),
                       "Pain": Pain(self,self.main)
                     }

    def JoyFulState(self):
        return self.states["Joyful"]

    def SadState(self):
        return self.states["Sad"]

    def AngryState(self):
        return self.states["Angry"]

    def HappyState(self):
        return self.states["Happy"]

    def EcstaticState(self):
        return self.states["Ecstatic"]

    def ExcitedState(self):
        return self.states["Excited"]

    def FrustratedState(self):
        return self.states["Frustrated"]

    def MadState(self):
        return self.states["Mad"]

    def AnnoyedState(self):
        return self.states["Annoyed"]

    def SorrowState(self):
        return self.states["Sorrow"]

    def PainState(self):
        return self.states["Pain"]

    def DepressedState(self):
        return self.states["Depressed"]

