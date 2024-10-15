import os

#  Obtener el directorio Actual
"""cwd = os.getcwd() #Current Working Directory
print("Directorio de trabajo actual", cwd)"""

# Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt:", txt_files)

# Renombrar archivo
os.rename('caperucita.txt', 'cuento.txt')
print('Archivo renombrado')

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt:", txt_files)