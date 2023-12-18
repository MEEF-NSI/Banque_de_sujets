#Création du lexique:
with open('lexique.txt', 'r', encoding='utf8') as f:
    mots = f.readlines()

LEXIQUE = [m.lower().rstrip('\n') for m in mots]

#Définition des fonctions



#Programme principal

