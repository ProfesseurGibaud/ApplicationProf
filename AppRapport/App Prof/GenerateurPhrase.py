import random as rd # On importe un package pour mettre de l'aléa
import os
import sqlite3
from copy import *
def dossier():
    import os
    os.chdir("Google Drive//Python//Application Prof//App Prof")
#dossier()
from FonctionRapport import * # On importe toute les fonctions de FonctionRapport




"""

Ceci ne sont que des indications. Tout l'objectif est que vous trouviez des idées auquelles je n'aurais pas penser

"""

#Il faut aller chercher les info dans le csv (comme dans MAJ_Eleve)
def FichierEleve(classe,nom):
    dico = LireCSVversDico(classe)
    dicoeleve = dico[nom]
    return dicoeleve


def TexteMotif(classe,nom,ListeMotifs):
    conn = sqlite3.connect("Eleve.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ELEVE WHERE Nom = '{}' AND Classe = '{}'".format(nom,classe))
    for eleve in cursor:
        if eleve["Classe"] == classe:
            DicoEleve = dict(eleve)
        else :
            print("Erreur dans TexteMotif")
    #DicoEleve = FichierEleve(classe,nom)
    DicoPh = DicoPhrases()
    Prenom = DicoEleve["Prenom"]
    Nom = DicoEleve["Nom"]
    Sexe = (DicoEleve["Sexe"]=="F")*"elle" + (DicoEleve["Sexe"]=="H")*"il"
    Conj = deepcopy(ConjCoord)
    String = ""
    for i in range(0,len(ListeMotifs)):
        u = rd.randint(0,2)
        if i == 0:
            #Manque traduction entre les motifs affichés et ceux de la base de données : Faire un dico de correspondance
            add = DicoPh[ListeMotifs[i]][u].format(Prenom,Sexe)
            add = add.capitalize()
        else :
            add = DicoPh[ListeMotifs[i]][u]
            add0 = add[0].lower()
            add = add0 + add[1:]
            add = add.format(Prenom,Sexe)
        String = String + add
        if i < len(ListeMotifs) -2:
            v = rd.randint(0,len(Conj)-1)
            String = String + Conj.pop(v)
    return String

        



def DicoPhrases():
    dico = {} # on va assigner à chaque motif, trois phrases 
    dico["Bavardages répétés"] = ["{} ne cesse de bavarder avec ses camarades.", "{} bavarde et perturbe le cours.", "Malgrès plusieurs rappels {} ne cesse de bavarder et perturbe l'ensemble de la classe."] # Que des prénoms
    dico["Refuse de changer de place "] = ["{} refuse de changer de place.", "Malgrès plusieurs demandes, {} ne change pas de place.", "{} empèche ses camarades de se concentrer et refuse de changer de place."] #Que des prénom
    dico["N'a pas son matériel"] = ["{} n'a pas son matériel pour le cours de mathématiques.", "À plusieurs reprises, {} a oublié son matériel.", "{} n'a pas son matériel pour travailler correctement."] #Que des prénom
    dico["S'esclaffe en cours"] = ["{} ne cesse de rigoler et perturbe ses camarades.","Au lieu de travailler, {} ne cesse de rigoler.", "{} s'esclaffe en cours."] # Que des prénom
    dico["Dort en classe"] = ["{} ne suit pas le cours et s'endort en classe.", "Au lieu d'écouter et de participer {} s'endort en classe.", "{} ne suit pas le cours."] #Que des prénom
    dico["Casquette + Pas Bonjour"] = ["Le comportement de {} est inapproprié : Port de Casquette et Ne dit pas Bonjour.", "{} est impoli, {} refuse de retirer sa casquette et de dire bonjour.", "{} refuse d'enlever sa casquette et manque de politesse."] #Après la virgule {sexe}
    dico["Fait des bruits d'animaux"] = ["{} fait des bruits d'animaux en classe.","{} fait des bruits d'animaux en classe.","{} fait des bruits d'animaux en classe."]
    dico["Devoirs non faits"] = ["{} n'a pas fait ses devoirs.", "Pour la n-ième fois {} n'a pas fait ses devoirs.", "Le travail à la maison n'a pas été réalisé."]
    dico["Se retourne vers ses camarades"] = ["{} ne cesse de se retourner vers ses camarades.", "{} ne tient pas sur sa chaise et ne cesse de se retourner.", "{} ne cesse de se retourner et perturbe ses camarades."]
    dico["Parle fort"] = ["{} parle fort et perturbe le cours.", "L'attitude de {} n'est pas acceptable : {} parle fort et perturbe la classe.", "{} s'exclamme en cours de mathématiques et perturbe le cours."]  #Après les : {sexe}
    dico["Fait rire ses camarades"] = ["{} s'amuse à faire rire ses camarades et perturbe le cours.", "{} passe plus de temps à amuser ses camarades qu'à travailler.", "Le cours n'est pas un lieu pour faire rire ses camarades comme le pense {}." ]
    dico["Répond au professeur"] = ["{} est insolent et répond au professeur.", "L'attitude de {} est inacceptable, {} est insolent et ne cesse de répondre au professeur.", "{} n'accepte pas les remarques et répond au professeur."] #Après la virgule {sexe}
    dico["Refuse de donner son carnet "] = ["{} refuse de donner son carnet.", "Après réprimande, {} refuse de donner son carnet au professeur.", "{} perturbe la classe et refuse de donner son carnet au professeur."]
    dico["N'a pas son carnet"] = ["{} vient en cours sans son carnet."," {} n'a pas son carnet.", "{} est venu en cours sans avoir son carnet."]
    dico["Utilisation abusive d'Internet"] = ["{} va sur des sites qui n'ont rien à voir avec le cours.","{} n'a pas respecté les conditions d'utilisation d'internet en classe.","{} va sur des sites qui n'ont rien à voir avec le cours."]
    return dico




ConjCoord = [" De plus ", " Egalement ", " En outre ", " Par ailleurs ", " Aussi ", " D'autre part "," Par dessus le marché, ", " De surcroit "]