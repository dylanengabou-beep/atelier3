from voiture import Voiture
from parc_voitures import ParcVoitures

parc = ParcVoitures()

voitures1 = Voiture("Toyota", "Corolla", 2025)
voitures2 = Voiture("lamborgini", "Aventador", 2024)

parc.ajouter_voitures(voitures1)
parc.ajouter_voitures(voitures2)
parc.afficher_voitures()