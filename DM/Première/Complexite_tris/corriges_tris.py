def indice_minimum(debut , liste):
  '''
  algorithme de recherche de l'indice de l'élément minimum
  entrée : debut (int), liste (list)
  '''
    ind_mini = debut
    for j in range(debut,len(liste)):
            if liste[ind_mini] > liste[j]:
                ind_mini = j
    return ind_mini

def tri_selection(liste):
  '''
  algorithme de tri par selection
  entrée : liste (list)
  '''
  n = len(liste)
    for i in range(n):
        ind_mini = indice_minimum(i, liste)
        l[ind_mini],l[i] = l[i],l[ind_mini]



##########################################################


def inserer(l,debut):
  '''
  algorithme d'insertion de valeurs dans une liste
  entrée : liste (list), i indice de fin de la zone d'insertion
  sortie : None
  '''
    k = debut
    while k > 0 and l[k-1] > l[k]:
        l[k-1],l[k] = l[k],l[k-1]
        k-=1

def tri_insertion(liste):
  '''
  algorithme de tri par insertion
  entrée : liste (list)
  sortie : None
  '''
    n = len(liste)
    for i in range(1, n):
        inserer(liste, i)
