# Exercice 1 :

## Partie A : 
On a l'équipe suivante :

```python
equipe_1 = [ [1, 5, "Paul"], [7,0, "Didier"], [2, 3, "Marc"] ]
```

### Question 1 :
```python
def nom_membres_equipe(equipe):
    res = []
    for i in equipe:
        res.append(i[2])
    return res
```

### Question 2 :

```python
def nombre_buts_equipe(equipe):
    res = 0
    for i in equipe:
        res += i[1]
    return res
```

### Question 3 :

```python
equipe_mauvais_id = [ [1, 5, "Paul"], [1,0, "Didier"], [2, 3, "Marc"] ]
equipe_vide = []
def validation(equipe):
    res = True
    
    for i in equipe:
        for j in equipe:
            if i!=j and i[0] == j[0]:
                res = False
    return len(equipe)>0 and res

>>>validation(equipe_mauvais_id)
False
>>> validation(equipe_vide)
False
>>> validation(equipe_1)
True
```

## Partie B :

On a les listes suivantes en plus et une compétition :

```python
equipe_2 = [ [42, 2, "Blaise"], [1, 1, "Pascal"], [3, 2, "Matuidi"] ]
equipe_3 = [ [88, 5, "Victor"], [7,0, "Hugo"], [2, 3, "Zidane"] ]
equipe_4 = [ [3, 78, "Paul"], [15 , 1, "Valéry"], [21, 68, "Marc"] ]

competition = [ [equipe_1, equipe_2, equipe_3, equipe_4], [ equipe_1, equipe_4] , [ equipe_1] ]
```

### Question 4 :

```python
def equipe_ayant_le_plus_marque(competition):
    """ On part du principe que les équipes sont valides"""
    les_equipes = competition[0]
    res = les_equipes[0]
    max_but = nombre_buts_equipe(les_equipes[0])
    
    for i in range(1, len(les_equipes)):
        nb_but_equipe_i = nombre_buts_equipe(les_equipes[i])
        if max_but < nb_but_equipe_i:
            res = les_equipes[i]
            max_but = nb_but_equipe_i
    return res
```

### Question 5 :

Non, l'équipe ayant le plus marqué n'est pas forcement la vainqueur du tournoi. Une équipe peut marquer le plus de points de tout le tournoi lors de son premier match et perdre au suivant et se retrouver éliminée.

Exemple : l'équipe 4

### Question 6 :

```python

def equipe_vainqueuses(competition):
    return competition[-1]
```

### Question 7 :

```python

def equipe_perdantes(competition):
    res = []
    vainqueuse = equipe_vainqueuse(competition)
    
    for i in competition:
        if i != vainqueuse:
            res.append(i)
    return rse
```

### Question 8 :

Les dictionnaires

### Question 9 :

```python
mon_equipe = {1:[5,"Paul"], 7:[0,"Didier"], 2:[3,"Marc"]}
```
Il est possible de remplacer les listes par des tuples (int,str)

## Partie C :

On a une equipe :

```python
equipe_5 = [ [1, 2, "Boris"], [7,0, "Vian"], [2, 3, "Claude"] , [28, 3, "François"], [12, 3, "Patrick"],
[38, 3, "Sébastien"], [27, 3, "Thierry"], [3, 3, "Henry"], [52, 3, "Michael"], [42, 3, "Jordan"]]
```

### Question 10 :

```python
def est_present(equipe, id):
    for i in equipe:
        if i[0] == id:
            return True
    return False
```

### Question 11 :

- Meillleur des cas : l'ID est le 1er élément de la liste;
- Pire des cas : l'ID n'existe pas ou est le dernier élément de la liste.

### Question 12 :

```python

def selection(l, idx):
    mini = l[idx]
    res = idx
    
    for i in range(idx, len(l)):
        if l[i] < mini:
            mini = l[i]
            res = i
    return res

def tri_selection(equipe):
    for i in range(len(equipe)):
        mini_select = selection(equipe,i)
        equipe[i], equipe[mini_select] = equipe[mini_select], equipe[i]
```

### Question 13 :

Le tri selection

### Question 14 :

Comme vue question 11, le meilleur des cas est celui ou l'élément est soit au début, soit très proche du début.

En effectuant un tri sur l'équipe 5, on créer une sitation ou la recherche d'un élément est plus "optimisé".

Or il est possible qu'avec une liste non trié on est un résultat plus "rapide". Car si de manière aléatoire notre ID est le plus grand (donc mit en dernier place de notre liste trié), il est possible qu'une liste trié qui a cette id plus tôt dans la liste renvoie une réponse plus rapidement.

Les deux réponses peuvent êtres juste si il y a une bonne justification.

### Question 15 :

Elle permet de faire une recherche dichotomique d'un élément V (representant un id) sur une liste d'équipe **trié**.

### Question 16 :

```python

def recherche_dichotomique_recursive( element, liste_triee, idx_deb = 0, idx_fin = -1 ):
    if idx_deb == idx_fin : 
        return idx_deb
    if idx_fin == -1 : 
        idx_fin = len(liste_triee)-1
    m = (idx_deb+idx_fin)//2
    if liste_triee[m] == element :
        return m
    elif liste_triee[m][0] > element :
        return recherche_dichotomique_recursive(element, liste_triee, idx_deb, m-1)
    else :
        return recherche_dichotomique_recursive(element, liste_triee, m+1, idx_fin)
```


# Exercice 2 : 

1. jeu_video(**id**, nom, studio, annee_sortie, note_critique)

2. L'attribut studio peut être différent suivant les enregistrement : Cyberpunk -> CD Projekt ; AC Mirage -> Ubisoft

3. Les jeux développés par CD Projekt : The Witcher 3 : Wild Hunt,  Cyberpunk 2077

4. 
```sql
SELECT nom
FROM jeu_video
WHERE studio = 'Ubisoft' AND annee_sortie > 2013;
```

5.
```sql
UPDATE jeu_video
SET note_critique = 4
WHERE nom = 'OverWatch';
```

6.
```sql
INSERT INTO jeu_video(id, nom, studio, annee_sortie, note_critique) VALUES (42, 'TitanFall', 'Respawn Entertainment', 2014, 7);
```

7.
```sql
SELECT nom
FROM jeu_video
WHERE note_critique < 6 AND studio = 'Nintendo';
```

8.
```sql
DELETE FROM jeu_video
WHERE nom = 'Fallout 4';
```

9. Cela permet de ne pas surcharger la table jeu_video d'informations qui ne concernent pas les jeux vidéos mais les studios par exemple.

10. id_studio est une clef étrangère dans la table jeu_video. Elle permet de relier les tables jeu_video et studio.

11.
```sql

SELECT nom
FROM jeu_video JV
JOIN studio S ON s.id = JV.id_studio
WHERE S.pays = 'France';
```

12. CSV signifie Comma Separated Values. Ce sont des fichiers qui permettent d'organiser des données en les séparant par des virgules (plus souvent des points virgules).

13.
```python
    def jeux_du_studio(self, studio:str) -> list[jeu_video]:
        jeux = []
        for jeu in self.ludotheque :
            if jeu.studio == studio:
                jeux.append(jeu)
        return jeux
```

14.
```python
    def jeux_sortis_avant(self, annee:int) -> list[jeu_video]:
            jeux = []
            for jeu in self.ludotheque:
                if jeu.annee == annee :
                    jeux.append(jeu)
            return jeux
```

15. Comme la méthode est écrite, elle ne permet pas de gérer les doublons. De plus, les fichiers CSV avec algorithmes python ne gèrent pas la concurrence d'accès aux données ou ne gèrent pas non plus l'historique de modifications. Un SGBD est donc plus adapté à cet usage.