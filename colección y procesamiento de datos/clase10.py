numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])

information = {"nombre": "Edwin",
               "Apellido": "Cabrera",
               "Altura": 1.66,
               "Edad": 35}
print(information)
del information["Edad"]
print(information)

claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)

pairs = information.items()
print(pairs)
contacts = { "Edwin": {"Apellido": "Cabrera",
               "Altura": 1.66,
               "Edad": 35},
              "Diego": {"Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29},
               }
print(contacts["Edwin"])
print(contacts["Diego"])
