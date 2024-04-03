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
import graphviz

#instancia global de la lista maquetas
lista_maquetas=ListaMaquetas()
#lista_maquetas2=ListaMaquetas() hacer una nueva instancia
#lista_objetivos=ListaObjetivos() esta instancia me creaba problemas
#en esta lista se guardaban todos los objetos "objetivo" de todas las maquetas
#no solamente a los que si pertenecian, se movio la instancia mas abajo y funciono
class Interfaz:
    def __init__(self,root:tk.Tk):
        self.root = root

        self.root.title("Ventana Principal")
        self.root.geometry("600x450")
        #self.lista_maquetas=ListaMaquetas() tamvbien pude definir aqui la lista
        #y acceder a ella desde cualquier metodo utilizando "self"
        self.cargarWidgets()

    def cargarWidgets(self):
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
        self.txtEntrada.delete("1.0", tk.END)  # Limpiar el contenido existente
        self.txtEntrada.insert(tk.END, lista_maquetas.txt_maquetas())

    def ayuda(self):
        resultado=messagebox.askquestion("¿Desea ver la documentacion?", "Estudiante: Jorge Estuardo Pumay Soy \nCarnet: 201213421\nIntroducción a la programación y computacion 2\nSecciónn: N\n\nhttps://drive.google.com/drive/u/0/folders/1IPnevElS62--NXbgSsCxPlHbopFFWySJ")
        if resultado == "yes":
            webbrowser.open_new("https://drive.google.com/drive/u/0/folders/1IPnevElS62--NXbgSsCxPlHbopFFWySJ")
            
    def graficarMaqueta(self):
        nombre=self.txtNompreMaqueta.get()
        
        maquetaG=lista_maquetas.buscar_maqueta_nombre(nombre)

        txtEstructuras=maquetaG.lista_estructuras.txt_estructura()
        print(txtEstructuras)

        nueva_lista_estructuras=ListaEstructuras()
        for i in range(maquetaG.filas):
            for j in range(maquetaG.columnas):
                indice = i * maquetaG.columnas + j
                if indice < len(txtEstructuras):
                    nueva_lista_estructuras.insertar_estructura(Estructura(i,j,txtEstructuras[indice]))
        ##se crea un nuevo objeto
        nuevoObjetoMaqueta=Maqueta(maquetaG.nombre,maquetaG.filas,maquetaG.columnas,
                                   maquetaG.entrada,maquetaG.lista_objetivos,
                                   nueva_lista_estructuras)
       
        if maquetaG:
            #AQUI SE GRAFICA LA MAQUETA
            self.reemplazarYgraficar(nuevoObjetoMaqueta)
            #####
        elif nombre=="":
            messagebox.showerror("Error", f"No se ha ingresado ningun nombre")
        else:
            messagebox.showerror("Error", f"No se encontró la maqueta con nombre «{nombre}» ")
            
    def ordenarLista(self):
        lista_maquetas.ordenar_maquetas_por_nombre()
        self.txtEntrada.delete("1.0", tk.END)  # Limpiar el contenido existente
        self.txtEntrada.insert(tk.END, lista_maquetas.txt_maquetas())

    def reemplazarYgraficar(self,maquetaG):#se debe ingresar un objeto maqueta
        nombreM=maquetaG.nombre
        filasM=maquetaG.filas
        columnasM=maquetaG.columnas
        filaEntrada=maquetaG.entrada.fila
        columnaEntrada=maquetaG.entrada.columna
        caracterEntrada=maquetaG.entrada.caracter

        
        lista_objetivos=maquetaG.lista_objetivos
        lista_estructurasM=maquetaG.lista_estructuras


        if lista_estructurasM.devolver_caracter(filaEntrada,columnaEntrada)=="-": 
            lista_estructurasM.reemplazarCaracter(filaEntrada,columnaEntrada,caracterEntrada)
        elif lista_estructurasM.devolver_caracter(filaEntrada,columnaEntrada)=="*":
            messagebox.showerror("Error", "No se puede colocar el inicio en una pared")
        else:
            messagebox.showerror("Error", "coordenada incorrecta")

        for objetivo in lista_objetivos:#por cada objetivo de la lista objetivos, se remplaza en la lista de estructuras
            if lista_estructurasM.devolver_caracter(objetivo.fila,objetivo.columna)=="-":
                lista_estructurasM.reemplazarCaracter(objetivo.fila, objetivo.columna, objetivo.nombre)
                
                #funcion graficar
            elif lista_estructurasM.devolver_caracter(objetivo.fila,objetivo.columna)=="*":
                messagebox.showerror("Error", "No se puede colocar un objetivo en una pared")

            elif lista_estructurasM.devolver_caracter(objetivo.fila,objetivo.columna)=="+":
                messagebox.showerror("Error", "No se puede colocar un objetivo en el inicio")
            else:
                messagebox.showerror("Error", "Objetivo en posicion incorrecta")

        self.graficarConGraphviz(lista_estructurasM,filasM,columnasM,"MaquetaInicial")

        #lista_estructurasM.imprimir_lista_estructuras()
    
    def graficarConGraphviz(self,lista_estructuras,filas,columnas,nombreArchivo):
        
        #texto="digraph G {\n node [shape=plaintext];\nlabel=\"Tablero facilito\";\nsome_node [\nlabel=<\n<table border=\"1\" cellborder=\"0\" cellspacing=\"0\" width=\"100%\" height=\"100%\">\n"
        texto="<<table>"
        for i in range(filas):
            texto+="<tr>\n"#fila
            for j in range(columnas):
                if lista_estructuras.devolver_caracter(i,j)=="*":#pared
                    texto+=f"<td bgcolor='black' width='25' height='25'>"+str(lista_estructuras.devolver_caracter(i,j))+"</td>\n" #columna
                elif lista_estructuras.devolver_caracter(i,j)=="-": #camino
                    texto+=f"<td bgcolor='white' width='25' height='25'><font color='white'>"+str(lista_estructuras.devolver_caracter(i,j))+"</font></td>\n"
                elif lista_estructuras.devolver_caracter(i,j)=="+":#inicio
                    texto+=f"<td bgcolor='lime' width='25' height='25'><font color='lime'>"+str(lista_estructuras.devolver_caracter(i,j))+"</font></td>\n"
                elif lista_estructuras.devolver_caracter(i,j)=="#": #solucion
                    texto+=f"<td bgcolor='aqua' width='25' height='25'><font color='aqua'>"+str(lista_estructuras.devolver_caracter(i,j))+"</font></td>\n"
                else: #objetivos
                    texto+=f"<td bgcolor='tomato' width='25' height='25'>"+str(lista_estructuras.devolver_caracter(i,j))+"</td>\n"
            texto+="</tr>\n"
        texto+="</table>>"

        dot = graphviz.Graph(filename=nombreArchivo,format="svg")
        dot.attr('node', shape='plaintext')
        dot.node('tab', texto)

        dot.render(directory='', view=True)
    
    def graficarSolucion(self):
        nombre=self.txtNompreMaqueta.get()
        
        maquetaG=lista_maquetas.buscar_maqueta_nombre(nombre)
        maquetaD=lista_maquetas.buscar_maqueta_nombre(nombre)

        filasM=maquetaG.filas
        columnasM=maquetaG.columnas
        filaEntrada=maquetaG.entrada.fila
        columnaEntrada=maquetaG.entrada.columna

        txtEstructuras=maquetaG.lista_estructuras.txt_estructura()
        lista_objetivos=maquetaG.lista_objetivos.clonar()
        print(txtEstructuras)

        nueva_lista_estructuras=ListaEstructuras()
        lista_solucion=ListaEstructuras()
        for i in range(maquetaG.filas):
            for j in range(maquetaG.columnas):
                indice = i * maquetaG.columnas + j
                if indice < len(txtEstructuras):
                    nueva_lista_estructuras.insertar_estructura(Estructura(i,j,txtEstructuras[indice]))


        if nueva_lista_estructuras.devolver_caracter(filaEntrada,columnaEntrada)=="-": 
            nueva_lista_estructuras.reemplazarCaracter(filaEntrada,columnaEntrada,"+")
        
        for objetivo in lista_objetivos:#por cada objetivo de la lista objetivos, se remplaza en la lista de estructuras
            if nueva_lista_estructuras.devolver_caracter(objetivo.fila,objetivo.columna)=="-":
                                                                                         #NOTA2 se reemplazan los objetivos por paredes "*"                 
                nueva_lista_estructuras.reemplazarCaracter(objetivo.fila, objetivo.columna, "*") #objetivo.nombre
        


        for objetivo in lista_objetivos:
            #NOTA3 antes de aplicar el algoritmo de busqueda, se cambia por su nombre original (A,B,C etc)
            nueva_lista_estructuras.reemplazarCaracter(objetivo.fila, objetivo.columna,objetivo.nombre )
            if self.buscarCamino(filaEntrada,columnaEntrada,nueva_lista_estructuras,objetivo.nombre)==False:
                messagebox.showerror("Error", "no se encontro el objetivo «"+objetivo.nombre+"»")
                break   
            self.buscarCamino(filaEntrada,columnaEntrada,nueva_lista_estructuras,objetivo.nombre)
            filaEntrada=objetivo.fila
            columnaEntrada=objetivo.columna

       
        nueva_lista_estructuras.reemplazarCaracter(maquetaD.entrada.fila,maquetaD.entrada.columna,"+")
        
        for objetivo in lista_objetivos:#por cada objetivo de la lista objetivos, se remplaza en la lista de estructuras
                nueva_lista_estructuras.reemplazarCaracter(objetivo.fila, objetivo.columna, objetivo.nombre)
        
        self.graficarConGraphviz(nueva_lista_estructuras,filasM,columnasM,"MaquetaSolucion")

    #pared=*    camino=-  inicio=+  solucion=# Objetivos=char
        
    def buscarCamino(self,fila,columna,nueva_lista_estructuras,objetivo):
        if nueva_lista_estructuras.devolver_caracter(fila,columna)==objetivo:
            return True
        else:
            if nueva_lista_estructuras.devolver_caracter(fila,columna)!="*" and nueva_lista_estructuras.devolver_caracter(fila,columna)!="#":
                nueva_lista_estructuras.reemplazarCaracter(fila,columna, "#")                                                               
                if  (self.buscarCamino(fila-1,columna,nueva_lista_estructuras,objetivo) or #abajo
                     self.buscarCamino(fila+1,columna,nueva_lista_estructuras,objetivo) or #arriba
                     self.buscarCamino(fila,columna-1,nueva_lista_estructuras,objetivo) or #izquierda
                     self.buscarCamino(fila,columna+1,nueva_lista_estructuras,objetivo)):  #derecha
                    return True
                else:
                    nueva_lista_estructuras.reemplazarCaracter(fila,columna, "-")
        return False
    
