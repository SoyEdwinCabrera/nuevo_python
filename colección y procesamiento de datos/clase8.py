# LISTAS
to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1, 2, 3, 4, "cinco"]
print(type(numbers)) 
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Último elemento", mix[-1])

string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Último elemento", string[-1])

#slicing

print(mix[0:2]) # es buena practica dejarlo vacio [0:2]
print(mix[2:]) 

#Agregar valores a una lista

print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)


#index
print(mix.index(["a","b"]))
numbers = [1,2,100.01,90.45,3,4,5]
print (numbers)
print("Mayor", max(numbers))
print("Menor", min(numbers))

#eliminar

del numbers[-1]
print(numbers)

del numbers[:2]
print(numbers)

del numbers
print (numbers) # cunado imprimimos, el sistema arroja un error, por que en este punto ya no exite un lista

