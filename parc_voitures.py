from voiture import Voiture

class ParcVoitures:
    def __init__(self):
        self.voitures = []

    def ajouter_voitures(self, voiture):
        self.voitures.append(voiture)

    def afficher_voitures(self):
        for voiture in self.voitures:
            voiture.afficher_details()
            print("-------------------")


