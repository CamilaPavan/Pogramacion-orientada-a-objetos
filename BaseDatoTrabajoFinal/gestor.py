from firebase_admin import db

class Gestor_BD:
    def insertar(self, ref, data):
        try:
            ref.set(data)
        except Exception as e: 
            print(e)

    def obtener(self, mail_a_buscar):
        #Me conecto a la base de datos
        ref = db.reference("/")
        #Obtengo la base de datos, get
        base_de_dato = ref.get()
        #Recorro las personas de la base de dato
        flag = True
        while flag:
            if base_de_dato != None: 
                for clave, valor in base_de_dato.items():
                    #Si el mail de la persona es igual al ingresado, imprimo los datos
                    if(valor["Mail"] == mail_a_buscar):
                        print("\t---MAIL REGISTRADO---")
                        #Recorre e imprime en formato clave - valor
                        for clave, valor in valor.items():
                            print(f"\t    {clave}: {valor}")
                            flag = False
                if flag == True:
                    print("Mail no registrado")
                    return
            else:
                print ("No hay usuario registrados en la base de datos.")

    def actualizar(self, mail_a_buscar):
        #Me conecto a la base de datos
        ref = db.reference("/")
        #Obtengo la base de datos, get
        base_de_dato = ref.get()
        #Recorro las personas de la base de dato
        flag = True
        while flag:
            if base_de_dato != None:
                for clave, valor in base_de_dato.items():
                    #Si el mail de la persona es igual al ingresado, imprimo los datos
                    if(valor["Mail"] == mail_a_buscar):
                        while True:
                            dato_cambiar = input("""Ingrese el dato a cambiar:
                                1. Nombre
                                2. Apellido
                            Opcion: """).capitalize()
                            if dato_cambiar == "1" or dato_cambiar == "Nombre":
                                while True:
                                    dato_nuevo = input("Ingrese el nuevo nombre: ").capitalize()
                                    if dato_nuevo.isalpha():
                                        #Actualizo el diccionario con el nuevo nombre
                                        valor.update({"Nombre":dato_nuevo})
                                        #Actualizo la base de datos
                                        ref.update(base_de_dato)
                                        print("---Modificado con exito!---")
                                        return
                                    else:
                                        print("El nuevo nombre solo debe tener letras del alfabeto.")
                            elif dato_cambiar == "2" or dato_cambiar == "Apellido":
                                while True:
                                    dato_nuevo = input("Ingrese el nuevo apellido: ").capitalize()
                                    if dato_nuevo.isalpha():
                                        valor.update({"Apellido":dato_nuevo})
                                        ref.update(base_de_dato)
                                        print("---Modificado con exito!---")
                                        return
                                    else:
                                        print("El nuevo apellido solo debe tener letras del alfabeto.") 
                            else:
                                print("Opcion invalida, reintentar.")
                    #Si no esta, muestro que no esta registrado
                if flag == True:
                    print("Mail no registrado")
                    return
            else:
                print ("No hay usuario registrados en la base de datos.")

    def eliminar(self, mail_a_buscar):
        #Me conecto a la base de datos
        ref = db.reference("/")
        #Obtengo la base de datos, get
        base_de_dato = ref.get()
        #Recorro las personas de la base de dato
        flag = True
        while flag: 
            if base_de_dato != None: 
                #Clave son las personas_ID y valor los campos del diccionario
                for clave, valor in base_de_dato.items():
                    #Si el mail de la persona es igual al ingresado, imprimo los datos
                    if(valor["Mail"] == mail_a_buscar):
                        #Borro y actualizo la base de datos
                        ref.child(clave).set({})
                        print("\nEliminado con exito!!")
                        flag = False
                        return
                if flag == True:
                    print("Mail no registrado")
                    return
            else:
                print ("No hay usuario registrados en la base de datos.")
    
    def eliminar_mascota(self, mail_a_buscar):
        #Me conecto a la base de datos
        ref = db.reference("/")
        #Obtengo la base de datos, get
        base_de_dato = ref.get()
        #Recorro las personas de la base de dato
        flag = True
        while flag:
            if base_de_dato!= None: 
                #Clave son las personas_ID y valor los campos del diccionario
                for clave, valor in base_de_dato.items():
                    #Si el mail de la persona es igual al ingresado, imprimo los datos
                    if (valor["Mail"] == mail_a_buscar):
                        #Si existe el clave en el diccionario retorna el valor sino retorna None
                        valor_1 = valor.get("Mascota") 
                        if valor_1 == None: #Si la clave no existe es por que el usuario no posee ese animal
                            print("El usuario no posee esa mascota.")
                            return
                        elif valor["Mascota"] and valor_1 != None: #Si la clave existe entonces borramos la mascota
                            #Borro el diccionario mascota
                            valor["Mascota"].clear() 
                            #Actualizo la base de datos
                            ref.update(base_de_dato)
                            print("\nEliminado con exito!!")
                            flag = False
                            return
                if flag == True:
                    print("Mail no registrado")
                    return
            else:
                print ("No hay usuario registrados en la base de datos.")


