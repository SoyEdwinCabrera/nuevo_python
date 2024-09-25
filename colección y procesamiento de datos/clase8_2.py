# Metodo Slice

'''
Cuando asignamos una lista a una nueva variable, por ejemplo,
`B = A`, no estamos creando una copia independiente. 
Ambas variables apuntan al mismo espacio de memoria. 
Así, cualquier cambio en`A`se reflejará en `B`.
'''

a = [1,2,3,4,5]
b = a
print (a)
print (b)

del a[0]
print (id(a))
print (id(b))

c = a[:]
print (id(a))
print (id(b))
print (id(c))

a.append(6)
print (a)
print (b)
print (c)
