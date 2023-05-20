from abc import ABC,abstractmethod


def p(text):
    print(text)
class Emotions(ABC):

    @abstractmethod
    def EnterState(self):
        pass

    @abstractmethod
    def UpdateState(self):
        pass

    @abstractmethod
    def InitializeSubState(self):
        pass

    def __init__(self,_stateCache):

        self.stateCache = _stateCache

        self.RootState = False

        self.currentSubState = self
        self.currentSuperState = self


    def SwitchState(self,newState):
        newState.EnterState()

        if self.RootState:
            self._stateMachine.currentState = newState
            p("is Root State")

        elif self.currentSuperState is None:
            self.currentSuperState.SetSubstate(self)


    def SetSuperState(self,newSuperState):
        self.currentSuperState = newSuperState

    def SetSubstate(self ,newSubState):
        self.currentSubState = newSubState
        newSubState.SetSuperState(self)
        newSubState.EnterState()


# region SuperStates

class JoyfulState(Emotions):

    def __int__(self,stateCache):
        self.RootState = True



    def EnterState(self):
        print("Welcome To Joyful State :)")
        self.InitializeSubState()

    def UpdateState(self):
        pass

    def InitializeSubState(self):
        self.SetSubstate(self.stateCache.HappyState())

class SadState(Emotions):

    def __int__(self,stateCache):
        self.RootState = True

    def EnterState(self):
        print("Im Sad :(")
        self.InitializeSubState()

    def UpdateState(self):
        pass
    def InitializeSubState(self):
        pass


class AngryState(Emotions):

    def __int__(self,stateCache):
        self.RootState = True

    def EnterState(self):
        print("Im Angry")
        self.InitializeSubState()

    def UpdateState(self):
        pass

    def InitializeSubState(self):
        pass

# endregion

#region Substates

class Happy(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered HappyState")
        self.InitializeSubState()
        self.UpdateState()

    def UpdateState(self):
        pass

    def InitializeSubState(self):
        pass


class Excstatic(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered ExcstaticState")
        self.InitializeSubState()

    def UpdateState(self):
        pass
    def InitializeSubState(self):
        pass


class Excited(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered ExcstaticState")
        self.InitializeSubState()

    def UpdateState(self):
        pass

    def InitializeSubState(self):
        pass


class Frustrated(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered FrustratedState")
        self.InitializeSubState()

    def UpdateState(self):
        pass

    def InitializeSubState(self):
        pass

class Annoyed(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered AnnoyedState")
        self.InitializeSubState()

    def UpdateState(self):
        pass

    def InitializeSubState(self):
        pass

class Mad(Emotions):

    def __int__(self, stateCache):
        pass
    def EnterState(self):
        p("Entered MadState")
        self.InitializeSubState()

    def UpdateState(self):
        pass

    def InitializeSubState(self):
        pass


class Depressed(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered Depressed State")
        self.InitializeSubState()

    def UpdateState(self):
        pass

    def InitializeSubState(self):
        pass

class Sorrow(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered Sorrow State")
        self.InitializeSubState()

    def UpdateState(self):
        pass

    def InitializeSubState(self):
        pass

class Pain(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered Pain State")
        self.InitializeSubState()

    def UpdateState(self):
        pass

    def InitializeSubState(self):
        pass

#endregion