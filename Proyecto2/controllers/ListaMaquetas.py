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


            actual=actual.siguiente

