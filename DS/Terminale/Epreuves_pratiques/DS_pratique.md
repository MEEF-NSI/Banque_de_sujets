# DS PRATIQUE : FONCTIONS

*Dans cet exercice, vous devrez developper des fonctions en python comme demandées.*

## Complétion de fonction

1. Recopier, compléter et spécifier la fonction suivante. **L'exécuter avec comme paramètre 5.**

```python
def factorielle(n):
   res = ...
   for i in range(...):
      res = res * ...
   return res
```

2. 
   1. Recopier la fonction ci-dessous et l'exécuter avec la chaîne "HEllo WOrld" en paramètre. Le résultat est-il bien celui attendu? 
   2. Écrire en commentaire le type du paramètre d'entrée et le type de la valeur de sortie de la fonction.

```python
def compte_voyelles(chaine):
   voyelles = "aeiouAEIOU"
   nb_voyelles = 0
   for char in chaine:
      if char in voyelles:
         nb_voyelles = nb_voyelles  + 1
   return nb_voyelles
```
## Écriture de fonction

1. Écrire une fonction qui renvoie la somme des entiers de 1 jusque n, avec n un nombre entier passé en paramètres.  
2. Écrire une fonction pair_ou_impair qui prend en paramètre un entier $n$ et qui renvoie **True** si l'entier est pair et **False** si celui-ci est impair.

## Chaîne de caractères

*Vous écrirez dans votre programme python les instructions pour obtenir les tâches qui vous seront demandées. Vous répondrez aux questions dans un commentaire python.*

On dispose de la chaîne de caractère, la recopier dans un fichier python :

```python
chaine = "J aime la NSI"
```

1. Afficher le 3eme et le 7eme caractères de la chaîne. 
<br/>
2. Afficher tous les caractères de la chaîne un par un en utilisant les 3 manières de réaliser une boucle vues en cours.  
   <br/>
3. Donner les caractères de la chaîne entre la position 8 et la position 11 inclues.

<br/>
4. Concaténer la chaîne donnée avec la chaîne suivante

   ```python
      chaine_2 = ' depuis Septembre.'
   ```
<br/>
5. Remplacer le premier espace par un guillemet simple ( ' ).
