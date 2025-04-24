from customtkinter import CTk, CTkFrame
from enum import Enum
from .func.check import Checker

class Turns(Enum):
    Player1 = 0
    Player2 = 1
    OVER = 2


class App(CTk):
    mainFrame: CTkFrame
    turno = Turns.Player1
    qntOwned = 0
    ArrayFodinhas = [[]]
    Sqrs = 100
    winFactor = 4
    
    def __construct_Grid(self):
        # from .Btn import QuadradoFoda
        from .canvas import QuadradoFoda
        
        self.ArrayFodinhas = [[QuadradoFoda for _ in range(self.Sqrs)] for _ in range(self.Sqrs)]
        
        print(self.ArrayFodinhas)
        
        for i in range(self.Sqrs):
            for j in range(self.Sqrs):
                self.ArrayFodinhas[i][j] = QuadradoFoda(self.mainFrame, 600/self.Sqrs, 600/self.Sqrs)
                self.ArrayFodinhas[i][j].__set__(parent=self, r=i, w=j)

    
    def __init__(self):
        CTk.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.mainFrame = CTkFrame(self, 600, 600, 0, 0, "black")
        self.mainFrame.grid(row=0, column=0)
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        
        self.__construct_Grid()
    
    
    def _Game_Over(self, winner):
        self.turno = Turns.OVER
    
    def _Handle_Turn(self):
        res = Checker.check(self.ArrayFodinhas, self.Sqrs, self.winFactor)
        
        if res != 0:
            winner = Turns.Player1
            if res < 0: winner = Turns.Player2
            return self._Game_Over(winner)
        
        self.__passTurn__()
    
    def __passTurn__(self):
        if self.turno == Turns.Player1: self.turno = Turns.Player2
        else: self.turno = Turns.Player1