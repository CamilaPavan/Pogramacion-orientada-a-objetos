"""
Utilizando la clase Cola y sus métodos

*   Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
"""

import ClassCola as co

cola_1 = co.Cola()

cola_1.encolar(4)
cola_1.encolar(7)
cola_1.encolar(12)
cola_1.encolar(6)
cola_1.encolar(5)
cola_1.encolar(23)
cola_1.encolar(10)

print(cola_1.get_tamanio())

cola_aux = co.Cola()

for i in cola_1.items:
    contador = 0
    for j in range(1,i):
        if i % j == 0:
            contador +=1
    if contador >= 2:
        print (f"El numero {i} NO es primo, se mantiene en la cola")
        cola_aux.encolar(i)
    else:
        print (f"El numero {i} es primo, se borra de la cola. ")


cola_aux.ver_cola()

