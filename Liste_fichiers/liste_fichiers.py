import os

def list_directory_contents(directory, seen=None):
    if seen is None:
        seen = set()  # Enregistre les répertoires vides déjà rencontrés
    
    total_size = 0  # Initialiser la taille totale à 0
    branch_count = 0  # Compteur de branches vides
    
    for root, dirs, files in os.walk(directory):
        # Vérifier si le répertoire est vide (ne contient pas de fichiers ni de sous-répertoires)
        if not files and not dirs:
            if root not in seen:
                seen.add(root)
                branch_count += 1
                print(f"Branch vide: {root}")
        
        # Afficher le répertoire actuel
        print(f"Répertoire: {root}")
        
        # Calculer la taille totale des fichiers dans le répertoire courant
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size
            print(f"  Fichier: {file}, Taille: {file_size} octets")
        
        # Afficher le nombre de fichiers dans le répertoire courant
        print(f"  Nombre de fichiers: {len(files)}")
        
        # Afficher le nombre de sous-répertoires dans le répertoire courant
        print(f"  Nombre de sous-répertoires: {len(dirs)}")
    
    print(f"Poids total de l'arborescence: {total_size} octets")
    print(f"Nombre de branches vides: {branch_count}")

    # Proposer de supprimer les branches vides
    confirm = input("\nSouhaitez-vous supprimer les branches vides ? (o/n) ")
    if confirm.lower() == 'o':
        for branch in seen:
            try:
                os.rmdir(branch)
                print(f"Branch supprimée: {branch}")
            except OSError as e:
                print(f"Erreur lors de la suppression de {branch}: {e}")
        print("Suppression terminée.")
    else:
        print("Suppression annulée.")

# Utiliser le répertoire courant comme point de départ
directory_to_analyze = os.path.dirname(__file__)

# Appeler la fonction pour lister les éléments du répertoire et leurs poids
list_directory_contents(directory_to_analyze)