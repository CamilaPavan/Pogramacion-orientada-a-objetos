

class Pila:
    def __init__ (self):
        print ("Se crea una pila vacia.")
        self.items = []

    def apilar (self,x):
        self.items.append(x)
        print (f"se agrega el elemnto {x} en la pila")

    def desapilar (self):
        print("Se elemina el ultimo elemento agregado a la pila, en caso de estar vacia, devuelve error")
        try:
            return self.items.pop()
        except:
            print ("La pila esta vacia")

    def ver_pila (self):
        print (self.items)

    def pila_vacia (self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def get_tamanio (self):
        return len(self.items)

    def get_cima (self):
        return self.items[-1]
    
    def ver_pila (self):
        #opcion 1 : for i in range(len(x)-1,-1,-1):
        for i in reversed(self.items):
            print(i)
