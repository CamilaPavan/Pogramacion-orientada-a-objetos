from libreria import Persona as pe
#Solo importamos lo que nos importa


try:
  peso = int(input("ingrese el peso: "))
  estatura = int(input("ingrese su estatura: "))
except:
  print("Error")

print(f"El IMC = {pe.Persona.calcular_IMC(peso,estatura)}")