from models.Nodo_maqueta import Nodo_maqueta

class ListaMaquetas:
    def __init__(self):
        self.primero = None
                           #ingresa un objeto tipo maqueta
    def insertar_maqueta(self,maqueta):
        if self.primero is None:
            self.primero = Nodo_maqueta(maqueta=maqueta)
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo_maqueta(maqueta=maqueta)

    def imprimir_lista_maquetas(self):
        actual=self.primero
        while actual !=None:
            print("================================================")
            print("Nombre:",actual.maqueta.nombre)
            print("Filas:",actual.maqueta.filas)
            print("Columnas:",actual.maqueta.columnas)
            print("Entrada")
            print("     Fila:",actual.maqueta.entrada.fila)
            print("     Columna:",actual.maqueta.entrada.columna)
            print("     Caracter:",actual.maqueta.entrada.caracter)
            print("Objetivos:")
            actual.maqueta.lista_objetivos.imprimir_lista_objetivos()
            print("Estructura:")
            print("     "+actual.maqueta.lista_estructuras.txt_estructura())
            #actual.maqueta.lista_estructuras.imprimir_lista_estructuras()
            actual=actual.siguiente

    def txt_maquetas(self):
        actual=self.primero
        text=""
        while actual !=None:
            text+="======================================\n"
            text+="Nombre: "+actual.maqueta.nombre+"\n"
            text+="Filas: "+str(actual.maqueta.filas)+"\n"
            text+="Columnas: "+str(actual.maqueta.columnas)+"\n"
            text+="Entrada "+"\n"
            text+="     Fila: "+str(actual.maqueta.entrada.fila)+"\n"
            text+="     Columna: "+str(actual.maqueta.entrada.columna)+"\n"
            text+="     Caracter: "+actual.maqueta.entrada.caracter+"\n"
            text+="Objetivos: "+"\n"
            text+=actual.maqueta.lista_objetivos.txt_objetivos()
            text+="Estructura: "+"\n"
            text+="     "+actual.maqueta.lista_estructuras.txt_estructura()+"\n"
            #actual.maqueta.lista_estructuras.imprimir_lista_estructuras()
            actual=actual.siguiente
        return text

