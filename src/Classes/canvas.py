from customtkinter import CTkCanvas
from .App import App
from .App import Turns

class QuadradoFoda(CTkCanvas):
    parent: App
    width: int
    height: int
    owner = None
    ownerVal = 0
    
    def __set__(self, parent, r, w):
        self.parent = parent
        self.grid(row=r, column=w)
        self.create_rectangle(0, 0, self.width, self.height, fill="#ffb691")


    def __draw_Equivalence(self):
        m = 7
        
        if self.owner == Turns.Player1:
            self.create_line(
                self.width/m, self.height/m,
                (m-1)*self.width/m, (m-1)*self.height/m,
                fill="black", width=15*3/self.parent.Sqrs)
            
            self.create_line(
                self.width/m, (m-1)*self.height/m,
                (m-1)*self.width/m, self.height/m,
                fill="black", width=15*3/self.parent.Sqrs)
            return
        
        self.create_oval(
            self.width/m, self.height/m,
            (m-1)*self.width/m, (m-1)*self.height/m,
            width=15*3/self.parent.Sqrs
        )               

    def __clicked__(self, event):
        if self.owner or self.parent.turno == Turns.OVER: return
        print(self.parent.turno)
        
        self.owner = self.parent.turno
        self.ownerVal += int(self.owner == Turns.Player1)*2 -1
        self.__draw_Equivalence()
        self.parent.qntOwned += 1
        self.parent._Handle_Turn()


    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height)
        
        self._bg_color = "red"
        self.width = width
        self.height= height
        
        self.bind('<Button-1>', self.__clicked__)