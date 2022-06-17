"""
Bucle por selección. 

Ejercicio 2.14
Dada una lista de letrar, modificar el algoritmo de seleccion para que ordene por orden alfabetico.
"""

def seleccion(lista):
  cont = 0
  for i in range(0,len(lista)-1):
    minimo = i
    for j in range(i+1,len(lista)):
      if(lista[j] < lista[minimo]):
        minimo = j
        print(f"minimo: {lista[minimo]}")
      print(lista)
      cont+=1
    lista[i],lista[minimo] = lista[minimo],lista[i]

  print(f"Cantidad de operaciones: {cont}")


lista= ["x","b", "j", "a"]

seleccion(lista)
