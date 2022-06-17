"""
Ejercicio 2.4
Utilizando la clase Pila y sus metodos

Permitir que el usuario cargue una palabra y cargar letra a letra en una Pila
Con metodos de la pila visualizarla en forma inversa.
"""

import ClassPila as pi


pila_1 = pi.Pila()
palabra = input ("Ingrese la letra que desea cargar en la pila: ")

#Se crea una lista, para tener cada letra. 
palabra_en_lista = list(palabra)

#Se recorre la lista, y se va agregando cada elemento a la pila. 
for i in palabra_en_lista:
    pila_1.apilar(i)


pila_1.ordenar()

