import tkinter as tk

class Interfaz:
    def __init__(self,root:tk.Tk):
        self.root = root

        self.root.title("Ventana Principal")
        self.root.geometry("600x450")

        #ventana principal
        btnAbrir=tk.Button(self.root,text="Cargar Archivo XML",command=self.abrirArchivo)
        btnAbrir.place(x=10,y=5)

        btnBorrar=tk.Button(self.root,text="Borrar Lista",command=self.borrar)
        btnBorrar.place(x=90,y=410)

        btnActualizar=tk.Button(self.root,text="Actualizar Lista",command=self.actualizar)
        btnActualizar.place(x=170,y=410)

        btnAyuda=tk.Button(self.root,text="Ayuda",command=self.ayuda)
        btnAyuda.place(x=550,y=5)

        lblEntrada=tk.Label(self.root,text="Listado de maquetas")
        lblEntrada.place(x=10,y=50)

        self.txtEntrada=tk.Text(self.root,width=40, height=20)
        self.txtEntrada.place(x=10,y=80)


        frmFrameGestionar=tk.Frame(self.root,width=220, height=220,borderwidth=2, relief="ridge", bg="lightgrey")
        frmFrameGestionar.place(x=350,y=125)

        #form
        lblframe=tk.Label(frmFrameGestionar, text="Gestionar maqueta")
        lblframe.place(x=60,y=5)

        lblNombre=tk.Label(frmFrameGestionar, text="Nombre de la maqueta",)
        lblNombre.place(x=50,y=40)

        self.txtNompreMaqueta=tk.Entry(frmFrameGestionar,width=33)
        self.txtNompreMaqueta.place(x=7,y=70)

        btnGraficarMaqueta=tk.Button(frmFrameGestionar,text="Graficar Maqueta",command=self.graficarMaqueta)
        btnGraficarMaqueta.place(x=5,y=95)

        btnGraficarMaqueta=tk.Button(frmFrameGestionar,text="Graficar Solucion",command=self.graficarSolucion)
        btnGraficarMaqueta.place(x=110,y=95)



    def abrirArchivo(self):
        print("este boton abrira un archivo")

    def borrar(self):
        print("este boton borrara las listas y tood lo que este en el cuadros de texto")
    
    def actualizar(self):
        print("Este boton actualizara lo que hay en las listas")

    def ayuda(self):
        print("este boton proporcionara informacion de del estudiante y su documentacion")
    
    def graficarMaqueta(self):
        print("este boton realizara una imagen con graphviz de la maqueta")

    def graficarSolucion(self):
        print("este boton realizara una imagen con graphviz de la solucion y la maqueta")