import math

class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não permitida!")
        return a / b

    def fatorial(self, n):
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos!")
        return math.factorial(n)

    def potencia(self, base, exp):
        return base ** exp

# Função para mostrar o menu de operações
def mostrar_menu():
    print("\nOperações disponíveis:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Fatorial")
    print("6. Potência")
    print("0. Sair")

# Função para interagir com o usuário e realizar as operações
def executar_calculadora():
    calc = Calculadora()

    while True:
        mostrar_menu()

        opcao = input("Escolha a operação (0-6): ")

        if opcao == '0':
            print("Saindo...")
            break

        if opcao in ['1', '2', '3', '4', '5', '6']:
            if opcao == '1':  # Somar
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"Resultado: {calc.somar(a, b)}")
            elif opcao == '2':  # Subtrair
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"Resultado: {calc.subtrair(a, b)}")
            elif opcao == '3':  # Multiplicar
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print(f"Resultado: {calc.multiplicar(a, b)}")
            elif opcao == '4':  # Dividir
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                try:
                    print(f"Resultado: {calc.dividir(a, b)}")
                except ValueError as e:
                    print(f"Erro: {e}")
            elif opcao == '5':  # Fatorial
                n = int(input("Digite um número para calcular o fatorial: "))
                try:
                    print(f"Resultado: {calc.fatorial(n)}")
                except ValueError as e:
                    print(f"Erro: {e}")
            elif opcao == '6':  # Potência
                base = float(input("Digite a base: "))
                exp = float(input("Digite o expoente: "))
                print(f"Resultado: {calc.potencia(base, exp)}")

        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal para rodar a calculadora
if __name__ == "__main__":
    executar_calculadora()
