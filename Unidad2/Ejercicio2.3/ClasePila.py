class Pila:
    def __init__(self):
        print("Crea una pila vacía.")
        self.items=[]
    
    def apilar(self, x):
        self.items.append(x)
        print(f"Agrega el elemento {x} a la pila.")
    
    def desapilar(self):
        print(" Devuelve el elemento tope y lo elimina de la pila.Si la pila está vacía levanta una excepción. ")
        try:
            return self.items.pop()
        except:
            print("La pila está vacía")

    def pila_vacia(self):
        if(len(self.items)==0):
            return True
        else:
            return False

    def get_tamanio(self):
        return len(self.items)
    
    def get_cima(self):
        return self.items[-1]

    def ver_pila(self):
        #for i in range(len(x)-1, -1, -1):
        for i in reversed(self.items):
            print(i)


 # ver pila ordenada