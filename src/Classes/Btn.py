# DECRAPTED: see why in line 15

from customtkinter import CTkButton
from .App import App

class QuadradoFoda(CTkButton):
    parent: App
    
    def __set__(self, parent, r, w):
        self.parent = parent
        self.grid(row=r, column=w)
        self.configure(text="X")
        self.configure(font=(self._font, 200))
        
        # the text-font is too awful

    
    
    def __init__(self, master, width, height):
        super().__init__(master, width=width, height=height)
        self._bg_color = "red"
        
        print("QuadradoFoda iniciado")
        pass