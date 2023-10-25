import numpy as np 
import random as rd





def Compilation():
    Exo = open("C://Users//Utilisateur//Google Drive//Python//Générateur d'Exercice//Exo.txt", "a")
    Developpement(10,Liste)
    Exo.close()
    
    
    
def Developpement(n,Liste):
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
            Exo.write("\n Développer les expressions suivantes : ")
            Exo.write("\n")
            Exo.write("\n \\begin{align}")
            for l in range(0,Liste[i]):
                Exo.write(StrDevDur())
            Exo.write("\n \end{align}")
        
    Exo.write("\end{document}")
    
def StrDevSimple():
    
    return "".format()

def StrDevMoyen():
    return"Moyen \\\\"
    
def StrDevDur():
    return "Dur \\\\"

