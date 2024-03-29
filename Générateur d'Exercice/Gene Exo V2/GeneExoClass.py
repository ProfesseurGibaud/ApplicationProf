
#%%
import os
import shutil
from ExerciceClasse import *
import random as rd
#%%

"""

Initialisation des Variables et des Fichiers

"""

path = os.getcwd()
os.chdir("..")
path2 = os.getcwd()
os.chdir(path)

Titre = 0
Date = 0

Exo = open("Exo.txt","w")
Correction = open("Correction.txt","w")
Exo.close()
Correction.close()

#%%
"""
******************************************
Fonction d'\\'ecriture
******************************************
"""    

def WriteSection(type,difficulte,texte):
    TitreSection = "\n \section{Exercices de " + type + " " + difficulte + "s" + "}"
    with open("Exo.txt","a") as Exo:
        Exo.write(TitreSection + "\n")
        Exo.write(Consigne(type,difficulte) + "\n")
    with open("Correction.txt","a") as Correction:
        Correction.write(TitreSection + "\n")
        Correction.write("\n Corrig\\'e " + type + " " + difficulte + "\n")
        if type == "Tableaux de Variation":
            Correction.write("\n Dans la suite, vous verrez la d\\'eriv\\'ee puis le domaine o\`u la d\\'eriv\\'ee est positive \n")
        if type == "Equation de Droite du Plan":
            Correction.write("\n Dans la suite, vous verrez la/les \'equations de droites puis leur intersection")
    texte += TitreSection
    return texte

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
    if type == "Equation de Droite du Plan" and difficulte == "Facile":#Equation de Droite
        text = "\n Donner l'\'equation de :"
    if type == "Equation de Droite du Plan" and difficulte == "Moyen":#Equation de Droite
        text = "\n Donner les \'equations de :"
    if type == "Equation de Droite du Plan" and difficulte == "Dur":#Equation de Droite
        text = "\n Donner les \'equations des droites suivantes ainsi que leur intersection :"
    if type == "Proba":
        text = "Faire les exos suivants"
        text = text + "\\\\ \n"
    return text

#%%
"""

Fonctions de Navigation avec les fichiers et les dossiers

"""

def move(a, b):
    try:
        shutil.move(a, b)
    except:
        print("veuillez renommer vos devoirs")
        aa = a + "veuillez renommer vos devoirs.pdf"
        os.rename(a, aa)
        move(aa, b)

def DeplacerPdf(Titre):
    os.rename("Exo.pdf", Titre + ".pdf")
    source = os.listdir(path)
    destination = path2
    """for files in source:
        if files.endswith(".pdf"):
            move(files,destination)
    """

def StrW(fichier, string):
    with open("Data/"+fichier + ".txt", "w") as file:
        file.write(str(string))

def StrR(fichier):
    with open("Data/"+fichier + ".txt") as file:
        String = str(file.read())
    return String

"""
Ecriture Pr\\'eambule
"""
#%%
def PreIncomp():
    texte =  ""
    texte += "\\documentclass[a4paper,oneside,11pt]{article} \n"
    texte += "\\usepackage[utf8]{inputenc} \n \\usepackage[T1]{fontenc} \n \\usepackage{textcomp} \n  \\usepackage[french]{babel} \n \\usepackage[autolanguage]{numprint} \n \\usepackage{amsmath,amssymb,amsthm} \n \setlength{\hoffset}{-20pt}   \n"
    with open("Exo.txt","a") as Exo:
        Exo.write("\\documentclass[a4paper,oneside,11pt]{article} \n")
        Exo.write("\\usepackage[utf8]{inputenc} \n \\usepackage[T1]{fontenc} \n \\usepackage{textcomp} \n  \\usepackage[french]{babel} \n \\usepackage[autolanguage]{numprint} \n \\usepackage{amsmath,amssymb,amsthm} \n \setlength{\hoffset}{-20pt}   \n")
    return texte
    
def PreTitre(Titre,Auteur,texte):
    if len(str(Titre))< 10:
        title = "Devoir d'Entrainement"
    else:
        title = str(Titre)
    if len(str(Auteur))<3:
        author = "S.Gibaud"
    else:
        author = str(Auteur)
    texte += "\\title{"+title+"} \n"
    texte += "\n \\author{" + author + "}"
    with open("Exo.txt","a") as Exo:
        Exo.write("\\title{"+title+"} \n")
        Exo.write("\n \\author{" + author + "}")
    return texte
    
def PreDate(Date,texte):
    if len(str(Date))<3:
        date = "\n \\date{\\`A rendre ou pas :) }"
    else:
        date = "\n \\date{\\`A rendre avant le " + str(Date) +"}" +"\n"
    texte += "\n \\date{\\`A rendre avant le " + str(Date) +"}" +"\n"
    with open("Exo.txt","a") as Exo:
        Exo.write(date)
    return texte


def Preambule(Titre,Auteur,Date,Classe,texte):
    # On change le répertoire de Travail : Mettre son répertoire de Travail : à la place du \ mettre //
    os.chdir(path)
    print("Preambule")
    pre_ = PreIncomp()
    pre_ = PreTitre(Titre,Auteur,texte)
    pre_ = PreDate(Date,texte)
    pre_ += "\\begin{document}"
    pre_ += "\n \\maketitle"
    with open("Exo.txt","a") as Exo:
        Exo.write("\\begin{document}")
        Exo.write("\n \\maketitle")
    return pre_ + texte


#%%


"""

Fonction de Verif

"""

def DicoVideFalse(dico):
    return sum(dico.values())!=0
def DicoNombre(dico):
    return sum(dico.values())


"""

Compilation

"""

def DevoirComplet(DicoExo,Titre,Auteur,Date,Classe,ZeroOuUn):
    Preambule(Titre,Auteur,Date,Classe)
    ListeType(DicoExo,Classe)
    PdfLatex(ZeroOuUn,Titre)



def PdfLatex(ZeroOuUn,Titre):
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
    DeplacerPdf(Titre)

def ListeType(DicoExo,Classe,texte):
    texte = texte
    for ttype in DicoExo:
        if DicoVideFalse(DicoExo[ttype]):
            for difficulte in DicoExo[ttype]:
                if DicoExo[ttype][difficulte]>0:
                    texte += WriteSection(ttype,difficulte,texte)
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
                        texte += Exoo.EcrireExo()
                        texte += "\n"
                        #Exoo.EcrireCorrection()
    return texte


"""

Gene Exo sans Interface Graphique Jolie

"""

def ChangerValeurs(Titre,Auteur,Date,Classe,ZeroOuUn):
    TTitre = input(Titre + "\n")
    if len(TTitre) > 0:
        Titre = TTitre
    AAuteur = input(Auteur + "\n")
    if len(AAuteur) > 0:
        Auteur = AAuteur
    DDate = input(Date + "\n")
    if len(DDate) > 0:
        Date = DDate
    ZZeroOuUn = input("Correction :" + str(ZeroOuUn) + "\n")
    if len(ZZeroOuUn) > 0:
        ZeroOuUn = int(ZZeroOuUn)
    return [Titre,Auteur,Date,Classe,ZeroOuUn]

def DicoExoGene():
    N = int(input("Nombre d'Exo aux total"))
    TType = ["D\\'eveloppement", "In\\'equation", "Equation", "Tableaux de Variation", "Fraction",
             "Equation de Droite du Plan", "Proba"]
    m = N
    #On tire au hasard la difficulté des exercices (pas de facile)
    DDifficulte = ["Facile", "Moyen", "Dur"]
    DicoExo = {}
    for ttype in TType:
        DicoExo[ttype] = {}
        for difficulte in DDifficulte:
            DicoExo[ttype][difficulte] = 0
    for difficulte in DDifficulte:
        DicoExo["Proba"][difficulte] = 0
        DicoExo["Equation de Droite du Plan"][difficulte] = 0

    for i in range(len(TType)-1):
        if input(TType[i]) != "0":
            u = rd.randint(0,m)
            m = m - u
            v = rd.randint(0,m)
            m = m - v
            DicoExo[TType[i]]["Dur"] = u
            DicoExo[TType[i]]["Moyen"] = v
            print("Ajouté")
    return DicoExo

DicoExo = {}
DicoExo["D\\'eveloppement"] = {"Facile":0,"Moyen":0,"Dur":0}
DicoExo["In\\'equation"] = {"Facile":20,"Moyen":40,"Dur":40}
DicoExo["Tableaux de Variation"] = {"Facile":20,"Moyen":40,"Dur":40}


for i in range(len(os.listdir("fichier_exo")),30):
    ListeType(DicoExo,"","")
    os.rename("Exo.txt",f"fichier_exo/{i}.txt")

