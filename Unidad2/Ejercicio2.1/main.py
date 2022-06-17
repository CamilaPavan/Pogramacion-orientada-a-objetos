"""
Ejercicio 2.1
Utilizando la clase Pila y sus metodos

Dada una pila de letras determinar cuántas vocales contiene.
"""

import ClassPila as pi


pila_1 = pi.Pila() #Se crea el objeto. 
pila_2 = pi.Pila() 

pila_1.apilar("a")
pila_1.apilar("no")
pila_1.apilar("e")
pila_1.apilar("u")
pila_1.apilar("v")
pila_1.apilar("i")


pila_1.ver_pila()



print (f"La pila tiene {pila_1.contador_vocales()} vocales")




