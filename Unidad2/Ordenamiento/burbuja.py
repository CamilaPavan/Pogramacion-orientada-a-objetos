#este metodo recorre los items y los compara adyacentemente. 

"""def burbuja(lista):
for i in range(0,len(lista)-1):
for j in range(0,len(lista)-i-1): #ubicarme en el valor de I? 
    if(lista[j] > lista[j+1]):
    lista[j],lista[j+1] = lista[j+1],lista[j]
    print(lista)

lista = [8,7,6,5,4,3,2,1]
burbuja(lista)
print(lista)"""


def burbuja_mejorado(lista):
  i=0
  control = True
  while( i <= len(lista)-2 and control ):
    control = False
    for j in range(0,len(lista)-i-1):
      if(lista[j] > lista[j+1]):
        lista[j],lista[j+1] = lista[j+1],lista[j]
        control = True
        print(lista)
    i+=1

lista = [10,2,3,8,5,6,7,9]
#lista = [8,7,6,5,4,3,2,1]
burbuja_mejorado(lista)
print(lista)