======================================================================
README — 0. Log Parsing
======================================================================

DESCRIPTION
-----------
Cet exercice consiste à écrire un script Python capable de lire des logs
depuis l’entrée standard (stdin), de les analyser en temps réel et
d’afficher des statistiques cumulées.

Le programme doit être robuste, tolérant aux lignes invalides et capable
de produire un état des métriques à intervalles réguliers ou lors d’une
interruption clavier.

----------------------------------------------------------------------
OBJECTIF DU SCRIPT
------------------
- Lire stdin ligne par ligne.
- Extraire deux informations :
    * le code de statut HTTP
    * la taille du fichier
- Accumuler les métriques globales.
- Afficher les statistiques :
    * toutes les 10 lignes valides
    * ou lors d’un CTRL + C (KeyboardInterrupt)

----------------------------------------------------------------------
FORMAT D’ENTRÉE ATTENDU
-----------------------
Chaque ligne doit respecter strictement le format suivant :

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Exemple :
192.168.0.1 - [2024-02-12] "GET /projects/260 HTTP/1.1" 200 512

Toute ligne ne respectant pas ce format doit être ignorée.

----------------------------------------------------------------------
STATISTIQUES À AFFICHER
-----------------------

1. Taille totale des fichiers :
   File size: <total size>

2. Nombre d’occurrences par code HTTP :
   <status code>: <count>

Codes pris en charge :
200, 301, 400, 401, 403, 404, 405, 500

Règles :
- n’afficher un code que s’il est apparu
- afficher les codes dans l’ordre croissant

----------------------------------------------------------------------
COMPORTEMENT LORS D’UNE INTERRUPTION
------------------------------------
En cas de CTRL + C :
- afficher les statistiques courantes
- terminer proprement le programme

----------------------------------------------------------------------
CONTRAINTES TECHNIQUES
----------------------
- Le script ne doit pas s’exécuter lors d’un import :
      if __name__ == "__main__":
          ...
- Aucun module externe n’est autorisé.
- Le code doit être propre, lisible et conforme aux bonnes pratiques.

----------------------------------------------------------------------
UTILISATION
-----------
- Rendre le script exécutable :
      chmod +x 0-stats.py
- Exécuter en fournissant des logs sur stdin :
      cat logs.txt | ./0-stats.py
- Ou utiliser le générateur de logs intégré :
      ./0-generator.py | ./0-stats.py

EXEMPLE D’EXÉCUTION
-------------------
$ cat logs.txt | ./0-stats.py
File size: 4210
200: 3
301: 1
404: 2

(Note : les valeurs affichées peuvent varier.)

----------------------------------------------------------------------
BUT PÉDAGOGIQUE
----------------
Cet exercice vise à renforcer :
- la manipulation de stdin
- le parsing de chaînes
- la gestion d’exceptions
- la construction de compteurs et d’agrégations
- la robustesse face aux formats imprévus
- la gestion d’interruptions système
- la structuration d’un script Python non exécutable à l’import

======================================================================
