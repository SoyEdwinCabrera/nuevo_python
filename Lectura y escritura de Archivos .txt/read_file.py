# Leer un archivo línea por linea
"""with open('cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

# Leer todas las líneas en una lista
"""with open('cuento.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

# Añadir texto
"""with open('cuento.txt', 'a') as file:
    file.write ("\n\nBy:ChatGPT")"""

# Sobreescribir el texto
"""with open('cuento.txt', 'w') as file:
    file.write ("\n\nBy:ChatGPT")"""

# Conteo de lineas
with open('cuento.txt', 'r') as file:
    lines = file.readlines()
    print(f"El archivo tiene {(len(lines))} lineas")