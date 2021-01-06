"""
Ce programme est un ensemble de fonctions que je vais utiliser pour traiter les données. Il faut que dans le répertoire de travail il y ait les fichiers "Motifs.csv", un dossier "Classes" avec à l'intérieur les classes avec les élèves en format csv.
"""


"""
Initialement il y a dans le dossier "Classes" des fichiers csv (1 par classe). Dans chaque fichier csv, il y a le Nom, Prénom, Genre de chaque élève (1 élève par ligne). On veut transformer ce csv, pour qu'il ait aussi le nombres de rapports (pour chaque motifs) ainsi que le nombre de présences. Pour transformer le csv on a fait la fonction InitialiserCsvClasse. 

Pour ajouter incrémenter le nombre de rapport d'un élève on utilise la fonction MAJ_Eleve, et le nombre de présences d'un élève MAJ_Eleve_Presence.

"""


"""
On importe les pakage nécessaires pour récupérer les données et les traiter
"""

import csv # Pour utiliser des csv
import sqlite3
import os # Pour naviguer dans l'OS
from collections import OrderedDict #Le paquet csv génère des OrderedDict, je prends ce paquet pour les convertir


# C'est une petite fonction pour que j'aille dans mon dossier courant de Pyzo. Elle est à modifier suivant votre ordinateur
def dossier():
    import os
    os.chdir("Google Drive//Python//Application Prof//App Prof")

#dossier()    # Je la met en commentaire pour ne pas la lancer tout le temps.



# On fait cette fonction pour mettre des en-tête au fichier csv.
def Fieldnames():
    # On ouvre "Motifs.csv" que l'on appelle file.
    with open("Motifs.csv", "r") as file:
        # On utilise le lecteur du package csv, et MotifReader est le lecteur de file (donc de Motif.csv)
        MotifReader = csv.reader(file)
        # Je fais une liste fieldnames
        fieldnames = ["Nom","Prénom","Sexe","Présences"]
        # Pour toutes les lignes de "Motifs.csv"
        for row in MotifReader:
            # on ajoutes la ligne à fieldnames.
            fieldnames.append(row[0])
    # La fonction renvoie la liste fieldnames.
    return fieldnames


#On transforme un fichier csv facile à écrire à la main en fichier csv facilement utilisable informatiquement.
def InitialiserCsvClasse(string): 
    # mettre en string le fichier à convertir. avec Nom,Prénom, Sexe (chaque nouvel eleve en ligne)
    
    # On utilise la fonction précédente pour se préparer les en-tête
    fieldnames = Fieldnames()
    #On récupère l'adresse du dossier courant
    path = os.getcwd()
    #On va dans le dossier Classes
    os.chdir("Classes")
    #On ouvre le fichier csv de nom string. Deviner quel est le type de string ? On appelle ce fichier file. le "r" veut dire lecture.
    with open(string + ".csv","r") as file:
        #On appelle le lecteur : reader
        reader = csv.reader(file)
        #On crée une liste vide
        
        ListeEleve = [] # Chaque item sera un dico  (Ceci est un commentaire que je me suis mis quand j'ai fait ce bout de code)
        
        #Pour chaque ligne du fichier csv
        for row in reader:
            # On ajoute à ListeEleve la ligne (bon ben dans ListeEleve il n'y a pas de dictionnaire, j'ai dû changer d'avis entre temps ^^)
            ListeEleve.append(row)
        
    # On ouvre maintenant le fichier csv pour écriture.
    with open(string + ".csv","w") as file:
        # On crée un stylo que l'on appelle writer, et on met en en-tête notre en-tête préparée.
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # On écrit l'en-tête
        writer.writeheader()
        # Pour chaque Eleve de ListeEleve (un élève est une liste de 3 éléments)
        for eleve in ListeEleve:
            print(eleve)
            # On crée un dictionnaire temporaire vide.
            tempdico = {}
            #Pour chaque champ dans liste fieldnames
            for field in fieldnames:
                #On met dans le dictionnaire la valeur     field:0
                tempdico[field] = 0
                # Si le champ est Nom et ben on met le nom
                if field == "Nom":
                    tempdico[field] = eleve[0]
                # En exo
                if field == "Prénom":
                    tempdico[field] = eleve[1]
                # En exo
                if field == "Sexe":
                    tempdico[field] = eleve[2]
            # Puis on met dans le csv notre dictionnaire temporaire avant de remonter la boucle
            writer.writerow(tempdico)
    # Quand c'est fini on revient dans le dossier courant.        
    os.chdir(path)
 

    
# Toutes les fonctions de cette fonction ont déjà été introduites précédemment. A vous de le commenter en exercice
def LireCSVversDico(string): #Fonction intermediaire pour avoir un dico modifiable
    path = os.getcwd()
    os.chdir("Classes")
    with open(string + ".csv","r") as file:
        reader = csv.DictReader(file)
        DicoEleve = {} # Chaque item sera un dico
        for row in reader:
            DicoEleve[dict(row)["Nom"]] = dict(row)
    os.chdir(path)
    return DicoEleve



# Idem ici
def EcrireCsvDeDico(string,dico):
    fieldnames = Fieldnames()
    path = os.getcwd()
    os.chdir("Classes")
    with open(string + ".csv","w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for eleve in dico:
            tempdico = dico[eleve]
            writer.writerow(tempdico)
    os.chdir(path)


def MAJ_Eleve(nom,classe,motif): #Fonction à utiliser pour Ajouter un tick au compteur de rapport
    conn = sqlite3.connect("Eleve.db")
    cursor = conn.cursor()

    DicoTrad = {"Bavardages répétés": "Bavardages", "Refuse de changer de place ": "ChangePlace","N'a pas son matériel": "Materiel", "S'esclaffe en cours": "Rigole","Dort en classe": "Dort","Casquette + Pas Bonjour" : "CasquetteBonjour", "Fait des bruits d'animaux": "Animaux", "Devoirs non faits": "DevoirNonFaits","Se retourne vers ses camarades": "Retourne", "Parle fort" : "ParleFort", "Fait rire ses camarades": "FaitRire", "Répond au professeur" : "Repond","Refuse de donner son carnet ": "RefuseCarnet","N'a pas son carnet" : "PasCarnet", "Utilisation abusive d'Internet" : "Internet" }

    #On cherche le nombre de fois où il y a eu ce motif dans la Base de données
    cursor.execute("SELECT {} FROM Eleve WHERE Nom = '{}'".format(DicoTrad[motif],nom))
    for i in cursor:
        n = i[0]

    # On met à jour la base de données avec la nouvelle itération du motif.
    cursor.execute("UPDATE Eleve SET {} = {} WHERE Nom = '{}'".format(DicoTrad[motif],n+1,nom))

    
    
# Commenter en exercice.
def MAJ_Eleve_Presence(nom,classe):
    DicoEleves = LireCSVversDico(classe)
    n = int(DicoEleves[nom]["Présences"])
    DicoEleves[nom]["Présences"] = str(n+1)
    EcrireCsvDeDico(classe,DicoEleves)
    
    


