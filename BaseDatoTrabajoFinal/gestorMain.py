import gestor as gp
import server as ser
from firebase_admin import db

#Instancio la clase GESTOR
gestorbd = gp.Gestor_BD()

def crear_usuario():
    #Me conecto a la base de datos
    ref = db.reference("/")
    #Obtengo la base de datos, get
    base_de_dato = ref.get()
    print("") 
    #Solicito nombre de la persona
    while True:
        nombre = input("Ingrese el nombre: ").capitalize()
        if nombre.isalpha():
            break
        else:
            print("Error, reintentar.")
    #Solicito apellido de la persona
    while True:
        apellido = input("Ingrese el apellido: ").capitalize()
        if apellido.isalpha():
            break
        else:
            print("Error, reintentar.")
    flag = True
    while flag:
        contador = 0 #Si su valor varia entonces el mail esta registrado
        mail = input("Ingrese el mail: ").lower()
        if "@" in mail and ".com" in mail and base_de_dato != None: #Comparo mail si la base de datos no esta vacia  
            mail_a_buscar = mail
            for clave, valor in base_de_dato.items():
                #Si el mail de la persona es igual al ingresado, imprimo error
                if(valor["Mail"] == mail_a_buscar):
                    print("Mail ya registrado, intente nuevamente.")
                    contador += 1 #Encontro el mail, entonces modifico la variable
            if contador == 0: #Solo rompe el while si el mail no fue encontrado en la base de datos
                flag = False
        elif "@" in mail and ".com" in mail: #Si la base de datos esta vacia solo comparo que sea un mail valido
            flag = False
        else:
            print("El mail debe contener un @ y terminar en .com.")
    #Obtenemos la cantidad de personas registradas en el diccionario
    if base_de_dato != None: #None indica si la base de datos esta vacia, no entra si esta vacia
        for clave,valor in base_de_dato.items():
            lista_vacia = []
            lista_vacia.append(clave)
            ultima_persona = lista_vacia[-1]
            id_persona = int(ultima_persona[-1])+1
    else: #Si la base de datos esta vacia crea un usuario admin por defecto que no se puede borrar
        base_de_dato = {"AsuarioAdmin0":{
                        "Nombre": "Null",
                        "Apellido": "Null",
                        "Mail": "Null"
        }}
        id_persona = 1
    #Convierto a string la persona con el ID
    persona = ("Persona" + str(id_persona)) 
    #Creo un diccionario con los datos que habiamos solicitado de la persona
    dic_usuario = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Mail": mail
    }
    while True:
        opcion = input("Desea registrar su mascota? \n\t1. Si\n\t2. No\nOpcion: ").upper()
        if opcion == "SI" or opcion == "1":
            while True:
                try:
                    nombre_mascota = input("Ingrese el nombre de la mascota: ").capitalize()
                    break
                except:
                    print("Error")
            while True:
                try:
                    tipo_mascota = input("Ingrese que tipo de mascota es: ").capitalize()
                    break
                except:
                    print("Error")
            dic_mascota = {"Nombre Mascota": nombre_mascota,
                            "Tipo de Mascota": tipo_mascota
            }
            #Agregamos la mascota al usuario
            dic_usuario.update({"Mascota": dic_mascota})
            #Agregamos al usuario con la mascota a la base de datos
            base_de_dato.update({persona: dic_usuario})
            #Subimos la informacion a la base de datos
            gestorbd.insertar(ser.ref, base_de_dato)
            print("\nAgregado con exito!!")
            break          
        elif opcion == "NO" or opcion == "2":
            #Agrego a mi base de datos, la persona
            base_de_dato.update({persona: dic_usuario}) #Nunca lo va a pisar, por que el ID cambia cada vez que creo una persona
            #Agrego la persona con sus datos a la base de datos
            #Agrego a la base de datos la informacion, metodo insertar de la clase gestor
            #atributo ref de server y la base de datos
            gestorbd.insertar(ser.ref, base_de_dato)
            print("\nAgregado con exito!!")
            break
        else:
            print("Error, opcion no valida. Reintentar.")

def mostrar_informacion_de_usuario():
    print("")
    #Pedimos un mail a verificar en la base de datos
    mail_a_buscar = input("Ingrese el correo de la persona que desea buscar: ")
    if "@" in mail_a_buscar and ".com" in mail_a_buscar:
        #Llamamos al gestor
        gestorbd.obtener(mail_a_buscar)
    else:
        print("Usted no ha ingresado un mail valido.")

def actualizar_datos():
    print("")
    #Pedimos un mail a verificar en la base de datos
    mail_a_buscar = input("Ingrese el correo de la persona que desea cambiar el dato: ")
    if "@" in mail_a_buscar and ".com" in mail_a_buscar:
        #Llamamos al gestor
        gestorbd.actualizar(mail_a_buscar)
    else:
        print("Usted no ha ingresado un mail valido.")

def eliminar_usuario():
    print("")
    #Pedimos un mail a verificar en la base de datos
    mail_a_buscar = input("Ingrese el correo de la persona que desea eliminar: ")
    if "@" in mail_a_buscar and ".com" in mail_a_buscar: #Esta linea es la que logra que usuario admin no pueda ser eliminado
        #Llamamos al gestor
        gestorbd.eliminar(mail_a_buscar)
    else:
        print("Usted no ha ingresado un mail valido.")

def eliminar_mascota():
    print("")
    #Pedimos un mail a verificar en la base de datos
    mail_a_buscar = input("Ingrese el correo de la persona que desea eliminar la mascota: ")
    if "@" in mail_a_buscar and ".com" in mail_a_buscar: #Esta linea es la que logra que usuario admin no pueda ser eliminado
        #Llamamos al gestor
        gestorbd.eliminar_mascota(mail_a_buscar)
    else:
        print("Usted no ha ingresado un mail valido.")
    print("")
    #Pedimos un mail a verificar en la base de datos
    mail_a_buscar = input("Ingrese el correo de la persona que desea eliminar la mascota: ").lower()
    gestorbd.eliminar_mascota(mail_a_buscar)