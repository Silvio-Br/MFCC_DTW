# MFCC_DTW
BRANCATI Silvio, BRIOT Anthony  
*Année Universitaire 2022-2023*

## Introduction

Ce projet a pour but de réaliser un système de reconnaissance de parole à l'aide de la méthode MFCC et de la méthode DTW.

### Prérequis

- Python 3.9
- numpy
- librosa

### Utilisation

Pour lancer le programme, il faut se placer dans le dossier src et lancer le fichier main.py avec la commande suivante :

```bash
python main.py <path_to_ref_oui.txt> <path_to_ref_non.txt> <path_to_tests_txt>
```

## Réponse aux questions

### Question 1

### Question 2

### Question 3
En testants les fichiers de références OUI et NON avec eux-mêmes, on obtient les résultats suivants :  

**En utilisant la moyenne**
- Bonnes réponses OUI : 6/8
- Bonnes réponses NON : 7/8

On obtient un taux de reconnaissance total de : 81.25%
Taux de reconnaissance OUI : 75%
Taux de reconnaissance NON : 87.5%  

**En utilisant le minimum**
- Bonnes réponses OUI : 8/8
- Bonnes réponses NON : 8/8

On obtient un taux de reconnaissance total de : 100%
Taux de reconnaissance OUI : 100%
Taux de reconnaissance NON : 100%
