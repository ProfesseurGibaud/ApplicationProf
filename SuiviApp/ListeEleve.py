from datetime import datetime as date
import csv
from copy import *
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
    bool = False
    for eleve in Liste:
        bool = bool or CompNom(Nom,eleve)
    return bool

def AppelMini(Classe,Liste):
    ListeAbsent = []
    GrosDico = CSV_Vers_DicoClasse()
    DicoClasse = DicoSimple(GrosDico)
    ListeEleveClasse = DicoClasse[Classe]
    for NomEleve in ListeEleveClasse:
        if not NomDansListe(NomEleve,Liste):
            NomAbsent = NomEleve[1].capitalize() + " " + NomEleve[0].capitalize()
            ListeAbsent.append(NomAbsent)
    return ListeAbsent

def AppelGros(Classe,Liste,GrosDico):
    ListeAbsent = []
    DicoClasse = DicoSimple(GrosDico)
    ListeEleveClasse = DicoClasse[Classe]
    for NomEleve in ListeEleveClasse:
        if not NomDansListe(NomEleve,Liste):
            NomAbsent = NomEleve[1].capitalize() + " " + NomEleve[0].capitalize()
            ListeAbsent.append(NomAbsent)
    return ListeAbsent