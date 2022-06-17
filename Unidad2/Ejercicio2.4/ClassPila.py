
class Pila:
    def __init__ (self):
        self.items=[]


    def apilar (self,x):
        self.items.append(x)

    def desapilar (self):
        try:
            return self.items.pop()
        except:
            print ("La pila esta vacia. ")

    def ordenar (self):
        #se da vuelta los items en la pila, para que los imprima de manera correcta. 
        for i in reversed(self.items):
            print (i)

    def get_tamanio (self):
        return len(self.items)

    def get_cima(self):
        return self.items[-1]
    

