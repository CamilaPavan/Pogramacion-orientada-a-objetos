def factorial(numero):
  if(numero == 0):
    return 1
  else:
    return numero * factorial(numero-1)

numero = int(input("Ingrese el numero que quiere el factorial: "))
print(f"Factorial de {numero} = {factorial(numero)}")