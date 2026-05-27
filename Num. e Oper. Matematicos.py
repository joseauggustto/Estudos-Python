# let's go

#Inteiros, floats. 

myint = 45
myint2 = 15

print(type(myint))
print(type(myint2))

sum = myint + myint2
print(sum)

diff = myint - myint2
print(diff)

mult = myint * myint2
print(mult)

div = myint / myint2
print(div)

rest = myint % myint2
print(rest) 

#------------------------
print("-" * 33)

myfloat = 4.5
myfloat2 = 0.5 

print(type(myfloat))
print(type(myfloat2))

sum = myfloat + myfloat2
print(sum)

diff = myfloat - myfloat2
print(diff)

mult = myfloat * myfloat2
print(mult)

div = myfloat / myfloat2
print(div)

rest = myfloat % myfloat2
print(rest) 

# ------------------------

# Função round() para arredondar um número.

float4 = 3.14159
print(round(float4,2))
print(round(float4))

# Atribuições Aumentadas, como +=, -=, *=, /=, %=. Pode ser usado para string também, como += para concatenar.

myvar = 10
myvar += 5
print(myvar)

myvarr = 10
myvarr -= 3
print(myvarr)

# ------------------------

# Desafio 

running_total = 0
num_of_friends = 4

appetizers = 37.89
main_courses = 57.84
desserts = 39.39 
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print(f"Total bill so far: {running_total}")

tip = running_total * 0.25
print(f"Tip amount: {tip}")

running_total += tip
print(f"Total with tip: {running_total}")

final_bill = running_total / num_of_friends
print(f"Bill per person: {final_bill}")

each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')

