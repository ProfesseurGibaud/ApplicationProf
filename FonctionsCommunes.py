import os

def dossier():
    os.chdir("Google Drive//Python//ApplicationProf")
dossier()
def GeneExo():
    os.chdir("GenerateurExercice")
    import ExerciceClasse as Ex
    import GeneExoClass as Ge
    os.chdir("..")


from GenerateurExercice.GeneExoClass import *
