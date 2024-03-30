from models.Nodo_estructura import Nodo_estructura

class ListaEstructuras:
    def __init__(self):
        self.primero = None
        self.filas=0
        self.columnas=0
                           #ingresa un objeto tipo 
    def insertar_estructura(self,estructura):
        if self.primero is None:
            self.primero = Nodo_estructura(estructura=estructura)
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo_estructura(estructura=estructura)

    def imprimir_lista_estructuras(self):
        actual=self.primero
        while actual !=None:
            print("     Fila:",actual.estructura.fila, "Columna:",actual.estructura.columna, "Caracter:",actual.estructura.caracter )
            actual=actual.siguiente

    def imprimir_matriz_estructuras(self,filas, columnas):
        pass

    def txt_estructura(self):
        actual=self.primero
        text=""
        while actual !=None:
            text+=actual.estructura.caracter
            actual=actual.siguiente
        return text
    
    def devolver_caracter(self,fila,columna):
        actual=self.primero
        while actual !=None:
            if actual.estructura.fila==fila and actual.estructura.columna==columna:
                return actual.estructura.caracter
            actual=actual.siguiente
    