"""
BURBUJA
Ejercicio 2.12
Dada una lista de palabras, modificar el algoritmo de burbuja para que ordene por el largo de estas.
"""

def burbuja_mejorado(lista):
  i=0
  control = True
  while( i <= len(lista)-2 and control ):
    control = False
    for j in range(0,len(lista)-i-1):
      if(len(lista[j]) < len(lista[j+1])):
        lista[j],lista[j+1] = lista[j+1],lista[j]
        control = True
        print(lista)
    i+=1

lista = ["hola","oso","argentina","uruguay","chile"]
burbuja_mejorado(lista)
print(lista)