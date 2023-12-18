# **DS : Bases de données relationnelles**

## **Exercice 1 : Questions de cours**

1. Qu'est-ce qu'un SGBD ?
2. Citer 3 noms de SGBD.
3. Avec quel conquête, l'idée des bases de données apparaît ? 
4. Citer les 5 modèles de SGBD ?
5. Citer 2 contraintes d'intégrité, donner des exemples pour les illustrer.
6. Expliquer la notion de clef primaire et clef étrangère dans une relation.
7. Donner les propriétés de la norme ACID.

Bonus :

8. Quel opération est effectuée quand on réalise une jointure ?

## **Exercice 2 : Correction de contraintes**

Toutes ces tables ont des erreurs de contraintes d'intégrité. Corriger les contraintes et expliquer l'erreur.

La relation Élève:
|id\_eleve|Prenom\_eleve|Nom\_eleve|Age|
| - | - | - | - |
|6654|Jack|Celere|15|
|96556|Emile|Ehimage|543|
|666A|Lara|Clette|16|
|5375|Tim|Punk|16|

La relation Enseignant:
|id\_enseignant|Nom\_enseignant|id\_Matiere|
| - | - | - |
|42351|Martin|9|
|78567|Petit|15|
||Anderson|6|
|7877745|Alami|5465|

La relation matière:

|id\_Matiere|Nom\_Matiere|Coefficient|
| - | - | - |
|6|Technologie|1|
|9|SVT|6|
|9|NSI|9|
|5465|Info-Com|6|


## Exercice 3 :  Ajout, Suppression et modification de donneés dans une table

Une SPA (Société Protectrice des Animaux) a besoin d'un système de gestion pour suivre les adoptions d'animaux et les informations sur les adoptants. On propose les relations suivantes.

Un animal est défini par un identifiant, son espece, sa race, son nom, son age et sa date d'arrivée.
Un adpotant est défini par son id d'adoptant, son prénom, son nom et le nombre d'animaux qu'il possède.
On représente l'adoption une relation qui est définie par l'identifiant de l'animal, celui de l'adoptant et la date d'adoption.

1. Donner le schéma relationnel de ces relations. **Vous soulignerez les clefs primaires et vous mettrez un # devant chaque clef étrangère**.
   
2. Ajoutez les données suivantes aux tables :
    * Animal :
      * 1, Chat, Siamois, Whiskers, 3, 2023-01-15
      * 2, Chien, Labrador, Buddy, 2, 2023-02-20
      * 3, Chien, Golden Retriever, Bella, 4, 2023-03-10
    * Adoptant :
      * 12345, Jeff, Paspied, 2
      * 54321, Jean, Bono , 1
      * 98765, David, Hégoliate, 0
    * Adoption :
      * 1, 12345, 2023-02-25
      * 2, 54321, 2023-03-15

3. Monsieur Paspied souhaite adopter le chien nommé Bella le 14/11/2023.
    * Ajouter à la table Adoption la requête correspondante.
    <br/>
    * Comme le chien Bella sera adopté, retirer ses informations de la base de données.
    <br/>
    * Quelle modification est aussi à réaliser par rapport aux informations de monsieur Smith dans la base de données ? La réaliser.



## Exercice 4 : Requêtes SQL 

Un groupe de praticiens a décidé de s'unir pour louer un batiment pour créer leurs cabinets pour réduire leurs frais.
Les patients sont donc amenés à se diriger au cabinet médical pour être consultés par leurs médecins.
Une base de données permet à ces medecins de renseigner quels patients sont venus, voir quel praticien.
Les rendez-vous sont renseignés aussi dans la base de données pour permettre aux medecins de voir quelles sont les demandes les plus récurrentes.

On propose les relations suivantes :

Patient(**id_patient**, nom, prenom, age, ville, #id_praticien)
</br>



| id_patient | nom      | prenom    | age | ville      | id_praticien |
|------------|----------|-----------|-----|------------|--------------|
| 1          | Dupont   | Bernard   | 45  | Paris      | 101          |
| 2          | Dubois   | Pierre    | 32  | Loos       | 102          |
| 3          | Nelson   | Paul      | 28  | Lille      | 103          |
| 4          | Wong | Jeannine  | 50  | Ajaccio    | 104          |
| 5          | Newmann   | Pauline   | 22  | Marseille  | 101          |

Praticien(**id_praticien**, nom, prenom, profession)
</br>
| id_praticien | nom      | prenom | profession            |
|--------------|----------|--------|-----------------------|
| 101          | Mamour   | Jean   | Médecin généraliste  |
| 102          | Alami    | Ahmed  | Cardiologue           |
| 103          | Fonfec    | Sophie | Dermatologue          |
| 104          | Pètre | Napoleon | Chirurgien         |

RendezVous(**#id_praticien, #id_patient**, date, objet)
</br>
| id_praticien | id_patient | date       | objet                  |
|--------------|------------|------------|------------------------|
| 101          | 1          | 2023-01-15 | Consultation générale  |
| 102          | 2          | 2023-02-20 | Examen cardiaque       |
| 103          | 3          | 2023-03-10 | Contrôle dermatologique|
| 101          | 4          | 2023-04-05 | Chirurgie du genou     |
| 102          | 5          | 2023-05-12 | Bilan cardiaque        |



1. Donner tous les patients se prénommant *Bernard*.

2. Compléter la requête SQL suivante :
Donner tous les rendez-vous ayant été proposés avant le 18-05-2023.
```sql
SELECT * FROM RendezVous WHERE date < '_______';
```

3. Donner tous les patients ayant pour nom de famille *Dubois* et vivant à Loos.

4. Donner les praticiens que monsieur *Alami* a reçu.

5. Donner l'âge de toutes les personnes ayant un nom de famille commençant par *N* et un prénom commençant par *P*

6. Donner tous les rendez vous effectués par le docteur *Mamour* en 2023.

7. A quoi sert cette requête ?
```sql
SELECT Pat.nom, Pat.prenom, R.objet
FROM RendezVous R
JOIN Patient Pat ON R.id_patient = Pat.id_patient
WHERE R.objet LIKE 'Consultation%';
```
   
**Bonus** : Donner le nombre de rendez-vous de monsieur *Wong* avec le docteur *Grey*.


## Exercice 5 : Listes chaînées
On dispose d'une liste chaînée de maillons. Celle-çi est obtenue en utilisant une approche par Programmation Orientée Objet impliquant une classe Maillon et une classe ListeChainee.

On considère la liste chaînée suivante :
[7|●]-->[3|●]-->[4|●]-->[5|X]
</br>
X correspond à un suivant qui est à None.
</br>
● correspond à un suivant qui est défini et qui est celui pointé par la flèche.

1. Inserer un maillon de valeur 9 entre le maillon de valeur 3 et le maillon de valeur 4.

2. Supprimer le maillon de valeur 2
