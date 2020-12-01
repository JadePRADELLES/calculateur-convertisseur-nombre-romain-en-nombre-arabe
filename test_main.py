from main import romain_arabe
from main import addition
from main import soustraction
from main import multiplication
from main import division

def test_romain_arabe():
    assert romain_arabe('I') == 1
    assert romain_arabe('II') == 2

    assert romain_arabe('V') == 5
    assert romain_arabe('VV') == 10

    assert romain_arabe('X') == 10
    assert romain_arabe('XX') == 20

    assert romain_arabe('L') == 50
    assert romain_arabe('LV') == 55

    assert romain_arabe('C') == 100
    assert romain_arabe('CL') == 150

    assert romain_arabe('D') == 500

    assert romain_arabe('M') == 1000


def test_addition():
    assert addition(1, 2) == 3
    assert addition(100, 2) == 102


def test_soustraction():
    assert soustraction(2, 1) == 1
    assert soustraction(1001, 1) == 1000

def test_multiplication():
    assert multiplication(2, 1) == 2
    assert multiplication(1001, 1) == 1001

def test_division():
    assert division(2, 1) == 2.0
    assert division(1001, 1) == 1001.0