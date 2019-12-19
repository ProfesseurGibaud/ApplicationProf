import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm,inch,mm
from datetime import date
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak,Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_config import defaultPageSize
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet

def dossier():
    import os
    os.chdir("Google Drive//Python//App Rapport//Application Rapport")
#dossier()

from Rapport import *




class FonctionPdf:
    
    def __init__(self,rapport):
        self.PageHeight = defaultPageSize[1]
        self.PageWidth = defaultPageSize[0]
        self.styles = getSampleStyleSheet()
        self.Title = "Rapport d'Incident" 
        self.rapport = rapport
        self.NomEleve = self.rapport.prenom + " " + self.rapport.nom
        self.pageinfo = "Rapport d'incident du " + str(rapport.hoy.day) + "/" + str(rapport.hoy.month) + "/" + str(rapport.hoy.year) + " de " + self.NomEleve


    def myFirstPage(self,canvas,doc):
        canvas.saveState()
        canvas.drawImage("Logo.png", 10,24*cm)
        canvas.setFont('Times-Bold',20)
        canvas.drawCentredString(1 * self.PageWidth/2,self.PageHeight - 30,self.Title)
        canvas.setFont('Helvetica',9)
        canvas.drawString(inch, 0.75*inch, "Page 1 / %s" % self.pageinfo)
        canvas.setFont("Helvetica",12)
        x = 3*cm
        y = self.PageHeight - 8*cm
        canvas.drawString(x,y,"Professeur : "+ self.rapport.prof)
        canvas.drawString(x,y-2*cm, "Lieu : "+self.rapport.lieu)
        canvas.drawString(x, y-1*cm, "Matière : "+self.rapport.matiere)
        canvas.drawString(x,y-3*cm, "Date : " + str(self.rapport.hoy.day) +"/" + str(self.rapport.hoy.month) + "/" + str(self.rapport.hoy.year) + " à " + str(self.rapport.hour) + "h" + str(self.rapport.minute))
        canvas.drawRightString(20*cm,y, "Eleve : "+self.rapport.prenom + " " + self.rapport.nom)
        canvas.drawRightString(20*cm,y - 1*cm,"Classe : "  + self.rapport.classe)
        canvas.drawString(x, y - 4*cm, "Punition demandée par l'enseignant : " + self.rapport.punition)
        canvas.drawString(x, y - 5*cm, "Sanction demandée par l'enseignant : " + self.rapport.sanction)
        canvas.drawString(x, y - 6*cm, "Décision de la Direction, ou du CPE : " )
        canvas.drawString(x, y - 8*cm, "Motifs : ")
        canvas.restoreState()
    
    def myLaterPages(self,canvas,doc):
        canvas.saveState()
        canvas.setFont('Helvetica',9)
        canvas.drawString(inch,0.75*inch, "Page %d %s" %(doc.page, self.pageinfo))
        canvas.restoreState()
        
    def go(self):
        path  = os.getcwd()
        os.chdir("..")
        os.chdir("Rapports")
        doc = SimpleDocTemplate(self.NomEleve + " le " + str(self.rapport.hoy.day) + "-" + str(self.rapport.hoy.month) + " à " + str(self.rapport.hour) +  "h" + str(self.rapport.minute) +  ".pdf")
        Story = [Spacer(1,14*cm)]
        style = self.styles["Normal"]
        p = Paragraph(self.rapport.motif,style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))
        doc.build(Story, onFirstPage = self.myFirstPage, onLaterPages = self.myLaterPages)
        #logo.drawOn(doc,100,100)
        os.chdir(path)
        
        
        
def test():
    Ro = Rapport()
    PP = FonctionPdf(Ro)
    PP.go()