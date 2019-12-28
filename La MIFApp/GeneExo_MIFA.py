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
from copy import *


import random as rd





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
        self.consigne = ""
        self.consignecorrection = ""
    
    def VersLatex(self):
        if self.type == "Tableaux de Variation" or self.type == "Fraction" or self.type == "Equation de Droite du Plan":
            if self.type == "Tableaux de Variation":
                self.enonce = "f(x) = " + sp.latex(self.expr)
        elif self.type == "Equation":
            self.enonce = sp.latex(self.expr) + "=0"
            self.correction = sp.latex(self.corr)
        else:
            self.enonce = sp.latex(self.expr)
            self.correction = sp.latex(self.corr)
    
    def FaireEnonce(self):
        if self.type == "D\\'eveloppement":
            if self.niveau == "Facile":
                u = rd.randint(0,2)
                self.expr = ((AxPb())**2 + sgnnbre() * AxPbCarre())
                self.enonce = sp.latex(self.expr)
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
            u = rd.randint(1,5)
            if u == 1:
                self.expr = A >= B
                self.res = A - B
            if u == 2:
                self.expr = A <= B
                self.res = B - A
            if u == 3:
                self.expr = 1 / B >= a
                self.res = 1 / B - a
            if u == 4:
                self.expr = 1 / B <= a
                self.res = -1 / B + a
            if u == 5:
                self.expr = I >= J
                self.res = I - J
            if u == 6 :
                self.expr = I <= J
                self.res = J - I
        if self.type == "Equation":
            u = rd.randint(0,5)
            if self.classe == "Terminale":
                u = rd.randint(0,3)  + rd.randint(0,4) + rd.randint(0,2)
            if u==0:
                A = AxPb()
                B = AxPb()
                self.expr = A - B
            if u==1:
                n = rd.randint(2,4)
                self.expr = AxPbDur()
                for i in range(0,n):
                    self.expr = self.expr * AxPbDur()
            if u == 2:
                A = IdRemarq()
                b = rd.randint(1,9)
                self.expr = A -b
            if u == 4:
                A = IdRemarq()
                B = racinepib()
                self.expr = A - B
            if u == 5:
                A = IdRemarq()
                B = IdRemarq()
                self.expr = A - B
            if u == 6:
                AA = AxPb()
                BB = AxPb()
                A = sp.exp(AA)
                B = sp.exp(BB)
                self.expr = A - B
            if u == 7:
                AA = AxPb()
                BB = AxPb()
                A = exp(AA)
                B = rd.randint(-5, 20)
                self.expr = A - B
            if u == 8:
                AA = AxPb()
                BB = AxPb()
                A = sp.log(AA)
                B = sp.log(BB)
                self.expr = A - B
            if u == 9:
                AA = AxPb()
                A = sp.log(AA)
                B = rd.randint(-5, 20)
                self.expr = A - B
        if self.type == "Fraction":
            u = rd.randint(0,1)
            if u == 0:
                [self.enonce,self.correction] = StrExoFraction(self.classe)
            if u == 1:
                [self.enonce,self.correction] = StrExoFractionMoyen(self.classe)
        if self.type == "Tableaux de Variation":
            u = rd.randint(0,5)
            if self.classe == "Terminale":
                u = rd.randint(0,3) + rd.randint(0,4) + rd.randint(0,2)
            if u == 0:
                self.expr = IdRemarq()
            if u == 1:
                self.expr = racinepib() * AxPb()
            if u == 2:
                A = IdRemarq()
                self.CheckDomaine = A
                self.expr = sp.sqrt(A)
            if u == 3:
                self.expr = AxPbCarreDur() + sgnnbre() + AxPb()
            if u == 4:
                self.expr = AxPbCarre() * AxPb()
            if u == 5:
                self.expr = AxPbCubeDur()
            if u == 6 or u ==9:
                A = AxPb()
                self.CheckDomaine = A
                self.expr = sp.log(A)/A
            if u == 7:
                self.expr = exp(AxPbCube())
            if u ==8:
                A = AxPbDur()
                self.CheckDomaine = A
                self.expr = sp.log(A) + ((AxPbDur())**3)
        self.FaireCorrection()
        self.VersLatex()

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
        if self.type == "D\\'eveloppement":
            self.consigne = "Développez l'expression suivante : "
        if self.type == "Fraction":
            self.consigne = "Simplifiez la fraction suivante"
        if self.type == "In\\'equation":
            self.consigne = "Résolvez l'inéquation suivante : "
        if self.type == "Equation":
            self.consigne = "Résolvez l'équation suivante : "
        if self.type == "Tableaux de Variation":
            self.consigne = "Donner la dérivée de f et la méthode pour trouver son signe"
        print(self.consigne)
    def EcrireCorrection(self):
        if self.type == "D\\'eveloppement":
            self.consignecorrection = "L'expression développée est : "
        if self.type == "In\\'equation":
            self.consignecorrection = "La solution de l'inéquation est : "
        if self.type == "Fraction":
            self.consignecorrection = "La fraction simplifié est :"
        if self.type == "Equation":
            self.consignecorrection = "La solution de l'équation est :"
        if self.type == "Tableaux de Variation":
            self.consignecorrection = "La dérivée de f est :"
        print(self.consignecorrection)

    def VersLatex(self):
        if self.type == "Tableaux de Variation" or self.type == "Fraction" or self.type == "Equation de Droite du Plan":
            if self.type == "Tableaux de Variation":
                self.enonce = "f(x) = " + sp.latex(self.expr)
                # Pour Faciliter la fonction qui affiche les corrections : Affiche la dérivée plutôt que le signe de la dérivée.
                self.correction = sp.latex(self.der)
        elif self.type == "Equation":
            self.enonce = sp.latex(self.expr) + "=0"
            self.correction = sp.latex(self.corr)
        else:
            self.enonce = sp.latex(self.expr)
            self.correction = sp.latex(self.corr)


def DevoirComplet(DicoExo,Titre,Auteur,Date,Classe):
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


