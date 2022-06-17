

def sort(lista):
    #creo las 3 listas que voy a necesitar
    menores = []
    igual_o_pivote = []
    mayores = []

    if len(lista) > 1:
        pivote = lista[0]
        for x in lista:
            if x < pivote:
                menores.append(x)
            elif x == pivote:
                igual_o_pivote.append(x)
            elif x > pivote:
                mayores.append(x)
            sort(menores)
            sort(pivote)
            sort(mayores)
        return sort(menores)+igual_o_pivote+sort(mayores) 

lista = [4,9,5,12]
sort(lista)


"""def qsort(lst):
    if len(lst) < 2:
        return lst

    pivot = lst[0]
    left = list(filter(lambda x: x <= pivot, lst[1:]))
    right = list(filter(lambda x: x > pivot, lst[1:]))
    
    print (f"{qsort(left)}  {[pivot]}   {qsort(right)}")


lista = [4,8,12,6,25]
qsort(lista)"""