squares = [x**2 for x in range (1,11)]
print("Cuadrados:", squares)

celsius =[0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) *32 for temp in celsius]
print("Temperature en F:", fahrenheit)


# Numeros pares

evens = [x for x in range (1,21) if x%2 ==0]
print(evens)

# Transponer una matriz

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# Ejemplo normal

transposed_1 = []
for i in range(len(matrix[0])):
    transposed_1_row = []
    for row in matrix:
        transposed_1_row.append(row[i])
    transposed_1.append(transposed_1_row)


# Ejemplo Comprehension list

transposed = [[row[i] for row in matrix] for i in range (len(matrix[0])) ]

print(matrix)
print(transposed)
print(transposed_1)