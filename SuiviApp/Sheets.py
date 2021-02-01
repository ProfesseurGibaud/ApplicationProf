import gspread

from oauth2client.service_account import ServiceAccountCredentials

from pprint import pprint

import datetime

import os

import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

from kivy.app import App

from kivy.uix.image import Image

from kivy.uix.gridlayout import GridLayout

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label
import PIL



if os.getcwd != r"C:\Users\Sylgi\Desktop\Python Temp\ApplicationProf\SuiviApp":
    os.chdir(r"C:\Users\Sylgi\Desktop\Python Temp\ApplicationProf\SuiviApp")

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]



creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)



client = gspread.authorize(creds)



sheetDebut = client.open("Questionnaire Gibaud Debut (réponses)").sheet1

sheetFin = client.open("Questionnaire Gibaud Fin (réponses)").sheet1



dataDebut = sheetDebut.get_all_records()

dataFin = sheetFin.get_all_records()



ListeQuestionDebut = ["Quelle est votre classe ?","Notez vos efforts dans VOTRE TRAVAIL À LA MAISON de hier soir.","Avez vous besoin de poser des questions à M. Gibaud aujourd'hui ?","À quel point comptez vous vous investir EN CLASSE d'aujourd'hui ?"]







"""

Les Data sont des listes (chaque item de la liste est une ligne)

Chaque item est un dictionnaire.





Dico : Clé Nom Défini Nombre d'apparition



"""









pprint(dataDebut[5].values())



"{:02d}".format(datetime.datetime.now().day)



dateGoogleDrive = "03/10/2019 10:17:01"



day = "{:02d}".format(datetime.datetime.now().day)

month = "{:02d}".format(datetime.datetime.now().month)

year = "{:02d}".format(datetime.datetime.now().year)

hour = "{:02d}".format(datetime.datetime.now().hour)

minute = "{:02d}".format(datetime.datetime.now().minute)


"""
day = "{:02d}".format(3)

month = "{:02d}".format(10)

year = "{:02d}".format(2019)

hour = "{:02d}".format(10)

minute = "{:02d}".format(17)
"""




HorodateurNow = day + "/" + month + "/" + year + ' ' + hour



# Tester si tous les noms sont dans la même classe



for item in dataDebut:

    if HorodateurNow in item["Horodateur"]:

        print(item[ListeQuestionDebut[0]].upper())



Invest = []

Question = []

Maison = []

for item in dataDebut:

    Invest.append(item[ListeQuestionDebut[-1]])

    Question.append(item[ListeQuestionDebut[2]])

    Maison.append(item[ListeQuestionDebut[1]])





"""

Investissement

"""

plt.clf()

CountInvest = [Invest.count(1),Invest.count(2),Invest.count(3),Invest.count(4),Invest.count(5),Invest.count(6)]



labels = '1', '2', '3', '4','5','6'

colors = ['red','yellowgreen', 'gold', 'grey', 'lightcoral','lightskyblue']



plt.pie(CountInvest, labels=labels, colors=colors,

        autopct='%1.1f%%', shadow=False, startangle=90)

plt.axis('equal')
plt.suptitle("Investissement",fontsize = 16)
plt.savefig("Pictures/Invest.png")



"""

Maison

"""

plt.clf()

CountMaison = [Maison.count(1),Maison.count(2),Maison.count(3),Maison.count(4),Maison.count(5),Maison.count(6)]

labels = '1', '2', '3', '4','5','6'

colors = ['red','yellowgreen', 'gold', 'grey', 'lightcoral','lightskyblue']





plt.pie(CountMaison, labels=labels, colors=colors,

        autopct='%1.1f%%', shadow=False, startangle=90)

plt.axis('equal')
plt.suptitle("Maison",fontsize = 16)
plt.savefig("Pictures/Maison.png")



"""

Question

"""
plt.clf()
plt.rcParams["figure.figsize"] = (1, 5)


CountQuestion = Question.count("Oui")/len(Question)

currentAxis = plt.gca()
k = 1
currentAxis.add_patch(Rectangle((0,0), k, CountQuestion*k,alpha=1,color = "Green"))
plt.suptitle("Question",fontsize = 16)
plt.savefig("Pictures/Question.png")
imgg = PIL.Image.open("Pictures/Question.png")
width, height = imgg.size
new_width = width/5
new_height = height
left = (width - new_width)/2
top = (height - new_height)/2
right = (width + new_width)/2
bottom = (height + new_height)/2

# Crop the center of the image
imgg = imgg.crop((left, top, right, bottom))

imgg.save("Pictures/Question.png")





"""



Modifier dans MatPlotLib : Mettre Titre dessin dans chaque dessin.



Allonger Barre Jauge





Effacer 3 noms de layout



"""













class ScreenApp(App):

    def build(self):

        Grid = GridLayout()

        Grid.cols = 1

        TextLayout = GridLayout()

        TextLayout.cols = 2

        TextLayout.size_hint_y = 0.1

        labelAbsent = Label(text = "Absents : ")

        labelFauxPresent = Label(text = "Error")

        TextLayout.add_widget(labelAbsent)

        TextLayout.add_widget(labelFauxPresent)

        Grid.add_widget(TextLayout)

        GridBas = GridLayout()

        GridBas.cols = 3

        QuestionLayout = GridLayout()

        QuestionLayout.cols = 1


        QuestionImage = Image(source = "Pictures/Question.png")
        QuestionLayout.size_hint_x = 0.2
        QuestionLayout.add_widget(QuestionImage)

        GridBas.add_widget(QuestionLayout)

        MaisonLayout = GridLayout(cols = 1)


        MaisonLayout.add_widget(Image(source = "Pictures/Maison.png"))

        GridBas.add_widget(MaisonLayout)

        InvestLayout = GridLayout(cols=1)

        InvestLayout.add_widget(Image(source="Pictures/Invest.png"))

        GridBas.add_widget(InvestLayout)











        Grid.add_widget(GridBas)





        return Grid



ScreenApp().run()

