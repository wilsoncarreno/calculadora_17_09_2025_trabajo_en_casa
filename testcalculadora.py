# test_calculadora.py
import pytest
from calculadora import calculadora_simple

def test_suma():
    assert calculadora_simple(5, 3, '+') == 8

def test_resta():
    assert calculadora_simple(10, 4, '-') == 6

def test_multiplicacion():
    assert calculadora_simple(3, 4, '*') == 12

def test_division_valida():
    assert calculadora_simple(8, 2, '/') == 4

def test_division_por_cero():
    assert calculadora_simple(5, 0, '/') == "Error: División/0"

def test_a_no_numerico():
    assert calculadora_simple('a', 5, '+') == "Error: 'a' no es número"

def test_b_no_numerico():
    assert calculadora_simple(5, 'b', '+') == "Error: 'b' no es número"

def test_operador_invalido():
    assert calculadora_simple(5, 3, '%') == "Error: Operador inválido"