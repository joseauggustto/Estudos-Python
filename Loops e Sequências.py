# Vamos lá...
# Estudo sobra laços e seqûencias.

# countries = ['Brazil', 'Australia', 'Suíça']
# print(countries[2])

# countries = ['Brazil', 'Australia', 'Suíça']
# print(countries[-1])

# nome = "Augusto"
# print(list(nome))

# sei_la = [3, 4, 6, 3, 2 , 65, 6 , 67]
# print(len(sei_la))

# languages = ["espanhol", "english"]
# languages[0] = "pt br"   # att valor, AAAAAAAA
# print(languages)

# languages = ["espanhol", "english"]
# del languages[0]   # deletar valor da lista
# print(languages)

# programming_languages = ['Python', 'Java', 'C++', 'Rust']    # saber se algo está ali...
# print("Rust" in programming_languages)
# print("JavaScripty" in programming_languages)

# developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
# print(developer[2]) # vai dar a segunda lista de dentro

# developer = ['Alice', 34, 'Rust Developer']
# name, *rest = developer
# print(name)
# print(rest)

# ------------------------

"""


.append adiciona um novo elemento a lista, criando uma sub lista inside ()

.extend faz com que adicione outros elementos na lista, sem criar sublista []

.insert adiciona um valor específico em um local específico na lista. Coloca onde eu quero o vizinho e depois o valor que eu quero como vizinho à direita. ()

.remove vai remover um dado específico da lista, coloca o número entre ()

.pop vai remover um elemento específico de acordo com o índice determinado, se eu colocar () vazio vai remover o último dado.

.clear já tá dizendo, vai foder com tudo

.sort vai reorganizar a lista do < para >, .sorted vai refazer uma lista nova, só que organizada. 

.reverse vai coloca a lista de trás para frente.

o comando .index serve para procurar na lista um valor específico retornando sua posição. 


"""


# numberss = [1, 2, 3, 4, 5]
# numberss.append(6)
# print(numberss)

# numbers = [1, 2, 3, 4, 5]
# outersnbrs = [6, 7, 8]
# numbers.append(outersnbrs)
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# outersnbrs = [6, 7, 8]
# numbers.extend(outersnbrs)
# print(numbers)

alo = [1, 2, 3, 4, 5]
alo.insert(3, 2.5)  #adicionar em um local específico...
print(alo)

