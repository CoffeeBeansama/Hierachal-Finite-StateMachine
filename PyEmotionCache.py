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




    def __init__(self,_sg):

        sg = _sg


        self.states = {
                       "Joyful": JoyfulState(self,sg),
                       "Sad": SadState(self,sg), "Angry": AngryState(self,sg),
                       "Happy": Happy(self,sg),
                       "Ecstatic": Ecstatic(self,sg),
                       "Excited": Excited(self,sg),
                       "Frustrated": Frustrated(self,sg),
                       "Annoyed": Annoyed(self,sg),
                       "Mad": Mad(self,sg),
                       "Depressed": Depressed(self,sg),
                       "Sorrow": Sorrow(self,sg),
                       "Pain": Pain(self,sg)
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

