"""
Guidotti, E., Ardia, D., (2020).
COVID-19 Data Hub
Journal of Open Source Software, 5(51):2376
https://doi.org/10.21105/joss.02376
"""

def lire_fichier_csv(path):
    '''str -> list
       retourne une liste de dictionnaires partageant les mêmes descripteurs
       issus du fichier csv dont le chemin est donné par path
       le fichier csv doit contenir une première ligne avec les descripteurs
    '''
    csv_file = open(path, "r") 
    liste = [] # creation de la liste  
    for index,ligne in enumerate(csv_file):
        if index == 0:
            # récuperation de la liste des descripteurs sur la premiere ligne
            descripteurs = ligne.strip().split(',')
        else:
            # nouvel enregistrement
            enregistrement={}
            donnees = ligne.strip().split(',')     
            for descripteur,donnee in zip(descripteurs,donnees):
                enregistrement[descripteur]=donnee
            # l'enregistrement est ajouté à la liste
            liste.append(enregistrement)    
    csv_file.close()
    return liste
