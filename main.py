val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def menu():
    choix = int(input('Que voulez vous faire?\n1.convertion:romain->arabe\n2.un calcul\n:'))
    if choix == 1:
        nb = demande_romain()
        print('en chiffre arabe:', romain_arabe(nb))
    elif choix == 2:
        calcul_romain()


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
        print(a, '+', b, '=', addition(a, b))
    elif op == 2:
        a = romain_arabe(demande_romain())
        b = romain_arabe(demande_romain())
        print(a, '-', b, '=', soustraction(a, b))
    elif op == 3:
        a = romain_arabe(demande_romain())
        b = romain_arabe(demande_romain())
        print(a, 'x', b, '=', multiplication(a, b))
    elif op == 4:
        a = romain_arabe(demande_romain())
        b = romain_arabe(demande_romain())
        print(a, '/', b, '=', division(a, b))


def addition(a, b):
    return (a + b)


def soustraction(a, b):
    return (a - b)


def multiplication(a, b):
    return (a * b)


def division(a, b):
    return (a / b)

#menu()