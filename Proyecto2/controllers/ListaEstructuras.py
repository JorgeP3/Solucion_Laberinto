from tkinter import messagebox
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

    def reemplazarCaracter(self,fila,columna,caracter):
        actual=self.primero
        while actual:
            if actual.estructura.fila==fila and actual.estructura.columna==columna: #and actual.estructura.caracter=="-":             
                actual.estructura.caracter=caracter
                print("se actualizo el caracter")
                return
            actual=actual.siguiente
        #messagebox.showerror("Error", "No se encontro la coordenada")


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
        return "*" #modificacion

    def clonar(self):
        nueva_lista = ListaEstructuras()  # Creamos una nueva instancia de ListaMaquetas
        actual = self.primero
        while actual:
            nueva_lista.insertar_estructura(actual.estructura)  # Insertamos una copia del objeto maqueta en la nueva lista
            actual = actual.siguiente
        return nueva_lista

    def __iter__(self):
        actual = self.primero
        while actual:
            yield actual.estructura
            actual = actual.siguiente
    