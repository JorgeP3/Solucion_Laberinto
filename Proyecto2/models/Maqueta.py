
class Maqueta:
    def __init__(self,nombre,filas,columnas,entrada,lista_objetivos,lista_estructuras):
        self.nombre=nombre
        self.filas=filas
        self.columnas=columnas
        self.entrada=entrada #esto es un objeto
        self.lista_objetivos=lista_objetivos #Lista de objetivos #esto es una caractreres como "X", "Y", exepto "*" o "-"
        self.lista_estructuras=lista_estructuras #lista de caracteres
    
    def txt_maqueta(self):
        text=""
        text+="Nombre: "+self.nombre+"\n"
        text+="Filas: "+str(self.filas)+"\n"
        text+="Columnas: "+str(self.columnas)+"\n"
        text+="Entrada "+"\n"
        text+="     Fila: "+str(self.entrada.fila)+"\n"
        text+="     Columna: "+str(self.entrada.columna)+"\n"
        text+="     Caracter: "+self.entrada.caracter+"\n"
        text+="Objetivos: "+"\n"
        text+=self.lista_objetivos.txt_objetivos()#imprima la lista de este objeto en espesifico
        text+="Estructura: "+"\n\n"
        text+=self.lista_estructuras.txt_estructura()
        return text

    