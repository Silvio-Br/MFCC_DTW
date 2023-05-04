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

*Le fichier test_mfcc_files/bon_silvio.mfcc est un oui (moyenne)*  
Distance à OUI (moyenne) : 0.012051950887259669  
Distance à NON (moyenne) : 0.017155309174933454  
Distance à OUI (min) : 0.008167235254624915  
Distance à NON (min) : 0.010025653535030018  

*Le fichier test_mfcc_files/bon_antho.mfcc est un oui (moyenne)*    
Distance à OUI (moyenne) : 0.0068909390586980295  
Distance à NON (moyenne) : 0.010112608128177786  
Distance à OUI (min) : 0.0038391660173252473  
Distance à NON (min) : 0.004781138477971674  

*Le fichier test_mfcc_files/buis_silvio.mfcc est un oui (moyenne)*  
Distance à OUI (moyenne) : 0.008937183712830636  
Distance à NON (moyenne) : 0.013122936770909928  
Distance à OUI (min) : 0.005071743510568746  
Distance à NON (min) : 0.00826901835315661  

*Le fichier test_mfcc_files/buis_antho.mfcc est un non (moyenne)*  
Distance à OUI (moyenne) : 0.026094841419067868  
Distance à NON (moyenne) : 0.02335688788090782  
Distance à OUI (min) : 0.012088263267323323  
Distance à NON (min) : 0.011289541596869323  

*Le fichier test_mfcc_files/don_silvio.mfcc est un non (moyenne)*  
Distance à OUI (moyenne) : 0.035752675599955416  
Distance à NON (moyenne) : 0.035187051697848075  
Distance à OUI (min) : 0.025661810493270928  
Distance à NON (min) : 0.021871677146081726  

*Le fichier test_mfcc_files/don_antho.mfcc est un non (moyenne)*  
Distance à OUI (moyenne) : 0.02040290941713862  
Distance à NON (moyenne) : 0.019404281187970336  
Distance à OUI (min) : 0.009092131463871517  
Distance à NON (min) : 0.009283428787758799  

*Le fichier test_mfcc_files/nuit_silvio.mfcc est un oui (moyenne)*  
Distance à OUI (moyenne) : 0.004393707515557996  
Distance à NON (moyenne) : 0.008148719839841752   
Distance à OUI (min) : 0.0008612050547772357  
Distance à NON (min) : 0.0010939318412986456  

*Le fichier test_mfcc_files/nuit_antho.mfcc est un oui (moyenne)*  
Distance à OUI (moyenne) : 0.02647152470360972  
Distance à NON (moyenne) : 0.027757309943837304  
Distance à OUI (min) : 0.012795421192520622  
Distance à NON (min) : 0.014207853743115745  

### Question 2

Pour rejeter un fichier qui n'est ni OUI ni NON, 

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
