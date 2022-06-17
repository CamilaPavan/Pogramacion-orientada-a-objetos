class Personas():
    def __init__(self,dni,nombre,apellido):
        self.dni=dni
        self.nombre=nombre
        self.apelido =apellido
   
    def get_dni (self):
        return self.dni
 
    def set_dni (self,dni):
        self.dni= dni
        print(f"el dni ahora es {dni}")

    #Me imprime un NONE despues de cada persona
    def presentar (self):
        print (f"{self.nombre}. \t   {self.apelido}. \t  {self.dni}.")

 

class Empleado (Personas):
    def __init__(self, dni, nombre, apellido,funcion,ano_ingreso):
        super().__init__(dni, nombre, apellido)
        self.funcion=funcion
        self.ano_ingreso= ano_ingreso
 
    def get_funcion (self):
        return self.funcion
 
    def set_funcion (self,funcion):
        self.funcion= funcion
        print(f"La funcion ahora es {funcion}")