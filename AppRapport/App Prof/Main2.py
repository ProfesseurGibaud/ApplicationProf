from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from PyPDF2 import PdfFileMerger
from copy import *
import os
import sqlite3
import csv
from Rapport import *
from FonctionPdf import *
import random
from datetime import *
from FonctionRapport import *

#Permet d'écrire la date
def today():
    D = datetime.today()
    return str(D.day) + " " + str(D.month) + " " + str(D.year)

#Vérifie que la date correspond à aujourd'hui
def checkToday(str):
    booleen = False
    path = os.getcwd()
    os.chdir("Date")
    try:
        with open(str + ".txt", 'r') as file:
            test = file.read()
            if test == today():
                booleen = True
    except:
        print("Rien pour le moment")
    os.chdir(path)
    return booleen

#Permet d'écrire dans un texte la date
def StampToday(str):
    import os
    path = os.getcwd()
    os.chdir("Date")
    with open(str + ".txt", 'w') as file:
        file.write(today())
    os.chdir(path)


def dossier():
    import os
    os.chdir(r"C:\Users\Sylgi\Desktop\Python Temp\ApplicationProf\AppRapport\App Prof")


# dossier()


def DicoVersListeNomPrenom(DicoClasse):
    Liste = []
    for nom in DicoClasse:
        TempListe = [DicoClasse[nom]["Nom"], DicoClasse[nom]["Prenom"]]
        Liste.append(TempListe)
    return Liste

#Fonction de Lecture de CSV pour placer les places du plan de classe
def LireListeCsvInt(str):
    with open(str + ".txt") as file:
        r = csv.reader(file)
        L = []
        LL = []
        for row in r:
            L.append(row)
        for i in L[0]:
            LL.append(int(i))
    return LL


#Permet de mélanger les noms d'une lise (comme un rd.shuffle mais une des premières fonctions de mes élèves)
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

"""

Paquet de petite fonctions utiles de manipulation de fichiers

"""

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


def Merge():
    print("Merge")
    list = os.listdir()
    pdfs = []
    for item in list:
        if item[len(item) - 4:] == ".pdf":
            pdfs.append(item)
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("Rapports Condensé.pdf")


def SalleW(Room):
    with open("Salle.txt", "w") as Salle:
        Salle.write(Room)


def PrepLabel(DicoLabel, str):
    DicoLabel[str] = Label(text=str)
    return DicoLabel

"""

Lecture et Modification Base de Données

"""


def LireCSVversDico(string): #Fonction intermediaire pour avoir un dico modifiable
    path = os.getcwd()
    os.chdir("Classes")
    with open(string + ".csv","r") as file:
        reader = csv.DictReader(file)
        DicoEleve = {} # Chaque item sera un dico
        for row in reader:
            DicoEleve[dict(row)["Nom"]] = dict(row)
    os.chdir(path)
    return DicoEleve

#On va charger toutes les listes de toutes les classes
def BDD_Vers_DicoClasse():
    conn = sqlite3.connect('Eleve.db')
    conn.row_factory = sqlite3.Row
    Dico = {}
    DicoEleve = {}
    cursor = conn.cursor()
    cursor2 = conn.cursor()
    cursor.execute("""SELECT nom FROM Classe""")
    for classe in cursor:
        nomclasse = classe[0]
        print(nomclasse)
        DicoEleve.clear()
        cursor2.execute("SELECT * FROM Eleve WHERE Classe = '{}'".format(nomclasse))
        Eleves = cursor2.fetchall()
        for eleve in Eleves:
            DicoEleve[dict(eleve)["Nom"]] = dict(eleve)
        Dico[nomclasse] = DicoEleve
        Dico = deepcopy(Dico)
    return Dico




def CSV_Vers_DicoClasse():
    # On va charger toutes les listes de toutes les classes.
    Dico = {}
    tempdico = {}
    path = os.getcwd()
    TempListe = []
    os.chdir("Classes")
    for classe in os.listdir():
        nomclasse = classe[:len(classe) - 4]
        print(nomclasse)
        # TempListe.clear()
        tempdico.clear()
        os.chdir(path)
        tempdico = LireCSVversDico(nomclasse)  #tempDico est un dico pour un élève
        Dico[nomclasse] = tempdico
        Dico = deepcopy(Dico)

    return Dico



def restart():
    ListePunis = []  # liste avec les noms des punis
    ListeNomPunis = []
    ListePrenomPunis = []
    Rappo = []
    Feuille = []  # Tester .set
    ListeMotifs = []
    ClasseEnCours = []
    ListeSeconde = []
    StrW("EleveEnCours", "0")
    labelmotif = Label(text=str(ListeMotifs))
    Prof = Label()
    Salle = Label()
    TexteMotif = ""
    TextInputVerif = TextInput()
    CompteurRapport = 0
    LabelEleve = Label()
    # ListeSeconde = CSV_Vers_ListeSeconde(ListeSeconde)
    #Dico = CSV_Vers_DicoClasse()
    Dico = BDD_Vers_DicoClasse()
    TextInputSanction = TextInput()
    TextInputPunition = TextInput()
    DicoLabel = {}
    LabelPunisSeconde = {}
    for classe in Dico:
        LabelPunisSeconde = PrepLabel(DicoLabel, classe)
    return [ListePunis, ListeNomPunis, ListePrenomPunis, Rappo, Feuille, ListeMotifs, ClasseEnCours, LabelPunisSeconde,
            labelmotif, TexteMotif, TextInputVerif, CompteurRapport, LabelEleve, ListeSeconde, Salle, Prof, Dico,
            DicoLabel, TextInputSanction, TextInputPunition]


[ListePunis, ListeNomPunis, ListePrenomPunis, Rappo, Feuille, ListeMotifs, ClasseEnCours, LabelPunisSeconde, labelmotif,
 TexteMotif, TextInputVerif, CompteurRapport, LabelEleve, ListeSeconde, Salle, Prof, Dico, DicoLabel, TextInputSanction,
 TextInputPunition] = restart()


def restartP():
    ListePunis = []  # liste avec les noms des punis
    ListeNomPunis = []
    ListePrenomPunis = []
    Rappo = []
    Feuille = []  # Tester .set
    ListeMotifs = []
    ClasseEnCours = []
    ListeSeconde = []
    StrW("EleveEnCours", "0")
    labelmotifP = Label(text=str(ListeMotifs))
    ProfP = Label()
    SalleP = Label()
    TexteMotif = ""
    TextInputVerifP = TextInput()
    CompteurRapport = 0
    LabelEleveP = Label()
    # ListeSeconde = CSV_Vers_ListeSeconde(ListeSeconde)
    Dico = BDD_Vers_DicoClasse()
    #Dico = CSV_Vers_DicoClasse()
    TextInputSanctionP = TextInput()
    TextInputPunitionP = TextInput()
    DicoLabelP = {}
    LabelPunisSecondeP = {}
    for classe in Dico:
        LabelPunisSecondeP = PrepLabel(DicoLabelP, classe)
    return [ListePunis, ListeNomPunis, ListePrenomPunis, Rappo, Feuille, ListeMotifs, ClasseEnCours, LabelPunisSecondeP,
            labelmotifP, TexteMotif, TextInputVerifP, CompteurRapport, LabelEleveP, ListeSeconde, SalleP, ProfP, Dico,
            DicoLabelP, TextInputSanctionP, TextInputPunitionP]


[ListePunis, ListeNomPunis, ListePrenomPunis, Rappo, Feuille, ListeMotifs, ClasseEnCours, LabelPunisSecondeP,
 labelmotifP, TexteMotif, TextInputVerifP, CompteurRapport, LabelEleveP, ListeSeconde, SalleP, ProfP, Dico, DicoLabelP,
 TextInputSanctionP, TextInputPunitionP] = restartP()

sm = ScreenManager()  # Create the screen manager, il est forcement global


# On construit 4 ecrans : Un Menu et un ecran par classe
class MenuScreen(Screen):
    def build(self):
        # Le nom de l'ecran
        self.name = 'Menu'
        # On cree le contenu:
        Menu_Layout = BoxLayout(padding=20, spacing=10, orientation='vertical')

        MiniLayout = BoxLayout(padding=20, spacing=10, orientation="horizontal")
        Prof.text = "Professeur : " + StrR("Professeur")
        MiniLayout.add_widget(Prof)

        Salle.text = "Lieu : " + StrR("Salle")
        MiniLayout.add_widget(Salle)

        Menu_Layout.add_widget(MiniLayout)
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

        self.Bouton_PlanDeClasse = Button(text="Plan De Classe")
        self.Bouton_PlanDeClasse.background_color = [0, 1, 0, 1]
        self.Bouton_PlanDeClasse.bind(on_press=self.VersPlanDeClasse)
        Menu_Layout.add_widget(self.Bouton_PlanDeClasse)

        self.Bouton_Outils = Button(text="Outils/ Paramètre")
        self.Bouton_Outils.background_color = [1, 0, 0, 1]
        self.Bouton_Outils.bind(on_press=self.Vers_Outils)
        Menu_Layout.add_widget(self.Bouton_Outils)

        sm.add_widget(self)

    # Une fonction pour aller aux écrans des classes :
    def Vers_Seconde(self, instance):
        sm.current = 'Seconde'

    def Vers_Premiere(self, instance):
        sm.current = 'Premiere'

    def Vers_Terminale(self, instance):
        sm.current = 'Terminale'

    def Vers_Outils(self, instance):
        sm.current = 'Outils'

    def VersPlanDeClasse(self, instance):
        sm.current = 'Menu P'


class OutilsScreen(Screen):
    def build(self):
        # Le nom de l'ecran
        self.name = 'Outils'
        print(self.name)
        # On cree le contenu:
        Outils_Layout = GridLayout(padding=20, spacing=10, cols=2)
        self.NouveauNomProf = TextInput(text="Nouveau Prof")
        Outils_Layout.add_widget(self.NouveauNomProf)
        self.BoutonNomProf = Button(text="Changer Nom Prof")
        self.BoutonNomProf.bind(on_press=self.ChangerNomProf)
        Outils_Layout.add_widget(self.BoutonNomProf)

        self.NouveauLieu = TextInput(text="Nouveau Lieu")
        Outils_Layout.add_widget(self.NouveauLieu)
        self.BoutonLieu = Button(text="Changer Lieu")
        self.BoutonLieu.bind(on_press=self.ChangerLieu)
        Outils_Layout.add_widget(self.BoutonLieu)

        self.BoutonMerge = Button(text="Merge")
        self.BoutonMerge.bind(on_press=self.Merge)
        Outils_Layout.add_widget(self.BoutonMerge)

        self.Bouton_Menu = Button(text="Menu")
        self.Bouton_Menu.bind(on_press=self.Vers_Menu)
        Outils_Layout.add_widget(self.Bouton_Menu)

        self.add_widget(Outils_Layout)
        sm.add_widget(self)

    def ChangerNomProf(self, instance):
        StrW("Professeur", self.NouveauNomProf.text)
        Prof.text = StrR("Professeur")

    def Vers_Menu(self, instance):
        sm.current = "Menu"

    def Merge(self, instance):
        Merge()

    def ChangerLieu(self, instance):
        SalleW(self.NouveauLieu.text)
        Salle.text = StrR("Salle")


"""
*********************************************************
Seconde
*********************************************************
"""


class SecondeScreen(Screen):  # Le deuxieme ecran : Seconde
    def build(self):
        self.name = 'Seconde'
        Seconde_Layout = Seconde()  # On creer le contenu
        Seconde_Layout.build()
        self.add_widget(Seconde_Layout)  # On ajoute le contenu dans l'ecran
        sm.add_widget(self)  # On ajoute l'ecran menu dans le ScreenManager


class Seconde(BoxLayout):  # Le contenu de lecran du jeu
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
        ListePunis.clear()
        ListeNomPunis.clear()
        ListePrenomPunis.clear()
        ClasseEnCours.clear()
        ClasseEnCours.append(instance.id)
        print(ClasseEnCours)
        sm.current = ClasseEnCours[0]

    # Une fonction pour aller a l'ecran du menu:
    def Vers_Menu(self, instance):
        sm.current = 'Menu'


"""
******************************************************************
Premiere
******************************************v************************
"""


class PremiereScreen(Screen):  # Le deuxieme ecran : Premiere
    def build(self):
        self.name = 'Premiere'
        Premiere_Layout = Premiere()  # On creer le contenu
        Premiere_Layout.build()
        self.add_widget(Premiere_Layout)  # On ajoute le contenu dans l'ecran
        sm.add_widget(self)  # On ajoute l'ecran menu dans le ScreenManager


class Premiere(BoxLayout):  # Le contenu de lecran du jeu
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
        ListePunis.clear()
        ListeNomPunis.clear()
        ListePrenomPunis.clear()
        ClasseEnCours.clear()
        ClasseEnCours.append(instance.id)
        print(ClasseEnCours)
        sm.current = ClasseEnCours[0]

    # Une fonction pour aller a l'ecran du menu:
    def Vers_Menu(self, instance):
        sm.current = 'Menu'


"""
************************************************************************
Terminales
*************************************************************************
"""


class TerminaleScreen(Screen):  # Le deuxieme ecran : Terminale
    def build(self):
        self.name = 'Terminale'
        Terminale_Layout = Terminale()  # On creer le contenu
        Terminale_Layout.build()
        self.add_widget(Terminale_Layout)  # On ajoute le contenu dans l'ecran
        sm.add_widget(self)  # On ajoute l'ecran menu dans le ScreenManager


class Terminale(BoxLayout):  # Le contenu de lecran du jeu
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
        ListePunis.clear()
        ListeNomPunis.clear()
        ListePrenomPunis.clear()
        ClasseEnCours.clear()
        ClasseEnCours.append(instance.id)
        print(ClasseEnCours)
        sm.current = ClasseEnCours[0]

    # Une fonction pour aller a l'ecran du menu:
    def Vers_Menu(self, instance):
        sm.current = 'Menu'


"""
*************************************************************
Motifs
*************************************************************
"""


class MotifsScreen(Screen):  # Le deuxieme ecran : Seconde
    def build(self):
        self.name = 'Motifs'
        motifgroslayout = MotifGrosLayout()
        motifgroslayout.build()
        self.add_widget(motifgroslayout)
        # Seconde8_Layout=Seconde8()#On creer le contenu
        # Seconde8_Layout.build()
        # self.add_widget(Seconde8_Layout)#On ajoute le contenu dans l'ecran
        sm.add_widget(self)  # On ajoute l'ecran menu dans le ScreenManager


class BoutonsEtLabelMotif(BoxLayout):
    def build(self):
        self.orientation = "horizontal"
        self.size_hint = (1, .1)
        self.Bouton_Retour = Button(text='Retour aux élèves')
        self.Bouton_Retour.bind(on_press=self.Vers_Retour)
        # On ajoute le bouton dans l'affichage:
        self.add_widget(self.Bouton_Retour)
        self.VerificationButton = Button()
        self.VerificationButton.text = "Vérification"
        self.VerificationButton.id = "Vérification"
        self.VerificationButton.bind(on_press=self.VersVerification)
        self.add_widget(self.VerificationButton)
        self.add_widget(labelmotif)

    def VersVerification(self, instance):
        print("Vérification")
        Rappo.clear()
        for i in range(len(ListePunis)):
            Rappo.append(Rapport())
            Rappo[i].prof = StrR("Professeur")
            Rappo[i].lieu = StrR("Salle")
            Rappo[i].data = []
            Rappo[i].nom = ListeNomPunis[i]
            Rappo[i].prenom = ListePrenomPunis[i]
            Rappo[i].classe = ClasseEnCours[0]
            Rappo[i].motif = Rappo[i].FaireMotif(ListeMotifs)
            Rappo[i].punition = "Pour Information" * (len(ListeMotifs) == 1) + "{0} heures de colle".format(
                len(ListeMotifs) - 1) * (len(ListeMotifs) > 1)
            for motif in ListeMotifs:
                MAJ_Eleve(ListeNomPunis[i], ClasseEnCours[0], motif)
            print(Rappo[i].punition)
        EleveEnCours = 0
        Feuille = []
        print(Rappo)
        LabelEleve.text = ListePrenomPunis[EleveEnCours]
        TextInputVerif.text = Rappo[EleveEnCours].motif
        TextInputPunition.text = Rappo[EleveEnCours].punition
        TextInputSanction.text = Rappo[EleveEnCours].sanction
        sm.current = 'Vérification'

        # Une fonction pour aller a l'ecran du menu:

    def Vers_Retour(self, instance):
        print(ClasseEnCours[0])
        sm.current = ClasseEnCours[0]


class MotifGrosLayout(BoxLayout):
    def build(self):
        self.orientation = "vertical"
        self.spacing = 10
        boutonsEtLabelMotif = BoutonsEtLabelMotif()
        boutonsEtLabelMotif.build()
        self.add_widget(boutonsEtLabelMotif)
        MotifScroll = ScrollMotif()
        MotifScroll.build()
        self.add_widget(MotifScroll)


class Motif(GridLayout):  # Le contenu de lecran du jeu
    def build(self):
        self.cols = 1
        self.row_default_height = 60
        self.size_hint_y = None
        # self.size_hint_y = None
        self.orientation = 'vertical'
        self.spacing = 20
        self.bind(minimum_height=self.setter('height'))
        self.Mes_Boutons()
        self.ListeMotifs = []
        # On cree un bouton:

    def Mes_Boutons(self):
        # On cree une liste pour les boutons:
        self.Liste_Boutons = []
        self.ListeMotifs = []
        # On fait tourner une boucle pour creer 10 boutons:

        try:
            cr = csv.reader(open("Motifs.csv", "r"))
            for row in cr:
                self.ListeMotifs.append(row[0])
            taille = len(self.ListeMotifs)
        except IOError:
            print("Erreur! Le fichier n' pas pu être ouvert")
        for i in range(0, taille):
            # On ajoute un bouton dans la liste:
            self.Liste_Boutons.append(Button())
            # On lui donne un texte qui depend de i:
            self.Liste_Boutons[i].text = self.ListeMotifs[i]
            # On lui donne un identite "id" pour le retrouver hors de la liste:
            self.Liste_Boutons[i].id = self.ListeMotifs[i]
            # On lui associe une fonction:
            self.Liste_Boutons[i].bind(on_press=self.AddMotifs)
            # On ajoute le bouton au layout principal:
            self.add_widget(self.Liste_Boutons[i])

    def AddMotifs(self, instance):
        print(instance.id)
        print(ListeMotifs)
        # labelmotif.text_size = (self.width, self.height)
        if ListeMotifs.count(instance.id) > 0:
            print("on enlève")
            ListeMotifs.remove(instance.id)
            instance.background_color = [0.5, 0.5, 0.5, 1]
            labelmotif.text = str(ListeMotifs)
        else:
            print("on enleve pas")
            instance.background_color = [1, 0, 0, 1]  # En rouge
            ListeMotifs.append(instance.id)
            if len(ListeMotifs) < 3:
                labelmotif.text = str(ListeMotifs)
            else:
                labelmotif.text = "Trop de Motifs pour affichage"
        print(ListeMotifs)


class ScrollMotif(ScrollView):
    def build(self):
        self.size_hint = (1, None)
        self.size_hint_y = 0.8
        Motiff = Motif()
        Motiff.build()
        self.add_widget(Motiff)


"""
*******************************************************************
Ecran Vérification
*******************************************************************
"""


class VerifScreen(Screen):  # Le deuxieme ecran : Seconde
    def build(self):
        self.name = 'Vérification'
        verifgroslayout = VerifGrosLayout()
        verifgroslayout.build()
        self.add_widget(verifgroslayout)
        sm.add_widget(self)  # On ajoute l'ecran menu dans le ScreenManager


class BoutonsEtLabelVerif(BoxLayout):
    def build(self):
        self.orientation = "horizontal"
        self.size_hint = (1, 15)
        self.Bouton_Retour = Button(text='Retour aux motifs')
        self.Bouton_Retour.bind(on_press=self.Vers_Retour)
        # On ajoute le bouton dans l'affichage:
        self.add_widget(self.Bouton_Retour)
        self.RapportButton = Button()
        self.RapportButton.text = "Faire Rapports"
        self.RapportButton.id = "Faire Rapports"
        self.RapportButton.bind(on_press=self.FaireRapport)
        self.add_widget(self.RapportButton)
        self.add_widget(LabelEleve)
        self.Rappo = Rappo
        self.EleveEnCours = 0

    def FaireRapport(self, instance):
        self.EleveEnCours = IntR("EleveEnCours")
        Rappo[self.EleveEnCours].motif = TextInputVerif.text
        Rappo[self.EleveEnCours].sanction = TextInputSanction.text
        Rappo[self.EleveEnCours].punition = TextInputPunition.text

        if self.EleveEnCours < len(Rappo):
            Feuille.append(FonctionPdf(Rappo[self.EleveEnCours]))
            Feuille[self.EleveEnCours].go()
            LabelEleve.text = ListePrenomPunis[self.EleveEnCours]
            TextInputVerif.text = Rappo[self.EleveEnCours].motif
            TextInputSanction.text = Rappo[self.EleveEnCours].sanction
            TextInputPunition.text = Rappo[self.EleveEnCours].punition

            StrW("EleveEnCours", self.EleveEnCours + 1)
            self.EleveEnCours = IntR("EleveEnCours")

            if self.EleveEnCours < len(Rappo):
                LabelEleve.text = Rappo[self.EleveEnCours].prenom
                TextInputVerif.text = Rappo[self.EleveEnCours].motif
                TextInputSanction.text = Rappo[self.EleveEnCours].sanction
                TextInputPunition.text = Rappo[self.EleveEnCours].punition
            if self.EleveEnCours >= len(Rappo):
                StrW("EleveEnCours", 0)
                sm.current = "Finish"
                print("Pas d'autre Eleve")

    def Vers_Retour(self, instance):
        StrW("EleveEnCours", 0)
        sm.current = "Motifs"


class VerifGrosLayout(BoxLayout):
    def build(self):
        self.orientation = "vertical"
        self.spacing = 10
        boutonsEtLabelVerif = BoutonsEtLabelVerif()
        boutonsEtLabelVerif.build()
        self.add_widget(boutonsEtLabelVerif)

        PunitionLayout = BoxLayout(padding=20, spacing=10, orientation="horizontal", size_hint_y=10)
        PunitionLabel = Label(text="Punition donné par l'enseignant : ")
        PunitionLayout.add_widget(PunitionLabel)
        PunitionLayout.add_widget(TextInputPunition)
        self.add_widget(PunitionLayout)

        SanctionLayout = BoxLayout(padding=20, spacing=10, orientation="horizontal", size_hint_y=10)
        SanctionLabel = Label(text="Sanction demandée par l'enseignant : ")
        SanctionLayout.add_widget(SanctionLabel)
        SanctionLayout.add_widget(TextInputSanction)
        self.add_widget(SanctionLayout)

        Veriff = Verif()
        Veriff.build()
        self.add_widget(Veriff)


class Verif(BoxLayout):  # Le contenu de lecran du jeu
    def build(self):
        self.cols = 1
        self.size_hint_y = 50
        # self.size_hint_y = None
        self.orientation = 'vertical'
        self.spacing = 20
        self.add_widget(TextInputVerif)


"""
************************************************************
Finish (Donner le nombre de Rapports Ecrits (Sans Tricher))
************************************************************
"""


class FinishScreen(Screen):
    def build(self):
        # Le nom de l'ecran
        self.name = 'Finish'
        # On cree le contenu:
        Finish_Layout = BoxLayout(padding=20, spacing=10, orientation='vertical')
        # On cree le label:
        self.Finish_Label = Label(text="C'est Fini", font_size=30, color=[1, 0, 0, 1])
        Finish_Layout.add_widget(self.Finish_Label)

        # On cree le bouton retour:
        self.Bouton_Menu = Button(text='Vers le menu')
        self.Bouton_Menu.bind(on_press=self.Vers_Menu)
        # On ajoute le bouton dans l'affichage:
        Finish_Layout.add_widget(self.Bouton_Menu)

        # On ajoute le Layout dans l'ecran de menu
        self.add_widget(Finish_Layout)
        # On ajoute l'ecran menu dans le ScreenManager:
        sm.add_widget(self)

    def Vers_Menu(self, instance):
        # ScreenApp().stop()
        sm.current = 'Menu'


"""
*************************************************************************
Fenêtres Classe
**************************************************************************
"""


class ClasseScreen(Screen):  # Le deuxieme ecran : Seconde
    def build(self, name):
        self.name = name
        classegroslayout = ClasseGrosLayout()
        classegroslayout.build(name)
        self.add_widget(classegroslayout)
        sm.add_widget(self)  # On ajoute l'ecran menu dans le ScreenManager


class ScrollClasse(ScrollView):
    def build(self, name):
        self.data = name
        self.size_hint = (1, None)
        self.size_hint_y = 0.8
        GridLayoutClasse = ClasseGridLayout()
        GridLayoutClasse.build(name)
        self.add_widget(GridLayoutClasse)


class ClasseGrosLayout(BoxLayout):
    def build(self, name):
        self.data = name
        self.orientation = "vertical"
        self.spacing = 10
        boutonsEtLabel = BoutonsEtLabelClasse()
        boutonsEtLabel.build(name)
        self.add_widget(boutonsEtLabel)
        ClasseScroll = ScrollClasse()
        ClasseScroll.build(name)
        self.add_widget(ClasseScroll)


class BoutonsEtLabelClasse(BoxLayout):
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
        self.add_widget(DicoLabel[self.data])

    def VersMotif(self, instance):
        print(ClasseEnCours)
        sm.current = 'Motifs'

        # Une fonction pour aller a l'ecran du menu:

    def Vers_Menu(self, instance):
        sm.current = 'Menu'


class ClasseGridLayout(GridLayout):  # Le contenu de lecran du jeu
    def build(self, name):
        self.data = name
        self.cols = 1
        self.row_default_height = 60
        self.size_hint_y = None
        # self.size_hint_y = None
        self.orientation = 'vertical'
        self.spacing = 20
        self.bind(minimum_height=self.setter('height'))
        self.ListeAPunir = []
        self.Liste = DicoVersListeNomPrenom(Dico[name])
        self.Mes_Boutons()
        # On cree un bouton:

    def Mes_Boutons(self):
        # On cree une liste pour les boutons:
        self.Liste_Boutons = []
        # On fait tourner une boucle pour creer 10 boutons:

        for i in range(0, len(self.Liste)):
            # On ajoute un bouton dans la liste:
            self.Liste_Boutons.append(Button())
            # On lui donne un texte qui depend de i:
            self.Liste_Boutons[i].text = self.Liste[i][0] + " " + self.Liste[i][1]
            # On lui donne un identite "id" pour le retrouver hors de la liste:
            self.Liste_Boutons[i].id = str(i)
            self.Liste_Boutons[i].size_hint_y = (1, 0.4)
            self.Liste_Boutons[i].background_color = [0.5, 0.5, 0.5, 1]
            # On lui associe une fonction:
            self.Liste_Boutons[i].bind(on_press=self.APunir)
            # On ajoute le bouton au layout principal:
            self.add_widget(self.Liste_Boutons[i])

    def APunir(self, instance):
        print(ListePrenomPunis)
        # label.text_size = (self.width, self.height)
        if instance.id in ListePunis:
            print("Remove")
            print(ListePunis)
            ListePunis.remove(instance.id)
            print(ListePunis)
            print(ListePrenomPunis)
            print(self.Liste[int(instance.id)][0])
            print("Remove from Liste Punis. Vers Liste Prenom")
            ListePrenomPunis.remove(self.Liste[int(instance.id)][1])
            ListeNomPunis.remove(self.Liste[int(instance.id)][0])
            instance.background_color = [0.5, 0.5, 0.5, 1]
        else:
            print("Add")
            instance.background_color = [1, 0, 0, 1]
            ListePunis.append(instance.id)
            ListePrenomPunis.append(self.Liste[int(instance.id)][1])
            ListeNomPunis.append(self.Liste[int(instance.id)][0])
            print(ListePrenomPunis)
        if len(ListeNomPunis) < 5:
            LabelPunisSeconde[ClasseEnCours[0]].text = str(ListePrenomPunis)
        else:
            LabelPunisSeconde[iClasseEnCours[0]].text = "Trop de prénoms pour affichage"


"""
**************************************************************************************************
Plan de Classe
**************************************************************************************************

"""


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
Fenêtres Classe Plan
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
            self.Liste = DicoVersListeNomPrenom(Dico[name])
            self.Liste = listenum(self.Liste)
            self.SaveListe(name)
        print(self.Liste)
        StampToday(name)
        self.Mes_Boutons()

    def LireListeSave(self, name):
        path = os.getcwd()
        os.chdir("Sauvegarde")
        L = []
        with open(name + ".csv", 'r') as file:
            cr = csv.reader(file)
            for row in cr:
                L.append(row)
        os.chdir(path)
        return L

    def SaveListe(self, name):
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
        PosX = LireListeCsvInt("PosX")
        PosY = LireListeCsvInt("PosY")
        j = 0
        k = 0
        for i in range(0, N):
            self.Liste_Boutons.append(Button())
            self.Liste_Boutons[i].text = self.Liste[i][1] + " " + self.Liste[i][0][0]
            self.Liste_Boutons[i].size_hint = [0.1, 0.04]
            print(j, k)
            self.Liste_Boutons[i].pos = [PosX[j], PosY[k]]
            j = j + 1
            if j > len(PosX) - 1:
                j = 0
                k = k + 1
            self.Liste_Boutons[i].id = str(i)
            self.Liste_Boutons[i].background_color = [1, 1, 1, 1]
            # On lui associe une fonction:
            self.Liste_Boutons[i].bind(on_press=self.APunir)
            # On ajoute le bouton au layout principal:
            self.add_widget(self.Liste_Boutons[i])

        Tableau = Button(text="Tableau")
        Tableau.size_hint = [0.3, 0.12]
        Tableau.pos = [500, 50]
        self.add_widget(Tableau)

        Couloir = Button(text="Coté Couloir")
        Couloir.size_hint = [0.15, 0.08]
        Couloir.pos = [1225, 50]
        self.add_widget(Couloir)

        Fenetre = Button(text="Coté Fenêtre")
        Fenetre.size_hint = [0.15, 0.08]
        Fenetre.pos = [15, 50]
        self.add_widget(Fenetre)

    def APunir(self, instance):
        print(ListePrenomPunis)
        # label.text_size = (self.width, self.height)
        if instance.id in ListePunis:
            print("Remove")
            ListePunis.remove(instance.id)
            ListePrenomPunis.remove(self.Liste[int(instance.id)][1])
            ListeNomPunis.remove(self.Liste[int(instance.id)][0])
            instance.background_color = [1, 1, 1, 1]
        else:
            print("Add")
            instance.background_color = [1, 0, 0, 1]
            ListePunis.append(instance.id)
            ListePrenomPunis.append(self.Liste[int(instance.id)][1])
            ListeNomPunis.append(self.Liste[int(instance.id)][0])
            print(ListePrenomPunis)
        if len(ListeNomPunis) < 5:
            LabelPunisSecondeP[ClasseEnCours[0]].text = str(ListePrenomPunis)
        else:
            LabelPunisSecondeP[iClasseEnCours[0]].text = "Trop de prénoms pour affichage"


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
        sm.current = 'Motifs'

    def Vers_Menu(self, instance):
        sm.current = 'Menu P'


"""
****************************************************************************
Application
****************************************************************************
"""


class ScreenApp(App):

    def build(self):
        Menu = MenuScreen()  # On definit l'ecran menu
        Menu.build()  # On le construit
        Motif = MotifsScreen()
        Motif.build()
        Finish = FinishScreen()
        Finish.build()
        Verif = VerifScreen()
        Verif.build()
        Tools = OutilsScreen()
        Tools.build()
        ClasseDico = {}
        for classe in Dico:
            ClasseDico[classe] = ClasseScreen()
            ClasseDico[classe].build(classe)
        Terminale = TerminaleScreen()  # On definit l'ecran jeu
        Terminale.build()  # On le construit
        Premiere = PremiereScreen()  # On définit l'écran premiere
        Premiere.build()  # On le construit
        Seconde = SecondeScreen()  # On définit l'écran seconde
        Seconde.build()  # On le construit

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

        sm.current = 'Menu'  # On envoie en premier l'ecran du menu grace a son nom
        return sm


ScreenApp().run()
