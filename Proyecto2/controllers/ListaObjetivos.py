from models.Nodo_objetivo import Nodo_objetivo
#los objetivos no pueden ir adentro de una pared
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
            print("     Fila:",actual.objetivo.fila)
            print("     Columna:",actual.objetivo.columna)
            print("     -------------")
            actual=actual.siguiente
    
    def txt_objetivos(self):
        actual=self.primero
        text=""
        while actual !=None:
            text+="     Nombre:"+actual.objetivo.nombre+"\n"
            text+="     Fila:"+str(actual.objetivo.fila)+"\n"
            text+="     Columna:"+str(actual.objetivo.columna)+"\n"
            text+="     -------------\n"
            actual=actual.siguiente
        return text
    
    def clonar(self):
        nueva_lista = ListaObjetivos()  
        actual = self.primero
        while actual:
            nueva_lista.insertar_objetivo(actual.objetivo)  
            actual = actual.siguiente
        return nueva_lista
    
    def __iter__(self):
        actual = self.primero
        while actual:
            yield actual.objetivo
            actual = actual.siguiente