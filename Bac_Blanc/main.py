import csv


class jeu_video:

    def __init__(self, nom:str, studio:str, annee_sortie:int,note_critique:int) -> None:
        assert int(note_critique) <= 10 and int(note_critique) >= 0, "La note doit être comprise entre 0 et 10"
        self.nom = nom
        self.studio = studio
        self.annee_sortie = annee_sortie
        self.note_critique = note_critique

    def __str__(self) -> str:
        return f"{self.nom} est un jeu de {self.studio} sorti en {self.annee_sortie} et a eu une note critique de {self.note_critique}/10"
    

class ludotheque:
    def __init__(self, csv_file) -> None:
        self.ludotheque = []
        with open(csv_file, "r") as csv_file:
            dictReader = csv.DictReader(csv_file)
            for ligne in dictReader:
                jeu = jeu_video(ligne["nom"], ligne["studio"], ligne["annee_sortie"], ligne["note_critique"])
                self.ludotheque.append(jeu)

    def jeux_du_studio(self, studio:str) -> list[jeu_video]:
        jeux = []
        for jeu in ... :
            if jeu.studio == ...:
                jeux.append(...)
        return ...
    
    def jeux_sortis_avant(self, annee:int) -> list[jeu_video]:
        jeux = []
        for jeu in ...:
            if ... :
                jeux.append(...)
        return ...

    def ajouter_jeu(self, jeu) -> None:
        '''
        Ajoute un jeu à la ludothèque en vidant le fichier CSV et réécrivant tous les jeux.
        '''
        self.ludotheque.append(jeu)
        champs = ['nom', 'studio', 'annee_sortie', 'note_critique']

        # Réécriture du fichier CSV avec tous les jeux de la ludothèque
        with open("jeux.csv", "a", newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=champs)
            writer.writerow({'nom': jeu.nom, 'studio': jeu.studio, 'annee_sortie': jeu.annee_sortie, 'note_critique': jeu.note_critique})


if __name__ == "__main__":
    RDR = jeu_video("Red Dead Redemption", "Rockstar", 2018, 10)
    AC = jeu_video("Assassin's Creed", "Ubisoft", 2007, 9)

    ludo = ludotheque('jeux.csv')
    GOW = jeu_video("God Of War", "Santa Monica Studio", 2018, 9)
    FG = jeu_video("Fall Guys", "Mediatonic", 2020, 8)

    ludo.ajouter_jeu(FG)
