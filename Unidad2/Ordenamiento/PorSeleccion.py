"""
Esta funcion recoore la lista, busca a valor mas chico y lo acomoda a la derecha de la lista. 
"""

"""def seleccion(lista):
for i in range(0,len(lista)-1):
minimo = i
for j in range(i+1,len(lista)):
    if(lista[j] < lista[minimo]):
    minimo = j   #guardo en J al valor del minimo. 
lista[i],lista[minimo] = lista[minimo],lista[i]

#lista = [1,2,3,4,5,6,7,8]
lista = [8,7,6,5,4,3,2,1]
seleccion(lista)
print(lista)"""


def seleccion(lista):
  cont = 0 #para pasar en limpio cuantas veces se recorre para acomodarlo. 
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

#lista = [1,2,3,4,5,6,7,8]
lista = [8,7,6,5,4,3,2,1]
seleccion(lista)
print(lista)