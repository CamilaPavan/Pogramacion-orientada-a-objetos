"""
El programa debe:
Contar con:
Contar con una Clase  con los atributos (dni (int - único), nombre (string), apellido (string))
Contar con una Clase Hija  que use el constructor de la clase padre con los atributos:
funcion (string)
año_ingreso (string 'yyyy')
Se deben crear los siguientes métodos para la clase padre Persona (que heredará la clase hija):
Set y Get dni.
Se deben crear los siguientes métodos para la clase hija.
Set y Get funcion.
Se debe contar y crear funciones para un menu que tenga las siguiente opciones,
Crear un empleado y guardarlo en una lista_empleados
Recorrer la lista de empleados segun DNI, mayor a menor o menor a mayor
Recorrer la lista de empleados segun fecha_ingreso, mayor a menor o menor a mayor
Eliminar el ultimo empleado agregado
IMPORTANTE:
Se deben crear metodos y clases a criterio
Gestionar posibles errores
Estructurar el programa a criterio propio
"""

import gestorPersonas as gp
gestor = gp.GestorPersonas()


while True:
    condicion=input(
""" ------ MENU PRINCIPAL ------
Por favor ingrese una opcion
        1. Crear empleado
        2. Recorrer segun DNI
        3. Recorrer segun anio de ingreso
        4. listar
        5. Eliminar ultimo agregado.
        6. Salir
Numero : """)
    if (condicion=="1"): 
        gestor.crear_persona() #Funciona
    elif (condicion=="2"):
        gestor.ordenar_sorted() #Funciona con sorted
    elif (condicion=="3"):
        gestor.ordenar_por_ingreso()  #No esta hecha. 
    elif (condicion=="4"):
       gestor.presentar() #FUNCIONA PERO APARECE UN "None" despues de cada persona.
    elif (condicion == "5"):
        gestor.eliminar_ultimo() #FUNCIONA
    elif (condicion=="6"):
        print ("Gracias") #funciona (? jajaja
        break 
    else:
        print("ninguna opcion correcta")