# Listas, tuplas e ranges. 

# Lista é uma sequencia ordenada de elementos (pode ser alterada).

cities = ['Los Angeles', 'New York', 'Miami', 'Dallas']
print(cities)
print(cities[3])
print(len(cities))

#list
developer = 'José Augusto'
print(list(developer))

#len
print(len(developer))

#Add valor
cities[0:1] = 'Taperoá', 'CG' 
print(cities)

#Deletando Valor
cities.remove('Taperoá')
del cities[0]
print(cities)

#in 
print('Dallas' in cities)