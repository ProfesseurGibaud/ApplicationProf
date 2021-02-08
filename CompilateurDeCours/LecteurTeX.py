import os
import codecs
from treelib import Node,Tree
import sympy as sp

"""

On va faire deux bases de données. Une base avec toutes les définitions, théorèmes, etc ... avec comme attribut juste la classe et l'auteur

On va faire une seconde Table rempli avec une structure d'arbre (On ouvre une branche par chapitre puis une autre par section. Chaque définiions,thm etc... aura une numéro de chapitre et de section (Ce sera fait juste à partir de mes cours.

"""

tree = Tree()

def Chapter(ligne,TitreChapitre):
    global tree,subsectionOuiNon
    if r"\chapter{" in ligne and "Correction" not in ligne:
        TitreChapitre = ligne
        TitreChapitre = TitreChapitre.replace(r"\chapter{", "")
        TitreChapitre.replace("}", "")
        tree.create_node(TitreChapitre, TitreChapitre, parent="Root")
        subsectionOuiNon = False
    return TitreChapitre

def Section(ligne,TitreSection):
    global subsectionOuiNon,SectionOuiNon,tree
    if r"\section{" in ligne:
        TitreSection = ligne
        TitreSection = TitreSection.replace(r"\section{", "")
        TitreSection = TitreSection.replace(r"}", "")
        tree.create_node(TitreSection, TitreSection, parent=TitreChapitre)
        subsectionOuiNon = False
        SectionOuiNon = True
    return TitreSection

def SubSection(ligne,TitreSubSection):
    global subsectionOuiNon,tree
    if r"\subsection{" in ligne:
        TitreSubSection = ligne
        TitreSubSection = TitreSubSection.replace(r"\subsection{", "")
        TitreSubSection = TitreSubSection.replace(r"}", "")
        tree.create_node(TitreSubSection, TitreSubSection, parent=TitreSection)
        subsectionOuiNon = True
    return TitreSubSection

def LectureType(ligne,type):  #Fonction en Cours pour eviter de refaire n fois la lecture. Il faudra peut être Faire un Dico pour les tempcontainer
    global DicoRecord,DicoTempRecorder,DicoContainer,compteur


    if r"\end{"+type+r"}" in ligne:
        DicoRecord[type] = False
        DicoContainer[type].append(DicoTempRecorder[type])
        tree.create_node(type + " {0:0=02d}".format(compteur),str(compteur),data=DicoTempRecorder[type],parent=parent)
        compteur += 1
        DicoTempRecorder[type] = ""
    if DicoRecord[type]  == True:
        DicoTempRecorder[type] += ligne
    if r"\begin{" + type + r"}" in ligne:
        DicoRecord[type]  = True




Type = ["definition","theorem", "example","proof"]
DicoRecord = {"definition":False,"theorem":False,"example":False,"proof":False}
DicoTempRecorder = {"definition":"","theorem":"","example":"","proof":""}
DicoContainer = {"definition":[],"theorem":[],"example":[],"proof":[]}

with codecs.open("CoursPremièreGibaud T1.tex","r", encoding = 'utf-8') as file:
    Container = []
    tempcontainer = ""
    compteur = 0
    tree.create_node("1G","Root")
    subsectionOuiNon = False
    SectionOuiNon = False
    TitreChapitre = "Rien"
    TitreSection = "Rien"
    TitreSubSection = "Rien"
    parent = "Nobody"
    for ligne in file:
        TitreChapitre = Chapter(ligne,TitreChapitre)
        TitreSection = Section(ligne,TitreSection)
        TitreSubSection = SubSection(ligne,TitreSubSection)
        if subsectionOuiNon:
            parent = TitreSubSection
        elif SectionOuiNon:
            parent = TitreSection
        for type in Type:
            LectureType(ligne,type)


tree.show()



