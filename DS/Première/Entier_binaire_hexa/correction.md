# Correction DS

## Questions de cours 

1. Une base correspond à un système de numérotation utilisant des symboles uniques.
2. binaire (2) informatique en général, octal (8) simplifier l'écriture binaire, hexadecimal (16) couleurs, adresse mémoire etc... , shadok(4), ternaire(3)
3. Une infinité de bases existent. On doit faire attention à ce que les symboles soient tous uniques
4. On divise le nombre que l'on souhaite convertir par le nombre de la base. On divise successivement le quotient en gardant bien le reste. Ce reste correspond à la représentation dans la base souhaitée. On doit bien faire attention à bien partir du bas vers le haut pour avoir l'écriture dans la base correcte.
5. Un octet est un ensemble de 5 bits.


## Représentation en base 2,10,16

### Exercice 1 : 
1.
* $45_{10}$ -> 32 + 8 + 4 +1  = $2^5 + 2^3 + 2^2 + 2^0 = 101101_2$
* $48_{16}$ -> $0100~1000_2$


2. 
* $5C_{16}$ -> $0101~1100_2 = 2^6+2^4+2^3+2^2 = 64 + 16 + 8 + 4 = 92_{10}$
* $110110_2$ -> $2^1 + 2^2 + 2^4 + 2^5 = 32 + 16 + 4 + 2 = 54_{10}$
  
3.
* $439_{10} = 110110111_{2} = 1B7_{16}$
* $1110101_{2} = 75_{16}

### Exercice 2 : 

1. 
   * $10010_2$
   * $11001_2$

2.
   * $10001_2$
   * $11101_2$

3.
   * $11110_2$
   * $1011011_2$
  
4.
   * $11~\texttt{reste}~100$
   * $10~\texttt{reste}~111$

5. On appelle cela le décalage de bits vers la gauche ou la droite.

## Fonctions
1. fonction addition de 1 jusque n
```python
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
```

2. fonction occurence de lettre 
```python
def occurence_lettres(chaine, lettre):
    """
    Retourne le nombre d'occurences de la lettre dans la chaine
    :param chaine: la chaine de caractères
    :param lettre: la lettre à chercher
    :return: le nombre d'occurences de la lettre dans la chaine
    """
    nb_occurences = 0
    for c in chaine:
        if c == lettre:
            nb_occurences += 1
    return nb_occurences
```