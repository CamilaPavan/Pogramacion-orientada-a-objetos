"""Ejercicio 2.1
Utilizando la clase Pila y sus metodos

Dada una pila de letras determinar cuántas vocales contiene."""
import ClassPila as pi

lista_letras = ['a','b','c','d','e','f']
lista_vocales = ['a','e','i','o','u']

pila_1 = pi.Pila()
pila_aux = pi.Pila()

for i in lista_letras:
    pila_1.apilar(i)
    pila_aux.apilar(i)

cont_vocales =0

for j in range(pila_aux.get_tamanio()):
    if pila_aux.desapilar() in lista_vocales:
        cont_vocales+=1

print(f"La cantidad de vocales es de: {cont_vocales}")