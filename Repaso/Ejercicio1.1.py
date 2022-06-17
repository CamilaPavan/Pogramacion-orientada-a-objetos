"""
El programa debe:

Permitir la carga por teclado un texto con finalización en punto .
Estas palabras separas tienen que estar separadas por un espacio en blanco
Al finalizar la carga el programa debe:

Determinar cuántas palabras tienen 3, 5 o 7 letras
Retornar la cantidad
Guardar en tres listas distintias estas palabras
IMPORTANTE:

Se deben crear metodos y clases a criterio
Gestionar posibles errores
Estructurar el programa a criterio propio
"""

lista_3_letras=[]
lista_5_letras=[]
lista_7_letras=[]
lista_otras = []


print ("""BIENVENDIDO, 
    EL PROGRAMA LE VA A PERMITIR SEPARAR LAS PALABRAS DE UNA TEXTO POR CANTIDAD DE LETRAS
    Recuerde que la oracion debe terminar en un punto""")
    
while True:
    texto = input("Por favor escribi un texto: ")
    if(texto[len(texto)-1]!= '.'): #texto[-1]
        print("La oracion no termina con punto, vuelva a redactar su texto")
    else:
        break

#Se convierte el texto en lista, donde cada palabra es un elemento de la lista.
texto_lista = texto.split()

for i in texto_lista:
    palabra =len(i)
    if palabra == 3:
        lista_3_letras.append(i)
    elif palabra == 5:
        lista_5_letras.append(i)
    elif palabra == 7:
        lista_7_letras.append (i)
    else:
        lista_otras.append(i)

print (f"""
El texto: {texto}
Tiene:
    # {len(lista_3_letras)} palabras con 3 letras, las mismas son {lista_3_letras}
    # {len(lista_5_letras)} palabras con 5 letras, las mismas son {lista_5_letras}
    # {len(lista_7_letras)} palabras con 7 letras, las mimas son {lista_7_letras}
    # Las palabras {lista_otras} no cuentan con la cantidad de letras antes mencionada

""")