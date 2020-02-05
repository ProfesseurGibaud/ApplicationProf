from datetime import datetime as date
import csv
from copy import *
from Sheets import *


class Date:
    def __init__(self):
        self.Annee = 0
        self.Mois = 0
        self.Jour = 0
        self.Heure = 0
        self.Minute = 0
    def Maintenant(self):
        D = date.now()
        return (self.Annee == D.year) and (self.Mois == D.month) and (self.Jour == D.day) and (abs(D.hour - self.Heure)<3)
    def Update(self,Str):
        self.Jour = int(Str[0:2])
        self.Mois = int(Str[3:5])
        self.Annee = int(Str[6:10])
        self.Heure = int(Str[11:13])

    def MaintenantProg(self,Str):
        D = Date()
        D.Update(Str)
        return (self.Annee == D.Annee) and (self.Mois == D.Mois) and (self.Jour == D.Jour) and (abs(D.Heure - self.Heure)<3)


class Eleve:
    def __init__(self,dico):
        self.Nom = dico["Nom"].capitalize()
        self.Date = Date()
        self.Date.Update(dico["Horodateur"])
        #print(self.Nom)
        self.Prenom = dico["Prénom"].capitalize()
        self.Classe = dico["Quelle est votre classe ? (S03,1NSI,TSTI2,TS2,TSpéMath)"]   # A changer tous les ans !
        self.DebutFin =  dico['Est ce le début ou la fin de la leçon ?']
        self.dico = dico
        self.QuestionPrevue = 0
        self.QuestionPosee = 0
        self.EffortMaisonPrevu = 0
        self.EffortMaisonReel = 0
        self.InvestissementPrevu = 0
        self.InvestissementReel = 0
        self.Update()

    def Update(self):
        if "Avez vous besoin de poser des questions à M. Gibaud aujourd'hui ?" in self.dico:
            q = self.dico["Avez vous besoin de poser des questions à M. Gibaud aujourd'hui ?"]
            self.QuestionPrevue = 1*(q == 'Oui') + 0*(q == 'Non')
        else:
            q = self.dico["Avez vous posé des questions à M. Gibaud aujourd'hui ?"]
            self.QuestionPosee = 1*(q == "0ui") + 0*(q == "Non")

        if "Notez vos efforts dans VOTRE TRAVAIL À LA MAISON de hier soir." in self.dico:
            self.EffortMaisonReel = self.dico["Notez vos efforts dans VOTRE TRAVAIL À LA MAISON de hier soir."]
        else :
            self.EffortMaisonPrevu = self.dico["À quel point comptez vous vous travailler A LA MAISON ce soir (En Math/NSI) ?"]

        if "À quel point comptez vous vous investir EN CLASSE d'aujourd'hui ?" in self.dico:
            self.InvestissementPrevu = self.dico["À quel point comptez vous vous investir EN CLASSE d'aujourd'hui ?"]
        else:
            self.InvestissementReel = self.dico["Notez vos efforts EN CLASSE aujourd'hui"]