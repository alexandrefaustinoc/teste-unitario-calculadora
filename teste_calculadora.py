import pytest
from calculadora import Calculadora

calc = Calculadora()
#Teste de Soma
def test_somar():
    assert calc.somar(2, 3) == 5
    assert calc.somar(-1, 1) == 0
    assert calc.somar(0, 0) == 0
#Teste de Subtração
def test_subtrair():
    assert calc.subtrair(5, 3) == 2
    assert calc.subtrair(1, 1) == 0
    assert calc.subtrair(-2, -3) == 1
#Teste de multiplicação
def test_multiplicar():
    assert calc.multiplicar(2, 3) == 6
    assert calc.multiplicar(0, 1) == 0
    assert calc.multiplicar(-1, 5) == -5
#Teste de Divisão
def test_dividir():
    assert calc.dividir(6, 3) == 2
    assert calc.dividir(9, 3) == 3

    #Teste de divisão por zero
    with pytest.raises(ValueError):
        calc.dividir(1, 0)

#Testes de fatorial
def test_fatorial():
    assert calc.fatorial(5) == 120
    assert calc.fatorial(0) == 1  # Fatorial de 0 é 1
    with pytest.raises(ValueError):
        calc.fatorial(-1)  # Fatorial não é definido para números negativos

# Testes de potência
def test_potencia():
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1  # Qualquer número elevado a 0 é 1
    assert calc.potencia(3, -2) == 1/9  # Potência com expoente negativo
