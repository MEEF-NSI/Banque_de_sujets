Le tri par dénombrement est un algorithme de tri qui n'agit pas par comparaisons mais par comptage des éléments de la liste.

Exemple : Dans la liste L **[3,2,1,2]**, on peut dénombrer les valeurs de cette manière : une occurence de 1, deux occurences de 2 et une occurence de 3.

*Principe de fonctionnement :*
On considère la liste L précédente:

* On créée une liste d'occurences contenant un nombre de 0 équivalent à la valeur maximale + 1 de la liste à trier et une liste vide qui contiendra, à la fin, les éléments de la liste de départ triés.


    **L = [3, 2, 1, 2]
    occurences = [0,0,0,0]
    liste_triee = []**


* On parcourt la liste L à trier et à chaque élément, on incrémente la valeur à l'indice du nombre rencontré dans la liste d'occurences.

| itération | L                | occurences   |
| --------- | ---------------- | ------------ |
| 0         | [3,2,1,2]        | [0, 0, 0, 0] |
| 1         | [**3**, 2, 1, 2] | [0, 0, 0, 1] |
| 2         | [3, **2**, 1, 2] | [0, 0, 1, 1] |
| 3         | [3, 2, **1**, 2] | [0, 1, 1, 1] |
| 4         | [3, 2, 1, **2**] | [0, 1, 2, 1] |
  

* On peuple la liste vide de $x$ fois le nombre rencontré en balayant la liste d'occurences.

| itération | occurences       | liste_triee |
| --------- | ---------------- | ----------- |
| 1         | [**0**, 1, 2, 1] | []          |
| 2         | [0, **1**, 2, 1] | [1]         |
| 3         | [0, 1, **2**, 1] | [1, 2, 2]   |
| 4         | [0, 1, 2, **1**] | [1,2,2,3]   |
