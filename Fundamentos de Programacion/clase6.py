# Operadores numéricos
a = 10
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("Potenciación:", a ** b)
print("División:", a / b)
print("Parte entera de la División:", a // b)
print("Modulo:", a % b)
a += 2 # -=. *=, /=
print(a)
operation_1 = 2 + 3 * 4
operation_2 = (2 + 3) * 4
print(operation_1)
print(operation_2)
operation_3 = (2 + 3) * (4**2)/ 8-1
print(operation_3)


'''

# Operadores Aritméticos
a = 5
b = 3

print("Operadores Aritméticos")
print(f"Suma: {a} + {b} = {a + b}")       # Salida: 8
print(f"Resta: {a} - {b} = {a - b}")      # Salida: 2
print(f"Multiplicación: {a} * {b} = {a * b}")  # Salida: 15
print(f"División: {a} / {b} = {a / b}")   # Salida: 1.6666666666666667
print(f"División Entera: {a} // {b} = {a // b}")  # Salida: 1
print(f"Módulo: {a} % {b} = {a % b}")     # Salida: 2
print(f"Potencia: {a} ** {b} = {a ** b}") # Salida: 125

print("\nOperadores de Comparación")
print(f"Igual: {a} == {b} -> {a == b}")   # Salida: False
print(f"Distinto: {a} != {b} -> {a != b}")# Salida: True
print(f"Mayor que: {a} > {b} -> {a > b}") # Salida: True
print(f"Menor que: {a} < {b} -> {a < b}") # Salida: False
print(f"Mayor o igual que: {a} >= {b} -> {a >= b}") # Salida: True
print(f"Menor o igual que: {a} <= {b} -> {a <= b}") # Salida: False

print("\nOperadores Lógicos")
print(f"and: {a} > {b} and {a} > 0 -> {a > b and a > 0}")   # Salida: True
print(f"or: {a} > {b} or {a} < 0 -> {a > b or a < 0}")      # Salida: True
print(f"not: not({a} > {b}) -> {not(a > b)}")              # Salida: False

print("\nOperadores de Asignación")
c = 10
print(f"Asignación: c = {c}")                              # Salida: 10
c += 5
print(f"Asignación de suma: c += 5 -> c = {c}")            # Salida: 15
c -= 3
print(f"Asignación de resta: c -= 3 -> c = {c}")           # Salida: 12
c *= 2
print(f"Asignación de multiplicación: c *= 2 -> c = {c}")  # Salida: 24
c /= 4
print(f"Asignación de división: c /= 4 -> c = {c}")        # Salida: 6.0
c %= 3
print(f"Asignación de módulo: c %= 3 -> c = {c}")          # Salida: 0.0
c = 10
c //= 2
print(f"Asignación de división entera: c //= 2 -> c = {c}") # Salida: 5
c **= 3
print(f"Asignación de potencia: c **= 3 -> c = {c}")       # Salida: 125

print("\nOperadores Bit a Bit")
print(f"AND: {a} & {b} -> {a & b}")    # Salida: 1
print(f"OR: {a} | {b} -> {a | b}")     # Salida: 7
print(f"XOR: {a} ^ {b} -> {a ^ b}")    # Salida: 6
print(f"NOT: ~{a} -> {~a}")            # Salida: -6
print(f"Desplazamiento a la izquierda: {a} << 1 -> {a << 1}") # Salida: 10
print(f"Desplazamiento a la derecha: {a} >> 1 -> {a >> 1}")   # Salida: 2

```Salida&#x20;

Operadores Aritméticos

Suma: 5 + 3 = 8

Resta: 5 - 3 = 2

Multiplicación: 5 \* 3 = 15

División: 5 / 3 = 1.6666666666666667

División Entera: 5 // 3 = 1

Módulo: 5 % 3 = 2

Potencia: 5 \*\* 3 = 125



Operadores de Comparación

Igual: 5 == 3 -> False

Distinto: 5 != 3 -> True

Mayor que: 5 > 3 -> True

Menor que: 5 < 3 -> False

Mayor o igual que: 5 >= 3 -> True

Menor o igual que: 5 <= 3 -> False



Operadores Lógicos

and: 5 > 3 and 5 > 0 -> True

or: 5 > 3 or 5 < 0 -> True

not: not(5 > 3) -> False



Operadores de Asignación

Asignación: c = 10

Asignación de suma: c += 5 -> c = 15

Asignación de resta: c -= 3 -> c = 12

Asignación de multiplicación: c \*= 2 -> c = 24

Asignación de división: c /= 4 -> c = 6.0

Asignación de módulo: c %= 3 -> c = 0.0

Asignación de división entera: c //= 2 -> c = 5

Asignación de potencia: c \*\*= 3 -> c = 125



Operadores Bit a Bit

AND: 5 & 3 -> 1

OR: 5 | 3 -> 7

XOR: 5 ^ 3 -> 6

NOT: ~5 -> -6

Desplazamiento a la izquierda: 5 << 1 -> 10

Desplazamiento a la derecha: 5 >> 1 -> 2
'''