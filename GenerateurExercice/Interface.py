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
from kivy.properties import ObjectProperty,ListProperty,StringProperty,NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.cache import Cache
from kivy.uix.slider import Slider


from GeneExoClass import *


"""


Kivy Implémentation



"""



Titre = "Devoir de Rattrapage de "
Auteur = "S. Gibaud"
Date = "18 Novembre"
Classe = "Terminale"
ZeroOuUn = 1

TType = ["D\\'eveloppement", "In\\'equation", "Equation", "Tableaux de Variation", "Fraction",
         "Equation de Droite du Plan", "Proba"]
DDifficulte = ["Facile", "Moyen", "Dur"]
CClasse = ["Seconde", "Premiere", "Terminale"]
TTType = ["Développement", "Inéquation", "Equation", "Tableaux de Variation", "Fraction", "Equation de Droites du Plan",
          "Proba"]


def TransTType2TTType(t):
    i = TType.index(t)
    return TTType[i]


def IntR(fichier):
    with open(fichier + ".txt") as file:
        n = int(file.read())
    return n


sm = ScreenManager()


class SliderTypeDiff(GridLayout):
    def __init__(self, type, difficulte):
        super(SliderTypeDiff, self).__init__()
        self.type = type
        self.difficulte = difficulte
        self.cols = 4
        self.nombre = Slider(min=0, max=30, value=0)
        # 1st row - one label, one slider
        self.add_widget(Label(text=difficulte))
        self.add_widget(self.nombre)
        # 2nd row - one label for caption,
        # one label for slider value
        self.add_widget(Label(text="Nombre d'Exos"))
        self.labelnombre = Label(text='0')
        self.add_widget(self.labelnombre)
        # On the slider object Attach a callback
        # for the attribute named value
        self.nombre.bind(value=self.on_value)

    # Adding functionality behind the slider
    # i.e when pressed increase the value
    def on_value(self, instance, babar):
        self.labelnombre.text = "% d" % babar
        DicoExo[self.type][self.difficulte] = int(babar)
        updateLabel()

    # The app class


class OptionScreen(Screen):
    def build(self):
        # Le nom de l'ecran
        self.name = 'Options'
        # On cree le contenu:
        Option_Layout = GridLayout(padding=20, spacing=10, cols=2)
        self.NouveauTitre = TextInput(text=StrR("Titre"))
        Option_Layout.add_widget(self.NouveauTitre)
        self.BoutonNouveauTitre = Button(text="Changer Titre")
        self.BoutonNouveauTitre.bind(on_press=self.changertitre)
        Option_Layout.add_widget(self.BoutonNouveauTitre)
        self.NouveauNomProf = TextInput(text=StrR("Auteur"))
        Option_Layout.add_widget(self.NouveauNomProf)
        self.BoutonNomProf = Button(text="Mettre Nom Prof")
        self.BoutonNomProf.bind(on_press=self.ChangerNomProf)
        Option_Layout.add_widget(self.BoutonNomProf)
        self.NouvelleClasse = TextInput(text=StrR("Classe"))
        Option_Layout.add_widget(self.NouvelleClasse)
        self.BoutonClasse = Button(text="Changer (Seconde, Premiere, Terminale)")
        self.BoutonClasse.bind(on_press=self.ChangerClasse)
        Option_Layout.add_widget(self.BoutonClasse)
        self.NouvelleDate = TextInput(text="Date de retour")
        Option_Layout.add_widget(self.NouvelleDate)
        self.BoutonDate = Button(text="Changer Date de Retour")
        self.BoutonDate.bind(on_press=self.ChangerDate)
        Option_Layout.add_widget(self.BoutonDate)
        self.NouvelleCorrection = TextInput(text=StrR("ZeroOuUn"))
        Option_Layout.add_widget(self.NouvelleCorrection)
        self.BoutonCorrection = Button(text="Changer Correction : Avec = 1, Sans = 0")
        self.BoutonCorrection.bind(on_press=self.ChangerCorrection)
        Option_Layout.add_widget(self.BoutonCorrection)

        self.BoutonRetour = Button(text="Retour")
        self.BoutonRetour.bind(on_press=self.Retour)
        Option_Layout.add_widget(self.BoutonRetour)

        self.add_widget(Option_Layout)
        sm.add_widget(self)

    def ChangerNomProf(self, instance):
        StrW("Auteur", self.NouveauNomProf.text)
        Auteur = StrR("Auteur")

    def changertitre(self, instance):
        StrW("Titre", self.NouveauTitre.text)
        Titre = StrR("Titre")

    def ChangerClasse(self, instance):
        StrW("Classe", self.NouvelleClasse.text)
        Classe = StrR("Auteur")

    def ChangerDate(self, instance):
        StrW("Date", self.NouvelleDate.text)
        Date = StrR("Date")

    def ChangerCorrection(self, instance):
        StrW("ZeroOuUn", self.NouvelleCorrection.text)
        ZeroOuUn = IntR("ZeroOuUn")

    def Retour(self, instance):
        sm.current = "Acceuil"




DicoExo = {}
DicoSlider = {}
DicoLabel = {}
DicoLabel2 = {}
for ttype in TType:
    DicoExo[ttype] = {}
    DicoSlider[ttype] = {}
    for difficulte in DDifficulte:
        DicoExo[ttype][difficulte] = 0
        DicoSlider[ttype][difficulte] = SliderTypeDiff(ttype, difficulte)
    DicoLabel[ttype] = Label(text="Quantité = " + str(DicoNombre(DicoExo[ttype])))
    DicoLabel2[ttype] = Label(text=str(DicoNombre(DicoExo[ttype])), size_hint_x=0.1)
for difficulte in DDifficulte:
    DicoExo["Proba"][difficulte] = 0
    DicoExo["Equation de Droite du Plan"][difficulte] = 0


def updateLabel():
    for ttype in TType:
        DicoLabel[ttype].text = "Quantité = " + str(DicoNombre(DicoExo[ttype]))
        DicoLabel2[ttype].text = str(DicoNombre(DicoExo[ttype]))


updateLabel()


class EcranOption(Screen):
    def build(self):
        pass


class EcranType(Screen):
    def build(self, type):
        self.name = type
        self.type = type
        self.tttype = TransTType2TTType(self.type)
        layout = BoxLayout(orientation="vertical")
        PremierLayout = BoxLayout(orientation="horizontal")
        BoutonRetour = Button(text="Retour")
        BoutonRetour.bind(on_press=self.VersDebut)
        PremierLayout.add_widget(BoutonRetour)
        PremierLayout.add_widget(Label(text=self.tttype))
        PremierLayout.add_widget(DicoLabel[self.type])
        layout.add_widget(PremierLayout)
        for difficulte in DDifficulte:
            layout.add_widget(DicoSlider[self.type][difficulte])
        self.add_widget(layout)
        sm.add_widget(self)

    def VersDebut(self, instance):
        sm.current = "Acceuil"


class EcranAcceuil(Screen):
    def build(self):
        self.name = "Acceuil"
        GrosLayout = BoxLayout(orientation="vertical")
        TitreEcran = Label(text="Générateur d'Exercice")
        TitreEcran.size_hint_y = 0.3
        GrosLayout.add_widget(TitreEcran)
        EnDessousLayout = GridLayout(cols=3)
        GaucheLayout = GridLayout(cols=2)
        self.DicoBouton = {}
        for ttype in TType:  # J'en suis ici Faire les lignes Un bouton Un Total
            self.DicoBouton[ttype] = Button(text=TransTType2TTType(ttype), id=ttype)
            self.DicoBouton[ttype].bind(on_press=self.VersType)
            GaucheLayout.add_widget(self.DicoBouton[ttype])
            GaucheLayout.add_widget(DicoLabel2[ttype])
        EnDessousLayout.add_widget(GaucheLayout)
        EnDessousLayout.add_widget(Label())
        DroiteLayout = BoxLayout(orientation="vertical")
        GeneBoutton = Button(text="Génerer les Exercices", id="Gene")
        GeneBoutton.bind(on_press=self.GenererExo)
        DroiteLayout.add_widget(GeneBoutton)
        OptionBouton = Button(text="Options", id="Options")
        OptionBouton.bind(on_press=self.VersOption)
        DroiteLayout.add_widget(OptionBouton)
        EnDessousLayout.add_widget(DroiteLayout)
        GrosLayout.add_widget(EnDessousLayout)
        self.add_widget(GrosLayout)
        sm.add_widget(self)

    def VersOption(self, instance):
        sm.current = "Options"

    def VersType(self, instance):
        sm.current = instance.id

    def GenererExo(self, instance):
        DevoirComplet(DicoExo, Titre, Auteur, Date, Classe,ZeroOuUn)


class SliderExample(App):
    def build(self):
        DicoEcran = {}
        for ttype in TType:
            DicoEcran[ttype] = EcranType()
            DicoEcran[ttype].build(ttype)
        EcranAccceuil = EcranAcceuil()
        EcranAccceuil.build()
        OptionScreeen = OptionScreen()
        OptionScreeen.build()

        sm.current = "Acceuil"
        return sm

    # creating the object root for ButtonApp() class

root = SliderExample()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.


root.run()
