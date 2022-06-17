class Persona:
    def __init__(self,dni,nombre,apellido):
        self.dni=dni
        self.nombre=nombre
        self.apellido = apellido
    
    def set_dni(self,dni_nuevo):
        self.dni = dni_nuevo
    
    def get_dni(self):
        return self.dni

lista_personas = []
persona_1 = Persona("123","agus","cornille")
persona_2 = Persona("560","rami","calvo")
persona_3 = Persona("222","cris","nieto")
lista_personas.append(persona_1)
lista_personas.append(persona_2)
lista_personas.append(persona_3)

def imprimir_lista_objetos(lista):
  for i in lista:
    print(i.get_dni(), end=",")
  print("")
  
def burbuja_mejorado(lista):
  i=0
  control = True
  while( i < len(lista)-1 and control ):
    control = False
    for j in range(0,len(lista)-i-1):
      if(lista[j].get_dni() > lista[j+1].get_dni()):
        lista[j],lista[j+1] = lista[j+1],lista[j]
        control = True
        imprimir_lista_objetos(lista)
    i+=1

imprimir_lista_objetos(lista_personas)
burbuja_mejorado(lista_personas)
imprimir_lista_objetos(lista_personas)