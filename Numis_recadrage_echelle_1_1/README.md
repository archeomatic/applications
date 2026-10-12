# Numis recadrage 1:1

Outil web **local** (un seul fichier HTML) pour **mettre à l'échelle et recadrer en carré des photos à l'échelle réelle 1:1, à 300 dpi**, à partir de l'échelle graphique présente sur chaque photo.

Pensé pour des séries de photos d'objets (monnaies, petit mobilier, etc.) où l'échelle graphique varie légèrement d'une prise de vue à l'autre.

> Aucune installation, aucun serveur, aucun envoi de données : tout se passe dans le navigateur, les photos ne quittent pas votre ordinateur.

## Principe

1. Vous chargez un dossier de photos.
2. Pour chaque photo, vous cliquez deux points distants d'**1 cm** sur l'échelle graphique : l'outil calcule le nombre de pixels par centimètre.
3. Vous indiquez la taille du carré voulue en sortie (en mm) : un carré rouge, à la taille réelle correspondante, s'affiche sur la photo.
4. Vous positionnez le carré, puis enregistrez : l'image exportée est recadrée et rééchantillonnée pour que 1 px de sortie = 1/300 pouce, soit une taille physique exacte à 300 dpi.

## Utilisation

1. Télécharger (ou cloner) le dépôt et **double-cliquer sur `Numis_recadrage_1_1.html`** pour l'ouvrir dans le navigateur.
2. **Choisir un dossier** photo (le sélecteur en haut à gauche).
3. **Calibrer** : cliquer deux points distants d'1 cm dans la réalité sur l'échelle graphique.
4. Indiquer la **taille du carré en sortie** (en mm, 30 mm par défaut).
5. **Déplacer le carré rouge** à la souris pour cadrer l'objet.
6. Cliquer sur **« Enregistrer la photo recadrée »**.
7. Passer à la photo suivante avec **« Suivante → »** (ou revenir avec **« ← Précédente »**).

### Boutons

| Bouton                        | Effet                                                           |
| ----------------------------- | --------------------------------------------------------------- |
| ← Précédente / Suivante →     | Navigue dans les photos du dossier (tri alphabétique/numérique) |
| Refaire la calibration        | Efface les deux points et le carré pour recommencer la mesure   |
| Recentrer le carré            | Replace le carré rouge au centre de la photo                    |
| Enregistrer la photo recadrée | Exporte le recadrage en PNG                                     |

## Résultat

- Format : **PNG**
- Nom du fichier : `<nom_original>_ech1-1_300dpi.png`
- Taille en pixels : `taille_mm / 25,4 × 300` (par ex. 30 mm → 354 × 354 px, 20 mm → 236 × 236 px)
- Le fichier est téléchargé par le navigateur (dossier de téléchargements habituel).

## Formats d'images acceptés

JPEG (`.jpg`, `.jpeg`), PNG, WebP, TIFF (`.tif`, `.tiff`).

> Le TIFF n'est affiché que par les navigateurs qui le gèrent nativement (Safari notamment). Dans Chrome, Edge ou Firefox, convertir au préalable en JPEG ou PNG.

## Compatibilité

Navigateur récent (Chrome, Edge, Firefox, Safari) avec prise en charge de la sélection de dossier (`webkitdirectory`). Fonctionne hors ligne.

## Limites connues

- La calibration est **à refaire pour chaque photo** (c'est voulu, l'échelle varie d'une photo à l'autre).
- Le PNG exporté a la bonne taille en pixels pour 300 dpi, mais le navigateur n'écrit pas la métadonnée de résolution (dpi) dans le fichier. Si votre logiciel de mise en page ou de dessin lit cette métadonnée, il peut être nécessaire de la définir à 300 dpi à l'ouverture.
- La précision dépend de celle des deux clics : zoomer la photo d'origine ou choisir des repères nets sur l'échelle graphique améliore le résultat.

## Origine du code

Ce script a été généré avec l'aide de **ChatGPT 5.6** (le 21/09/2026), à partir de deux prompts :

1. *« J'ai une série de photos avec des échelles graphiques (de taille légèrement différente sur chaque photo) et je voudrais les recadrer au format carré à l'échelle réelle 1:1 à 300 dpi. Est-ce que tu peux me faire une interface type web en local dans laquelle je charge un dossier et image par image je peux cliquer sur 2 points de distance 1 cm sur la photo puis recadrer en carré à 300 dpi. »*
2. *« La v1 est déjà pas mal mais je ne vois pas les photos quand j'ai sélectionné le dossier. »*

## Auteur

[@rcheomatic](https://github.com/rcheomatic) — Sylvain Badey, Inrap, 2026

## Licence

[![CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/deed.fr)

Ce travail est mis à disposition selon les termes de la licence [Creative Commons Attribution - Pas d'Utilisation Commerciale 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.fr). Voir le fichier [`LICENSE`](LICENSE).
