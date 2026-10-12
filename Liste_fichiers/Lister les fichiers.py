# Pour lister les fichiers d'un répertoire en Python, vous pouvez utiliser le module moderne pathlib

from pathlib import Path

# Définissez le chemin du dossier
chemin_dossier = Path(r'C:\Users\sbadey\Documents\SLY_Perso\Inrap\Chantiers_en_cours\2024\D152267_Auxerre_Yonne_VNF\donnee_spatiale\image_georef\Carte_1888_BnF')

# Lister uniquement les fichiers .tif
for fichier in chemin_dossier.iterdir():
    if fichier.is_file() and fichier.suffix.lower() == '.tif':
        print(fichier.name)
