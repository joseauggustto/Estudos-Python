# Hello. Hoje estudaremos valores booleanos(True ou False) e condicionais. 
#Esse valroes servem para administrar o programa de acordo com certo valores condicionais.

# Operadores de comparação: 
# == se isso é igual aquilo 
# !# se dois valores não são iguais
# > se esse valor é maior que esse
# < se esse valor é menor que esse
# >= se esse valor é maior que esse ou igual
# <= se esse valor é menor que esse ou igual

#print(3 > 5)
#print(5 < 9)
#print(5 == 5)
#print(5 != 5)

# Em py a codicional mais básica é o if. Funciona assim:

age = 19
if age > 18:
    print('Você tá fudido')

altura = 1.80
if altura >= 1.75:
    print('Alto')

#Quando a função if gera um 'false', aí então entra o comando else:

peso = 75
if peso > 95:
    print('balão')
else:
   print('tá ok')

carro = 1 
if carro > 2:
    print('rico')
else:
    print('pobre premium')

# Para haver múltiplas condcições, é só usar o comando elif:

age = 50
if age > 30:
    print('velho')

elif age <= 10:
    print('Vai estudar')

# --------------------------------------------------------

# Os valores truthy ou falsy servem para saber se os campos estão vazios ou não. 
# Para checar, usa-se o comando bool()

print(bool(2))
print(bool('aí')) 

print(bool(''))
print(bool(0))

#----------------------------------------------------

# Existem trẽs operadores booleanos em python: and, or e not. 

# Primeiro o and: ele vai checar os valores para ver se a condição é atendida. Podem ser vários.

is_citizen = True
age = 17 
if is_citizen and age >=18:
    print('Pode votar')

else:
    print('Rai pa la')

# Agora o comando or
# O 'or' vai ver se pelo menos uma das condições é atendida:

age = 17
is_employed = True
is_white = False

if age > 18 or is_employed or is_white:
    print('tá empregado')

else: 
    print('sai daqui')

# Por último o comando not. 
# O comando not simplesmente converte qualquer valor. Se é true vira false e vice versa.

print(not '')
print(not 2)

is_admin = True

if not is_admin:
    print('Access denied for non-administrators.')
else:
    print('Welcome, Administrator!')

#Isso aqui foi dificil de entende, pqp

#Construíndo uma calculadora de ticket de cinema. 

base_price = 15
age = 21

seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')

else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0 

if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

print('Discount:', discount)

extra_charges = 0

if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

print('Extra charges:', extra_charges)

if age >= 21 or age >=18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    
    if seat_type == 'Premium':
        service_charges = 5
    
    elif seat_type == 'Gold':
        service_charges = 3

        print('Services charges:', service_charges)

    else:
        service_charges = 1
    
    final_price = base_price + extra_charges + service_charges - discount

    print('Final price of ticket:', final_price) 
else:
    print('Ticket booking failed due to restrictions')


