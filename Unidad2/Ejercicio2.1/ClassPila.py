"""
Ejercicio 2.1
Utilizando la clase Pila y sus metodos

Dada una pila de letras determinar cuántas vocales contiene.
"""

class Pila:

    def __init__ (self):
        print ("Se crea una pila vacia. ")
        self.items = []
        

    def apilar(self,x):
        print (f"Se agrega el elemento {x} en la pila")
        self.items.append(x)

    def desapilar (self):
        try:
            return self.items.pop()
        except:
            print ("La pila esta vacia ")

    def ver_pila (self):
        print (self.items)

    def contador_vocales (self):
        contador = 0
        for i in self.items:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                contador += 1
        return contador



