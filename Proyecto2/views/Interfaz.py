import tkinter as tk

class Interfaz:
    def __init__(self,root:tk.Tk):
        self.root = root

        self.root.title("Ventana Principal")
        self.root.geometry("600x500")


        btnAbrir=tk.Button(self.root,text="Cargar Archivo XML",command=self.abrirArchivo)
        btnAbrir.place(x=10,y=5)

        btnBorrar=tk.Button(self.root,text="Borrar Lista",command=self.borrar)
        btnBorrar.place(x=10,y=450)

        btnActualizar=tk.Button(self.root,text="Actualizar Lista",command=self.actualizar)
        btnActualizar.place(x=120,y=450)

        lblEntrada=tk.Label(self.root,text="Listado de maquetas")
        lblEntrada.place(x=10,y=50)

        self.txtEntrada=tk.Text(self.root,width=40, height=20)
        self.txtEntrada.place(x=10,y=80)


        frFrameGestionar=tk.Frame(self.root,)


    def abrirArchivo(self):
        print("este boton abrira un archivo")

    def borrar(self):
        print("este boton borrara las listas y tood lo que este en el cuadros de texto")
    
    def actualizar(self):
        print("Este boton actualizara lo que hay en las listas")