======================================================================
PRIME GAME
======================================================================

DESCRIPTION
-----------
Maria et Ben jouent à un jeu basé sur les nombres premiers.
Pour chaque round, on considère un ensemble d’entiers consécutifs allant de
1 à n. Les joueurs jouent à tour de rôle :

    - Maria commence toujours.
    - À chaque tour, le joueur choisit un nombre premier encore présent.
    - Ce nombre et tous ses multiples sont retirés de l’ensemble.
    - Le joueur qui ne peut plus jouer (aucun nombre premier disponible)
      perd le round.

Ils jouent x rounds, avec des valeurs de n différentes pour chaque round.
Les joueurs jouent **optimalement**.

Votre tâche est d’écrire une fonction :

    def isWinner(x, nums)

qui détermine le joueur ayant gagné le plus de rounds.

Retour :
    - "Maria" si Maria gagne le plus de rounds
    - "Ben" si Ben gagne le plus de rounds
    - None si aucune conclusion ne peut être tirée

Contraintes :
    - x et n ≤ 10000
    - Aucun import autorisé
    - Le comportement doit être optimal et efficace

----------------------------------------------------------------------
EXEMPLE
-------
x = 3
nums = [4, 5, 1]

Round 1 : n = 4
    Maria choisit 2 → retire 2, 4
    Ben choisit 3 → retire 3
    Ben gagne (plus de prime pour Maria)

Round 2 : n = 5
    Maria choisit 2 → retire 2, 4
    Ben choisit 3 → retire 3
    Maria choisit 5 → retire 5
    Maria gagne

Round 3 : n = 1
    Aucun nombre premier → Maria ne peut pas jouer
    Ben gagne

Résultat : Ben gagne le plus de rounds.

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
    - Le code doit respecter PEP 8 (version 1.7.x)
    - Aucun package ne peut être importé

----------------------------------------------------------------------
OBJECTIF GLOBAL
---------------
Ce projet vous apprend à :
    - analyser un jeu combinatoire basé sur les nombres premiers,
    - optimiser le calcul des nombres premiers jusqu’à 10000,
    - comprendre les stratégies gagnantes dans les jeux à deux joueurs,
    - implémenter une solution efficace sans imports,
    - structurer un algorithme déterministe basé sur la théorie des nombres.

======================================================================
