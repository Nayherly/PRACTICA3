#2. Crea un programa en Python que mantenga un historial de tareas pendientes. 
# El programa debe permitir al usuario agregar una tarea al inicio de la lista, eliminar una tarea del final de la lista 
# y mostrar todas las tareas en la lista en orden inverso al que se agregaron. 
# Además, el programa debe contar la cantidad total de tareas en la lista y mostrar ese número al usuario.

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

    def vacia(self):
        return self.primero == None

    
    def agregar_inicio (self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.primero  = self.primero
            self.primero = aux
        self.size += 1


    def recorrer_final_inicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
         
            

    
    def eliminar_final(self):
        if self.vacia():
            print("lista vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None 
            self.size -= 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1

    def cantidad_tareas(self):
        cantidad = self.size
        print('La cantidad de total de tareas es: ', cantidad)

try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaDoble()
        
        while opcion !=7:
            print("\n HISTORIAL DE TAREAS: \n 1.Agregar tarea al inicio \n 2.Eliminar ultima tarea \n 3.Mostrar tareas inverso \n 4. Cantidad total de tareas \n 5.Salir")
            opcion = int(input("Ingrese opcion: "))

            if opcion == 1:
                dato = input("Ingrese la tarea: ")
                lista.agregar_inicio(dato)
            elif opcion == 2:
                lista.eliminar_ultimo()
            elif opcion == 3:
                lista.recorrer_final_inicio()
            elif opcion == 4:
                lista.cantidad_tareas()

            elif opcion == 5:
                print("FIN")
            else:
                print("Ingrese un dato correcto")

except Exception as e:
    print(e)