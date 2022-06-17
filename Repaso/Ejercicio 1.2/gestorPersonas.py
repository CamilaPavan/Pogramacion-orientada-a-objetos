
import ClassPersonas as cp



lista_personas = []
dni_lista = []
 

class GestorPersonas():
    def chequear_que_sea_unico(self,dni): 
        flag_agregar = True
        for persona in lista_personas: 
            if dni == persona.dni:
                flag_agregar = False
                return flag_agregar
        if flag_agregar==True :
            return flag_agregar
    
    
    def crear_persona(self):
        #tipo de persona
        while True:
            tipo = input( """
            Ingrese que tipo de personas desea crear:
            1. Persona
            2. Empleado
            opcion: """)
            if tipo == "1":
                break
            elif tipo == "2":
                break
            else:
                print ("No ingreso una opcion correcta")
    
    
        #DNI
        while True:
            try:
                dni = int (input("ingrese el dni: "))
                if self.chequear_que_sea_unico(dni):
                    break
                else:
                    print("el dni ya se encuentra en el sistema")
            except:
                print ("Por favor ingrese un valor numerico")
    
        #nombre
        nombre = input("Ingrese el nombre: ")
        #apellido
        apellido = input  ("Ingrese el apellido: ")
    
    
        if tipo == "1":
            instacia = cp.Personas(dni,nombre,apellido)
        elif tipo == "2":
            #funcion
            funcion = input ("ingrese la funcion del empleado: ")
            #anio ingreso
            ano_ingreso = input ("ingrese el anio de ingreso: ")
            instacia = cp.Empleado (dni,nombre,apellido,funcion, ano_ingreso)
    
        lista_personas.append(instacia)
        
    

    #Imprimer un None despues de cada persona Y NO SE PORQUEEEEEEEEE. 
    def presentar (self):
        print (f"PERSONA \t APELLIDO \t DNI")
        for i in lista_personas:
            print (i.presentar())



    #FUNCIONA, PERO NO SE COMO ACOMODAR CON ESTA LISTA DE DNI, LA LISTA DE PERSONAS. 
    def ordenar_lista_segun_dni (self):
        dni_menor = 9999999999999999 
        for i in lista_personas:
            dni_por_persona = i.get_dni()
            #print (dni_por_persona) 
            if dni_menor > dni_por_persona:
                dni_lista.insert(0,dni_por_persona)
                dni_menor = dni_por_persona
            else:
                dni_lista.append
        print (dni_lista)

    #SI FUNCIONA
    def ordenar_sorted (self):
        lista_ordenada_por_dni = sorted(lista_personas, key = lambda persona : persona.dni)
        print ("lista ordenada segun DNI: ")
        for i in lista_ordenada_por_dni:
            print (i.presentar())


    def ordenar_por_ingreso(self):
        print ("no esta hecha, copiaria el formato de sorted")

        


    def eliminar_ultimo (self):
        lista_personas.pop()
        for i in lista_personas:
            print (i.presentar())










