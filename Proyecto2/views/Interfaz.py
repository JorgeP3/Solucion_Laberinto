#Listas
from controllers.ListaMaquetas import ListaMaquetas
from controllers.ListaObjetivos import ListaObjetivos
from controllers.ListaEstructuras import ListaEstructuras

#Clases
from models.Maqueta import Maqueta
from models.Entrada import Entrada
from models.Objetivo import Objetivo
from models.Estructura import Estructura

#Librerias
import tkinter as tk
from tkinter import messagebox
import webbrowser
from tkinter import filedialog
from xml.dom import minidom

#instancia global de la lista maquetas
lista_maquetas=ListaMaquetas()
#lista_objetivos=ListaObjetivos() esta instancia me creaba problemas
#en esta lista se guardaban todos los objetos "objetivo" de todas las maquetas
#no solamente a los que si pertenecian, se movio la instancia mas abajo y funciono
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

        #FRAME
        frmFrameGestionar=tk.Frame(self.root,width=220, height=220,borderwidth=2, relief="ridge", bg="lightgrey")
        frmFrameGestionar.place(x=350,y=125)

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

        btnOrdebarMaqueta=tk.Button(frmFrameGestionar,text="Ordenar Maquetas \npor nombre",command=self.ordenarLista)
        btnOrdebarMaqueta.place(x=55,y=125)

    def abrirArchivo(self):
        try:
            path = filedialog.askopenfilename(
                title="Selecciona un archivo",
                initialdir="C:/Users/lmpgp/Documents/1. Ingenieria en sistemas/1. Introduccion a la computacion 2/Laboratorio IPC2/IPC2_Proyecto2_201213421/Proyecto2",
                filetypes=(("Archivos de texto", "*.xml"), ("Todos los archivos", "*.*"))
            )
            print("Ruta del archivo seleccionado:", path)
            
            xml=minidom.parse(path)
            maquetas=xml.getElementsByTagName("maqueta")

            for maqueta in maquetas:
                #listas
                lista_objetivos=ListaObjetivos()
                lista_estructuras=ListaEstructuras()
                #VARIBLES MAQUETA
                nombreMaqueta=(maqueta.getElementsByTagName("nombre")[0].firstChild.data)
                filasMaqueta=int(maqueta.getElementsByTagName("filas")[0].firstChild.data)
                columnasMaqueta=int(maqueta.getElementsByTagName("columnas")[0].firstChild.data)

                entrada=maqueta.getElementsByTagName("entrada")[0]

                #objetivos
                objetivos=maqueta.getElementsByTagName("objetivos")[0]
                objetivoL=objetivos.getElementsByTagName("objetivo")
                
                #lista de objetivos
                for objetivo in objetivoL:
                    nombreObjetivo=objetivo.getElementsByTagName("nombre")[0].firstChild.data
                    filaObjetivo=int(objetivo.getElementsByTagName("fila")[0].firstChild.data)
                    columnaObjetivo=int(objetivo.getElementsByTagName("columna")[0].firstChild.data)

                    nuevoObjetivo=Objetivo(nombreObjetivo.strip(),
                                           filaObjetivo,
                                           columnaObjetivo)
                    lista_objetivos.insertar_objetivo(nuevoObjetivo)

                estructura=maqueta.getElementsByTagName("estructura")[0].firstChild.data
                estructuraSE=estructura.strip()

                for i in range(filasMaqueta):
                    for j in range(columnasMaqueta):
                        indice = i * columnasMaqueta + j
                        if indice < len(estructuraSE):
                            lista_estructuras.insertar_estructura(Estructura(i,j,estructuraSE[indice]))

                
                nuevaEntrada=Entrada(int(entrada.getElementsByTagName("fila")[0].firstChild.data),
                                     int(entrada.getElementsByTagName("columna")[0].firstChild.data))
                
                if lista_maquetas.buscar_maqueta_nombre(nombreMaqueta.strip()):
                    messagebox.showerror("Error", f"El nombre de maqueta  «{nombreMaqueta.strip()}» ya existe, no se pudo almacenar")
                else:
                    nuevaMaqueta=Maqueta(nombreMaqueta.strip(),
                                        filasMaqueta,
                                        columnasMaqueta,
                                        nuevaEntrada,
                                        lista_objetivos,
                                        lista_estructuras)
                    
                    lista_maquetas.insertar_maqueta(nuevaMaqueta)
            
            lista_maquetas.imprimir_lista_maquetas()

            self.txtEntrada.delete("1.0", tk.END)  # Limpiar el contenido existente
            self.txtEntrada.insert(tk.END, lista_maquetas.txt_maquetas())

            '''
            archivo = open(path, "r", encoding="utf-8")
            texto_entrada = archivo.read()

            self.txtEntrada.delete("1.0", tk.END)  # Limpiar el contenido existente
            self.txtEntrada.insert(tk.END, texto_entrada)
            '''
        except FileNotFoundError:
            print("\033[91mError no se encontró el archivo\033[0m")

    def borrar(self):
        global lista_maquetas
        lista_maquetas = ListaMaquetas()
        self.txtEntrada.delete("1.0", tk.END)
    
    def actualizar(self):
        print("Este boton actualizara lo que hay en las listas")

    def ayuda(self):
        resultado=messagebox.askquestion("¿Desea ver la documentacion?", "Estudiante: Jorge Estuardo Pumay Soy \nCarnet: 201213421\nIntroducción a la programación y computacion 2\nSecciónn: N\n\nhttps://drive.google.com/drive/u/0/folders/1IPnevElS62--NXbgSsCxPlHbopFFWySJ")
        if resultado == "yes":
            webbrowser.open_new("https://drive.google.com/drive/u/0/folders/1IPnevElS62--NXbgSsCxPlHbopFFWySJ")
            
    def graficarMaqueta(self):
        print("este boton realizara una imagen con graphviz de la maqueta") 

    def graficarSolucion(self):
        print("este boton realizara una imagen con graphviz de la solucion y la maqueta")

    def ordenarLista(self):
        lista_maquetas.ordenar_maquetas_por_nombre()
        self.txtEntrada.delete("1.0", tk.END)  # Limpiar el contenido existente
        self.txtEntrada.insert(tk.END, lista_maquetas.txt_maquetas())