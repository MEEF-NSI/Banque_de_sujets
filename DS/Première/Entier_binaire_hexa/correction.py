def somme_entiers(n):
    """
    Retourne la somme des entiers de 1 à n
    :param n: le nombre entier
    :return: la somme des entiers de 1 à n
    """
    somme = 0
    for i in range(1, n + 1):
        somme += i
    return somme

def trouver_indice(L, valeur):
    '''
    Retourne l'indice de la première occurrence de valeur dans L
    '''
    res = -1
    i = 0
    while i < len(L) and res == -1:
        if L[i] == valeur:
            res = i
        i += 1
    return res

def factorielle(n):
    '''
    Retourne la factorielle de n
    '''
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
