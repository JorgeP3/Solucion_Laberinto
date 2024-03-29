from models.Nodo_objetivo import Nodo_objetivo

class ListaObjetivos:
    def __init__(self):
        self.primero = None
                           #ingresa un objeto tipo maqueta
    def insertar_objetivo(self,objetivo):
        if self.primero is None:
            self.primero = Nodo_objetivo(objetivo=objetivo)
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo_objetivo(objetivo=objetivo)

    def imprimir_lista_objetivos(self):
        actual=self.primero
        while actual !=None:
            print("     Nombre:",actual.objetivo.nombre)
            print("     Filas:",actual.objetivo.fila)
            print("     Columnas:",actual.objetivo.columna)
            print("     -------------")
            actual=actual.siguiente