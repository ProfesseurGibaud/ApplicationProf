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
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.cache import Cache
from PyPDF2 import PdfFileMerger
from copy import *
from datetime import *
import random
import os
import csv
from Rapport import *
from FonctionPdf import *
from datetime import *



def today():
    D = datetime.today()
    return str(D.day) + " " + str(D.month) + " " + str(D.year)

def checkToday(str):
    booleen = False
    path = os.getcwd()
    os.chdir("Date")
    try :
        with open(str + ".txt",'r') as file:
            test = file.read()
            if test == today():
                booleen = True
    except:
        print("Rien pour le moment")
    os.chdir(path)
    return booleen

def StampToday(str):
    import os
    path = os.getcwd()
    os.chdir("Date")
    with open(str + ".txt", 'w') as file:
        file.write(today())
    os.chdir(path)



def listenum(liste):
    # On fait une liste vide appelée lliste
    lliste = []

    # On fait une boucle For. Pour i de 0 au nombre d'éléments de la liste
    for i in range(0, len(liste)):
        # On  ajoute à lliste l'element i de liste
        lliste.append(liste[i])
    """
    En fait il y a un outil qui s'appelle deepcopy qui fait ça en une ligne. Mais je ne le connaissais pas quand j'ai fait ce programme.
    """
    # On crée une liste vide appelé liste finale
    listefinale = []

    # Pour i allant de 0 au nombre d'éléments de lliste
    for i in range(0, len(lliste)):
        # On prend un nombre u au hasard entre 0 et le nombre d'elt de la liste (-1)
        u = random.randint(0, len(lliste) - 1)
        # On appelle Lili l'element de la liste choisit au hasard par le nombre u
        Lili = lliste[u]
        # On met dans listefinale l'element Lili
        listefinale.append(Lili)
        # On supprime l'élément que l'on a mit dans listefinale
        del lliste[u]
        # La fonction envoie en sortie listefinale qui est la liste mais mélangée.
    return listefinale

def dossier():
    import os
    os.chdir("Google Drive//Python//App Rapport//Application Rapport")


# dossier()


def CSV_Vers_DicoClasse():
    # On va charger toutes les listes de toutes les classes.
    Dico = {}
    path = os.getcwd()
    TempListe = []
    os.chdir("Classes")
    for classe in os.listdir():
        nomclasse = classe[:len(classe) - 4]
        print(nomclasse)
        TempListe.clear()
        try:
            print(classe)
            cr = csv.DictReader(open(classe, "r"))
            for row in cr:
                tempdico = dict(row)
                TempListe.append(list(tempdico.values()))
            print(TempListe[0][1])
            Dico[nomclasse] = TempListe
            Dico = deepcopy(Dico)
            print(Dico[nomclasse][0][1])
        except IOError:
            print("Erreur! Csv Vers DicoClasse")
    os.chdir(path)
    return Dico


def StrW(fichier, string):
    with open(fichier + ".txt", "w") as file:
        file.write(str(string))


def StrR(fichier):
    with open(fichier + ".txt") as file:
        String = str(file.read())
    return String


def IntR(fichier):
    with open(fichier + ".txt") as file:
        n = int(file.read())
    return n


def PrepLabel(DicoLabel, str):
    DicoLabel[str] = Label(text=str)
    return DicoLabel

def restartP():
    ListePunis =[] #liste avec les noms des punis
    ListeNomPunis = []
    ListePrenomPunis = []
    Rappo = []
    Feuille = []  #Tester .set
    ListeMotifs = []
    ClasseEnCours = []
    ListeSeconde = []
    StrW("EleveEnCours","0")
    labelmotifP = Label(text = str(ListeMotifs))
    ProfP = Label()
    SalleP = Label()
    TexteMotif =""
    TextInputVerifP = TextInput()
    CompteurRapport = 0
    LabelEleveP =Label()
    #ListeSeconde = CSV_Vers_ListeSeconde(ListeSeconde)
    Dico = CSV_Vers_DicoClasse()
    TextInputSanctionP = TextInput()
    TextInputPunitionP = TextInput()
    DicoLabelP = {}
    LabelPunisSecondeP = {}
    for classe in Dico:
        LabelPunisSecondeP = PrepLabel(DicoLabelP,classe)
    return [ListePunis,ListeNomPunis,ListePrenomPunis,Rappo,Feuille,ListeMotifs,ClasseEnCours,LabelPunisSecondeP,labelmotifP,TexteMotif,TextInputVerifP,CompteurRapport,LabelEleveP,ListeSeconde,SalleP,ProfP,Dico,DicoLabelP,TextInputSanctionP,TextInputPunitionP]

[ListePunis,ListeNomPunis,ListePrenomPunis,Rappo,Feuille,ListeMotifs,ClasseEnCours,LabelPunisSecondeP,labelmotifP,TexteMotif,TextInputVerifP,CompteurRapport,LabelEleveP,ListeSeconde,SalleP,ProfP,Dico,DicoLabelP,TextInputSanctionP,TextInputPunitionP] = restartP()

sm = ScreenManager()  # Create the screen manager, il est forcement global


# On construit 4 ecrans : Un Menu et un ecran par classe
class MenuScreenP(Screen):
    def build(self):
        # Le nom de l'ecran
        self.name = 'Menu P'
        # On cree le contenu:
        Menu_Layout = BoxLayout(padding=20, spacing=10, orientation='vertical')
        # On cree un premier bouton:
        self.Bouton_Seconde = Button(text="Seconde")
        self.Bouton_Seconde.bind(on_press=self.Vers_Seconde)
        # On ajoute le bouton dans l'affichage:
        Menu_Layout.add_widget(self.Bouton_Seconde)

        # On cree un deuxieme bouton:
        self.Bouton_Premiere = Button(text='Première')
        self.Bouton_Premiere.bind(on_press=self.Vers_Premiere)
        # On ajoute le bouton dans l'affichage:
        Menu_Layout.add_widget(self.Bouton_Premiere)

        # On cree un troisième bouton:
        self.Bouton_Terminale = Button(text='Terminale')
        self.Bouton_Terminale.bind(on_press=self.Vers_Terminale)
        # On ajoute le bouton dans l'affichage:
        Menu_Layout.add_widget(self.Bouton_Terminale)

        # On ajoute le Layout dans l'ecran de menu
        self.add_widget(Menu_Layout)
        # On ajoute l'ecran menu dans le ScreenManager:
        sm.add_widget(self)

    # Une fonction pour aller aux écrans des classes :
    def Vers_Seconde(self, instance):
        sm.current = 'Seconde P'

    def Vers_Premiere(self, instance):
        sm.current = 'Premiere P'

    def Vers_Terminale(self, instance):
        sm.current = 'Terminale P'




"""
*********************************************************
Seconde
*********************************************************
"""


class SecondeScreenP(Screen):  # Le deuxieme ecran : Seconde
    def build(self):
        self.name = 'Seconde P'
        Seconde_Layout = SecondeP()  # On creer le contenu
        Seconde_Layout.build()
        self.add_widget(Seconde_Layout)  # On ajoute le contenu dans l'ecran
        sm.add_widget(self)  # On ajoute l'ecran menu dans le ScreenManager

class SecondeP(BoxLayout):  # Le contenu de lecran du jeu
    def build(self):
        self.orientation = 'vertical'
        self.spacing = 20
        self.Mes_Boutons()
        # On cree un bouton:
        self.Bouton_Menu = Button(text='Retour au menu', size_hint=(0.4, 0.4))
        self.Bouton_Menu.bind(on_press=self.Vers_Menu)
        # On ajoute le bouton dans l'affichage:
        self.add_widget(self.Bouton_Menu)

    def Mes_Boutons(self):
        # On cree une liste pour les boutons:
        self.Dico_Boutons = {}
        # On fait tourner une boucle pour creer 10 boutons:
        for classe in Dico:  # J'en suis ici (Attention aux "i" qui n'est plus à jour)
            if classe[0] == "S":
                # On ajoute un bouton dans la liste:
                self.Dico_Boutons[classe] = Button()
                # On lui donne un texte qui depend de i:
                self.Dico_Boutons[classe].text = classe
                self.Dico_Boutons[classe].id = classe
                # On lui associe une fonction:
                self.Dico_Boutons[classe].bind(on_press=self.VersClasse)
                # On ajoute le bouton au layout principal:
                self.add_widget(self.Dico_Boutons[classe])

    def VersClasse(self, instance):
        ClasseEnCours.clear()
        ClasseEnCours.append(instance.id)
        print(ClasseEnCours)
        sm.current = ClasseEnCours[0] + " P"

    # Une fonction pour aller a l'ecran du menu:
    def Vers_Menu(self, instance):
        sm.current = 'Menu P'


"""
******************************************************************
Premiere
******************************************************************
"""


class PremiereScreenP(Screen):  # Le deuxieme ecran : Premiere
    def build(self):
        self.name = 'Premiere P'
        Premiere_Layout = PremiereP()  # On creer le contenu
        Premiere_Layout.build()
        self.add_widget(Premiere_Layout)  # On ajoute le contenu dans l'ecran
        sm.add_widget(self)  # On ajoute l'ecran menu dans le ScreenManager

class PremiereP(BoxLayout):  # Le contenu de lecran du jeu
    def build(self):
        self.orientation = 'vertical'
        self.spacing = 20
        self.Mes_Boutons()
        # On cree un bouton:
        self.Bouton_Menu = Button(text='Retour au menu', size_hint=(0.4, 0.4))
        self.Bouton_Menu.bind(on_press=self.Vers_Menu)
        # On ajoute le bouton dans l'affichage:
        self.add_widget(self.Bouton_Menu)

    def Mes_Boutons(self):
        # On cree une liste pour les boutons:
        self.Dico_Boutons = {}
        # On fait tourner une boucle pour creer 10 boutons:
        for classe in Dico:  # J'en suis ici (Attention aux "i" qui n'est plus à jour)
            if classe[0] == "1":
                # On ajoute un bouton dans la liste:
                self.Dico_Boutons[classe] = Button()
                # On lui donne un texte qui depend de i:
                self.Dico_Boutons[classe].text = classe
                self.Dico_Boutons[classe].id = classe
                # On lui associe une fonction:
                self.Dico_Boutons[classe].bind(on_press=self.VersClasse)
                # On ajoute le bouton au layout principal:
                self.add_widget(self.Dico_Boutons[classe])

    def VersClasse(self, instance):
        ClasseEnCours.clear()
        ClasseEnCours.append(instance.id)
        print(ClasseEnCours)
        sm.current = ClasseEnCours[0] + " P"

    # Une fonction pour aller a l'ecran du menu:
    def Vers_Menu(self, instance):
        sm.current = 'Menu P'


"""
************************************************************************
Terminales
*************************************************************************
"""


class TerminaleScreenP(Screen):  # Le deuxieme ecran : Terminale
    def build(self):
        self.name = 'Terminale P'
        Terminale_Layout = TerminaleP()  # On creer le contenu
        Terminale_Layout.build()
        self.add_widget(Terminale_Layout)  # On ajoute le contenu dans l'ecran
        sm.add_widget(self)  # On ajoute l'ecran menu dans le ScreenManager

class TerminaleP(BoxLayout):  # Le contenu de lecran du jeu
    def build(self):
        self.orientation = 'vertical'
        self.spacing = 20
        self.Mes_Boutons()
        # On cree un bouton:
        self.Bouton_Menu = Button(text='Retour au menu', size_hint=(0.4, 0.4))
        self.Bouton_Menu.bind(on_press=self.Vers_Menu)
        # On ajoute le bouton dans l'affichage:
        self.add_widget(self.Bouton_Menu)

    def Mes_Boutons(self):
        # On cree une liste pour les boutons:
        self.Dico_Boutons = {}
        # On fait tourner une boucle pour creer 10 boutons:
        for classe in Dico:  # J'en suis ici (Attention aux "i" qui n'est plus à jour)
            if classe[0] == "T":
                # On ajoute un bouton dans la liste:
                self.Dico_Boutons[classe] = Button()
                # On lui donne un texte qui depend de i:
                self.Dico_Boutons[classe].text = classe
                self.Dico_Boutons[classe].id = classe
                # On lui associe une fonction:
                self.Dico_Boutons[classe].bind(on_press=self.VersClasse)
                # On ajoute le bouton au layout principal:
                self.add_widget(self.Dico_Boutons[classe])

    def VersClasse(self, instance):
        ClasseEnCours.clear()
        ClasseEnCours.append(instance.id)
        print(ClasseEnCours)
        sm.current = ClasseEnCours[0] + " P"

    # Une fonction pour aller a l'ecran du menu:
    def Vers_Menu(self, instance):
        sm.current = 'Menu P'




"""
*************************************************************************
Fenêtres Classe
**************************************************************************
"""

class ClasseScreenP(Screen):  # Le deuxieme ecran : Seconde
    def build(self, name):
        self.name = name + " P"
        classegroslayout = ClasseGrosLayoutP()
        classegroslayout.build(name)
        self.add_widget(classegroslayout)
        sm.add_widget(self)  # On ajoute l'ecran menu dans le ScreenManager

class PlanClasseP(FloatLayout):
    def build(self, name):
        self.data = name
        if checkToday(name):
            self.Liste = self.LireListeSave(name)
        else:
            self.Liste = listenum(Dico[name])
            self.SaveListe(name)
        print(self.Liste)
        StampToday(name)
        self.Mes_Boutons()

    def LireListeSave(self,name):
        path = os.getcwd()
        os.chdir("Sauvegarde")
        L = []
        with open(name + ".csv", 'r') as file:
            cr = csv.reader(file)
            for row in cr:
                L.append(row)
        os.chdir(path)
        return L

    def SaveListe(self,name):
        L = self.Liste
        path = os.getcwd()
        os.chdir("Sauvegarde")
        with open(name + ".csv", 'w') as file:
            for i in range(0, len(L) - 1):

                j = "{}".format(L[i][0]) + "," + "{}".format(L[i][1])
                file.write(j)
                if i != len(L) - 2:
                    file.write("\n")
        os.chdir(path)



    """
    
    Taille fenetre : en x environ 25 - 1300
                     en y environ 100 - 800
    Taille Boutton : size_hint 0.1,0.04
                     Espacement horizontal: 145
                     Espacement vertical : 150
                     
    """

    def Mes_Boutons(self):

        self.Liste_Boutons = []
        N = len(self.Liste)
        Taille_Max_Classe = 35
        PosX = [15,160,305,585,730,1010,1155,1300]
        PosY = [200,350,500,650,800]
        j = 0
        k = 0
        for i in range(0,N):
            self.Liste_Boutons.append(Button())
            self.Liste_Boutons[i].text = self.Liste[i][0] + " " + self.Liste[i][1][1]
            self.Liste_Boutons[i].size_hint = [0.1,0.04]
            print(j,k)
            self.Liste_Boutons[i].pos = [PosX[j],PosY[k]]
            j = j + 1
            if j > len(PosX) - 1 :
                j = 0
                k = k + 1
            self.add_widget(self.Liste_Boutons[i])

class ClasseGrosLayoutP(BoxLayout):
    def build(self, name):
        self.data = name
        self.orientation = "vertical"
        self.spacing = 10
        boutonsEtLabel = BoutonsEtLabelClasseP()
        boutonsEtLabel.build(name)
        self.add_widget(boutonsEtLabel)
        ClassePlan = PlanClasseP()
        ClassePlan.build(name)
        self.add_widget(ClassePlan)

class BoutonsEtLabelClasseP(BoxLayout):
    def build(self, name):
        self.data = name
        self.orientation = "horizontal"
        self.size_hint = (1, .1)
        self.Bouton_Menu = Button(text='Retour au menu')
        self.Bouton_Menu.bind(on_press=self.Vers_Menu)
        # On ajoute le bouton dans l'affichage:
        self.add_widget(self.Bouton_Menu)
        self.MotifButton = Button()
        self.MotifButton.text = "Vers les motifs"
        self.MotifButton.id = "Motif"
        self.MotifButton.bind(on_press=self.VersMotif)
        self.add_widget(self.MotifButton)
        self.add_widget(DicoLabelP[self.data])

    def VersMotif(self, instance):
        print(ClasseEnCours)
        #sm.current = 'Motifs'
        # Une fonction pour aller a l'ecran du menu:

    def Vers_Menu(self, instance):
        sm.current = 'Menu P'





"""
***************************************************************************************
Application
**************************************************************************************
"""


class ScreenAppP(App):

    def build(self):
        MenuP = MenuScreenP()  # On definit l'ecran menu
        MenuP.build()  # On le construit
        ClasseDicoP = {}
        for classe in Dico:
            ClasseDicoP[classe] = ClasseScreenP()
            ClasseDicoP[classe].build(classe)

        TerminaleP = TerminaleScreenP()  # On definit l'ecran jeu
        TerminaleP.build()  # On le construit
        PremiereP = PremiereScreenP()  # On définit l'écran premiere
        PremiereP.build()  # On le construit
        SecondeP = SecondeScreenP()  # On définit l'écran seconde
        SecondeP.build()  # On le construit
        sm.current = 'Menu P'  # On envoie en premier l'ecran du menu grace a son nom
        return sm


if __name__ == '__main__':
    ScreenAppP().run()








