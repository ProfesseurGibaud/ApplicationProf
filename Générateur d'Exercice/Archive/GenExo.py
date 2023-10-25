import os
import sympy as sp
import numpy as np 
import random as rd
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy.solvers.inequalities import solve_rational_inequalities
from sympy import solveset,S
from sympy import together

from sympy import fraction, Rational, Symbol

Liste = [20,20,20]
TType = ["D\\'eveloppement", "In\\'equation", "Equation", "Tableaux de Variation", "Fraction"]
DDifficulte = ["Facile", "Moyen", "Dur"]
Titre = 0
Date = 0


"""
Fonctions Principales
"""
def Test():
    print("ohoh")

def DevoirComplet(Liste,Lieu,Titre,Auteur,Date):
    o=0
    [o,Exo,Correction] = Ouverture(o,Lieu)
    PreIncomp(Exo)
    PreTitre(Titre,Auteur,Exo)
    PreDate(Date,Exo)
    Exo.write("\\begin{document}")
    Exo.write("\n \\maketitle")
    Exo.close()
    Correction.close()
    for type in TType:
        [Exo,Correction] = ListeType(o,type,Liste,Lieu)
    [o,Exo,Correction] = Ouverture(o,Lieu)
    Exo.close()
    Correction.close()
    return [Exo,Correction]


def Preambule(Lieu,Titre,Auteur,Date):
    o=0
    [o,Exo,Correction] = Ouverture(o,Lieu)
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
    os.remove("Correction.txt")
    os.remove("Exo.log")
    os.remove("Exo.aux")

def ListeType(o,type,Liste,Lieu):
    [o,Exo,Correction]=Ouverture(o,Lieu)
    for difficulte in DDifficulte:
        [j,k] = TypeDifficulte(type,difficulte)
        print (type + " " + difficulte)
        if Liste[k]>0:
            WriteSection(type,difficulte,Exo,Correction)
            for l in range(Liste[k]):
                print(l)
                WriteExo(type,difficulte,l,Exo,Correction)
    Exo.close()
    Correction.close()
    return [Exo,Correction]
    
 
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


def OuverturePortable(o):
    os.chdir("C://Users//Sylgi//Google Drive//Python//Générateur d'Exercice")
    if o == 0:
        Exo = open("Exo.txt","x")
        Correction = open("Correction.txt","x")
        o=1
    else:
        Exo = open("Exo.txt","a")
        Correction = open("Correction.txt","a")
    return [o,Exo,Correction]


def OuvertureBureau():
    Exo = open("C://Users//Utilisateur//Google Drive//Python//G\\'en\\'erateur d'Exercice//Exobis.txt", "a")
    Correction = open("C://Users//Utilisateur//Google Drive//Python//G\\'en\\'erateur d'Exercice//Correction2.txt","a")
    return [Exo,Correction]

    
def Ouverture(o,Lieu):
    if Lieu =="Port" or Lieu == "port" or Lieu == "Portable" or Lieu == "portable":
        [o,Exo,Correction]=OuverturePortable(o)
    else:
        [o,Exo,Correction]=OuvertureBureau(o)
    return [o,Exo,Correction]
        




"""
******************************************
Fonction d'\\'ecriture
******************************************
"""    


def WriteSection(type,difficulte,Exo,Correction):
    TitreSection = "\n \section{Exercices de " + type + " " + difficulte + "s" + "}"
    Exo.write(TitreSection + "\n")
    Exo.write(Consigne(type) + "\n")
    Correction.write(TitreSection + "\n")
    Correction.write("\n Corrig\\'e " + type + " " + difficulte + "\n")
    if type == "Tableaux de Variation":
        Correction.write("\n Dans la suite vous verrez la d\\'eriv\\'ee puis le domaine o\`u la d\\'eriv\\'ee est positive \n")
    
def WriteExo(type,difficulte,l,Exo,Correction):
    [exxo,corrr,der]= ExoEtCorr(type,difficulte)
    Exo.write(type + " num\\'ero " + "{0}".format(l))
    Exo.write(" \\[" +  exxo +  "\\]")
    if type == "Tableaux de Variation":
                Correction.write( "\n Fonction {0}".format(l))
                Correction.write("\\["+ exxo +"\]")
                Correction.write("\n \\[f'(x) = " + der + "\]")
                Correction.write("\n \\[" + corrr + "\]")
                
    else:            
        Correction.write("\n Correction " + type + " num\\'ero " + "{0}".format(l) + "\\[")
        Correction.write(corrr)
        Correction.write("\n \\]")

def Consigne(type):
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
    text = text + "\\\\ \n"
    return text



def TypeDifficulte(type,difficulte): # Petite fonction quasi inutile juste pour suivre plus facilement les type est les difficultes.
    for k in range(len(DDifficulte)):
        if difficulte == DDifficulte[k]:
            SSS = k
    for l in range(len(TType)):
        if type == TType[l]:
            TTT = l
    return [TTT,SSS]
    

    



def ExoEtCorr(type,difficulte):
    der = "" # Pour les tableaux de variation j'ai besoin de la d\\'eriv\\'ee donc je suis oblig\\'e de la rajouter partout
    if TypeDifficulte(type,difficulte) == [0,0]:
        [exo,corr] = StrDevSimple()
    if TypeDifficulte(type,difficulte) == [0,1]:
        [exo,corr] = StrDevMoyen()
    if TypeDifficulte(type,difficulte) == [0,2]:
        [exo,corr] = StrDevMoyen() #Modifier le prog développement Dur
    if TypeDifficulte(type,difficulte) == [1,0]:
        [exo,corr] = StrIneSimple()
    if TypeDifficulte(type,difficulte) == [1,1]:
        [exo,corr] = StrIneMoyen()
    if TypeDifficulte(type,difficulte) == [1,2]:
        [exo,corr] = StrIneDur()
    if TypeDifficulte(type,difficulte) == [2,0]:
        [exo,corr] = StrEqSimple()
    if TypeDifficulte(type,difficulte) == [2,1]:
        [exo,corr] = StrEqMoyenne()
    if TypeDifficulte(type,difficulte) == [2,2]:
        [exo,corr] = StrEqDure()    
    if TypeDifficulte(type,difficulte) == [3,0]:
        [exo,corr,der] = StrTabVarSimple()
    if TypeDifficulte(type,difficulte) == [3,1]:
        [exo,corr,der] = StrTabVarMoyen()
    if TypeDifficulte(type,difficulte) == [3,2]:
        [exo,corr,der] = StrTabVarDur()
    if TypeDifficulte(type,difficulte) == [4,0]:
        [exo,corr] = StrExoFraction()
    if TypeDifficulte(type,difficulte) == [4,1]:
        [exo,corr] = StrExoFractionMoyen()
    if TypeDifficulte(type,difficulte) == [4,2]:
        [exo,corr] = StrExoFractionDur()
    return [exo,corr,der]
    
   
   
   
    
   







    
    
x = sp.var('x')











"""

*********************************************************************
Caractères Sp\\'eciaux
*********************************************************************

"""
def sqrt():
    return "\\sqrt"
    
def sqrtalea():
    u=rd.randint(0,1)
    if u==0:
        return "\\sqrt"
    if u==1:
        return ""

def pi():
    u=rd.randint(0,1)
    if u==0:
        return sp.pi
    if u==1:
        return 1
    
def racine():
    u=rd.randint(0,5)
    v = rd.randint(1,20)
    expr = sp.sqrt(v)
    if u<5:
        return expr
    if u==5:
        return 1



def sgnadd():
    u=rd.randint(0,1)
    if u==0:
        return " + "
    if u==1:
        return " - "

def sgnadda():
    u=rd.randint(0,1)
    if u==0:
        return +rd.randint(1,9)
    if u==1:
        return -rd.randint(1,9)

def sgnaddmult():
    u=rd.randint(0,5)
    if u==0:
        return " +{0} ".format(rd.randint(1,9))
    if u==1:
        return " -{0} ".format(rd.randint(1,9))
    if u>=2:
        return  "{0}".format(rd.randint(1,9))

def sgnnbre():
    u=rd.randint(0,5)
    if u==0:
        return 1
    if u>0:
        return -1
    
    
def Carre(expr):
    u=rd.randint(0,5)
    if u>0:
        return expr**2
    if u==0:
        return expr

def Cube(expr):
    u=rd.randint(0,1)
    if u==0:
        return expr**3
    if u==1:
        return expr
"""

******************************************************************************
Formation de parenthèses
******************************************************************************

"""


def racinepib():
    return pi() * racine()
    
def supinf():
    u=rd.randint(0,1)
    if u==0:
        return r"\geq"
    if u==1:
        return r"\leq"







"""

******************************************************************************
Parenthèses form\\'ees
******************************************************************************

"""
    
    
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
    return racinepib() * Carre(x) + sgnnbre() + racinepib()
    
    

    
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
****************************************************************************
Fonction d'Exercices
****************************************************************************
"""
    

def StrDevSimple():
    expr = AxPb() * AxPbCarre() + sgnnbre()*AxPb() * AxPbCarre()
    return [sp.latex(expr) + "\\\\",sp.latex(expr.expand())]

def StrDevMoyen():
    expr = AxPbCarre() * AxPbCarre() + sgnnbre()  * AxPbCarre() * AxPbCarre()
    return [sp.latex(expr) + "\\\\",sp.latex(expr.expand())]
    
def StrDevDur():
    S=1
    for k in range(3,6):
        S = S  *  AxPbCarreDur()
        S = S  + sgnnbre() * rd.randint(2,10)*AxPb()
    S = S * AxPbCarreDur()
    return [sp.latex(S) + "\\\\",sp.latex(S.expand())]

def StrIneSimple():
    u=rd.randint(0,1)
    v=rd.randint(0,1)
    A = AxPb()
    B = AxPb()
    AA = AxPbCarreSeul()
    BB = AxPbCarreSeul()
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


    
def StrIneMoyen():
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



def StrIneDur():
    u=rd.randint(0,1)
    v=rd.randint(0,1)
    A = AxPb()
    B = AxPb()
    C = AxPb()
    D = AxPb()
    if v==0:
        expr = A/B >= C/D
        res = A/B - C/D
    if v==1:
        expr = A/B <= C/D
        res = C/D - A/B
    exprcorrige = solveset(res>=0, domain = S.Reals)
    return [sp.latex(expr) + "\\\\", sp.latex(exprcorrige)]



def StrTabVarSimple():
    u=rd.randint(0,2)
    
    if u==0:
        expr = AxPbCarreDur() + sgnnbre() + AxPb()
        S1 =  "f(x)  =" + sp.latex(expr) + "\\\\"
    if u==1:
        expr = AxPb() * AxPb()
        S1 =  "f(x)  = " + sp.latex(AxPb() * AxPb()) +"\\\\"
    if u==2:
        expr = AxPbCubeDur()
        S1 = "f(x)  =  " + sp.latex(expr) + "\\\\"
    deriv = sp.diff(expr,x)
    resultat = solveset(deriv>=0, domain = S.Reals)
    return [S1,sp.latex(resultat),sp.latex(deriv)]
    

def StrTabVarMoyen():
    u=rd.randint(0,2)
    if u==0:
        expr = AxPbCubeDur()+ sgnnbre()*AxPbCarreDur()
        S1 = "f(x)  =" + sp.latex(expr) + "\\\\"
    if u==1:
        expr = AxPb()*AxPb()
        S1 = "f(x)  = " + sp.latex(expr) +"\\\\"
    if u==2:
        expr = AxPb()/AxPb()
        S1 = "f(x)  =  " + sp.latex(expr) + "\\\\"
    deriv = sp.diff(expr,x)
    resultat = solveset(deriv>=0, domain = S.Reals)
    return [S1, sp.latex(resultat),sp.latex(deriv)]


def StrTabVarDur():
    u=rd.randint(0,2)
    if u==0:
        expr = racinepib()*AxPbCubeDur()
        S1 = "f(x)  = " + sp.latex(expr) + "\\\\"
    if u==1:
        expr = AxPb()*racinepib()*AxPbCarreDur()
        S1 = "f(x)  = " + sp.latex(expr) +"\\\\"
    if u==2:
        expr = AxPbCarreDur()/AxPb()
        S1 = "f(x)  =  " + sp.latex(expr) + "\\\\"
    deriv = sp.diff(expr,x)
    resultat = solveset(deriv>=0, domain = S.Reals)
    return [S1, sp.latex(resultat),sp.latex(deriv)]    
      

    
    
def StrEqSimple():
    u=rd.randint(0,1)
    if u==0:
        A = AxPb()
        B = AxPb()
        expr = A - B
        pprint = sp.latex(A) + "=" + sp.latex(B)
    if u==1:
        n = rd.randint(2,6)
        expr = AxPbDur()
        for i in range(0,n):
            expr = expr * AxPbDur()
        pprint = sp.latex(expr) + "= 0"
    Sol = solveset(expr,domain = S.Reals)
    return [pprint + "\\\\",sp.latex(Sol)]

def StrEqMoyenne():
    A = IdRemarq()
    b = rd.randint(1,9)
    expr = A -b
    Sol = solveset(expr,domain = S.Reals)
    return [sp.latex(A) + "\\\\",sp.latex(Sol)]
   
    
def StrEqDure():
    u = rd.randint(0,1)
    if u==0:
        A = IdRemarq()
        B = racinepib()
    if u==1:
        A = IdRemarq()
        B = IdRemarq()
    expr = A - B 
    Sol = solveset(expr,domain = S.Reals)
    return [sp.latex(A) +"=" + sp.latex(B), sp.latex(Sol)]
    

def StrExoFraction():
    a = rd.randint(1,200)
    b = rd.randint(1,200)
    return ["\\frac{"+"{0}".format(a)+"}"+"{"+"{0}".format(b)+"}",sp.latex(Rational(a,b))]
    
def StrExoFractionMoyen():
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
    


def StrExoFractionDur():
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

    
    
"""
***********************************************************
***********************************************************


Archive 


**********************************************************
**********************************************************



def Inequations(Liste):
    for i in range(0,len(Liste)):
        if i == 0:
            Exo.write("\n \section{Exercices d'In\\'equations Simples}")
            Exo.write("\n")
            Exo.write("\n R\\'esoudre les in\\'equations suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            Correction.write("\n \section{Exercices d'In\\'equations Simples}")
            Correction.write("\n")
            Correction.write("\n Corrig\\'e In\\'equations Simples: ")
            Correction.write("\n")
            for l in range(0,Liste[i]):
                [exxo,corr] = StrIneSimple()
                Exo.write(exxo)
                Correction.write("\n \\begin{align*}")
                Correction.write(corr)
                Correction.write("\n \end{align*}")
            Exo.write("\n \end{align}")
        if i == 1 : 
            Exo.write("\n \section{Exercices d'In\\'equations Moyennes}")
            Exo.write("\n")
            Exo.write("\n R\\'esoudre les in\\'equations suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            Correction.write("\n \section{Exercices d'In\\'equations Moyennes}")
            Correction.write("\n")
            Correction.write("\n Corrig\\'e In\\'equations Moyennes: ")
            Correction.write("\n")
            for l in range(0,Liste[i]):
                [exxo,corr] = StrIneMoyen()
                Exo.write(exxo)
                Correction.write("\n \\begin{align*}")
                Correction.write(corr)
                Correction.write("\n \end{align*}")
            Exo.write("\n \end{align}")
        if i == 2 : 
            Exo.write("\n \section{Exercices d'In\\'equations Dures}")
            Exo.write("\n")
            Exo.write("\n R\\'esoudre les in\\'equations suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            Correction.write("\n \section{Exercices d'In\\'equations Dures}")
            Correction.write("\n")
            Correction.write("\n Corrig\\'e In\\'equations Dures: ")
            Correction.write("\n")
            for l in range(0,Liste[i]):
                [exxo,corr] = StrIneDur()
                Exo.write(exxo)
                Correction.write("\n \\begin{align*}")
                Correction.write(corr)
                Correction.write("\n \end{align*}")
            Exo.write("\n \end{align}")

def Equations(Liste):
    for i in range(0,len(Liste)):
        if i == 0:
            Exo.write("\n \section{Exercices d'Equations Simples}")
            Exo.write("\n")
            Exo.write("\n R\\'esoudre les \\'equations suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(EqSimple()[0])
            Exo.write("\n \end{align*}")
        if i == 1 : 
            Exo.write("\n \section{Exercices d'\\'equations Moyens}")
            Exo.write("\n")
            Exo.write("\n R\\'esoudre les \\'equations suivantes ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(EqMoyenne()[0])
            Exo.write("\n \end{align*}")
        if i == 2 : 
            Exo.write("\n \section{Exercices d'\\'equations Durs}")
            Exo.write("\n")
            Exo.write("\n R\\'esoudre les \\'equations suivantes (si les multiplications deviennent trop dures les laisser apparentes): ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(EqDure()[0])
            Exo.write("\n \end{align*}") 





    


def Developpement(Liste):
    for i in range(0,len(Liste)):
        if i == 0:
            WriteSection("D\\'eveloppement",Type[i])
            Exo.write("\n \\begin{align}")
            for l in range(0,Liste[i]):
                [exxo,corr] = StrDevSimple()
                Exo.write(exxo)
                Correction.write("\n \\begin{align*}")
                Correction.write(corr)
                Correction.write("\n \end{align*}")
            Exo.write("\n \end{align}")
        if i == 1 : 
            Exo.write("\n \section{Exercices de D\\'eveloppement Moyens}")
            Exo.write("\n")
            Exo.write("\n D\\'evelopper les expressions suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            Correction.write("\n \section{Exercices de D\\'eveloppement Moyens}")
            Correction.write("\n")
            Correction.write("\n D\\'evelopper les expressions suivantes : ")
            Correction.write("\n")
            for l in range(0,Liste[i]):
                [exxo,corr] = StrDevMoyen()
                Exo.write(exxo)
                Correction.write("\n \\begin{align*}")
                Correction.write(corr)
                Correction.write("\n \end{align*}")
            Exo.write("\n \end{align}")
        if i == 3 : #Je d\\'esactive les developpements durs.
            Exo.write("\n \section{Exercices de D\\'eveloppement Durs}")
            Exo.write("\n")
            Exo.write("\n D\\'evelopper les expressions suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            Correction.write("\n \section{Correction de D\\'eveloppement Dur}")
            Correction.write("\n")
            Correction.write("\n D\\'evelopper les expressions suivantes : ")
            Correction.write("\n")
            for l in range(0,Liste[i]):
                [exxo,corr] = StrDevDur()
                Exo.write(exxo)
                Correction.write("\n \\begin{align*}")
                Correction.write(corr)
                Correction.write("\n \end{align*}")
            Exo.write("\n \end{align}") 



def EtudeDeFonction(Liste):
    for i in range(0,len(Liste)):
        if i == 0:
            Exo.write("\n \section{Exercices de Tableaux de Variations Simples}")
            Exo.write("\n")
            Exo.write("\n Donner les variations des fonctions suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(StrTabVarSimple()[0])
            Exo.write("\n \end{align*}")
        if i == 1 : 
            Exo.write("\n \section{Exercices de Tableaux de Variations Moyens}")
            Exo.write("\n")
            Exo.write("\n Donner les variations des fonctions suivantes (Attention il y a des petits pièges): ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(StrTabVarMoyen()[0])
            Exo.write("\n \end{align*}")
        if i == 2 : 
            Exo.write("\n \section{Exercices de Tableaux de Variations Durs}")
            Exo.write("\n")
            Exo.write("\n Donner les variations des fonctions suivantes (Attention il y a des petits pièges) (si les multiplications deviennent trop dures les laisser apparentes): ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(StrTabVarDur()[0])
            Exo.write("\n \end{align*}")         







def EtudeDeFonctionCorr(Liste):
    for i in range(0,len(Liste)):
        if i == 0:
            Exo.write("\n \section{Exercices de Tableaux de Variations Simples}")
            Exo.write("\n")
            Exo.write("\n Donner les variations des fonctions suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            Correction.write("\n \section{Exercices de Tableaux de Variations Simples}")
            Correction.write("\n")
            Correction.write("\n Corrig\\'e Tableaux de Tableaux Simples: ")
            Correction.write("\n")
            Correction.write("Dans la suite vous verrez la d\\'eriv\\'ee puis le domaine o\`u la d\\'eriv\\'ee est positive")
            Correction.write("\n")
            for l in range(0,Liste[i]):
                [exxo,der,corr] = StrTabVarSimple()
                Exo.write(exxo)
                Correction.write( "\n Fonction {0}".format(l))
                Correction.write("\\["+ exxo +"\]")
                Correction.write("\n \\[f'(x) = " + der + "\]")
                Correction.write("\n \\[" + corr + "\]")
            Exo.write("\n \end{align}")
        if i == 1 : 
            Exo.write("\n \section{Exercices de Tableaux de Variations Moyens}")
            Exo.write("\n")
            Exo.write("\n Donner les variations des fonctions suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            Correction.write("\n \section{Exercices de Tableaux de Variations Moyens}")
            Correction.write("\n")
            Correction.write("\n Corrig\\'e Tableaux de Variations Moyens : ")
            Correction.write("\n")
            Correction.write("Dans la suite vous verrez la d\\'eriv\\'ee puis le domaine o\`u la d\\'eriv\\'ee est positive")
            Correction.write("\n")
            for l in range(0,Liste[i]):
                [exxo,der,corr] = StrTabVarMoyen()
                Exo.write(exxo)
                Correction.write( "\n Fonction {0}".format(l))
                Correction.write("\n \\["+ exxo +"\]")
                Correction.write("\n \\[f'(x) = " + der + "\]")
                Correction.write("\n \\[" + corr + "\]")
            Exo.write("\n \end{align}")
        if i == 2:
            Exo.write("\n \section{Exercices de Tableaux de Variations Durs}")
            Exo.write("\n")
            Exo.write("\n Donner les variations des fonctions suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            Correction.write("\n \section{Exercice de Tableaux de Variation Durs}")
            Correction.write("\n")
            Correction.write("\n Corrig\\'e des tableaux de Variation Durs : ")
            Correction.write("\n")
            Correction.write("Dans la suite vous verrez la d\\'eriv\\'ee puis le domaine o\`u la d\\'eriv\\'ee est positive")
            Correction.write("\n")
            for l in range(0,Liste[i]):
                [exxo,der,corr] = StrTabVarDur()
                Exo.write(exxo)
                Correction.write( "\n Fonction {0}".format(l))
                Correction.write("\n \\["+ exxo +"\]")
                Correction.write("\n \\[f'(x) = " + der + "\]")
                Correction.write("\n \\[" + corr + "\]")
            Exo.write("\n \end{align}")



def Fraction(Liste):
    l = Liste[0]
    ll = Liste[1]
    Exo.write("\n \section{Exercices de Simplification de Fractions de Nombres}")
    Exo.write("\n")
    Exo.write("\n Simplifier les fractions suivantes : ")
    Exo.write("\n")
    for l in range(0,l):
        [exo,corr]  = ExoFraction()
        Exo.write("\\[")
        Exo.write(exo)
        Exo.write("\\]")
        Correction.write("\\[")
        Correction.write(corr)
        Correction.write("\\]")
    
    Exo.write("\n \section{Exercices de Mise sous le m\\^eme d\\'enominateur}")
    Exo.write("\n")
    Exo.write("\n Simplifier les fractions suivantes : ")
    Exo.write("\n")
    for l in range(0,l):
        [exo,corr]  = ExoFractionDur()
        Exo.write("\\[")
        Exo.write(exo)
        Exo.write("\\]")
        Correction.write("\\[")
        Correction.write(corr)
        Correction.write("\\]"





    


def Compilation():
    Developpement(Liste)
    Inequations(Liste)
    EtudeDeFonctionCorr(Liste)
    Exo.write("\n\end{document}")
    Exo.close()
    Correction.close()

"""
