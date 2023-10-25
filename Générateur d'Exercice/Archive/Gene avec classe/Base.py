path = "Google Drive//Python//Générateur d'Exercice//Gene avec classe"

import os
import sympy as sp
import numpy as np 

from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy.solvers.inequalities import solve_rational_inequalities
from sympy import solveset,S,Interval
from sympy import together
from sympy.abc import x,y
from sympy import linsolve
from sympy import Function, Symbol
from sympy import functions
from sympy.functions.elementary import *
from sympy.simplify.simplify import *
from sympy import fraction, Rational, Symbol


os.chdir(path)
import random as rd
from CaractereSpeciaux import *
from FonctionParenthese import *
path = os.getcwd()




def DicoVideFalse(dico):
    return sum(dico.values())!=0





TType = ["D\\'eveloppement", "In\\'equation", "Equation", "Tableaux de Variation", "Fraction"," Equation de Droite du Plan","Proba"]
DDifficulte = ["1", "2", "3"]
CClasse = ["Seconde","Premiere","Terminale"]


Titre = 0
Date = 0


# On stoque les exercices dans un dictionnaire DicoExo, les clés de Dico sont les Types et les valeurs sont un autre dictionnaire dont les clés seront les difficultés et les valeurs le nombres d'exo que l'on veut.
DicoExo = {}
for ttype in TType:
    DicoExo[ttype] = {"1":0,"2":0,"3":0}


"""
Classe Exercices
"""

class Exercice:
    def __init__(self):
        self.expr = 0
        self.enonce = ""
        self.corr = 0
        self.correction = ""
        self.niveau = "1"
        self.numero = 1
        self.classe = "Seconde"
        self.type = "Développement"
        self.derive = ""
        self.StrExpr = ""
    def EcrireExo(self,Exo):
        Exo.write(self.enonce)
    def EcrireCorrection(self,Corr):
        Exo.write(self.correction)
    def VersLatex(self):
        if self.type == "TabVar" or self.type == "Fraction" or self.type == "Droite":
            pass
        else:
            self.enonce = sp.latex(self.expr)
            self.correction = sp.latex(self.corr)
            

        
class ExoDeveloppement(Exercice):
    def __init__(self):
        super().__init__()
    def FaireEnonce(self):
        if self.niveau == "1":
            self.expr = AxPb() * AxPbCarre() + sgnnbre() * AxPb() * AxPbCarre()
            self.enonce = sp.latex(self.expr)
        if self.niveau == "2":
            self.expr = self.expr = AxPbCarre() * AxPbCarre() + sgnnbre()  * AxPbCarre() * AxPbCarre()
        if self.niveau == "3":
            self.expr = 1
            for k in range(3, 6):
                self.expr = self.expr * AxPbCarreDur()
                self.expr = self.expr + sgnnbre() * rd.randint(2, 10) * AxPb()
            self.expr = self.expr * AxPbCarreDur()
    def FaireCorrection(self):
        self.corr = self.expr.expand()

class ExoInequation(Exercice):
    def __init__(self):
        super().__init__()
        self.res = 0
    def FaireEnonce(self):
        u = rd.randint(0, 1)
        v = rd.randint(0, 1)
        a = rd.randint(1, 9)
        b = rd.randint(1, 9)
        c = racinepib()
        d = racinepib()
        A = AxPb()
        B = AxPb()
        C = AxPb()
        D = AxPb()
        I = IdRemarq()
        J = IdRemarq()
        AA = AxPbCarreSeul()
        BB = AxPbCarreSeul()
        if self.classe == "Seconde":
            if self.niveau == "1":
                if v == 0:
                    self.expr = A >=B
                    self.res = A - B
                if v == 1:
                    self.expr = A <=B
                    self.res = B-A
            if self.niveau == "2":
                if v == 0:
                    self.expr = A/B >= c/d
                    self.res = A/B - c/d
                if v == 1:
                    self.expr = A/B <= c/d
                    self.res = -A/B + c/d
            if self.niveau == "3":
                if u == 0:
                    self.expr = I / A >= J / A
                    self.res = I / A - J / A
                if u == 1:
                    self.expr = I / A <= J / A
                    self.res = J / A - I / A
        else :
            if self.niveau == "1":
                if v == 0:
                    self.expr = AA >= BB
                    self.res = AA - BB
                if v == 1:
                    self.expr = AA <= BB
                    self.res = BB -  AA
            if self.niveau == "2":
                if v == 0:
                    self.expr = A/B >= c/d
                    self.res = A/B - c/d
                if v == 1:
                    self.expr = A/B <= c/d
                    self.res = -A/B + c/d
            if self.niveau == "3":
                if v == 0:
                    if u == 0:
                        self.expr = A / B >= C / D
                        self.res = A / B - C / D
                    if u == 1:
                        self.expr = A / B <= C / D
                        self.res = C / D - A / B
                if v == 1:
                    if u == 0:
                        self.expr = I / A >= J / A
                        self.res = I / A - J / A
                    if u == 1:
                        self.expr = I / A <= J / A
                        self.res = J / A - I / A

    def FaireCorrection(self):
        self.corr = solveset(self.res >= 0, domain=S.Reals)

class ExoEquation(Exercice):
    def __init__(self):
        super().__init__()
        self.res = 0
    def FaireEnonce(self):
        if self.niveau == "1":
            u=rd.randint(0,1)
            if u==0:
                A = AxPb()
                B = AxPb()
                self.expr = A - B
            if u==1:
                n = rd.randint(2,4)
                self.expr = AxPbDur()
                for i in range(0,n):
                    self.expr = self.expr * AxPbDur()
        if self.niveau == "2":
            A = IdRemarq()
            b = rd.randint(1,9)
            self.expr = A -b
        
        if self.niveau == "3":
            u = rd.randint(0,1)
            v = rd.randint(0,1)
            if u==0:
                A = IdRemarq()
                B = racinepib()
            if u==1:
                A = IdRemarq()
                B = IdRemarq()
            if self.classe == "Terminale":
                AA = AxPb()
                BB = AxPb()
                if u == 0:
                    if v == 0:
                        A = sp.exp(AA)
                        B = sp.exp(BB)
                    if v == 1:
                        A = exp(AA)
                        B = rd.randint(-5,20)
                if u==1:
                    if v==0:
                        A = sp.log(AA)
                        B = sp.log(BB)
                    if v==1:
                        A = sp.log(AA)
                        B = rd.randint(-5,20)
                self.expr = A - B 
    
    def FaireCorrection(self):
        self.corr = solveset(self.expr == 0, domain=S.Reals)



class ExoFraction(Exercice):
    def __init__(self):
        super().__init__()
        self.res = 0
    def FaireEnonceEtCorrection(self):
        if self.niveau == "1":
            [self.enonce,self.corr] = StrExoFraction(self.classe)
        if self.niveau == "2":
            [self.enonce,self.corr] = StrExoFractionMoyen(self.classe)
        if self.niveau =="3":
            [self.enonce,self.corr] = StrExoFractionDur(self.classe)


class ExoDroite(Exercice):
    def __init__(self):
        super().__init__()
    def FaireEnonceEtCorrection(self):
        if self.niveau == "1":
            [self.enonce,self.corr] = StrEqDroiteFacile(self.classe)
        if self.niveau == "2":
            [self.enonce,self.corr] = StrEqDroiteMoyenne(self.classe)
        if self.niveau =="3":
            [self.enonce,self.corr] = StrEqDroiteDure(self.classe)

class ExoProba(Exercice):
    def __init__(self):
        super().__init__()
    def FaireEnonceEtCorrection(self):
        [self.enonce,self.correction] = StrProba(self.classe)


class ExoTabVar(Exercice):
    def __init__(self):
        super().__init__()
        self.der = 0
        self.res = 0
        self.CheckDomaine = 0
        self.Df = S.Reals

    def FaireEnonce(self):  
        if self.niveau == "1":
            u = rd.randint(0, 2)
            if self.classe == "Seconde":
                v = rd.randint(0, 2)
                if v == 0:
                    self.expr = IdRemarq()
                if v == 1:
                    self.expr = racinepib() * AxPb()
                if v == 2:
                    A = IdRemarq()
                    self.CheckDomaine = A
                    self.expr = sp.sqrt(A)
            else:
                if u == 0:
                    self.expr = AxPbCarreDur() + sgnnbre() + AxPb()
                if u == 1:
                    self.expr = AxPbCarre() * AxPb()
                if u == 2:
                    self.expr = AxPbCubeDur()
        if self.niveau == "2":
            u = rd.randint(0,4)
            if self.classe != "Terminale":
                u = rd.randint(0,1)
            if u == 0:
                A = AxPb()
                self.CheckDomaine = A
                self.expr = AxPb() * sp.sqrt(A)
            if u == 2:
                A = AxPb()
                self.CheckDomaine = A
                self.expr = sp.log(A)/A
            if u == 3:
                self.expr = exp(AxPbCube())
            if u == 1:
                self.expr = AxPbDur() / AxPbDur()
            if u ==4:
                A = AxPbDur()
                self.CheckDomaine = A
                self.expr = sp.log(A) + sp.expand((AxPbDur())**3)
        if self.niveau == "3":
            u = rd.randint(0,3)
            if self.classe!= "Terminale":
                u = rd.randint(0,1)
            if u == 0:
                A = AxPbCarre()
                self.CheckDomaine = A
                self.expr= racinepib()*sp.sqrt(A)*AxPbDur()
            if u == 1:
                A = AxPbDur()
                B = AxPbCarreDur()
                self.CheckDomaine = B
                self.expr = racinepib()*sp.sqrt(A)/B
            if u == 2:
                self.expr = racinepib()*sp.exp(AxPbCarreDur()) * AxPbDur()
            if u == 3:
                A = AxPbCarreDur()/AxPb()
                self.CheckDomaine = A
                self.expr = racinepib()*sp.log(A)
                
            if self.classe == "Seconde":
                A = AxPbDur()
                self.CheckDomaine = A
                self.expr = self.expr = racinepib()* AxPbDur() * sp.sqrt(A)

        
    def FaireCorrection(self):
        self.der = sp.together(sp.expand(sp.together(sp.diff(self.expr, x))))
        self.Df = solveset(self.CheckDomaine >= 0, domain=S.Reals)
        [a, b] = fraction(self.der)
        self.res = solveset(a >= 0, domain=self.Df) # Ajouter Inter Df
        

    def VersLatexVar(self):
        self.enonce = "f(x) = " + sp.latex(self.expr)
        self.correction = "\\[ f'(x) = " +  sp.latex(self.der) + "\\]" + "\\[" + sp.latex(self.res) + "\\]"





















def DevoirComplet(Liste,Titre,Auteur,Date,Classe):
    [o,Exo,Correction] = Preambule(Titre,Auteur,Date,Classe)
    for type in TType:
        [Exo,Correction] = ListeType(o,type,Liste,Classe)
    [o,Exo,Correction] = Ouverture(o)
    Exo.close()
    Correction.close()
    return [Exo,Correction]


def Preambule(Titre,Auteur,Date,Classe):
    o=0
    # On change le répertoire de Travail : Mettre son répertoire de Travail : à la place du \ mettre //
    os.chdir(path) 
    [o,Exo,Correction] = Ouverture(o)
    PreIncomp(Exo)
    PreTitre(Titre,Auteur,Exo)
    PreDate(Date,Exo)
    Exo.write("\\begin{document}")
    Exo.write("\n \\maketitle")
    Exo.close()
    Correction.close()
    return[o,Exo,Correction]
    
    
def PdfLatex(ZeroOuUn):
    Exo = open("Exo.txt","a")
    if ZeroOuUn == 0:
        print("Pas de Correction")
    elif ZeroOuUn ==1:
        Corr = open("Correction.txt","r")
        text = Corr.read()
        Exo.write(text)
        Corr.close()
    else:
        print("Que fait on ?")
    Exo.write("\n \\end{document}")
    Exo.close()
    os.system("pdflatex Exo.txt")
    os.remove("Exo.txt")
    if ZeroOuUn == 1:
        os.remove("Correction.txt")
    os.remove("Exo.log")
    os.remove("Exo.aux")


def ListeType(o,type,Liste,Classe):
    [o,Exo,Correction]=Ouverture(o)
    for difficulte in DDifficulte:
        [j,k] = TypeDifficulte(type,difficulte,Classe)
        print (type + " " + difficulte)
        if Liste[k]>0:
            WriteSection(type,difficulte,Exo,Correction)
            for l in range(Liste[k]):
                print(l)
                WriteExo(type,difficulte,Classe,l,Exo,Correction)
    Exo.close()
    Correction.close()
    return [Exo,Correction]
    
    

def ListeType(o,type,DicoExo,Classe):
    [o,Exo,Correction]=Ouverture(o)
    for ttype in DicoExo:
        if DicoVideFalse(DicoExo[ttype]):
            for difficulte in DicoExo[ttype]:
                if DicoExo[ttype][difficulte]>0:
                    WriteSection(type,difficulte,Exo,Correction)
                    for l in range(DicoExo[ttype][difficulte]):
                #J'en suis ici
                
            
            
    

 
"""
Ecriture Pr\\'eambule
"""


def PreIncomp(Exo):
    Exo.write("\\documentclass[a4paper,oneside,11pt]{article} \n")
    Exo.write("\\usepackage[utf8]{inputenc} \n \\usepackage[T1]{fontenc} \n \\usepackage{textcomp} \n  \\usepackage[french]{babel} \n \\usepackage[autolanguage]{numprint} \n \\usepackage{amsmath,amssymb,amsthm} \n")
    
def PreTitre(Titre,Auteur,Exo):
    if len(str(Titre))< 10:
        title = "Devoir d'Entrainement"
    else:
        title = str(Titre)
    if len(str(Auteur))<3:
        author = "S.Gibaud"
    else:
        author = str(Auteur)
    Exo.write("\\title{"+title+"} \n")
    Exo.write("\n \\author{" + author + "}")
    
def PreDate(Date,Exo):
    if len(str(Date))<3:
        date = "\n \\date{\\`A rendre ou pas :) }"
    else:
        date = "\n \\date{\\`A rendre avant le " + str(Date) +"}" +"\n"
    Exo.write(date)



"""
Ouverture Fichier
"""


def Ouverture(o):
    if o == 0:
        Exo = open("Exo.txt","x")
        Correction = open("Correction.txt","x")
        o=1
    else:
        Exo = open("Exo.txt","a")
        Correction = open("Correction.txt","a")
    return [o,Exo,Correction]




"""
Input
"""
def Utilisateur():
    Compl = InputOuiNon("Voules vous choisir les exercices ?")
    #lieu = InputLieu()
    [titre,auteur] = InputTitreAuteur()
    date = InputDate()
    Classe = InputClasse()
    nFac = input("Combien d'exercices faciles voulez vous ?")
    nFac = int(nFac)
    nMoy = input("Combien d'exercices moyens voulez vous ?")
    nMoy = int(nMoy)
    nDur = input("Combien d'exercices difficiles voulez vous ?")
    nDur = int(nDur)
    Liste = [nFac,nMoy,nDur]
    if Compl == 0:
        DevoirComplet([nFac,nMoy,nDur],titre,auteur,date,Classe)
    else:
        [o,Exo,Corr] = Preambule(titre,auteur,date,Classe)
        if InputOuiNon("Voulez vous des Développements ?")==1:
            ListeType(o,TType[0],Liste,Classe)
        if InputOuiNon("Voulez vous des Inéquations ?")==1:
            ListeType(o,TType[1],Liste,Classe)
        if InputOuiNon("Voulez vous des Equations ?")==1:
            ListeType(o,TType[2],Liste,Classe)
        if InputOuiNon("Voulez vous des Tableaux de Variations ?")==1:
            ListeType(o,TType[3],Liste,Classe)
        if InputOuiNon("Voulez vous des Fractions ?")==1:
            ListeType(o,TType[4],Liste,Classe)
        if InputOuiNon("Voulez vous des équations de Droites ?") == 1:
            ListeType(o,TType[5],Liste,Classe)
        if InputOuiNon("Voulez vous des exercices de Probabilités ?") == 1:
            ListeType(o,TType[6],Liste,Classe)
        
    i=InputOuiNon("Voulez vous les corrections avec l'énoncé ?")
    PdfLatex(i)
    os.rename("Exo.pdf",titre + ".pdf")
    RetourHome()

    
def RetourHome():
    os.chdir("..")        
    os.chdir("..")
    os.chdir("..")
    text = os.system("dir")
    print("text")
    
def InputOuiNon(text):
    Comp = input(text +" (Oui ou Non) \n")
    if Comp =="Oui" or Comp=="oui" or Comp == "o" or Comp == "y" or Comp == "Yes":
        Complett =1
    elif Comp =="Non" or Comp =="non" or Comp =="n" or Comp =="No":
        Complett =0
    else:
        print("Vous n'avez pas rentré Oui ou Non")
        Complett = InputOuiNon()
    return Complett

def InputTitreAuteur():
    Titre = input("Quel est le titre des exercices ? \n")
    if len(str(Titre))< 10:
        title = "Devoir d'Entrainement"
    else:
        title = str(Titre)
    Auteur = input("Quel est l'auteur des exercices ? \n")
    if len(str(Auteur))<3:
        author = "S.Gibaud"
    else:
        author = str(Auteur)
    return [title,author]
    
def InputClasse():
    classe = input("Pour quelle classe est le controle (2,1,Term) \n")
    if classe == "seconde" or classe == "Seconde" or classe == 2 or classe ==str(2):
        Classe = "Seconde"
    elif classe =="première" or classe =="Première" or classe =="premiere" or classe == "Premiere" or classe =="1" or classe == 1:
        Classe = "Premiere"
    elif classe == "Term" or classe == "Terminale" or classe == "term" or classe == "terminale" or classe == "TES" or classe == "tes" or classe == "TS" or classe == "ts":
        Classe = "Terminale"
    else:
        print("Vous n'avez pas rentré de classe")
        Classe = InputClasse()
    return Classe

def InputDate(): 
    Date = input("Quand souhaitez vous récupérez le controle ? \n")
    if len(str(Date))<=1:
        date = "\n \\date{\\`A rendre ou pas :) }"
    else:
        date = "\n \\date{\\`A rendre avant le " + str(Date) +"}" +"\n"
    return date
    

"""
******************************************
Fonction d'\\'ecriture
******************************************
"""    


def WriteSection(type,difficulte,Exo,Correction):
    TitreSection = "\n \section{Exercices de " + type + " " + difficulte + "s" + "}"
    Exo.write(TitreSection + "\n")
    Exo.write(Consigne(type,difficulte) + "\n")
    Correction.write(TitreSection + "\n")
    Correction.write("\n Corrig\\'e " + type + " " + difficulte + "\n")
    if type == "Tableaux de Variation":
        Correction.write("\n Dans la suite, vous verrez la d\\'eriv\\'ee puis le domaine o\`u la d\\'eriv\\'ee est positive \n")
    if type == TType[5]:
        Correction.write("\n Dans la suite, vous verrez la/les \'equations de droites puis leur intersection")
    
    
def WriteExo(type,difficulte,Classe,l,Exo,Correction):
    [exxo,corrr,der]= ExoEtCorr(type,difficulte,Classe)
    Exo.write(type + " num\\'ero " + "{0}".format(l))
    Exo.write(" \\[" +  exxo +  "\\]")
    if type == "Tableaux de Variation":
                Correction.write( "\n Fonction {0}".format(l))
                Correction.write("\\["+ exxo +"\]")
                Correction.write("\n \\[f'(x) = " + der + "\]")
                Correction.write("\n \\[" + corrr + "\]")
    elif type == TType[5]: #Eq de Droite
        Correction.write("\n Correction " + type + " num\\'ero " + "{0}".format(l))
        Correction.write("\n \\[" + corrr + "\]")
        if difficulte == "Dur":
            Correction.write("\n L'intersection est \\[" + der + "\]")
    else:            
        Correction.write("\n Correction " + type + " num\\'ero " + "{0}".format(l) + "\\[")
        Correction.write(corrr)
        Correction.write("\n \\]")

def Consigne(type,difficulte):
    if type == "D\\'eveloppement":
        text = "\n D\\'evelopper les expressions suivantes : "
    if type == "Equation":
        text =  "\n R\\'esoudre les \\'equation suivantes : "
    if type == "In\\'equation":
        text = "\n R\\'esoudre les in\\'equations suivantes : "
    if type == "Tableaux de Variation":
        text = "\n Donner les variations des fonctions suivantes : "
    if type == "Fraction":
        text = "\n Simplifier les fractions suivantes (il faudra peut \\^etre mettre sous le m\\^eme d\\'enominateur) :"
    if type == TType[5] and difficulte == "Facile":#Equation de Droite
        text = "\n Donner l'\'equation de :"
    if type == TType[5] and difficulte == "Moyen":#Equation de Droite
        text = "\n Donner les \'equations de :"
    if type == TType[5] and difficulte == "Dur":#Equation de Droite
        text = "\n Donner les \'equations des droites suivantes ainsi que leur intersection :"
    if type == TType[6]: 
        text = "Faire les exos suivants"
        text = text + "\\\\ \n"
    return text



def TypeDifficulte(type,difficulte,Classe): # Petite fonction quasi inutile juste pour suivre plus facilement les type est les difficultes.
    for k in range(len(DDifficulte)):
        if difficulte == DDifficulte[k]:
            SSS = k
    for l in range(len(TType)):
        if type == TType[l]:
            TTT = l
    for m in range(len(CClasse)):
        if Classe == CClasse[m]:
            UUU = m
    return [TTT,SSS]
    

    



def ExoEtCorr(type,difficulte,Classe):
    der = "" # Pour les tableaux de variation j'ai besoin de la d\\'eriv\\'ee donc je suis oblig\\'e de la rajouter partout
    if TypeDifficulte(type,difficulte,Classe) == [0,0]:
        [exo,corr] = StrDevSimple(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [0,1]:
        [exo,corr] = StrDevMoyen(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [0,2]:
        [exo,corr] = StrDevMoyen(Classe) #Modifier le prog développement Dur
    if TypeDifficulte(type,difficulte,Classe) == [1,0]:
        [exo,corr] = StrIneSimple(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [1,1]:
        [exo,corr] = StrIneMoyen(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [1,2]:
        [exo,corr] = StrIneDur(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [2,0]:
        [exo,corr] = StrEqSimple(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [2,1]:
        [exo,corr] = StrEqMoyenne(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [2,2]:
        [exo,corr] = StrEqDure(Classe)    
    if TypeDifficulte(type,difficulte,Classe) == [3,0]:
        [exo,corr,der] = StrTabVarSimple(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [3,1]:
        [exo,corr,der] = StrTabVarMoyen(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [3,2]:
        [exo,corr,der] = StrTabVarDur(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [4,0]:
        [exo,corr] = StrExoFraction(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [4,1]:
        [exo,corr] = StrExoFractionMoyen(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [4,2]:
        [exo,corr] = StrExoFractionDur(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [5,0]:
        [exo,corr] = StrEqDroiteFacile(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [5,1]:
        [exo,corr] = StrEqDroiteMoyenne(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [5,2]:
        [exo,corr,der] = StrEqDroiteDure(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [6,0]:
        [exo,corr] = StrProba(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [6,1]:
        [exo,corr] = StrProba(Classe)
    if TypeDifficulte(type,difficulte,Classe) == [6,2]:
        [exo,corr] = StrProba(Classe)
    
    return [exo,corr,der]
    




















"""
**********************************************************************
**********************************************************************
**********************************************************************
ARCHIVE (Ne pas jeter (des fonctions appellent l'archive))
ARCHIVE (Ne pas jeter (des fonctions appellent l'archive))
ARCHIVE (Ne pas jeter (des fonctions appellent l'archive))
**********************************************************************
**********************************************************************
**********************************************************************
"""















"""
****************************************************************************
Fonction d'Exercices
****************************************************************************
"""
    

def StrDevSimple(classe):
    expr = AxPb() * AxPbCarre() + sgnnbre()*AxPb() * AxPbCarre()
    return [sp.latex(expr) + "\\\\",sp.latex(expr.expand())]

def StrDevMoyen(classe):
    expr = AxPbCarre() * AxPbCarre() + sgnnbre()  * AxPbCarre() * AxPbCarre()
    return [sp.latex(expr) + "\\\\",sp.latex(expr.expand())]
    
def StrDevDur(classe):
    S=1
    for k in range(3,6):
        S = S  *  AxPbCarreDur()
        S = S  + sgnnbre() * rd.randint(2,10)*AxPb()
    S = S * AxPbCarreDur()
    return [sp.latex(S) + "\\\\",sp.latex(S.expand())]

def StrIneSimple(classe):
    u=rd.randint(0,1)
    v=rd.randint(0,1)
    A = AxPb()
    B = AxPb()
    AA = AxPbCarreSeul()
    BB = AxPbCarreSeul()
    if classe == "Seconde":
        u = 0
    if u==0:
        if v==0:
            expr = A >= B
            res = A - B
        if v==1:
            expr = A <= B
            res = B - A
    if u==1:
        if v==0:
            expr = AA >= BB
            res = AA - BB
        if v==1:
            expr = AA <= BB
            res = BB - AA
    
    resultat = solveset(res>=0, domain = S.Reals)
    return [sp.latex(expr) + "\\\\",sp.latex(resultat)]

def StrIneMoyen(classe):
    a = rd.randint(1,9)
    b = rd.randint(1,9)
    u=rd.randint(0,1)
    v=rd.randint(0,1)
    A = AxPb()
    B = AxPb()
    c = racinepib()
    d = racinepib()
    if v==0:
        expr = A/B >= c/d
        res = A/B - c/d
    if v==1:
        expr = A/B <= c/d
        res = -A/B + c/d
    exprcorrige = solveset(res>=0, domain = S.Reals)
    return [sp.latex(expr) + "\\\\", sp.latex(exprcorrige)]

def StrIneDur(classe):
    u=rd.randint(0,1)
    v=rd.randint(0,1)
    A = AxPb()
    B = AxPb()
    C = AxPb()
    D = AxPb()
    I = IdRemarq()
    J = IdRemarq()
    if classe == "Seconde":
        if u==0:
            expr = I/A >= J/A
            res = I/A - J/A
        if u == 1:
            expr = I/A <= J/A
            res = J/A - I/A
    else:
        if v==0:
            if u==0:
                expr = A/B >= C/D
                res = A/B - C/D
            if u==1:
                expr = A/B <= C/D
                res = C/D - A/B
        if v==1:
            if u==0:
                expr = I/A >= J/A
                res = I/A - J/A
            if u == 1:
                expr = I/A <= J/A
                res = J/A - I/A
    exprcorrige = solveset(res>=0, domain = S.Reals)
    return [sp.latex(expr) + "\\\\", sp.latex(exprcorrige)]



def StrTabVarSimple(classe):
    u=rd.randint(0,2)
    if classe == "Seconde":
        u = -1 
        v= rd.randint(0,2)
    if u == -1:
        if v == 0:
            A = IdRemarq()
            S1 = StrFexpr(A)
            expr = A
        if v == 1:
            A = racinepib()*AxPb()
            S1 = StrFexpr(A)
            expr = A
        if v == 2 :
            A = IdRemarq()
            expr = sp.sqrt(A)
            S1 = StrFexpr(expr)
            deriv = sp.diff(expr,x)
            [a,b] = fraction(deriv)
            resultat = solveset(a>=0,domain = S.Reals)
    if u==0:
        expr = AxPbCarreDur() + sgnnbre() + AxPb()
        S1 =  StrFexpr(expr)
    if u==1:
        expr = AxPb() * AxPb()
        S1 =  StrFexpr(expr)
    if u==2:
        expr = AxPbCubeDur()
        S1 = StrFexpr(expr)
    if (u != -1 or v != 2):
        deriv = sp.diff(expr,x)
        resultat = solveset(deriv>=0, domain = S.Reals)
    return [S1,sp.latex(resultat),sp.latex(deriv)]
    

def StrTabVarMoyen(classe):
    u=rd.randint(0,2)
    if u==2:
        expr = AxPbCubeDur()+ sgnnbre()*AxPbCarreDur()
        if classe == "Seconde":
            a = rd.randint(1,9)
            b = rd.randint(1,8)
            expr = (a*x + b)**3
        S1 = StrFexpr(expr)
    if u==0:
        expr = AxPb()*AxPb()
        S1 = StrFexpr(expr)
    if u==1:
        expr = AxPb()/AxPb()
        S1 = StrFexpr(expr)
    deriv = sp.diff(expr,x)
    resultat = solveset(deriv>=0, domain = S.Reals)
    return [S1, sp.latex(resultat),sp.latex(deriv)]


def StrTabVarDur(classe):
    u=rd.randint(0,2)
    if classe == "Seconde":
        u=0
    if classe == "Terminale":
        u = rd.randint(3,4)
        v = rd.randint(0,2)
    if u==0:
        expr = racine()*AxPbCubeDur()
        if classe == "Seconde":
            a = rd.randint(1,9)*racinepib()
            b = rd.randint(1,8)*racinepib()
            expr = (a*x + b)**3
        S1 = StrFexpr(expr)
    if u==1:
        expr = AxPb()*racine()*AxPbCarreDur()
        S1 = StrFexpr(expr)
    if u==2:
        expr = AxPbCarreDur()/AxPb()
        S1 = StrFexpr(expr)
    if u==3: #Exponentielle
        if v== 0:
            expr = sp.exp(AxPbCarre()/AxPb())
            [S1,deriv,resultat] = AnalyseExpo(expr)
        if v == 1:
            expr = sp.exp(AxPb()*racinepib()*AxPbCarreDur())
            [S1,deriv,resultat]= AnalyseExpo(expr)
        if v==2:
            expr = AxPb()*sp.exp(AxPb())
            [S1,deriv,resultat] = AnalyseExpo(expr)
    if u == 4: #Logarithme
        if v==0:
            A = AxPbCarre()/AxPb()
            Df = sp.solveset(A>0, domain = S.Reals)
            expr = sp.ln(A)
            [S1,deriv,resultat] = AnalyseLog(expr,Df)
        if v == 1:
            A =AxPb()
            expr  = AxPbCube() + sp.ln(A)
            Df = sp.solveset(A>0, domain = S.Reals)
            [S1,deriv,resultat] = AnalyseLog(expr,Df)
        if v ==2 :
            A = AxPb()
            expr = sp.ln(A)/A
            Df = sp.solveset(A>0, domain = S.Reals)
            [S1,deriv,resultat] = AnalyseLog(expr,Df)
    if classe != "Terminale":
        deriv = sp.diff(expr,x)
        resultat = solveset(deriv>=0, domain = S.Reals)
    return [S1, sp.latex(resultat),sp.latex(deriv)]    
      

    
    
def StrEqSimple(classe):
    u=rd.randint(0,1)
    if u==0:
        A = AxPb()
        B = AxPb()
        expr = A - B
        pprint = sp.latex(A) + "=" + sp.latex(B)
    if u==1:
        n = rd.randint(2,4)
        expr = AxPbDur()
        for i in range(0,n):
            expr = expr * AxPbDur()
        pprint = sp.latex(expr) + "= 0"
    Sol = solveset(expr,domain = S.Reals)
    return [pprint + "\\\\",sp.latex(Sol)]

def StrEqMoyenne(classe):
    A = IdRemarq()
    b = rd.randint(1,9)
    expr = A -b
    Sol = solveset(expr,domain = S.Reals)
    return [sp.latex(A) + "= 0" + "\\\\",sp.latex(Sol)]
   
    
def StrEqDure(classe):
    u = rd.randint(0,1)
    v = rd.randint(0,1)
    if u==0:
        A = IdRemarq()
        B = racinepib()
    if u==1:
        A = IdRemarq()
        B = IdRemarq()
    if classe == "Terminale":
        AA = AxPb()
        BB = AxPb()
        if u == 0:
            if v == 0:
                A = sp.exp(AA)
                B = sp.exp(BB)
            if v == 1:
                A = exp(AA)
                B = rd.randint(-5,20)
        if u==1:
            if v==0:
                A = sp.log(AA)
                B = sp.log(BB)
            if v==1:
                A = sp.log(AA)
                B = rd.randint(-5,20)
    expr = A - B 
    Sol = solveset(expr,domain = S.Reals)
    return [sp.latex(A) +"=" + sp.latex(B), sp.latex(Sol)]
    

def StrExoFraction(classe):
    a = rd.randint(1,100)
    b = rd.randint(1,100)
    return ["\\frac{"+"{0}".format(a)+"}"+"{"+"{0}".format(b)+"}",sp.latex(Rational(a,b))]
    
def StrExoFractionMoyen(classe):
    a = rd.randint(1,50)
    b = rd.randint(1,50)
    c = rd.randint(1,50)
    d = rd.randint(1,50)
    e = rd.randint(1,50)
    f = rd.randint(1,50)
    u = rd.randint(0,5)
    v= rd.randint(0,1)
    u=1
    if u==0:
        if v==0:
            S1 = "\\frac{"+"{0}".format(a)+"}"+"{"+"{0}".format(b)+"}" + " + " + "\\frac{"+"{0}".format(c)+"}"+"{"+"{0}".format(d)+"}"
            res = Rational(a,b)+Rational(c,d)
        if v==1:
            S1 = "\\frac{"+"{0}".format(a)+"}" + "{" +"{0}".format(b)+"}" + " - " + "\\frac{"+"{0}".format(c)+"}" + "-" +"{"+"{0}".format(d)+"}"
            res = Rational(a,b)-Rational(c,d)
    if u>0:
        A = AxPb()
        B = AxPb()
        C = AxPb()
        D = AxPb()
        AA = sp.latex(A)
        BB = sp.latex(B)
        CC = sp.latex(C)
        DD = sp.latex(D)
        if v==0:
            S1 = "\\frac{"+ AA +"}"+"{"+ BB +"}" + " + " + "\\frac{"+CC+"}"+"{"+ DD +"}"
            res = sp.together(A/B + C/D)
        if v==1:
            S1 = "\\frac{"+AA+"}"+"{"+BB+"}" + " - " + "\\frac{"+CC+"}"+"{"+DD+"}"
            res = sp.together(A/B - C/D)
    return [S1,sp.latex(res)]
    


def StrExoFractionDur(classe):
    a = rd.randint(1,5)*racinepib()
    b = rd.randint(1,5)*racinepib()
    c = rd.randint(1,5)*racinepib()
    d = rd.randint(1,5)*racinepib()
    e = rd.randint(1,5)*racinepib()
    f = rd.randint(1,5)*racinepib()
    u = rd.randint(0,5)
    v= rd.randint(0,1)
    u=1
    if u==0:
        if v==0:
            S1 = "\\frac{"+"{0}".format(a)+"}"+"{"+"{0}".format(b)+"}" + " + " + "\\frac{"+"{0}".format(c)+"}"+"{"+"{0}".format(d)+"}"
            res = Rational(a,b)+Rational(c,d)
        if v==1:
            S1 = "\\frac{"+"{0}".format(a)+"}" + "{" +"{0}".format(b)+"}" + " - " + "\\frac{"+"{0}".format(c)+"}" + "-" +"{"+"{0}".format(d)+"}"
            res = Rational(a,b)-Rational(c,d)
    if u>0:
        A = AxPb()
        B = AxPb()
        C = AxPb()
        D = AxPb()
        AA = sp.latex(A)
        BB = sp.latex(B)
        CC = sp.latex(C)
        DD = sp.latex(D)
        if v==0:
            S1 = "\\frac{"+ AA +"}"+"{"+ BB +"}" + " + " + "\\frac{"+CC+"}"+"{"+ DD +"}"
            res = sp.together(A/B + C/D)
        if v==1:
            S1 = "\\frac{"+AA+"}"+"{"+BB+"}" + " - " + "\\frac{"+CC+"}"+"{"+DD+"}"
            res = sp.together(A/B - C/D)
    return [S1,sp.latex(res)]

    

def StrEqDroiteFacile(Classe):
    xa = rd.randint(1,9)
    ya = rd.randint(1,9)
    xb = rd.randint(1,9)
    yb = rd.randint(1,9)
    S1 = "\\text{Droite passant par }A"+ Vecteur2(xa,ya)+ "\\text{ et }B"+Vecteur2(xb,yb)
    corr = (x -xa)* (yb-ya)  - (y - ya)*(xb - xa)
    return [S1,sp.latex(corr)+" =0"]
    


def StrEqDroiteMoyenne(Classe):
    xa = rd.randint(1,9)*racinepib()
    ya = rd.randint(1,9)*racinepib()
    xb = rd.randint(1,9)*racinepib()
    yb = rd.randint(1,9)*racinepib()
    xc = rd.randint(1,9)*racinepib()
    yc = rd.randint(1,9)*racinepib()
    xd = rd.randint(1,9)*racinepib()
    yd = rd.randint(1,9)*racinepib()
    
    S1 = "\\text{Droite passant par }A "+ Vecteur2(xa,ya)+ "\\text{ et } B"+Vecteur2(xb,yb) +"\\text{ et la Droite passant par }C" + Vecteur2(xc,yc) + "\\text{ et } D" + Vecteur2(xd,yd)
    corr1 = (x - xa)* (yb - ya)  - (y - ya)*(xb - xa)
    corr1 = sp.latex(corr1) + "=0"
    corr2 = (x -xc)*(yd-yc) - (y - yc)*(xd - xc)
    corr2 = sp.latex(corr2) + "=0"
    Corr = "\\begin{array}{l}" + "{0}".format(corr1) + " \\\\ " + "{0}".format(corr2) + "\\end{array}"
    return [S1, Corr]
    
    
    
def StrEqDroiteDure(Classe):
    xa = rd.randint(1,9)*racinepib()
    ya = rd.randint(1,9)*racinepib()
    xb = rd.randint(1,9)*racinepib()
    yb = rd.randint(1,9)*racinepib()
    xc = rd.randint(1,9)*racinepib()
    yc = rd.randint(1,9)*racinepib()
    xd = rd.randint(1,9)*racinepib()
    yd = rd.randint(1,9)*racinepib()
    
    S1 = "\\text{Droite passant par }A "+ Vecteur2(xa,ya)+ "\\text{ et } B"+Vecteur2(xb,yb) +"\\text{ et la Droite passant par }C" + Vecteur2(xc,yc) + "\\text{ et } D" + Vecteur2(xd,yd)
    corr1 = (x - xa)* (yb - ya)  - (y - ya)*(xb - xa)
    Corr1 = sp.latex(corr1) + "=0"
    corr2 = (x -xc)*(yd-yc) - (y - yc)*(xd - xc)
    Corr2 = sp.latex(corr2) + "=0"
    Corr = "\\begin{array}{l}" + "{0}".format(Corr1) + " \\\\ " + "{0}".format(Corr2) + "\\end{array}"
    Corr2 = sp.latex(linsolve([corr1,corr2],[x,y]))
    return [S1,Corr,Corr2]
    
    
def StrProba(Classe):
    A = rd.randint(0,100)
    BsA = rd.randint(0,100)
    BsAb = rd.randint(0,100)
    
    
    Enonce = 'Un évenement $A$ arrive avec probabilité ${0}(A) =  {1}\%$ et un évenement $B$ arrive avec probabilité ${0}_A(B) =  {2}\% $  et ${0}_{3} (B) = {4}\%$'.format('\mathbb{P}',A,BsA,'{\overline{A}}',BsAb) 
    Question = "  \\begin{enumerate} \item Calculer $\mathbb{P}(A \cap B)$ \item Calculer $\mathbb{P}(B)$ \item Calculer $\mathbb{P}_B(A)$ \\end{enumerate}"
    
    S1 = Enonce + Question
    
    Corr1 = " \[  {0} (A \cap B) = {0}(A) \cdot {0}_A(B) = {1} \% \cdot {2} \% = {3}\] ".format("\mathbb{P}",A,BsA, A*BsA/10000) 
    Corr2 = "\[ {0} (B) = {0} (A \cap B) + {0} ({1} \cap B) = {2} \]".format("\mathbb{P}","\overline{A}",A*BsA/10000 + (100 - A)*BsAb/10000)
    Corr3 = "\[ {0}_B(A) = \\frac{1} {0} (A \cap B) {2} {1} {0} (B) {2} = \\frac {1} {3} {2} {1} {4} {2} = {5} \]".format("\mathbb{P}", "{", "}", A*BsA/10000, A*BsA/10000 + (100 - A)*BsAb/10000, (A*BsA/10000) / (A*BsA/10000 + (100 - A)*BsAb/10000))
    Corr = Corr1 + Corr2 + Corr3
    
    return [S1,Corr]
    
    

def ExoDeProba(m):
    
    [o,Exo,Correction] = Preambule("Exercice de Probabilité","S.Gibaud","Pour la noter","Seconde")
    [o,Exo,Correction] = Ouverture(o)
    for i in range(m):
        [S1,Corr] = StrProba("")
        Exo.write("\n \\section{Exercice %d} \n" %i)
        Exo.write(S1)
        Correction.write("\\section{Correction Exercice %d}" %i)
        Correction.write(Corr)
    Correction.close()
    Coorection = open('Correction.txt','r')
    t = Coorection.read()
    Exo.write(t)
    Exo.write("\n \\end{document}")
    Exo.close()
    Coorection.close()
    #os.system("pdflatex Exo.txt")
    #os.remove("Exo.txt")
    #os.remove("Exo.log")
    #os.remove("Exo.aux")
    
        
        
    
    
    

"""

******************************************************************************
Formation de parenthèses
******************************************************************************

"""


def racinepib():
    return pi() * racine()


def supinf():
    u = rd.randint(0, 1)
    if u == 0:
        return r"\geq"
    if u == 1:
        return r"\leq"


def Vecteur2(a, b):
    return "\\left( \\begin{array}{c}" + "{0}".format(a) + "\\\\" + "{0}".format(b) + "\\end{array}\\right)"


def Vecteur3(a, b, c):
    return "\\left( \\begin{array}{c}" + "{0}".format(a) + "\\\\" + "{0}".format(b) + "\\\\" + "{0}".format(
        c) + "\\end{array}\\right)"


def StrFexpr(expr):
    return "f(x) = " + sp.latex(expr) + "\\\\"


def AnalyseExpo(expr):
    S1 = StrFexpr(expr)
    deriv = sp.diff(expr, x)
    sgn = together(deriv / expr)
    [a, b] = fraction(sgn)
    a = a.expand()
    sgn = a / b
    deriv = sgn * expr
    resultat = solveset(sgn > 0, domain=S.Reals)
    return [S1, deriv, resultat]


def AnalyseLogA(expr):
    S1 = StrFexpr(expr)
    deriv = sp.diff(expr, x)
    sgn = together(deriv)
    [a, b] = fraction(sgn)
    a = a.expand()
    sgn = a / b
    deriv = sgn
    resultat = solveset(sgn > 0, domain=S.Reals)
    return [S1, deriv, resultat]


def AnalyseLog(expr, Df):
    S1 = StrFexpr(expr)
    deriv = sp.diff(expr, x)
    resultat = solveset(deriv > 0, domain=Df)
    return [S1, deriv, resultat]


def AnalyseLogFrac(expr, Df):
    S1 = StrFexpr(expr)
    deriv = sp.diff(expr, x)
    resultat = solveset(deriv > 0, domain=Df)
    return [S1, deriv, resultat]









def sqrt():
    return "\\sqrt"


def sqrtalea():
    u = rd.randint(0, 1)
    if u == 0:
        return "\\sqrt"
    if u == 1:
        return ""


def pi():
    u = rd.randint(0, 1)
    if u == 0:
        return sp.pi
    if u == 1:
        return 1


def racine():
    u = rd.randint(0, 5)
    v = rd.randint(1, 20)
    expr = sp.sqrt(v)
    if u < 5:
        return expr
    if u == 5:
        return 1


def sgnadd():
    u = rd.randint(0, 1)
    if u == 0:
        return " + "
    if u == 1:
        return " - "


def sgnadda():
    u = rd.randint(0, 1)
    if u == 0:
        return +rd.randint(1, 9)
    if u == 1:
        return -rd.randint(1, 9)


def sgnaddmult():
    u = rd.randint(0, 5)
    if u == 0:
        return " +{0} ".format(rd.randint(1, 9))
    if u == 1:
        return " -{0} ".format(rd.randint(1, 9))
    if u >= 2:
        return "{0}".format(rd.randint(1, 9))


def sgnnbre():
    u = rd.randint(0, 5)
    if u == 0:
        return 1
    if u > 0:
        return -1


def Carre(expr):
    u = rd.randint(0, 5)
    if u > 0:
        return expr ** 2
    if u == 0:
        return expr


def Cube(expr):
    u = rd.randint(0, 1)
    if u == 0:
        return expr ** 3
    if u == 1:
        return expr





def AxPb():
    a = rd.randint(1,10)
    b= rd.randint(1,10)
    return a*x + b
    
def AxPbDur():
    return racinepib() *x + racinepib()
    

def AxPbCarre():
    u=rd.randint(0,5)
    if u==1 or u == 2:
        a = rd.randint(0,9)
        b = rd.randint(0,9)
        c =rd.randint(0,9)
        return a*x**2 + b*x + c
    if u==0:
        return AxPb()
    if u > 2:
        return AxPb()**2
    
def AxPbCubeDur():
    a = rd.randint(1,9)
    b = rd.randint(1,9)
    c =rd.randint(1,9)
    d = rd.randint(1,9)
    u = rd.randint(0,1)
    expr1 = (racinepib()*a*x + b*racinepib())**3
    expr2 = a*racinepib()*x**3 + b*racinepib()*x**2 + racinepib()*c*x + d*racinepib()
    if u==0:
        return expr1
    if u==1:
        return expr2

def AxPbCube():
    a = rd.randint(1,9)
    b = rd.randint(1,9)
    c =rd.randint(1,9)
    d = rd.randint(1,9)
    u = rd.randint(0,1)
    expr1 = (a*x + b)**3
    expr2 = a*x**3 + b*x**2 + c*x + d
    if u==0:
        return expr1
    if u==1:
        return expr2
    
def AxPbCarreDur():
    return racinepib() * Carre(x) + sgnnbre() + racinepib()*x + sgnnbre() + racinepib()
    
    

    
def AxPbCarreSeul():
    u=rd.randint(0,5)
    if u==1 or u == 2:
        a = rd.randint(0,9)
        b = rd.randint(0,9)
        c =rd.randint(0,9)
        return a*x**2 + b*x + c
    if u==0:
        return AxPb()
    if u > 2:
        return AxPb()**2
    
    
def IdRemarq():
    a =rd.randint(1,5)
    b=rd.randint(1,5)
    expr = (a*x + sgnnbre() * b)**2
    return expr.expand()

