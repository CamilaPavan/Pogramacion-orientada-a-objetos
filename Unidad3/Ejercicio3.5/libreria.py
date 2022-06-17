""" ACA EL CODIGO"""
"""- calcular_edad, parametro (año_nacimiento)
- calcular_peso_promedio, parametro (estatura,genero) [Ayuda]"""

class Persona: 
    @staticmethod 
    def calcular_IMC (peso, altura):
        return (peso /altura **2)