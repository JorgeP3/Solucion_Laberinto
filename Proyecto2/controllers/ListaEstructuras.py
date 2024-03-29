from models.Nodo_estructura import Nodo_estructura

class ListaEstructuras:
    def __init__(self):
        self.primero = None
                           #ingresa un objeto tipo maqueta
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

    def imprimir_matriz_estructuras(self):
        pass