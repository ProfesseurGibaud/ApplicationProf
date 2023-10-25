

import os
import shutil
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
import sympy.assumptions.handlers
from copy import *


from kivy.app import App
from kivy.core.window import Window
from kivy.base import EventLoop
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import VariableListProperty
from kivy.properties import ObjectProperty,ListProperty,StringProperty,NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.cache import Cache
from kivy.uix.slider import Slider


import random as rd


path = os.getcwd()
os.chdir("..")
path2 = os.getcwd()
os.chdir(path)



def DicoVideFalse(dico):
    return sum(dico.values())!=0

def DicoNombre(dico):
    return sum(dico.values())







Titre = 0
Date = 0




Exo = open("Exo.txt","w")
Correction = open("Correction.txt","w")
Exo.close()
Correction.close()

"""
Classe Exercices
"""

class Exercice:
    def __init__(self):
        self.der = 0
        self.res = 0
        self.CheckDomaine = 0
        self.Df = S.Reals
        self.expr = 0
        self.enonce = ""
        self.corr = 0
        self.correction = ""
        self.correction2 = ""
        self.correction3 =""
        self.niveau = "Facile"
        self.numero = 1
        self.res = 0
        self.classe = "Seconde"
        self.type = "D\\'eveloppement"
        self.derive = ""
        self.StrExpr = ""

    def FaireEnonce(self):
        if self.type == "D\\'eveloppement":
            if self.niveau == "Facile":
                self.expr = AxPb() * AxPbCarre() + sgnnbre() * AxPb() * AxPbCarre()
                self.enonce = sp.latex(self.expr)
            if self.niveau == "Moyen":
                self.expr = self.expr = AxPbCarre() * AxPbCarre() + sgnnbre()  * AxPbCarre() * AxPbCarre()
            if self.niveau == "Dur":
                self.expr = 1
                for k in range(3, 6):
                    self.expr = self.expr * AxPbCarre()
                    self.expr = self.expr + sgnnbre() * rd.randint(2, 10) * AxPb()
                self.expr = self.expr * AxPbCarre()
        if self.type == "In\\'equation":
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
                if self.niveau == "Facile":
                    if v == 0:
                        self.expr = A >=B
                        self.res = A - B
                    if v == 1:
                        self.expr = A <=B
                        self.res = B-A
                if self.niveau == "Moyen":
                    if v == 0:
                        self.expr = A/B >= c/d
                        self.res = A/B - c/d
                    if v == 1:
                        self.expr = A/B <= c/d
                        self.res = -A/B + c/d
                if self.niveau == "Dur":
                    if u == 0:
                        self.expr = I / A >= J / A
                        self.res = I / A - J / A
                    if u == 1:
                        self.expr = I / A <= J / A
                        self.res = J / A - I / A
            else :
                if self.niveau == "Facile":
                    if v == 0:
                        self.expr = AA >= BB
                        self.res = AA - BB
                    if v == 1:
                        self.expr = AA <= BB
                        self.res = BB -  AA
                if self.niveau == "Moyen":
                    if v == 0:
                        self.expr = A/B >= c/d
                        self.res = A/B - c/d
                    if v == 1:
                        self.expr = A/B <= c/d
                        self.res = -A/B + c/d
                if self.niveau == "Dur":
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
        if self.type == "Equation":
            if self.niveau == "Facile":
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
            if self.niveau == "Moyen":
                A = IdRemarq()
                b = rd.randint(1,9)
                self.expr = A -b
            if self.niveau == "Dur":
                u = rd.randint(0,1)
                v = rd.randint(0,1)
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
                else:
                    if u==0:
                        A = IdRemarq()
                        B = racinepib()
                    if u==1:
                        A = IdRemarq()
                        B = IdRemarq()
                self.expr = A - B
            print(self.expr)
            
        if self.type == "Fraction":
            if self.niveau == "Facile":
                [self.enonce,self.correction] = StrExoFraction(self.classe)
            if self.niveau == "Moyen":
                [self.enonce,self.correction] = StrExoFractionMoyen(self.classe)
            if self.niveau =="Dur":
                [self.enonce,self.correction] = StrExoFractionDur(self.classe)
        if self.type == "Equation de Droite du Plan":
            if self.niveau == "Facile":
                [self.enonce,self.correction] = StrEqDroiteFacile(self.classe)
            if self.niveau == "Moyen":
                [self.enonce,self.correction] = StrEqDroiteMoyenne(self.classe)
            if self.niveau =="Dur":
                [self.enonce,self.correction,self.corr2] = StrEqDroiteDure(self.classe)
        if self.type == "Proba":
            [self.enonce,self.correction] = StrProba(self.classe)
        if self.type == "Tableaux de Variation":
            if self.niveau == "Facile":
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
            if self.niveau == "Moyen":
                u = rd.randint(0,3)
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
                if u ==4: #Je n'arrive pas à résoudre par info le signe de la dérivée
                    A = AxPbDur()
                    self.CheckDomaine = A
                    self.expr = sp.log(A) + ((AxPbDur())**3)
            if self.niveau == "Dur":
                u = rd.randint(0,3)
                if self.classe!= "Terminale":
                    u = rd.randint(0,1)
                if u == 0:
                    A = AxPbCarre()
                    self.CheckDomaine = A
                    self.expr= racinepib()*sp.sqrt(A)*AxPbDur()
                if u == 1:
                    A = AxPbDur()
                    B = AxPbCarre()
                    self.CheckDomaine = B
                    self.expr = racinepib()*sp.sqrt(A)/B
                if u == 2:
                    self.expr = racinepib()*sp.exp(AxPbCarre()) * AxPb()
                if u == 3:
                    A = AxPbCarreDur()/AxPb()
                    self.CheckDomaine = A
                    self.expr = racinepib()*sp.log(A)
                    
                if self.classe == "Seconde":
                    A = AxPbDur()
                    self.CheckDomaine = A
                    self.expr = self.expr = racinepib()* AxPbDur() * sp.sqrt(A)
        print(self.expr)
            
    def FaireCorrection(self):
        if self.type == "D\\'eveloppement":
            self.corr = self.expr.expand()
        if self.type == "In\\'equation":
            self.corr = solveset(self.res >= 0, domain=S.Reals)
        if self.type == "Equation":
            self.corr = solveset(self.expr, domain=S.Reals)
        if self.type == "Tableaux de Variation":
            self.der = sp.together(sp.expand(sp.together(sp.diff(self.expr, x))))
            self.Df = solveset(self.CheckDomaine >= 0, domain=S.Reals)
            [a, b] = fraction(self.der)
            self.res = solveset(a >= 0, domain=self.Df)
        
    def EcrireExo(self):
        with open("Exo.txt","a") as Exo:
            Exo.write(self.type + " num\\'ero " + "{0}".format(self.numero))
            ajoutdevant = "" #"f(x) = "*(self.type == "Tableaux de Variation")
            ajoutderriere = "= 0"*(self.type == "Equation")
            Exo.write(" \\[" + ajoutdevant +  self.enonce + ajoutderriere +  "\\]")

    def EcrireCorrection(self):
        if self.type == "Tableaux de Variation":
            with open("Correction.txt","a") as Correction:
                Correction.write( "\n Fonction {0}".format(self.numero))
                Correction.write("\\[ " +  self.enonce +"\]")
                Correction.write("\n \\[f'(x) = " + sp.latex(self.der) + "\]")
                Correction.write("\n \\[" + sp.latex(self.res) + "\]")
        elif self.type == TType[5]: #Eq de Droite
            with open("Correction.txt", "a") as Correction:
                Correction.write("\n Correction " + self.type + " num\\'ero " + "{0}".format(self.numero))
                Correction.write("\n \\[" + self.correction + "\]")
                if self.niveau == "Dur":
                    Correction.write("\n L'intersection est \\[" + self.corr2 + "\]")
        else:
            with open("Correction.txt", "a") as Correction:
                Correction.write("\n Correction " + self.type + " num\\'ero " + "{0}".format(self.numero) + "\\[")
                Correction.write(self.correction)
                Correction.write("\n \\]")

    def VersLatex(self):
        if self.type == "Tableaux de Variation" or self.type == "Fraction" or self.type == "Equation de Droite du Plan":
            if self.type == "Tableaux de Variation":
                self.enonce = "f(x) = " + sp.latex(self.expr)
        else:
            self.enonce = sp.latex(self.expr)
            self.correction = sp.latex(self.corr)


def DevoirComplet(DicoExo,Titre,Auteur,Date,Classe,ZeroOuUn):
    Preambule(Titre,Auteur,Date,Classe)
    ListeType(DicoExo,Classe)
    PdfLatex(ZeroOuUn)

def Preambule(Titre,Auteur,Date,Classe):
    # On change le répertoire de Travail : Mettre son répertoire de Travail : à la place du \ mettre //
    os.chdir(path)
    PreIncomp()
    PreTitre(Titre,Auteur)
    PreDate(Date)
    with open("Exo.txt","a") as Exo:
        Exo.write("\\begin{document}")
        Exo.write("\n \\maketitle")

def PdfLatex(ZeroOuUn):
    if ZeroOuUn == 0:
        print("Pas de Correction")
    elif ZeroOuUn ==1:
        with open("Correction.txt","r") as Corr:
            text = Corr.read()
        with open("Exo.txt","a") as Exo:
            Exo.write(text)
    else:
        print("Que fait on ?")
    with open("Exo.txt","a") as Exo:
        Exo.write("\n \\end{document}")
    os.system("pdflatex Exo.txt")
    os.remove("Exo.txt")
    if ZeroOuUn == 1:
        os.remove("Correction.txt")
    os.remove("Exo.log")
    os.remove("Exo.aux")
    DeplacerPdf()



def ListeType(DicoExo,Classe):
    for ttype in DicoExo:
        if DicoVideFalse(DicoExo[ttype]):
            for difficulte in DicoExo[ttype]:
                if DicoExo[ttype][difficulte]>0:
                    WriteSection(ttype,difficulte)
                    for l in range(DicoExo[ttype][difficulte]):
                        Exoo = Exercice()
                        Exoo.numero = l
                        print(l)
                        Exoo.type = ttype
                        Exoo.niveau = difficulte
                        Exoo.classe = Classe
                        Exoo.FaireEnonce()
                        Exoo.FaireCorrection()
                        Exoo.VersLatex()
                        Exoo.EcrireExo()
                        Exoo.EcrireCorrection()

"""
******************************************
Fonction d'\\'ecriture
******************************************
"""    

def WriteSection(type,difficulte):
    TitreSection = "\n \section{Exercices de " + type + " " + difficulte + "s" + "}"
    with open("Exo.txt","a") as Exo:
        Exo.write(TitreSection + "\n")
        Exo.write(Consigne(type,difficulte) + "\n")
    with open("Correction.txt","a") as Correction:
        Correction.write(TitreSection + "\n")
        Correction.write("\n Corrig\\'e " + type + " " + difficulte + "\n")
        if type == "Tableaux de Variation":
            Correction.write("\n Dans la suite, vous verrez la d\\'eriv\\'ee puis le domaine o\`u la d\\'eriv\\'ee est positive \n")
        if type == TType[5]:
            Correction.write("\n Dans la suite, vous verrez la/les \'equations de droites puis leur intersection")

def Consigne(type,difficulte):
    text = "Y'a un bug dans le programme"
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
 
"""
Ecriture Pr\\'eambule
"""

def PreIncomp():
    with open("Exo.txt","a") as Exo:
        Exo.write("\\documentclass[a4paper,oneside,11pt]{article} \n")
        Exo.write("\\usepackage[utf8]{inputenc} \n \\usepackage[T1]{fontenc} \n \\usepackage{textcomp} \n  \\usepackage[french]{babel} \n \\usepackage[autolanguage]{numprint} \n \\usepackage{amsmath,amssymb,amsthm} \n \setlength{\hoffset}{-20pt}   \n")
    
def PreTitre(Titre,Auteur):
    if len(str(Titre))< 10:
        title = "Devoir d'Entrainement"
    else:
        title = str(Titre)
    if len(str(Auteur))<3:
        author = "S.Gibaud"
    else:
        author = str(Auteur)
    with open("Exo.txt","a") as Exo:
        Exo.write("\\title{"+title+"} \n")
        Exo.write("\n \\author{" + author + "}")
    
def PreDate(Date):
    if len(str(Date))<3:
        date = "\n \\date{\\`A rendre ou pas :) }"
    else:
        date = "\n \\date{\\`A rendre avant le " + str(Date) +"}" +"\n"
    with open("Exo.txt","a") as Exo:
        Exo.write(date)













































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
    [a,b] = fraction(res)
    a = sp.expand(a)
    res = a/b
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
    xa = rd.randint(1,9)
    ya = rd.randint(1,9)
    xb = rd.randint(1,9)
    yb = rd.randint(1,9)
    xc = rd.randint(1,9)
    yc = rd.randint(1,9)
    xd = rd.randint(1,9)
    yd = rd.randint(1,9)
    
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
    a = sp.latex(a)
    b = sp.latex(b)
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




"""


Kivy Implémentation



"""


def StrW(fichier,string):
    with open(fichier+".txt","w") as file:
        file.write(str(string))

def StrR(fichier):
    with open(fichier + ".txt") as file:
        String = str(file.read())
    return String





Titre = "Devoir de Rattrapage de "
Auteur = "S. Gibaud"
Date = "18 Novembre"
Classe = "Terminale"
ZeroOuUn = 1




TType = ["D\\'eveloppement", "In\\'equation", "Equation", "Tableaux de Variation", "Fraction","Equation de Droite du Plan","Proba"]
DDifficulte = ["Facile", "Moyen", "Dur"]
CClasse = ["Seconde","Premiere","Terminale"]
TTType = ["Développement", "Inéquation","Equation", "Tableaux de Variation", "Fraction", "Equation de Droites du Plan","Proba"]

def TransTType2TTType(t):
    i = TType.index(t)
    return TTType[i]


def IntR(fichier):
    with open(fichier + ".txt") as file:
        n = int(file.read())
    return n

sm = ScreenManager()

class SliderTypeDiff(GridLayout):
    def __init__(self,type,difficulte):
        super(SliderTypeDiff, self).__init__()
        self.type = type
        self.difficulte = difficulte
        self.cols = 4
        self.nombre = Slider(min=0, max=30,value = 0)
        # 1st row - one label, one slider
        self.add_widget(Label(text=difficulte))
        self.add_widget(self.nombre)
        # 2nd row - one label for caption,
        # one label for slider value
        self.add_widget(Label(text="Nombre d'Exos"))
        self.labelnombre = Label(text='0')
        self.add_widget(self.labelnombre)
        # On the slider object Attach a callback
        # for the attribute named value
        self.nombre.bind(value=self.on_value)
    # Adding functionality behind the slider
    # i.e when pressed increase the value
    def on_value(self, instance, babar):
        self.labelnombre.text = "% d" % babar
        DicoExo[self.type][self.difficulte] = int(babar)
        updateLabel()


    # The app class

class OptionScreen(Screen):
    def build(self):
        # Le nom de l'ecran
        self.name = 'Options'
        # On cree le contenu:
        Option_Layout = GridLayout(padding=20, spacing=10,cols = 2)
        self.NouveauTitre = TextInput(text=StrR("Titre"))
        Option_Layout.add_widget(self.NouveauTitre)
        self.BoutonNouveauTitre = Button(text="Changer Titre")
        self.BoutonNouveauTitre.bind(on_press = self.changertitre)
        Option_Layout.add_widget(self.BoutonNouveauTitre)
        self.NouveauNomProf = TextInput(text = StrR("Auteur"))
        Option_Layout.add_widget(self.NouveauNomProf)
        self.BoutonNomProf = Button(text = "Mettre Nom Prof")
        self.BoutonNomProf.bind(on_press = self.ChangerNomProf)
        Option_Layout.add_widget(self.BoutonNomProf)
        self.NouvelleClasse = TextInput(text = StrR("Classe"))
        Option_Layout.add_widget(self.NouvelleClasse)
        self.BoutonClasse = Button(text="Changer (Seconde, Premiere, Terminale)")
        self.BoutonClasse.bind(on_press=self.ChangerClasse)
        Option_Layout.add_widget(self.BoutonClasse)
        self.NouvelleDate = TextInput(text="Date de retour")
        Option_Layout.add_widget(self.NouvelleDate)
        self.BoutonDate = Button(text = "Changer Date de Retour")
        self.BoutonDate.bind(on_press = self.ChangerDate)
        Option_Layout.add_widget(self.BoutonDate)
        self.NouvelleCorrection = TextInput(text=StrR("ZeroOuUn"))
        Option_Layout.add_widget(self.NouvelleCorrection)
        self.BoutonCorrection = Button(text="Changer Correction : Avec = 1, Sans = 0")
        self.BoutonCorrection.bind(on_press=self.ChangerCorrection)
        Option_Layout.add_widget(self.BoutonCorrection)

        self.BoutonRetour = Button(text = "Retour")
        self.BoutonRetour.bind(on_press = self.Retour)
        Option_Layout.add_widget(self.BoutonRetour)


        self.add_widget(Option_Layout)
        sm.add_widget(self)



    def ChangerNomProf(self,instance):
        StrW("Auteur",self.NouveauNomProf.text)
        Auteur = StrR("Auteur")

    def changertitre(self,instance):
        StrW("Titre",self.NouveauTitre.text)
        Titre = StrR("Titre")

    def ChangerClasse(self,instance):
        StrW("Classe", self.NouvelleClasse.text)
        Classe = StrR("Auteur")

    def ChangerDate(self,instance):
        StrW("Date", self.NouvelleDate.text)
        Date = StrR("Date")

    def ChangerCorrection(self,instance):
        StrW("ZeroOuUn", self.NouvelleCorrection.text)
        ZeroOuUn = IntR("ZeroOuUn")

    def Retour(self,instance):
        sm.current = "Acceuil"


def move(a,b):
    try:
        shutil.move(a,b)
    except:
        print("veuillez renommer vos devoirs")
        aa = a + "veuillez renommer vos devoirs.pdf"
        os.rename(a,aa)
        move(aa,b)
        

def DeplacerPdf():
    #Titre = StrR("Titre")    #A modifier
    os.rename("Exo.pdf",Titre + ".pdf")
    source = os.listdir(path)
    destination = path2
    """for files in source:
        if files.endswith(".pdf"):
            move(files,destination)
    """





DicoExo = {}
DicoSlider = {}
DicoLabel = {}
DicoLabel2 = {}
for ttype in TType:
    DicoExo[ttype] = {}
    DicoSlider[ttype] = {}
    for difficulte in DDifficulte:
        DicoExo[ttype][difficulte] = 0
        DicoSlider[ttype][difficulte] = SliderTypeDiff(ttype,difficulte)
    DicoLabel[ttype] = Label(text = "Quantité = " + str(DicoNombre(DicoExo[ttype])))
    DicoLabel2[ttype] = Label(text = str(DicoNombre(DicoExo[ttype])),size_hint_x = 0.1)
for difficulte in DDifficulte:
    DicoExo["Proba"][difficulte] = 0
    DicoExo["Equation de Droite du Plan"][difficulte] = 0
    



def updateLabel():
    for ttype in TType:
        DicoLabel[ttype].text = "Quantité = "  + str(DicoNombre(DicoExo[ttype]))
        DicoLabel2[ttype].text = str(DicoNombre(DicoExo[ttype]))

updateLabel()


class EcranOption(Screen):
    def build(self):
        pass

class EcranType(Screen):
    def build(self,type):
        self.name = type
        self.type = type
        self.tttype = TransTType2TTType(self.type)
        layout = BoxLayout(orientation = "vertical")
        PremierLayout = BoxLayout(orientation = "horizontal")
        BoutonRetour = Button(text = "Retour")
        BoutonRetour.bind(on_press=self.VersDebut)
        PremierLayout.add_widget(BoutonRetour)
        PremierLayout.add_widget(Label(text = self.tttype))
        PremierLayout.add_widget(DicoLabel[self.type])
        layout.add_widget(PremierLayout)
        for difficulte in DDifficulte:
            layout.add_widget(DicoSlider[self.type][difficulte])
        self.add_widget(layout)
        sm.add_widget(self)
    def VersDebut(self,instance):
        sm.current = "Acceuil"

class EcranAcceuil(Screen):
    def build(self):
        self.name = "Acceuil"
        GrosLayout = BoxLayout(orientation = "vertical")
        TitreEcran = Label(text = "Générateur d'Exercice")
        TitreEcran.size_hint_y = 0.3
        GrosLayout.add_widget(TitreEcran)
        EnDessousLayout = GridLayout(cols = 3)
        GaucheLayout = GridLayout(cols = 2)
        self.DicoBouton = {}
        for ttype in TType:  #J'en suis ici Faire les lignes Un bouton Un Total
            self.DicoBouton[ttype] = Button(text = TransTType2TTType(ttype),id = ttype)
            self.DicoBouton[ttype].bind(on_press = self.VersType)
            GaucheLayout.add_widget(self.DicoBouton[ttype])
            GaucheLayout.add_widget(DicoLabel2[ttype])
        EnDessousLayout.add_widget(GaucheLayout)
        EnDessousLayout.add_widget(Label())
        DroiteLayout = BoxLayout(orientation = "vertical")
        GeneBoutton = Button(text = "Génerer les Exercices",id = "Gene")
        GeneBoutton.bind(on_press = self.GenererExo)
        DroiteLayout.add_widget(GeneBoutton)
        OptionBouton = Button(text = "Options",id ="Options")
        OptionBouton.bind(on_press = self.VersOption)
        DroiteLayout.add_widget(OptionBouton)
        EnDessousLayout.add_widget(DroiteLayout)
        GrosLayout.add_widget(EnDessousLayout)
        self.add_widget(GrosLayout)
        sm.add_widget(self)

    def VersOption(self,instance):
        sm.current = "Options"
    def VersType(self,instance):
        sm.current = instance.id
    def GenererExo(self,instance):
        DevoirComplet(DicoExo,Titre,Auteur,Date,Classe)














class SliderExample(App):
    def build(self):
        DicoEcran = {}
        for ttype in TType:
            DicoEcran[ttype] = EcranType()
            DicoEcran[ttype].build(ttype)
        EcranAccceuil = EcranAcceuil()
        EcranAccceuil.build()
        OptionScreeen = OptionScreen()
        OptionScreeen.build()



        sm.current = "Acceuil"
        return sm

    # creating the object root for ButtonApp() class







#root = SliderExample()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.


#root.run()
