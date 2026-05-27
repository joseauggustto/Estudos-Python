# let's go

#Booleanos e Condicionais servem para tomar decisões, ou seja, para executar um código dependendo de uma condição.
#Booleanos podem ser apenas dois valores, true ou false.

# Operadores de comparação: 

# == igual a
# != diferente de
# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a

print(1 == 1)
print(2 != 3)
print(5 > 4)
print(3 < 2)
print(3 < 4)
print( 5 >= 5)
print(4 <= 5)

# Condicionais if, elif, else.

# Em python a condicional mais básica é o if, que executa um código se a condição for verdadeira.

if 5 > 3: 
    print("Yes")

# Else é usado para executar um código se a condição for falsa.

if 5 < 3:
    print("Yes")
else:
    print("No")

# Elif é usado para testar várias condições, ele é uma abreviação de else if.

if 5 < 3:
    print("Yes")
elif 5 == 5:
    print("Yes")
else:
    print("No")


# Operadores lógicos and, or, not.
# O operador and é usado para testar se duas condições são verdadeiras, ele retorna true se ambas as condições forem verdadeiras.

if 5 > 3 and 3 < 4:
    print("Yes")

# O operador or é usado para testar se pelo menos uma das condições é verdadeira, ele retorna true se pelo menos uma das condições for verdadeira.

if 5 > 3 or 3 > 4:
    print("Yes")

# O operador not é usado para inverter o valor de uma condição, ele retorna true se a condição for falsa e false se a condição for verdadeira.

if not 5 < 3:
    print("Yes")

# Calculadora de reserva de ingressos no cinema. 

base_price = 15
age = 21
seat_type = "Gold"
show_time = "Evening"

if age >= 17:
    print("User is eligible to book a ticket.")

if age >= 21:
    print("User is eligible for Evening shows")
else:
    print("User is not eligible for Evening shows")

is_member = False

is_weekend = False

discount = 0

if is_member and age >= 21:
    discount = 3 
    print("User qualifies for membership discount")
else:
    print("User does not qualify for membership discount")

print(f"Discount: {discount}")

extra_charges = 0

if is_weekend or show_time == "Evening": 
    extra_charges = 2
    print("Exra charges will be applied") 
else:
    print("No extra charges will be applied")

print("Extra charges: ", extra_charges)

if age >= 21 or age >= 18 and (show_time != "Evening" or is_member): 
    print("Ticket booking condition satisfied")

    service_charges = 0 
    if seat_type == "Premium":
        service_charges = 5
    elif seat_type == "Gold":
        service_charges = 3
    else:
        service_charges = 1
    print("Service charges:", service_charges)

    final_price = base_price + extra_charges + service_charges - discount
    print("Final price of ticket:", final_price)
else: 
    print("Ticket booking failed due to restrictions")