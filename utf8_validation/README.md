======================================================================
0. UTF-8 VALIDATION
======================================================================

DESCRIPTION
-----------
Écrire une méthode permettant de déterminer si un ensemble de données
représente un encodage UTF-8 valide.

Prototype :
    def validUTF8(data)

Retour :
    True  -> si les données représentent un encodage UTF-8 valide
    False -> sinon

RAPPELS SUR UTF-8
-----------------
- Un caractère UTF-8 peut occuper de 1 à 4 octets.
- Le jeu de données peut contenir plusieurs caractères successifs.
- Chaque élément de la liste représente un octet (0 à 255).
- Seuls les 8 bits de poids faible de chaque entier doivent être pris en compte.

STRUCTURE DES OCTETS UTF-8
--------------------------
1 octet :
    0xxxxxxx

2 octets :
    110xxxxx 10xxxxxx

3 octets :
    1110xxxx 10xxxxxx 10xxxxxx

4 octets :
    11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

RÈGLE GÉNÉRALE :
    - Le premier octet indique la longueur du caractère.
    - Les octets suivants doivent commencer par 10xxxxxx.
    - Toute séquence incorrecte invalide l’encodage.

EXEMPLE D’UTILISATION
---------------------
carrie@ubuntu:~/utf8_validation$ cat 0-main.py

# (contenu du fichier principal affiché ici par l’utilisateur)
# Ce fichier sert à tester la fonction validUTF8(data)

OBJECTIF DU CODE
----------------
Votre fonction doit :
    - analyser chaque octet,
    - déterminer si la séquence respecte les règles UTF-8,
    - gérer correctement les caractères multi-octets,
    - refuser toute séquence incomplète ou mal formée.

CONTRAINTE IMPORTANTE
---------------------
Vous ne devez manipuler que les 8 bits de poids faible de chaque entier
présent dans la liste.

======================================================================
