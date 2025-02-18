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