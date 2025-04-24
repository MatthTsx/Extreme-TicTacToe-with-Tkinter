import customtkinter as CTK
from Classes.App import App
import threading as th

app = App()
app.title("Velha velhada")
app.geometry("800x800")

thr = th.Thread(target= app.mainloop)
thr.run()