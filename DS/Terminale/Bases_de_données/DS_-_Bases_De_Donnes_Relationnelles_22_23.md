**DS - Bases De Données Relationnelles**

**Partie 1 : Contraintes d’intégrité                                 /4**

Les tables suivantes possèdent des erreurs de contraintes d’intégrité. On cherche à les corriger pour pouvoir rendre les données cohérentes. Pour chacune de ces tables, **citer en justifiant** la/les contrainte/s d’intégrité qui

n’est / ne sont pas respectée/s.

La relation Élève:

|id\_eleve|Prenom\_eleve|Nom\_eleve|Age|
| - | - | - | - |
|6654|Jack|Celere|15|
|96556|Emile|Ehimage|543|
|666A|Lara|Clette|16|
|5375|Tim|Punk|16|
|2134|Otto|Matik|12|
|4323|Sandy|Metrehé|14|
|2143|Sophie|Fonfec|353|

La relation Enseignant:



|id\_enseignant|Nom\_enseignant|id\_Matiere|
| - | - | - |
|42351|Martin|9|
|78567|Petit|15|
|872345|Anderson|6|




|id\_enseignant|Nom\_enseignant|id\_Matiere|
| - | - | - |
|7877745|Alami|5465|
|34514|Garcia|3|
|1239|Lopez|3|

La relation matière:



|id\_Matiere|Nom\_Matiere|Coefficient|
| - | - | - |
|6|Technologie|1|
|9|SVT|6|
|9|NSI|9|
|5465|Info-Com|6|
|3|Maths|7|

**Partie 2 : Requêtes SQL                                                     /10**

Une société de vente automobile utilise une base de données pour gérer les différents véhicules. Cette base de données permet aussi de répertorier tous ses vendeurs. Elle contient toutes les ventes des vendeurs au fil des années.

On considère les relations suivantes :

**Voiture** (*Id\_Voiture*, Modèle, Marque, Prix, Kilométrage, Année\_Mise\_en\_Vente) **Vendeur** (*Id\_Vendeur*, Nom, Prénom, Ancienneté)

**Vente** (*Num\_Vente*, Prix\_Vente\_Final, Date\_vente, #Id\_Voiture, #Id\_Vendeur)

On considère que l’Id\_Voiture est incrémenté à chaque création d’une voiture dans la base. Il n’y a donc aucune redondance de ces identifiants.

Pour simplifier, on considère que les voitures sont enregistrées à vie pour garder une trace dans leur historique VIN.

1. Identifier les clefs primaires et étrangères
2. Écrire en langage SQL les requêtes qui permettent d’afficher :
3. Toutes les voitures
4. Toutes les voitures de la marque ‘Renault’.
5. Toutes les voitures étant affichées à plus de 10000€.
6. Le nombre de voitures ayant plus de 100.000km.
7. Tous les vendeurs ayant pour nom de famille ‘Pernault’
8. Tous les vendeurs qui ont réalisé une vente où le prix de vente est plus élevé que le prix initial de la voiture.
9. Toutes les ventes des vendeurs ayant plus de 10 ans d’Ancienneté.
10. Toutes le voitures mises en vente après 2020 par ordre décroissant d’Années.
11. Le nombre de modèles en vente **sans doublons**.
12. Les vendeurs ayant été embauchés en 2015 ayant ‘nsi’ dans leur nom de famille.
13. Écrire en langage SQL les requêtes pour :
14. Insérer dans la table *Voiture* les données (501, Modus, Renault, 1235, 250584, 2014)
15. Modifier dans la table le prix de la voiture 274 à 4755 euros.
16. Supprimer toutes les voitures Citroën.

**Partie 3 : Conception d’une base de données                /6**

On considère une entreprise de vente en ligne.

Cette entreprise vend divers produits représentés par *une identificateur **unique**, un libellé et un prix*. 

Ces produits sont vendus à des clients qui sont renseignés par *leur nom, leur adresse en 3 champs : ville, rue et code Postal, leur adresse e-mail et leur date de naissance*. Ils sont associés à un *numéro **unique***.

Ces produits sont répertoriés en commandes identifiables par le numéro du client, celui de l’opérateur et celui du produit.

Les commandes sont réalisés par des opérateurs qui sont identifiés par *un numéro **unique**, leur nom et la ville où ils résident pour savoir à quel entrepôt ils travaillent*.

Enfin, ces commandes sont facturées. Ces factures contiennent les informations suivantes : *un numéro **unique**, une date, le numéro du client pour le retrouver et réaliser l’expédition et le numéro de l’opérateur pour gérer les erreurs dans les commandes s’il y en a, le numéro de commande*.

Avec toutes ces informations, proposer un schéma sous forme littérale ou en diagramme et indiquer les clefs primaires et étrangères et les relations entre les tables. 
