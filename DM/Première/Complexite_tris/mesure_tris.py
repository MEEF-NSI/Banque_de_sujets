import random
import timeit
import matplotlib.pyplot as plt
from ap_decorators import count
############################################### PARTIE 1 ###############################################

listes = [[random.randint(0,500) for _ in range(j)] for j in range(500)]

@count
def comparer(x,y):
    ...

def indice_minimum(debut , liste):
    ...

def tri_selection_minimum(liste):
    ...

def mesure_tri_selection_temps(n):
    # On initialise un tableau qui servira à récolter nos temps d'exécutions
    tab_mesure = []
    for i in range(n):
        '''On créée une liste de nombre aléatoires de taille i qui variera 
        jusqu'à la taille demandée en paramètre.
        '''
        liste_aleatoire = [random.randint(0,500) for _ in range(i)] 
        # On prend un temps de départ
        s_time = timeit.default_timer()
        # On trie la liste créée
        ...
        # On prend un temps de fin
        e_time = ...
        # On ajoute dans le tableau de mesures, la différence de temps mesurée entre les deux chronomètres.
        tab_mesure.append(...)

    # On réalise un graphique grâce au tableau de mesure que l'on affiche
    plt.plot(tab_mesure)
    plt.savefig("mesure_tri_selection_temps.png")

def mesure_tri_selection_comparaisons(n):
    # On initialise un tableau qui servira à récolter nos temps d'exécutions
    tab_mesure = []
    for i in range(n):
        '''On créée une liste de nombre aléatoires de taille i qui variera 
        jusqu'à la taille demandée en paramètre.
        '''
        liste_aleatoire = [random.randint(0,500) for _ in range(i)] 
        # On initialise le compteur à 0
        ...
        # On trie la liste créée
        ...
        # On récupère le nombre de comparaisons grâce au compteur
        nombre_comparaisons = ...
        # On ajoute dans le tableau de mesures, le nombre de comparaisons.
        tab_mesure.append(...)

    # On réalise un graphique grâce au tableau de mesure que l'on affiche
    plt.plot(tab_mesure)
    plt.savefig("mesure_tri_selection_comparaison.png")


############################################### PARTIE 2 ###############################################

def inserer(l,i, comp = comparer):
    ...


def tri_insertion(l,comp=comparer):
    ...

def mesure_tri_insertion_temps(n):
    # On initialise un tableau qui servira à récolter nos temps d'exécutions
    tab_mesure = []
    for i in range(n):
        '''On créée une liste de nombre aléatoires de taille i qui variera 
        jusqu'à la taille demandée en paramètre.
        '''
        liste_aleatoire = [random.randint(0,500) for _ in range(i)] 
        # On prend un temps de départ
        s_time = timeit.default_timer()
        # On trie la liste créée
        ...
        # On prend un temps de fin
        e_time = ...
        # On ajoute dans le tableau de mesures, la différence de temps mesurée entre les deux chronomètres.
        tab_mesure.append(...)

    # On réalise un graphique grâce au tableau de mesure que l'on affiche
    plt.plot(tab_mesure)
    plt.savefig("mesure_tri_insertion_temps.png")

def mesure_tri_insertion_comparaisons(n):
    # On initialise un tableau qui servira à récolter nos temps d'exécutions
    tab_mesure = []
    for i in range(n):
        '''On créée une liste de nombre aléatoires de taille i qui variera 
        jusqu'à la taille demandée en paramètre.
        '''
        liste_aleatoire = [random.randint(0,500) for _ in range(i)] 
        # On initialise le compteur à 0
        ...
        # On trie la liste créée
        ...
        # On récupère le nombre de comparaisons grâce au compteur
        nombre_comparaisons = ...
        # On ajoute dans le tableau de mesures, le nombre de comparaisons.
        tab_mesure.append(...)

    # On réalise un graphique grâce au tableau de mesure que l'on affiche
    plt.plot(tab_mesure)
    plt.savefig("mesure_tri_insertion_comparaison.png")