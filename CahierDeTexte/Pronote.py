#! /usr/bin/env python3
# coding: utf-8
#=======================================================================
#
#  Script python pour coller les notes et apprÃ©ciations sur PRONOTE
#  d'aprÃ¨s une colonne de tableur.
#
#  Parameters
#  ----------
#
#    - identifiants de connexion
#    - nom du navigateur
#      si firefox :
#       - rÃ©pertoire du driver gecko
#       - chemin vers l'exÃ©cutable firefox
#
#  Dependencies
#  ------------
#
#    - python standard library:
#        os, sys, time      (system)
#        textwrap           (text)
#        tkinter            (GUI)
#        selenium           (webbrowser interaction)
#
#  History
#  --------
#
#    0.1.1 - 09/01/2021 : adaptation Ã  la nouvelle grille de pronote
#            pour coller notes et apprÃ©ciations.
#
#    0.1.0 - 08/05/2019 : intÃ©gration de nouvelles URL pour diffÃ©rents
#            lycÃ©es et modification des modes de connexion associÃ©s
#            selon que l'on doive passer par un ENT ou non.
#
#    0.0.9 - 16/01/2019Â : correction d'un bug pour la saisie des
#            apprÃ©ciations.
#
#    0.0.8 - 30/11/2018Â : ajout d'une fonction supprimant le fichier log
#            du driver gecko en fin d'exÃ©cution.
#
#    0.0.7 - 12/11/2018Â : correction d'un bug de sÃ©lection avec
#            "active_element" avec selenium >=3.7.
#
#    0.0.6 - 18/10/2018 : correction du collage en cours (pb de type !)
#
#    0.0.5 - 17/10/2018 : correction de la condition de chargement et
#            ajout de la possibilitÃ© de coller Â«Â en cours de listeÂ Â».
#
#    0.0.4 - 18/01/2018 : ajout d'une condition de chargement pour la
#            connexion automatique permettant de s'adapter aux
#            connexions lentes.
#
#    0.0.3 - 16/12/2017 : correction d'une coquille dans la fonction
#            notes.
#
#    0.0.2 - 14/12/2017 : correction de la fonction pour coller les
#            apprÃ©ciations.
#
#    0.0.1 - 09/10/2017 (first release)
#
#
#  Copyright (c) 2017-2019 by Nicolas Mesnier <nmesnier@free.fr>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 or
#  above as published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#=======================================================================
# *** TO EDIT ***
#
# *** Identifiants de connexion
login="sylvain.gibaud"
password="Opmlki123"
# connexion automatique au lancement de l'application
AutoConnect=True

# *** Navigateur internet
#
# navigateur in ["firefox", "chrome", "internet explorer", "safari"]
navigateur='chrome'
#  Si firefox, Ã©diter les deux noms :
#    exe_navigateur="chemin absolu vers l'Ã©xÃ©cutabel firefox"
#    repertoire_plugin="rÃ©pertoire du plugin"
#  - GNU/Linux 64 bits
exe_navigateur=r"C:\Driver\chromedriver.exe"
repertoire_plugin=r"C:\Users\Sylgi\Desktop\Python Temp\ApplicationProf\CahierDeTexte"
#  - MAC OS X
# exe_navigateur= '/Applications/Firefox.app/Contents/MacOS/firefox'
# repertoire_plugin='/home/$(whoami)/pronote'
#  - MS Windows 64 bits
# exe_navigateur='C:\\Program Files\\Mozilla Firefox\\firefox.exe'
# repertoire_plugin='C:\\pronote'

# *** URL
REGION = ""
URL={"ENT":"", "ENT_login":"", "pronote":""}
#  DÃ©commenter quelques lignes ci-dessous en fonction de votre lycÃ©e ou
#  ajoutez vos URL de connexion Ã  pronote, si besoin passant par un ENT.
#  - LycÃ©e Jules Ferry, Versailles
REGION = "IDF"
URL["ENT"] = "https://ent.iledefrance.fr"
URL["ENT_login"] = "https://ent.iledefrance.fr/auth/login"
URL["pronote"] = "https://0782565p.index-education.net/pronote/"
#  - LycÃ©e Gustave Eiffel, Dijon
# REGION = "BFC"
# URL["ARENA"] = "https://bv.ac-dijon.fr"
# URL["IPROF"] = "https://bv.ac-dijon.fr/iprof/ServletIprof"
# URL["ENT"] = "https://cas.eclat-bfc.fr"
# URL["ENT_login"] = URL["ARENA"]
# URL["pronote"] = "https://0211033j.index-education.net/pronote/professeur.html"

#  - LycÃ©e Jean Perrin, Lyona
#REGION = "AURA"
#URL["ARENA"] = "https://portail.ac-lyon.fr"
#URL["IPROF"] = "https://portail.ac-lyon.fr/iprof/servletiprofe"
#URL["ENT"] = "https://ent.auvergnerhonealpes.fr/"
#URL["ENT_login"] = "https://cas.ent.auvergnerhonealpes.fr"
#URL["pronote"] = "https://0690082p.index-education.net/pronote/professeur.html"

#=======================================================================
# *** Packages
#=======================================================================
import os
import sys
import time
import textwrap
# *** GUI
import tkinter as Tk
# *** gestion du navigateur
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# *** navigateur web
if navigateur.lower()=='firefox':
# Ressources:
#   https://github.com/mozilla/geckodriver/releases
#   http://testerstories.com/2016/09/dance-of-the-automation-marionette/
#   https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver

    if os.pathsep+repertoire_plugin not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep+repertoire_plugin
    if os.pathsep+os.path.dirname(exe_navigateur) not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep+os.path.dirname(exe_navigateur)
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities["marionette"] = True
    firefox_capabilities['binary'] = exe_navigateur
    browser = webdriver.Firefox(capabilities=firefox_capabilities)

elif navigateur.lower()=="safari":# << non testÃ©
    browser = webdriver.Safari()
elif navigateur.lower()=="chrome":# << non testÃ©
    browser = webdriver.chrome()
elif navigateur.lower()=="internet explorer":# << non testÃ©
    browser = webdriver.ie()

##======================================================================
# *** Fonctions
#=======================================================================
def pressepapier():
    """
    Copie le presse papier et renvoie une liste.
    """
    tk = Tk.Tk()
    tk.withdraw()
    text = tk.clipboard_get()
    tk.destroy()
    notes=text.split("\n")
    return(notes[:-1])

def connexion():
    """
    Se connecte Ã  l'ENT ou Ã  pronote si les identifiants sont donnÃ©s
    en paramÃ¨tres, sinon ouvre la page de connexion.
    """
    if URL["ENT_login"]!="":
        browser.get(URL["ENT_login"])
        # on ajoute un cookie en AURA
        if REGION == "AURA"
            browser.add_cookie({
                "name":"preselection",
                "value":"LYON-AAA_enseignant" })
            browser.get(URL["ENT_login"])
            c = browser.find_elements(By.XPATH,"//input[@id='button-submit']")
            c[0].send_keys(Keys.ENTER)
    elif URL["pronote"]!="":
        browser.get(URL["pronote"])
    if len(login)>0 and len(password)>0:
        # check if page loaded (in place of a "time.sleep(1)")
        try:
            timeout = 30 # (s)
            if URL["ENT_login"]!="":
                if REGION in ["BFC", "AURA"]:
                    IDfield = "user"
                else:
                    IDfield = "email"
                WebDriverWait(browser, timeout).until(EC.element_to_be_clickable(
                    (By.XPATH,"//input[@name='"+IDfield+"']")
                    ))
                c = browser.find_elements(By.XPATH,"//input[@name='"+IDfield+"']")
                c[0].send_keys(login)
                c = browser.find_elements(By.XPATH,"//input[@name='password']")
                c[0].send_keys(password)
                c[0].send_keys(Keys.ENTER)
            elif URL["pronote"]!="":
                WebDriverWait(browser, timeout).until(EC.element_to_be_clickable(
                    (By.XPATH,"//input[@id='id_53']")
                    ))
                c = browser.find_elements(By.XPATH,"//input[@id='id_53']")
                c[0].send_keys(login)
                c = browser.find_elements(By.XPATH,"//input[@id='id_54']")
                c[0].send_keys(password)
                c[0].send_keys(Keys.ENTER)
        except TimeoutException:
            print("Timed out waiting for page to load.")
            print("Try a manual connection.")

def supprimer_navigateur_logfile():
    tmpfile="geckodriver.log"
    if os.path.isfile(tmpfile):
        os.remove(tmpfile)

def coller_Notes():
    """\
    1) sÃ©lectionner Â« Notes > Saisie des notes Â»
    2) sÃ©lectionner Â« CrÃ©er un devoir Â»
    3) une fois la colonne du tableau affichÃ©e,
       placer le curseur sur la premiÃ¨re note Ã  coller
    4) coller les notes du presse-papier
    5) vÃ©rifier la saisie puis l'enregistrer
    """
    notes = pressepapier()
    for k in range(len(notes)):
        e=browser.switch_to.active_element
        e.clear()
        e.send_keys(notes[k], Keys.ENTER)

def coller_Apps():
    """\
    1) sÃ©lectionner Â« Bulletins > Saisie des apprÃ©ciations Â»
    2) une fois le tableau affichÃ©,
       placer le curseur sur la premiÃ¨re apprÃ©ciation Ã  coller
    3) coller les apprÃ©ciations du presse-papier
    4) vÃ©rifier la saisie puis l'enregistrer
    """
    apps = pressepapier()
    for k in range(len(apps)):
        a=browser.switch_to.active_element
        a.send_keys(apps[k], Keys.TAB)
        time.sleep(1)

#=======================================================================
# *** Interface graphique
#=======================================================================
buttonwidth=25
textwidth=40
textwraplength=280
class Interface():
    def __init__(self, master, **kw):
        master.wm_title("tab2pronote")# titre
        if URL["ENT"]!="":
            master.wm_geometry("300x800")
        else:
            master.wm_geometry("300x650")
        self.master=master
        master.mainframe = Tk.Frame(master,borderwidth=0)
        master.mainframe.pack(side='top',padx=0, pady=0,
            fill=Tk.BOTH,expand=1)
        master.update()
        master.geometry(master.geometry())

        Frame1 = Tk.Frame(master.mainframe, borderwidth=0,
            relief=Tk.RAISED)
        Frame1.pack(side=Tk.TOP,fill=Tk.X)
        if not AutoConnect:# ajout d'un bouton de connexion
            if URL["ENT"]!="":
                Tk.Button(master=Frame1,
                    text="Connexion Ã  l'ENT",
                    command=connexion,
                    width=buttonwidth).pack(side='top',pady=2)
            else:
                Tk.Button(master=Frame1,
                    text="Connexion",
                    command=connexion,
                    width=buttonwidth).pack(side='top',pady=2)
        if URL["ENT"]!="":
            if URL["ARENA"]!="":
                Tk.Button(master=Frame1,
                    text="ARENA",
                    command=lambda : browser.get(URL["ARENA"]),
                    width=buttonwidth).pack(side='top',pady=5)
            if URL["IPROF"]!="":
                Tk.Button(master=Frame1,
                    text="I-Prof",
                    command=lambda : browser.get(URL["IPROF"]),
                    width=buttonwidth).pack(side='top',pady=5)

            Tk.Button(master=Frame1,
                text="ENT",
                command=lambda : browser.get(URL["ENT"]),
                width=buttonwidth).pack(side='top',pady=5)
            Tk.Button(Frame1,
                text="PRONOTE",
                command=lambda : browser.get(URL["pronote"]),
                width=buttonwidth).pack(side='top',pady=5)

        if URL["ENT"]!="":
            Frame2 = Tk.LabelFrame(master.mainframe, borderwidth=1,
                relief=Tk.GROOVE,
                text="Notes (depuis PRONOTE)",padx=5,pady=5)
        else:
            Frame2 = Tk.LabelFrame(master.mainframe, borderwidth=1,
                relief=Tk.GROOVE,
                text="Notes",padx=5,pady=5)
        Frame2.pack(side=Tk.TOP,fill=Tk.X,expand=1)

        Tk.Label(Frame2,
            text=textwrap.dedent(coller_Notes.__doc__),
            width=textwidth,justify=Tk.LEFT,wraplength=textwraplength
            ).pack(side='top',pady=5)
        Tk.Button(Frame2,
            text="Coller les notes",
            command=coller_Notes,
            width=buttonwidth).pack(side='top',pady=5)

        if URL["ENT"]!="":
            Frame3 = Tk.LabelFrame(master.mainframe, borderwidth=1,
                relief=Tk.GROOVE,
                text="ApprÃ©ciations (depuis PRONOTE)",padx=5,pady=5)
        else:
            Frame3 = Tk.LabelFrame(master.mainframe, borderwidth=1,
                relief=Tk.GROOVE,
                text="ApprÃ©ciations",padx=5,pady=5)
        Frame3.pack(side=Tk.TOP,fill=Tk.X,expand=1)

        Tk.Label(Frame3,
            text=coller_Apps.__doc__,
            width=textwidth,justify=Tk.LEFT,wraplength=textwraplength
            ).pack(side='top',pady=5)
        Tk.Button(Frame3,
            text="Coller les apprÃ©ciations",
            command=coller_Apps,
            width=buttonwidth).pack(side='top',pady=5)

        Frame4 = Tk.Frame(master.mainframe, borderwidth=0,
            relief=Tk.GROOVE,height=20)
        Frame4.pack(side=Tk.TOP,fill=Tk.BOTH)
        if URL["ENT"]!="":
            Tk.Label(master=Frame4,
                text="Se dÃ©connecter de l'ENT",
                width=buttonwidth).pack(side='top',pady=2)
        else:
            Tk.Label(master=Frame4,
                text="Se dÃ©connecter de PRONOTE",
                width=buttonwidth).pack(side='top',pady=2)
        Tk.Button(master=Frame4,
            text="Quitter",
            command=self.quitter,
            width=buttonwidth).pack(side='top',pady=2)
        Tk.Label(Frame4, text="Â© 2017-2021, N. Mesnier").pack(anchor="s")
        Tk.Label(Frame4, text="GNU GPL v3 (or above)").pack()
        # connexion automatique au site
        if AutoConnect:
            connexion()

    def quitter(self):
        browser.close()
        supprimer_navigateur_logfile()
        self.master.destroy()

if __name__ == "__main__":
    root = Tk.Tk()
    app = Interface(root)
    root.mainloop()

#====================================================================eof