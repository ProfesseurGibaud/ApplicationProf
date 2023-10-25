import numpy as np 
import random as rd



Liste = [10,10,20]

    """Exo = open("C://Users//Utilisateur//Google Drive//Python//Générateur d'Exercice//Exo.txt", "a")"""
    Exo = open("C://Users//Sylgi//Google Drive//Python//Générateur d'Exercice//Exo.txt","a")


def Compilation():
    Developpement(Liste)
    Inequations(Liste)
    EtudeDeFonction(Liste)
    Exo.write("\n\end{document}")
    Exo.close()
    


"""

Fonction d'écriture dans le texte

"""
    
def Developpement(Liste):
    for i in range(0,len(Liste)):
        if i == 0:
            Exo.write("\n \section{Exercices de Développement Simples}")
            Exo.write("\n")
            Exo.write("\n Développer les expressions suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            for l in range(0,Liste[i]):
                Exo.write(StrDevSimple())
            Exo.write("\n \end{align}")
        if i == 1 : 
            Exo.write("\n \section{Exercices de Développement Moyens}")
            Exo.write("\n")
            Exo.write("\n Développer les expressions suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            for l in range(0,Liste[i]):
                Exo.write(StrDevMoyen())
            Exo.write("\n \end{align}")
        if i == 2 : 
            Exo.write("\n \section{Exercices de Développement Durs}")
            Exo.write("\n")
            Exo.write("\n Développer les expressions suivantes  (si les multiplications deviennent trop dures les laisser apparentes): ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            for l in range(0,Liste[i]):
                Exo.write(StrDevDur())
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
                Exo.write(StrTabVarSimple())
            Exo.write("\n \end{align*}")
        if i == 1 : 
            Exo.write("\n \section{Exercices de Tableaux de Variations Moyens}")
            Exo.write("\n")
            Exo.write("\n Donner les variations des fonctions suivantes (Attention il y a des petits pièges): ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(StrTabVarMoyen())
            Exo.write("\n \end{align*}")
        if i == 2 : 
            Exo.write("\n \section{Exercices de Tableaux de Variations Durs}")
            Exo.write("\n")
            Exo.write("\n Donner les variations des fonctions suivantes (Attention il y a des petits pièges) (si les multiplications deviennent trop dures les laisser apparentes): ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(StrTabVarDur())
            Exo.write("\n \end{align*}")         

def Inequations(Liste):
    for i in range(0,len(Liste)):
        if i == 0:
            Exo.write("\n \section{Exercices d'Inequations Simples}")
            Exo.write("\n")
            Exo.write("\n Résoudre les inéquations suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(StrIneSimple())
            Exo.write("\n \end{align*}")
        if i == 1 : 
            Exo.write("\n \section{Exercices d'Inequations Moyens}")
            Exo.write("\n")
            Exo.write("\n Résoudre les inéquations suivantes ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(StrIneMoyen())
            Exo.write("\n \end{align*}")
        if i == 2 : 
            Exo.write("\n \section{Exercices d'Inequations Durs}")
            Exo.write("\n")
            Exo.write("\n Résoudre les inéquations suivantes (si les multiplications deviennent trop dures les laisser apparentes): ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(StrIneDur())
            Exo.write("\n \end{align*}")         

def Equations(Liste):
    for i in range(0,len(Liste)):
        if i == 0:
            Exo.write("\n \section{Exercices d'Equations Simples}")
            Exo.write("\n")
            Exo.write("\n Résoudre les équations suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(EqSimple())
            Exo.write("\n \end{align*}")
        if i == 1 : 
            Exo.write("\n \section{Exercices d'équations Moyens}")
            Exo.write("\n")
            Exo.write("\n Résoudre les équations suivantes ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(EqMoyenne())
            Exo.write("\n \end{align*}")
        if i == 2 : 
            Exo.write("\n \section{Exercices d'équations Durs}")
            Exo.write("\n")
            Exo.write("\n Résoudre les équations suivantes (si les multiplications deviennent trop dures les laisser apparentes): ")
            Exo.write("\n")
            Exo.write("\n \\begin{align*}")
            for l in range(0,Liste[i]):
                Exo.write(EqDure())
            Exo.write("\n \end{align*}") 



"""

*********************************************************************
Caractères Spéciaux
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
        return r'\pi'
    if u==1:
        return ""
    
def racine():
    return r'\sqrt{'+ "{0}".format(rd.randint(1,10)) + "}"



def sgnadd():
    u=rd.randint(0,1)
    if u==0:
        return " + "
    if u==1:
        return " - "

def sgnadda():
    u=rd.randint(0,1)
    if u==0:
        return " +{0} ".format(rd.randint(1,9))
    if u==1:
        return " -{0} ".format(rd.randint(1,9))

def sgnaddmult():
    u=rd.randint(0,5)
    if u==0:
        return " +{0} ".format(rd.randint(1,9))
    if u==1:
        return " -{0} ".format(rd.randint(1,9))
    if u>=2:
        return  "{0}".format(rd.randint(1,9))

def sgnnbre():
    u=rd.randint(0,1)
    return 2*u-1
    
    
def Carre():
    u=rd.randint(0,5)
    if u>0:
        return "^2"
    if u==0:
        return ""

def Cube():
    u=rd.randint(0,1)
    if u==0:
        return "^3"
    if u==1:
        return ""
"""

******************************************************************************
Formation de parenthèses
******************************************************************************

"""


def racinepib():
    return pi() + racine()+")"


def Para():
    a = sgnnbre()*rd.randint(0,10)
    return "({0}x".format(a) 
    
def bPar():
    b = rd.randint(0,10)
    return "{0})".format(b)
    
def Pracinepi():
    return "(" + "{0}".format(rd.randint(1,10)) + pi() +racine() +"x"
    
def supinf():
    u=rd.randint(0,1)
    if u==0:
        return r"\geq"
    if u==1:
        return r"\leq"
"""

******************************************************************************
Parenthèses formées
******************************************************************************

"""
    
    
def AxPb():
    return "{"+Para()+sgnadd()+bPar()+"}"
    
def AxPbDur():
    return "{" + Pracinepi() + sgnadd() + racinepib() + "}"
    

def AxPbCarre():
    return "{"+Para() + Carre() + sgnadd() + bPar() + Carre()+"}"
    
def AxPbCube():
    return "{"+Para() + sgnadd() + bPar() + Cube()+"}"
    
def AxPbCarreDur():
    return "{"+Pracinepi() + Carre() + sgnadd() + racinepib() + Carre()+"}"

def AxPbCubeDur():
    return "{"+Pracinepi() + sgnadd() + racinepib() + Cube()+"}"
    
def AxPbCarreSeul():
    u = rd.randint(0,1)
    if u==0:
        return "{"+Para() + Carre() + sgnadd() + bPar() +"}"
    if u==1:
        return "{"+Para()  + sgnadd() + bPar() + Carre() +"}"
    
    
def IdRemarq():
    a =rd.randint(1,9)
    aa = a*a
    b=rd.randint(1,9)
    bb =b*b
    ab = 2*a*b
    return "({0}x^2".format(aa) + sgnadd()+ r"{0}x".format(ab) + " + {0})".format(bb)
    

    
    
    
"""

****************************************************************************
Fonction d'Exercices
****************************************************************************

"""    
    

def StrDevSimple():
    return AxPb() + AxPb() + sgnadda() + AxPb() + AxPb() + "\\\\"

def StrDevMoyen():
    return AxPbCarre() + AxPbCarre() + sgnadda() + AxPbCarre() + AxPbCarre() + "\\\\"
    
def StrDevDur():
    S=""
    for k in range(3,6):
        S = S + AxPbCarreDur()
        S = S + sgnaddmult()
    S = S + AxPbCarreDur()
    S = S + "\\\\"
    return S

def StrTabVarSimple():
    u=rd.randint(0,2)
    if u==0:
        return "f(x) & =&" + AxPbCarreDur() + sgnadd() + AxPb() + "\\\\"
    if u==1:
        return "f(x) & = &" + AxPb() + sgnaddmult() + AxPb() +"\\\\"
    if u==2:
        return "f(x) & = & " + AxPbCubeDur() + "\\\\"

def StrTabVarMoyen():
    u=rd.randint(0,2)
    if u==0:
        return "f(x) & =&" + AxPbCubeDur() + sgnadd() + AxPbCarreDur() + "\\\\"
    if u==1:
        return "f(x) & = &" + AxPb() + sgnaddmult() + sqrtalea()+AxPb()+"\\\\"
    if u==2:
        return "f(x) & = & " + r"\frac{" + AxPb() + r"}{" + AxPb() + r"}" + "\\\\"
        
def StrTabVarDur():
    u=rd.randint(0,2)
    if u==0:
        return "f(x) & = &" + sqrt()+ AxPbCubeDur()  + "\\\\"
    if u==1:
        return "f(x) & = &" + AxPb() + sgnaddmult() + sqrtalea()+AxPbCarreDur()+"\\\\"
    if u==2:
        return "f(x) & = & " + r"\frac{" + AxPbCarreDur() + r"}{" + AxPbCarreDur() + r"}" + "\\\\"
        
        
def StrIneSimple():
    u=rd.randint(0,1)
    if u==0:
        return AxPb() + supinf() + AxPb() + "\\\\"
    if u==1:
        return AxPbCarreSeul() + supinf() + AxPbCarreSeul() + "\\\\"
        
    
def StrIneMoyen():
    return r"\frac{" + AxPb() + r"}{" + AxPb() + r"}" + supinf() + r"\frac{" +"{0}".format(rd.randint(1,9)) + r"}{" + "{0}".format(rd.randint(1,9)) + r"}" + "\\\\"



def StrIneDur():
    return r"\frac{" + AxPb() + r"}{" + AxPb() + r"}" + supinf() + r"\frac{" + AxPb() + r"}{" + AxPb() + r"}" + "\\\\"
    
    
def EqSimple():
    u=rd.randint(0,1)
    if u==0:
        return AxPb() + "=" + AxPb()
    if u==1:
        n = rd.randint(2,6)
        S = ""
        for i in range(0,n):
            S = S + AxPbDur()
        return S + "=0"
        
def EqMoyenne():
    return IdRemarq() + "=" + "{0}".format(rd.randint(1,9))+pi()
    
def EqDure():
    u = rd.randint(0,1)
    if u==0:
        return IdRemarq() + "=" + racine() + pi()
    if u==1:
        return IdRemarq() + "=" + IdRemarq()
        
        


            
        