from models.Nodo_maqueta import Nodo_maqueta

class ListaMaquetas:
    def __init__(self):
        self.primero = None
                           #ingresa un objeto tipo maqueta
    def insertar_dato(self,maqueta):
        if self.primero is None:
            self.primero = Nodo_maqueta(maqueta=maqueta)
            return
        actual= self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo_maqueta(maqueta=maqueta)

    def imprimir_lista(self):
        actual=self.primero
        while actual !=None:
            print("Nombre",actual.maqueta.nombre)
            print("Filas",actual.maqueta.filas)
            print("Columnas",actual.maqueta.columnas)
            print("Entrada")
            print("     Filas",actual.maqueta.entrada.fila)
            print("     Columnas",actual.maqueta.entrada.columna)

