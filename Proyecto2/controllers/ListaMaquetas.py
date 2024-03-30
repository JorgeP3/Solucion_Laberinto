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
    
      #busca las maquetas por nombre de maqueta y devuelve el objeto    
    def buscar_maqueta_nombre(self,nombreMaqueta):
        actual=self.primero
        while actual:
            if actual.maqueta.nombre==nombreMaqueta:
                return actual.maqueta
            actual=actual.siguiente
        return None
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
            print("")
            self.imprimir_maqueta_consola(actual.maqueta.nombre)
            #print("     "+actual.maqueta.lista_estructuras.txt_estructura())
            print("")
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
            text+=actual.maqueta.lista_objetivos.txt_objetivos()#imprima la lista de este objeto en espesifico
            text+="Estructura: "+"\n\n"
            text+=self.txt_imprimir_maqueta(actual.maqueta.nombre)+"\n"
            #actual.maqueta.lista_estructuras.imprimir_lista_estructuras()
            actual=actual.siguiente
        return text
    
    def ordenar_maquetas_por_nombre(self):
        if self.primero is None:
            return
        actual = self.primero
        while actual:
            minimo = actual
            siguiente = actual.siguiente
            while siguiente:
                if siguiente.maqueta.nombre < minimo.maqueta.nombre:
                    minimo = siguiente
                siguiente = siguiente.siguiente
            if minimo != actual:
                actual.maqueta, minimo.maqueta = minimo.maqueta, actual.maqueta
            actual = actual.siguiente
    
    def imprimir_maqueta_consola(self,nombre):
        maquetaG=self.buscar_maqueta_nombre(nombre)
        for i in range(0,maquetaG.filas):
            for j in range(0,maquetaG.columnas):
                print(maquetaG.lista_estructuras.devolver_caracter(i,j),end=" ")
            print("")
        print("")

    def txt_imprimir_maqueta(self,nombre):
        text=""
        maquetaG=self.buscar_maqueta_nombre(nombre)
        for i in range(0,maquetaG.filas):
            for j in range(0,maquetaG.columnas):
                text+=maquetaG.lista_estructuras.devolver_caracter(i,j)
            text+="\n"
        text+="\n"
        return text