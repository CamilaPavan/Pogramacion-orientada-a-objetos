"""###Ejercicio 2.3
Utilizando la clase Pila y sus metodos
*  Permitir que el usuario cargue valores en una Pila
*  Reemplazar todas las ocurrencias de un determinado elemento en una pila."""

import ClasePila as cp

pila_1 = cp.Pila()

while True:
    x = input("Ingrese lo que desea ingresar a la pila, si ingresa BASTA se corta el ingreso: ")
    if x == "BASTA":
        break
    else:
        pila_1.apilar(x)

ocurrencia_a_reemplazar = input("Ingrese la palabra que va reemplazar: ")
ocurrencia_que_reemplaza = input("Ingrese la palabra que reemplazara: ")


print("Pila al inicio")
pila_1.ver_pila()

pila_aux = cp.Pila()

for i in range(pila_1.get_tamanio()):
    elemento = pila_1.desapilar()
    if elemento == ocurrencia_a_reemplazar:
        pila_aux.apilar(ocurrencia_que_reemplaza)
    else:
        pila_aux.apilar(elemento)

print("Pila al con elemento reemplazado y desordenada")
pila_aux.ver_pila()

#volvemos a apilar la pila inicial
for i in range(pila_aux.get_tamanio()):
    pila_1.apilar(pila_aux.desapilar())

print("Pila al con elemento reemplazado y ordenada")
pila_1.ver_pila()
