# Autour de moi

Une page web minimaliste, pensée pour Chrome sur Android, qui liste les lieux d'intérêt autour de vous (patrimoine, nature, attractions) avec leur distance, leur direction et un lien vers l'article Wikipédia.

2 versions:

- une avec radar simple (sans carte) = **simple_autour-de-moi.html**

- une avec radar + carte = **carto_autour-de-moi.html**

## Fonctionnalités

- Géolocalisation avec un rayon au choix : 100 m, 200 m, 500 m, 1 km ou 2 km
- Liste des lieux triés du plus proche au plus éloigné : nom, distance à vol d'oiseau, direction
- Flèche d'orientation qui tourne avec la boussole du téléphone (elle indique la direction du lieu par rapport à vous)
- Compteur de lieux trouvés
- Radar à l'échelle du rayon, avec fond de carte OpenStreetMap en option (masquable en un appui sur la croix si la connexion est lente)
- Bouton **Wiki** pour ouvrir l'article ; pour l'écouter, utilisez la lecture vocale de Chrome (menu ⋮, puis « Écouter »)
- Bouton plein écran
- Thème clair ou sombre automatique

## Utilisation

1. Ouvrez la page dans Chrome sur Android.
2. Autorisez la localisation (de préférence « position précise »).
3. Choisissez un rayon, puis appuyez sur **Me localiser**.

Astuce : menu ⋮ de Chrome, puis « Ajouter à l'écran d'accueil » pour l'avoir comme une appli.

## Installation

Il n'y a rien à compiler : c'est un seul fichier HTML.

1. Déposez le fichier `index.html` dans un dépôt GitHub.
2. Activez GitHub Pages : **Settings, Pages, Deploy from a branch**, branche `main`, dossier `/ (root)`.
3. Ouvrez l'adresse `https://votre-nom.github.io/nom-du-depot/` sur votre téléphone.

La géolocalisation ne fonctionne qu'en `https://`, ce que GitHub Pages fournit automatiquement.

## Données et crédits

- Lieux : [Wikipédia](https://fr.wikipedia.org) (API de recherche géographique), filtrés par catégories pour écarter les commerces, entreprises, écoles, etc.
- Fond de carte : © les contributeurs [OpenStreetMap](https://www.openstreetmap.org/copyright), via les tuiles publiques d'OpenStreetMap. Usage léger uniquement : pour une diffusion large, passez par un fournisseur de tuiles avec clé.

## Limites

- Seuls les lieux ayant des coordonnées sur Wikipédia apparaissent ; en zone rurale, la liste peut être vide.
- Le filtre sur les catégories est approximatif : quelques lieux peuvent être affichés à tort ou écartés à tort.
- La boussole est plus fiable quand le téléphone est tenu à plat. Sans boussole, les flèches pointent vers le nord.
- Une connexion internet est nécessaire.

## Auteur

[@rcheomatic](https://github.com/rcheomatic) — Sylvain Badey, Inrap, 2026

## Licence

[![CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/deed.fr)

Ce travail est mis à disposition selon les termes de la licence [Creative Commons Attribution - Pas d'Utilisation Commerciale 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.fr). Voir le fichier [`LICENSE`](LICENSE).
