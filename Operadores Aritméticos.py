# + é igual adição
# - é igual a subtração
# * é igual a multiplicação
# / é igual a divisão
# ** é igual a potenciação
# // é igual a divisão inteira
# % é igual ao resto da divisão
# Dois simbolos de igual (==) é usado para testar os operadores
# Ordem de precedência = Primeiro () ; Segundo (**) ; Terceiro é (*, /, //, %); Em Quarto é (+ e -).

#--------------------------------

#Números inteiros e flutuantes, para os mais chegados: int e float.

my_int_number_1 = 56
my_int_number_2 = -6 

print(type(my_int_number_1))
print(type(my_int_number_2))

# Soma

sum_ints = my_int_number_1 + my_int_number_2
print(sum_ints, type(sum_ints))

#Diferença

diff_ints = my_int_number_1 - my_int_number_2 
print(diff_ints)

# Números Float ----------------------------

my_float_number_1 = 30.5
my_float_number_2 = 6.5

# Soma dos Flutuadores

sum_float = my_float_number_1 + my_float_number_2
print(sum_float)

# Diferença dos Flutuadores 

diff_float = my_float_number_1 - my_float_number_2
print(diff_float)

# ----------------------------------

#Posso converter um número inteiro para flutuante e vice versa.

my_int_number_3 = 70
my_float_number_3 = 70.0

conversion_int_to_float = float(my_int_number_3)
conversion_float_to_int = int(my_float_number_3)

#Posso arredondar números com o comando round 

round_number_1 = 2.345
round_number_2 = 3.234

print(round(round_number_1))
print(round(round_number_2, 2)) # Duas casas após a vírgula.

#-------------------------------------

#Eu posso reduzir essas operações muito rápido usando as atribuições aumentadas. Usa-se += ou -=
#Posso usar todas as outras operações simplesmente adicionando seus operadores antes do =

isso = 10
isso += 5
print(isso)

aquilo = 30
aquilo -= 15
print(aquilo)

#Outra forma:

isso = 30
isso = isso + 10

# Isso acima tambem funciona com strings, é só somar ou retirar strings sem precisar escrever códigos extensos.

#--------------------------------------

#Construindo um Bill Splitter 


num_of_friends = 4
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21
running_total = appetizers + main_courses + desserts + drinks

print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)
