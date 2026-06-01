import tkinter as tk
from tkinter.font import Font
import matplotlib as mpl
import numpy as np

root = tk.Tk()

root.title("GRAFIT")
root.geometry("1000x600")

title = tk.Label(text="GRAFIT - Gerador de Gráficos Táteis (Cinemática)", font=Font(size=20, weight="bold", family="Helvetica"))
title.pack()


root.mainloop()