path = "C://Users//Sylgi//Google Drive//Python//Générateur d'Exercice"



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
CClasse = ["Sec","Prem","Term"]
Titre = 0
Date = 0


"""
Fonctions Principales
"""

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
        Complett = Complet()
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
        Classe = "Sec"
    elif classe =="première" or classe =="Première" or classe =="premiere" or classe == "Premiere" or classe =="1" or classe == 1:
        Classe = "Prem"
    elif classe == "Term" or classe == "Terminale" or classe == "term" or classe == "terminale" or classe == "TES" or classe == "tes" or classe == "TS" or classe == "ts":
        Classe = "Term"
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
    Exo.write(Consigne(type) + "\n")
    Correction.write(TitreSection + "\n")
    Correction.write("\n Corrig\\'e " + type + " " + difficulte + "\n")
    if type == "Tableaux de Variation":
        Correction.write("\n Dans la suite vous verrez la d\\'eriv\\'ee puis le domaine o\`u la d\\'eriv\\'ee est positive \n")
    
def WriteExo(type,difficulte,Classe,l,Exo,Correction):
    [exxo,corrr,der]= ExoEtCorr(type,difficulte,Classe)
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
    if classe == "Sec":
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
    if classe == "Sec":
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
    if classe == "Sec":
        u = rd.randint(0,1)
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
    

def StrTabVarMoyen(classe):
    u=rd.randint(0,2)
    if u==2:
        expr = AxPbCubeDur()+ sgnnbre()*AxPbCarreDur()
        if classe == "Sec":
            a = rd.randint(1,9)
            b = rd.randint(1,8)
            expr = (a*x + b)**3
        S1 = "f(x)  =" + sp.latex(expr) + "\\\\"
    if u==0:
        expr = AxPb()*AxPb()
        S1 = "f(x)  = " + sp.latex(expr) +"\\\\"
    if u==1:
        expr = AxPb()/AxPb()
        S1 = "f(x)  =  " + sp.latex(expr) + "\\\\"
    deriv = sp.diff(expr,x)
    resultat = solveset(deriv>=0, domain = S.Reals)
    return [S1, sp.latex(resultat),sp.latex(deriv)]


def StrTabVarDur(classe):
    u=rd.randint(0,2)
    if classe == "Sec":
        u=0
    if u==0:
        expr = racinepib()*AxPbCubeDur()
        if classe == "Sec":
            a = rd.randint(1,9)*racinepib()
            b = rd.randint(1,8)*racinepib()
            expr = (a*x + b)**3
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
    if u==0:
        A = IdRemarq()
        B = racinepib()
    if u==1:
        A = IdRemarq()
        B = IdRemarq()
    expr = A - B 
    Sol = solveset(expr,domain = S.Reals)
    return [sp.latex(A) +"=" + sp.latex(B), sp.latex(Sol)]
    

def StrExoFraction(classe):
    a = rd.randint(1,200)
    b = rd.randint(1,200)
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

    

#def StrEqDroiteFac(Classe):
    
    
    
#def StrEqDroiteMoy(Classe):
    





    
    

"""
Execution
""" 



Utilisateur()
    
    