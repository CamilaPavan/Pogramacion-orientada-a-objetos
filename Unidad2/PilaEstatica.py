class Pila:
    def __init__(self, tamanio):
        print("Crea una pila estatica vacía.")
        self.items=[]
        self.tamanio = tamanio
    
    def apilar(self, x):
        
        if(len(self.items) < self.tamanio):
            self.items.append(x)
            print(f"Agrega el elemento {x} a la pila.")
        else:
            print(f"Pila llena, no es posible agregar {x}")
    
    def desapilar(self):
        print(" Devuelve el elemento tope y lo elimina de la pila.Si la pila está vacía levanta una excepción. ")
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    
    def ver_pila(self):
        print(self.items)