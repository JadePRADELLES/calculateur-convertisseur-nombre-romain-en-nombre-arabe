val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def menu():
    choix = int(input('Que voulez vous faire?\n1.convertion:romain->arabe\n2.un calcul\n:'))
    if choix == 1:
        nb = demande_romain()
        print('en chiffre arabe:', romain_arabe(nb))
    elif choix == 2:
        res = calcul_romain()
        print('le resultat en nombre romain:', arabe(res))


def demande_romain():
    string = str(input('Enter un nombre romain: '))
    string = string.upper()
    return (string)


def romain_arabe(string):
    nb_arabe = 0
    while string:
        if len(string) == 1 or val[string[0]] >= val[string[1]]:
            nb_arabe += val[string[0]]
            string = string[1:]
        else:
            nb_arabe += val[string[1]] - val[string[0]]
            string = string[2:]
    return (nb_arabe)


def calcul_romain():
    op = int(input('Quelle operation voulez vous faire?\n1.addition\n2.soustraction\n3.multiplication\n4.division\n:'))
    if op == 1:
        a = romain_arabe(demande_romain())
        b = romain_arabe(demande_romain())
        res = addition(a, b)
        print(a, '+', b, '=', res)
        return res
    elif op == 2:
        a = romain_arabe(demande_romain())
        b = romain_arabe(demande_romain())
        res = soustraction(a, b)
        print(a, '-', b, '=', res)
        return res
    elif op == 3:
        a = romain_arabe(demande_romain())
        b = romain_arabe(demande_romain())
        res = multiplication(a, b)
        print(a, 'x', b, '=', res)
        return res
    elif op == 4:
        a = romain_arabe(demande_romain())
        b = romain_arabe(demande_romain())
        res = division(a, b)
        print(a, '/', b, '=', res)
        return res


numlist = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
           (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def arabe(n):
    res = ""
    for k, v in numlist:
        while n >= k:
            n -= k
            res += v
    return res


def addition(a, b):
    return (a + b)


def soustraction(a, b):
    return (a - b)


def multiplication(a, b):
    return (a * b)


def division(a, b):
    return (a / b)

#menu()