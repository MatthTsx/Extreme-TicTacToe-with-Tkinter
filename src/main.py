import customtkinter as CTK
from Classes.App import App
import threading as th

Squares = 3
WinFactor = 4

app = App(Squares, min(WinFactor, Squares))
app.title("Velha velhada")
app.geometry("800x800")

thr = th.Thread(target= app.mainloop)
thr.run()