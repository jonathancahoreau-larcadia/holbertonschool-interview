======================================================================
N QUEENS
======================================================================

DESCRIPTION
-----------
Le problème des N reines consiste à placer N reines sur un échiquier de
taille N×N de manière à ce qu’aucune reine ne puisse en attaquer une autre.
Cela signifie :

    - aucune reine sur la même ligne
    - aucune reine sur la même colonne
    - aucune reine sur la même diagonale

L’objectif de ce projet est d’écrire un programme Python capable d’afficher
toutes les solutions possibles pour un N donné.

----------------------------------------------------------------------
USAGE
-----
    nqueens N

CONTRAINTES D’UTILISATION
-------------------------
- Si le nombre d’arguments est incorrect :
      Usage: nqueens N
  puis sortie avec le statut 1.

- Si N n’est pas un entier :
      N must be a number
  puis sortie avec le statut 1.

- Si N < 4 :
      N must be at least 4
  puis sortie avec le statut 1.

- Le programme doit afficher **toutes** les solutions possibles.
- Une solution par ligne.
- Format : liste de positions [row, col] pour chaque reine.
- L’ordre des solutions n’a pas d’importance.
- Vous ne pouvez importer que le module sys.

----------------------------------------------------------------------
EXEMPLE DE SORTIE (FORMAT)
--------------------------
Chaque solution doit être affichée sous la forme :

    [[0, 1], [1, 3], [2, 0], [3, 2]]

où chaque sous-liste représente la position d’une reine :
    [ligne, colonne]

----------------------------------------------------------------------
REQUIREMENTS
------------

GENERAL
    - Éditeurs autorisés : vi, vim, emacs
    - Tous les fichiers seront interprétés/compilés sur Ubuntu 14.04 LTS
      avec Python 3.4.3
    - Tous les fichiers doivent se terminer par une nouvelle ligne
    - Tous les fichiers doivent être exécutables
    - La première ligne de tous les fichiers doit être exactement :
          #!/usr/bin/python3
    - Un fichier README.md est obligatoire à la racine du projet
    - Le code doit respecter PEP 8 (version 1.7.*)
    - Vous ne pouvez importer que le module sys

----------------------------------------------------------------------
OBJECTIF GLOBAL
---------------
Ce projet vous apprend à :
    - résoudre un problème classique de backtracking,
    - manipuler la récursivité pour explorer toutes les possibilités,
    - gérer proprement les erreurs d’entrée utilisateur,
    - structurer un algorithme de recherche exhaustive,
    - produire des solutions dans un format strict et validable.

======================================================================
