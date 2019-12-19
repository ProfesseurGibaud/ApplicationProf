import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm,inch
from datetime import date,datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_config import defaultPageSize
from reportlab.lib.styles import getSampleStyleSheet
from FonctionRapport import *
from GenerateurPhrase import * 

class Rapport:
    def __init__(self):
        self.nom = "Macron"
        self.data = []
        self.prenom = "Eleve"
        self.classe = "TES2"
        self.motif = ("Paragraph number %s." % 4) *1000
        self.hoy = date.today()
        self.hour = datetime.now().hour
        self.minute = datetime.now().minute
        self.punition = "Pour Information"
        self.sanction = ""
        self.lieu = "Salle 306"
        self.prof = "Gibaud"
        self.matiere = "Mathématiques"
        self.demande = ""
        self.y = 27
    
    
    def FaireMotif(self,ListeMotifs):
        string = TexteMotif(self.classe,self.nom,ListeMotifs)
        return string
    
    def update(self):
        print("à faire")
    def Appliquer(self,CCanvas):
        y = self.y * cm
        x = 1 * cm
        CCanvas.setFont("Helvetica",12)
        CCanvas.drawString(x,y,"Professeur : "+ self.prof)
        CCanvas.drawString(x,y-2*cm, "Lieu : "+self.lieu)
        CCanvas.drawString(x, y-1*cm, "Matière : "+self.matiere)
        CCanvas.drawString(x,y-3*cm, "Date : " + str(self.hoy.day) +"/" + str(self.hoy.month) + " à " + str(self.hour) +"h"+str(self.minute))
        CCanvas.drawRightString(21*cm,y, "Eleve : "+self.prenom + " " + self.nom)
        CCanvas.drawRightString(21*cm,y - 1*cm,"Classe : "  + self.classe)
        CCanvas.drawString(x,y-4*cm, "Motif : " + self.motif)
