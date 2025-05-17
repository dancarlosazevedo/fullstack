saida =''
def adicao(a, b):
    return a + b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

def calculadora():
    while True:
        print("Escolha uma operação: \n1. Adição\n2. Multiplicação\n3. Divisão\n4. Sair\n")
        escolha = input("Digite o número da operação desejada: ")
        if escolha == '4':
            print("Saindo da calculadora.")
            break
        elif escolha in ['1', '2', '3']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = adicao(num1, num2)
                print(f"Resultado da adição: {resultado}")
            elif escolha == '2':
                resultado = multiplicacao(num1, num2)
                print(f"Resultado da multiplicação: {resultado}")
            elif escolha == '3':
                resultado = divisao(num1, num2)
                print(f"Resultado da divisão: {resultado}")
        else:
            print("Opção inválida. Tente novamente.")
        continuar = input("Deseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            print("Saindo da calculadora.")
            break
        
if __name__ == "__main__":
    calculadora()
    print("Obrigado por usar a calculadora!")