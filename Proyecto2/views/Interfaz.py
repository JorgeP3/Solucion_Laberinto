import tkinter as tk

class Interfaz:
    def __init__(self,root:tk.Tk):
        self.root = root

        self.root.title("Ventana Principal")
        self.root.geometry("400x200")