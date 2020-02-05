import os
if __name__ == '__main__':
    os.chdir("Google Drive//Python//ApplicationProf//SuiviApp")
from datetime import datetime as date
import csv
from copy import *
import matplotlib.pyplot as plt



from ClassesPython import *


def CSV_Vers_DicoClasse():
    # On va charger toutes les listes de toutes les classes.
    Dico = {}
    path = os.getcwd()
    TempListe = []
    os.chdir("Classes")
    for classe in os.listdir():
        nomclasse = classe[:len(classe) - 4]
        TempListe.clear()
        try:
            cr = csv.DictReader(open(classe, "r"))
            for row in cr:
                tempdico = dict(row)
                TempListe.append(list(tempdico.values()))
            Dico[nomclasse] = TempListe
            Dico = deepcopy(Dico)
        except IOError:
            print("Erreur! Csv Vers DicoClasse")
    os.chdir(path)
    return Dico


def DicoSimple(Dico):
    dico = {}
    for classe in Dico:
        dico[classe] = []
        Liste = Dico[classe]
        for eleve in Liste:
            dico[classe].append(eleve[0:2])
    return dico



def ListeMaintenant(ListeDico):
    L = []
    for dicoEleve in ListeDico:
        D = Date()
        D.Update(dicoEleve["Horodateur"])
        if D.Maintenant():
            L.append(Eleve(dicoEleve))
    return L

def ListeMaintenantProg(ListeDico,Str):
    L = []
    for dicoEleve in ListeDico:
        D = Date()
        D.Update(dicoEleve["Horodateur"])
        if D.MaintenantProg(Str):
            L.append(Eleve(dicoEleve))
    return L

def CompMot(Str1,Str2):
    test1 = Str1.upper()
    test2 = Str2.upper()
    if " " in test1:
        n = test1.index(" ")
        test1 = test1[0:n]
    if " " in test2:
        n = test2.index(" ")
        test2 = test2[0:n]
    return test1 == test2

def CompNom(Nom,Eleve): #Attention pas Symétrique
    boolNom = CompMot(Nom[0],Eleve.Nom)
    boolPrenom = CompMot(Nom[1],Eleve.Prenom)
    return boolNom and boolPrenom

def NomDansListe(Nom,Liste):
    ell = 0
    for eleve in Liste:
        if CompNom(Nom,eleve):
            ell = eleve
    return ell

def AppelGros(Classe,Liste,GrosDico):
    ListeAbsent = []
    ListePresent = []
    DicoClasse = DicoSimple(GrosDico)
    ListeEleveClasse = DicoClasse[Classe]
    for NomEleve in ListeEleveClasse:
        ell = NomDansListe(NomEleve,Liste)
        if ell == 0:
            NomAbsent = NomEleve[1].capitalize() + " " + NomEleve[0].capitalize()
            ListeAbsent.append(NomAbsent)
        else:
            ListePresent.append(ell)
    return (ListePresent,ListeAbsent)


def AppelMini(Classe,Liste):
    ListeAbsent = []
    GrosDico = CSV_Vers_DicoClasse()
    (ListePresent,ListeAbsent) = AppelGros(Classe,Liste,GrosDico)
    return (ListePresent,ListeAbsent)

ListeAttribut = ["Nom","Date","Prénom","Classe","Question Prévue", "Question Posée", "Effort Maison Prévue", "Effort Maison Réel", "Investissement Prévu", "Investissement Réel"]

def RecupAttribut(Liste,Attribut):
    LL = []
    a = Attribut
    for eleve in Liste:
        if a == "Nom":
            LL.append(eleve.Nom)
        if a == "Date":
            LL.append(eleve.Date)
        if a == "Prénom":
            LL.append(eleve.Prenom)
        if a == "Classe":
            LL.append(eleve.Classe)
        if a == "Question Prévue":
            LL.append(eleve.QuestionPrevue)
        if a == "Question Posée":
            LL.append(eleve.QuestionPosee)
        if a == "Effort Maison Prévue":
            LL.append(eleve.EffortMaisonPrevu)
        if a == "Effort Maison Réel":
            LL.append(eleve.EffortMaisonReel)
        if a == "Investissement Prévu":
            LL.append(eleve.InvestissementPrevu)
        if a == "Investissement Réel":
            LL.append(eleve.InvestissementReel)
    return LL

def Histogramme(Liste):
    ListeX = list(range(min(Liste)-2,max(Liste)+3))
    ListeY = []
    for i in ListeX:
        ListeY.append(Liste.count(i))
    return (ListeX,ListeY)

def FaireHisto(Liste,NomStr):
    (ListeX,ListeY) = Histogramme(Liste)
    plt.plot(ListeX,ListeY)
    path = ""
    plt.save(path +Str + ".png")

