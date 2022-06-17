"""
###**Ejercicio 3.6**
Crear una clase Persona con metodos estaticos, de clase y de instancia.
- Tiene que tener un atributo de clase: Nacionalidad

Los metodos a crear son:
- Conctructor con atributos DNI, nombre, apellido
-  **Metodos de clase:** set y get nacionalidad
-  **Metodos de intancia:** setters y getters, crear con @propierty
-  **Metodos estaticos:** ejercicio anterior

Crear un menu para probar todos los requerimientos
"""

class Persona (): 
    nacionalidad = "argentina"
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def set_nacionalidad(cls,x):
        cls.nacionalidad = x

    @classmethod
    def get_nacionalidad (cls):
        return cls.nacionalidad

    
