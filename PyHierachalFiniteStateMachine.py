import PySimpleGUI as sg
from abc import ABC, abstractmethod
from  enum import Enum


def p(text):
    print(text)


class Emotions(ABC):

    @abstractmethod
    def EnterState(self):
        pass

# region SuperStates

class JoyfulState(Emotions):
    def EnterState(self):
        print("Im Happy :)")

class SadState(Emotions):
    def EnterState(self):
        print("Im Sad :(")

class AngryState(Emotions):
    def EnterState(self):
        print("Im Angry")
# endregion

#region Substates

# Happy State
class HappyState(Emotions):
    def EnterState(self):
        p("Entered HappyState")

class Excstatic(Emotions):
    def EnterState(self):
        p("Entered ExcstaticState")

class Excited(Emotions):
    def EnterState(self):
        p("Entered ExcstaticState")

#Angry State
class Frustrated(Emotions):
    def EnterState(self):
        p("Entered FrustratedState")
class Annoyed(Emotions):
    def EnterState(self):
        p("Entered AnnoyedState")
class Mad(Emotions):
    def EnterState(self):
        p("Entered MadState")

#Sad State
class Depressed(Emotions):
    def EnterState(self):
        p("Entered Depressed State")
class Sorrow(Emotions):
    def EnterState(self):
        p("Entered Sorrow State")
class Pain(Emotions):
    def EnterState(self):
        p("Entered Pain State")

#endregion

class Mood(Enum):
    Joyful = 1
    Sad = 2
    Angry = 3


class HumanMood():
    def __init__(self):
        pass

class StateCache():
    humanMood = HumanMood()

    states = { Mood : Emotions }

    def __init__(self,HumanMood=HumanMood):
        self.humanMood = HumanMood

       #self.states[Mood.Joyful] = Continue Heeeeeeeeeee



