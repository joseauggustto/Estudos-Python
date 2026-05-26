# Strings são sequências de caracteres, usadas para armazenar e manipular texto

name = 'José' 
name1 = "José" #ambos estão certos, python não se importa se é aspas simples ou duplas. 
age = 22 
score = 80.9
altura = 1.89

# Uma string pode ser multilinha, para isso basta usar três aspas simples ou duplas.

string_multilinha = ''' Esta é uma string
multilinha, e isso é interessante para armazenar textos longos, como parágrafos ou até mesmo documentos inteiros.'''

# Se quise saber se algo está em uma streng, basta usar o comando in.

print('multilinha' in string_multilinha)

# INDEXAÇÃO DE STRINGS
# Cada caractere em uma string tem um índice, começando do 0.
#Para pbter o comprimento de uma string, basta usar o comando len().

my_string = "Hello, World!"
print(len(my_string))

#Você pode modificar o valor de uma string, mas não pode modificar os caracteres individuais, pois as strings são imutáveis.
greeting = "hi"
greeting = "hello"
print(greeting)

print("---------------------------------")

# Comando isinstance e type.
 
print(name ,type(name))
print(age, type(age))
print(score, isinstance(score, float))
print(altura, isinstance(altura, float))

#Aspas duplas para a String, informando que é uma citação.

print('She said, "Hello"')
my_str = "Hello"

#Comando in, usado para saber se existe aquilo na string

print("Hello" in my_str)
print('World' in my_str)

#Para selecionar um caractere pelo número, basta por [] com o número dentro.

alo = 'olameunomeéaí'
print(alo[5])
print(alo[1:6]) #lembre-se que ele conta a partir do 0, a saída aqui será 'lameu'
print(alo[2:7:2])
print(alo[::-1])

#Concatenando Strings

my_string_1 = 'oi'
my_string_2 = 'olá'

exit = my_string_1 + ' ' + my_string_2
print(exit)

#Replace substitui uma parte da string por outra, usando o comando replace(old, new).

eu = 'eu gosto de python'
eu2 = eu.replace("python", "programação")
print(eu2)

# Todos os carcateres de uma string em maíusculo ou minúsculo 

aloupper = alo.upper()
print(aloupper) 

alolower = alo.lower()
print(alolower)

# Para remover os espaços em branco é só usar Strip

alostripr = alo.strip()
print(alostripr)

#Para substituir uma palavra por outra, usa o comando replace(old, new)

#Para separar as palavras de uma String é só usar o comando Split

#O comando Join desfaz o que o Split faz

#-------------------------------------------------

#Construindo um gerador de perfil

first_name = "John"
last_name = "Doe"
print(first_name + " " + last_name)

full_name = first_name + " " + last_name
print(full_name)

address = "123 Main Street"
address += ", Apartment 4B"
print(address)

employee_age = 28

employee_info = full_name + " is " + str(employee_age) + " years old"
print(employee_info)

experience_years = 5 
expericene_info = "Experience: " + str(experience_years) + " years"
print(expericene_info)

position = "Data Analyst"
salary = 75000

employee_card = f"Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}"

print(employee_card)

employee_code = "DEV-2026-JD-001"
department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
print(year_code)

initials = employee_code[9:11]
print(initials)

last_three = employee_code[-3:]
print(last_three)