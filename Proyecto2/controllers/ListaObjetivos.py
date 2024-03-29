from models.Nodo_objetivo import Nodo_objetivo

class ListaObjetivos:
    def __init__(self):
        self.primero = None
                           #ingresa un objeto tipo maqueta
    def insertar_maqueta(self,objetivo):
        if self.primero is None:
            self.primero = Nodo_objetivo(objetivo=objetivo)
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo_objetivo(objetivo=objetivo)

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


            actual=actual.siguiente