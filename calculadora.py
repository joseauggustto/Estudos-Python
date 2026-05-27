def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def calculadora():
    print("=== CALCULADORA SIMPLES ===")
    print("Escolha a operação:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")

    while True:
        opcao = input("\nDigite a opção (1/2/3/4/5): ")

        if opcao == '5':
            print("Saindo da calculadora. Até mais!")
            break

        if opcao in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")
                continue

            if opcao == '1':
                print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
            elif opcao == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif opcao == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcao == '4':
                resultado = dividir(num1, num2)
                if isinstance(resultado, str):
                    print(resultado)
                else:
                    print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")

if __name__ == "__main__":
    calculadora()
