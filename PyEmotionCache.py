from enum import Enum

from PyEmotions import *

class Mood(Enum):
    Joyful = 1
    Sad = 2
    Angry = 3

    Happy = 4
    Excstatic = 5
    Excited = 6

    Frustrated = 7
    Annoyed = 8
    Mad = 9

    Depressed = 10
    Sorrow = 11
    Pain = 12


class StateCache:




    def __init__(self):



        self.states = {Mood.Joyful: JoyfulState(self),
                       Mood.Sad: SadState(self), Mood.Angry: AngryState(self),
                       Mood.Happy: Happy(self),
                       Mood.Excstatic: Excstatic(self),
                       Mood.Excited: Excited(self),
                       Mood.Frustrated: Frustrated(self),
                       Mood.Annoyed: Annoyed(self), Mood.Mad: Mad(self),
                       Mood.Depressed: Depressed(self),
                       Mood.Sorrow: Sorrow(self), Mood.Pain: Pain(self)}

    def JoyFulState(self):
        return self.states[Mood.Joyful]

    def SadState(self):
        return self.states[Mood.Sad]

    def AngryState(self):
        return self.states[Mood.Angry]

    def HappyState(self):
        return self.states[Mood.Happy]

    def ExcstaticState(self):
        return self.states[Mood.Excstatic]

    def ExcitedState(self):
        return self.states[Mood.Excited]

    def FrustratedState(self):
        return self.states[Mood.Frustrated]

    def MadState(self):
        return self.states[Mood.Mad]

    def AnnoyedState(self):
        return  self.states[Mood.Annoyed]

    def SorrowState(self):
        return self.states[Mood.Sorrow]

    def PainState(self):
        return self.states[Mood.Pain]

    def DepressedState(self):
        return self.states[Mood.Depressed]

