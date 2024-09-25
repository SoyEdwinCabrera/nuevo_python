# Estructura
'''
try:
    pass
except:
    pass
'''

try:
    divisor = int(input("Ingresa un numero divisor: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero")
    print("Ha ocurrido un error: ", e)
except ValueError as e:
    print("Error: Desbes introducir un número válido")
    print("Ha ocurrido un error: ", e)
