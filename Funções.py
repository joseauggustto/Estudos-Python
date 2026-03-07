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
    print(3 + 2)  #Isso aqui se chama identização, esse recuo para a direita.1 
sum()

# Função de soma mais completa:

def calculate(a, b, c):  # Essas letras são os parâmetros para a função.
    print(a * b + c)  # Aqui eu vou decidir o que cada um vai fazer, eu acho...
calculate(4, 4, 4)

print('-' * 20)

#Pequeno teste de combustpivel do gemini:

def verificar_combustível(quantidade):
    print(f'Verificando: {quantidade} litros...')
    return quantidade > 10

resultado1 = verificar_combustível(5)
print(resultado1)

resultado2 = verificar_combustível(13)
print(resultado2)

print('-' * 20)

# Porteiro da balada:

def pode_entrar(idade):
    print(idade)
    return idade > 18 

teste1 = pode_entrar(19)
print(teste1)

teste2 = pode_entrar(15)
print(teste2)

print('-' * 30)

# Desafio de desconto 

def calcular_preço_final(valor_produto):
    if valor_produto > 100:
        return valor_produto - 20
    else:
        return valor_produto

teste1 = calcular_preço_final(150)
print(teste1)

teste2 = calcular_preço_final(80)
print(teste2)

print('-' * 30)
#Desafio final: Analista de Desempenho

def analisar_vendas(nome_vendedor, valor_vendas):
    if valor_vendas >= 500:
        return (f'Parabéns {nome_vendedor}, você bateu a meta!')

    else:
        return (f'Vamo que vamo {nome_vendedor}, falta pouco!')

teste3 = analisar_vendas('João', 600)
print(teste3)

teste4 = analisar_vendas('Maria', 300)
print(teste4)

print('-' * 30)

# Teste de velocidade

def velocidade(kmh):
    if kmh < 40:
        return 'Muito lento, acelera!'
    elif kmh <= 80:
        return 'Velocidade ideal.'
    else:
        return 'Multado! Você está muito rápido.'
        
teste = velocidade(60)
print(teste)

print('-' * 30)

# Sistema RPG

def classificar_heroi_poder(poder):
    if poder < 100:
        return 'Recruta'
    elif poder < 500:
        return 'Guerreiro'
    elif poder < 1000:
        return 'Mestre'
    else:
        return 'Lenda'
    
testerpg = classificar_heroi_poder(99)
print(testerpg)

testerpg1 = classificar_heroi_poder(499)
print(testerpg1)

testerpg2 = classificar_heroi_poder(999)
print(testerpg2)

testerpg3 = classificar_heroi_poder(1001)
print(testerpg3)

print('-' * 30)

# Desafio do Clima

def temp_clima(temp):
    if temp < 15:
        return 'Está frio'
    elif temp == 25:
        return 'Temperatura Perfeita'
    elif temp > 30:
        return 'Está Quente'
    else:
        return 'Clima agradável'


print('-' * 30)

# Calculadora de Bônus

def bonus_calculator(salario, tempo_casa):

    if not isinstance(salario, (int, float)) or not isinstance(tempo_casa, (int, float)):
        return 'Só pode números!'
    
    elif tempo_casa < 1:
        return salario * 0
    elif tempo_casa < 3:
        return salario * 0.10
    else:
        return salario * 0.2
    
func1 = bonus_calculator('a', 0.5)
print(func1)

func2 = bonus_calculator(2000, 2)
print(func2)

func3 = bonus_calculator(2000, 5)
print(func3)