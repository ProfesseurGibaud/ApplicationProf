from GeneExoClass import *
DicoExo = DicoExoGene()
liste_eleve = ["Sayuri"]
DicoExo["D\\'eveloppement"]["Facile"] = 5
DicoExo["D\\'eveloppement"]["Moyen"] = 5
DicoExo["D\\'eveloppement"]["Dur"] = 10
DicoExo["Fraction"]["Facile"] = 5
DicoExo["Fraction"]["Moyen"] = 5
DicoExo["Fraction"]["Dur"] = 10
DicoExo["In\\'equation"]["Facile"] = 10
DicoExo["In\\'equation"]["Moyen"] = 25
DicoExo["In\\'equation"]["Dur"] = 25
DicoExo["Tableaux de Variation"]["Facile"] = 33 
DicoExo["Tableaux de Variation"]["Moyen"] = 33
DicoExo["Tableaux de Variation"]["Dur"] = 34
while len(liste_eleve)>0:
    titre = f"Devoir de {liste_eleve.pop()}"
    DevoirComplet(DicoExo,titre,"S. Gibaud","7 Novembre à 10h","1er Spé Math",0)