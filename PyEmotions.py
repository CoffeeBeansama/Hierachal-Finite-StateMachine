from abc import ABC,abstractmethod
import asyncio

def p(text):
    print(text)

def p2(text):
    for i in range(5):
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


    def __init__(self,_stateCache,_main):

        self.stateCache = _stateCache

        self.main = _main

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

    def ChooseSuperState(self):
        while True:
            try:
                SelectedSuperState = int(input("Choose SuperState 1: Joyful, 2: Sad, 3: Angry || 0: to Exit  "))

                if SelectedSuperState == 1:
                    self.SwitchState(self.stateCache.JoyFulState())
                elif SelectedSuperState == 2:
                    self.SwitchState(self.stateCache.SadState())
                elif SelectedSuperState == 3:
                    self.SwitchState(self.stateCache.AngryState())
                elif SelectedSuperState == 0:
                    self.main.ReadEmotion = False
                    break

                else:
                    p("Enter a valid value")


            except ValueError: p("Enter a valid value")

    def ChooseSadSubStates(self):
        while True:
            try:
                SelectedSubState = int(input("Choose SubState 1: Depressed, 2: Sorrow, 3: Pain || 0: to ChangeSuperState "))
                if SelectedSubState == 1:
                    self.SetSubstate(self.stateCache.DepressedState())
                elif SelectedSubState == 2:
                    self.SetSubstate(self.stateCache.SorrowState())
                elif SelectedSubState == 3:
                    self.SetSubstate(self.stateCache.PainState())
                elif SelectedSubState == 0:
                    self.ChooseSuperState()

                else: p("Enter a valid value")

            except ValueError: p("Enter a valid value")

    def ChooseAngrySubState(self):
        while True:
            try:
                SelectedSubState = int(input("Choose SubState 1: Mad, 2: Frustrated, 3: Annoyed || 0: to ChangeSuperState "))
                if SelectedSubState == 1:
                    self.SetSubstate(self.stateCache.MadState())
                elif SelectedSubState == 2:
                    self.SetSubstate(self.stateCache.FrustratedState())
                elif SelectedSubState == 3:
                    self.SetSubstate(self.stateCache.AnnoyedState())
                elif SelectedSubState == 0:
                    self.ChooseSuperState()


                else: p("Enter a valid value")

            except ValueError: p("Enter a valid value")
    def ChooseJoyfulSubStates(self):

        while True:
            try:
                SelectedSubState = int(input("Choose SubState 1: Happy, 2: Ecstatic, 3: Excited || 0: to ChangeSuperState "))

                if SelectedSubState == 1:
                    self.SetSubstate(self.stateCache.HappyState())
                elif SelectedSubState == 2:
                    self.SetSubstate(self.stateCache.EcstaticState())
                elif SelectedSubState == 3:
                    self.SetSubstate(self.stateCache.ExcitedState())
                elif SelectedSubState == 0:
                    self.ChooseSuperState()

                else: p("Enter a valid value")
            except ValueError: p("Enter a valid value")



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
        p("Entered JoyfulState")
        self.InitializeSubState()



    def UpdateState(self):



        self.ChooseSuperState()



    def InitializeSubState(self):
        self.ChooseJoyfulSubStates()


class SadState(Emotions):

    def __int__(self,stateCache):
        self.RootState = True


    def EnterState(self):
        p("Entered SadState")
        self.main.ChangeSuperState = False
        self.InitializeSubState()

    def UpdateState(self):
        if self.main.ChangeSuperState:
            self.ChooseSuperState()

    def InitializeSubState(self):
        self.ChooseSadSubStates()


class AngryState(Emotions):

    def __int__(self,stateCache):
        self.RootState = True

    def EnterState(self):
        p("Entered AngryState")
        self.main.ChangeSuperState = False
        self.InitializeSubState()

    def UpdateState(self):
        if self.main.ChangeSuperState:
            self.ChooseSuperState()

    def InitializeSubState(self):
        self.ChooseAngrySubState()


# endregion

#region Substates

class Happy(Emotions):

    def __int__(self, stateCache):
        pass


    def EnterState(self):
        p("EnteredHappyState")

        self.UpdateState()

    def UpdateState(self):
        p2("HappyState")
        self.ChooseJoyfulSubStates()




    def InitializeSubState(self):
        pass


class Ecstatic(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered Ecstatic State")
        self.UpdateState()

    def UpdateState(self):
        p2("EcstaticState")

        self.ChooseJoyfulSubStates()

    def InitializeSubState(self):
        pass


class Excited(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):

        p("Entered Excited State")
        self.UpdateState()



    def UpdateState(self):
        p2("Excited State")

        self.ChooseJoyfulSubStates()

    def InitializeSubState(self):
        pass


class Frustrated(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered FrustratedState")
        self.UpdateState()

    def UpdateState(self):
        p2("FrustratedState")
        self.ChooseAngrySubState()

    def InitializeSubState(self):
        pass

class Annoyed(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered AnnoyedState")
        self.UpdateState()

    def UpdateState(self):
        p2("Annoyed State")
        self.ChooseAngrySubState()

    def InitializeSubState(self):
        pass

class Mad(Emotions):

    def __int__(self, stateCache):
        pass
    def EnterState(self):
        p("Entered MadState")
        self.UpdateState()

    def UpdateState(self):
        p2("Mad State")
        self.ChooseAngrySubState()

    def InitializeSubState(self):
        pass


class Depressed(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered Depressed State")
        self.UpdateState()

    def UpdateState(self):
        p2("Depressed State")
        self.ChooseSadSubStates()

    def InitializeSubState(self):
        pass

class Sorrow(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered Sorrow State")
        self.UpdateState()

    def UpdateState(self):
        p2("Sorrow State")
        self.ChooseSadSubStates()

    def InitializeSubState(self):
        pass

class Pain(Emotions):

    def __int__(self, stateCache):
        pass

    def EnterState(self):
        p("Entered Pain State")
        self.UpdateState()

    def UpdateState(self):
        p2("Pain State")
        self.ChooseSadSubStates()

    def InitializeSubState(self):
        pass

#endregion