#Crea un programa en Python que simule una lista de compras. 
# El programa debe permitir al usuario agregar productos al final de la lista, eliminar
# productos del inicio de la lista y mostrar todos los productos en la lista en orden de compra.
class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
class ListaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.size += 1
    def recorrer_inicio_final(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def eliminar_inicio(self):
        if self.vacia():
            print("lista vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1    

    def recorrer_inicio_final(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente
    def vacia(self):
        return self.primero == None

try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaDoble()
        
        while opcion !=7:
            print("\n LISTA DE COMPRAS\n\n 1.Agregar productos final\n 2. Eliminar inicio\n 3.Mostrar recorrido\n 4.Salir")
            opcion = int(input("Ingrese opcion: "))

            if opcion == 1:
                dato = input("Ingrese un producto: ")
                lista.agregar_final(dato)
            elif opcion == 2:
                lista.eliminar_inicio()
            elif opcion == 3:
                lista.recorrer_inicio_final()
            elif opcion == 4:
                print("FIN")
            else:
                print("Ingrese un dato correcto")

except Exception as e:
    print(e)