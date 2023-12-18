# EXERCICE 1 (6 points)
Sur le réseau social TipTop, on s’intéresse au nombre de « like » des abonnés. **On abordera une approche orientée objet dans cet exercice**.

1. Créer la classe TipTop qui a pour attribut une liste qui correspond aux utilisateurs.
  - Son constructeur prendra une liste d'utilisateurs **ou par défaut, une liste vide**.
    
2. Créer la classe Utilisateur qui a pour attributs :
  - Leur nom
  - Leur nombre de like
  - Leur nombre de publication
  
3. Écrire une méthode *max_like()* de la classe TipTop et qui renvoie le nom de la personne qui a le plus de like.
```python
>>>user = Utilisateur('Timothée', 490, 130)
>>>user2 = Utilisateur('Titouan', 290, 55)
>>>t = TipTop([user,user2])
>>>t.max_like()
'Timothée'
```

4. Ecrire une méthode *afficher_informations()* qui affiche dans le terminal le nom de l'utilisateur, son nombre de like et son nombre de publication de cette manière :
```python
>>>timothee = Utilisateur('Timothée', 490, 130)

>>>timothee.afficher_informations()
Timothée a 490 like sur 130 publications.
```


# EXERCICE 2 (4 points)

Le but de l'exercice est de compléter une fonction qui détermine si une valeur est présente dans un tableau de valeurs triées dans l'ordre croissant.

L'algorithme traite le cas du tableau vide.
L'algorithme est écrit pour que la recherche dichotomique ne se fasse que dans le cas où la valeur est comprise entre les valeurs extrêmes du tableau.

On distingue les trois cas qui renvoient False en renvoyant **False,1** , **False,2** et **False,3**.

1. Expliquer ce qu'est la recherche dichotomique? L'indiquer en commentaire.

2. A quoi correspond les 3 cas de renvois ? L'indiquer en commentaire à côté des "#Cas" dans le code.

3. Recopier et compléter l'algorithme de dichotomie donné ci-après.
  
```python
def dichotomie(tab, x)
    """
    tab : tableau trié dans l’ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    #Cas 1
    if ...:
        return False,1
    #Cas 2
    if (x < tab[0]) or ...:
        return False,2
    #Cas 3
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = ...
        if x == tab[m]:
            return ...
        if x > tab[m]:
            debut = m + 1
        else:
            fin = ...
    return ...
```

Exemples :
```python
>>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)
True
>>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)
(False, 3)
>>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],1)
(False, 2)
>>> dichotomie([],28)
(False, 1)
```

4. Proposer un algorithme de recherche dichotomique récursive dans une liste triée.
