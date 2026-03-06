#Olá, vamos ver o que funções tem a nos ensinar.

#Uma das funções mais usadas em python é o input, que manda o usuário digitar algo.

name = ('Qual o seu nome?')
print('Prazer', name) 

# Já o comando int converte boolenaos e string numéricas em um número inteiro. 

print(int(True))
print(int(False))
print(int(3.14))
print(int('42'))

# Para escrever funções customizadas é só usar o comando def seguido do nome que você deseja dar a função, um par de parênteses e dois pontos.

def sum():
    print(3 + 2)    
sum()

# Função de soma mais completa:

def calculate(a, b, c):  # Essas letras são os parâmetros para a função.
    print(a * b + c)  # Aqui eu vou decidir o que cada um vai fazer, eu acho...
calculate(4, 4, 4)

# Regra de LEGB do python: Escopo Local, Escopo Envolvente, Escopo Local e Escopo Embutido

# Escolpo local: A variável declarada só pode ser acessada dentro da função:

def aqui():
    ali = 20 
    print(ali) #Só posso aqui
aqui()
print(aqui) #Isso vai dar erro

# Escopo envolvente: significa que uma função que está aninhada dentro de outra função pode acessar as variáveis da função na qual está aninhada.

def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func()

print('Não terminou o estudo')
