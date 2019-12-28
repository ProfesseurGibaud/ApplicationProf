import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import os

def dossier():
    os.chdir("Google Drive//Python//Google Form//Google Form treatment")

dossier()

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

sheetDebut = client.open("Questionnaire Gibaud Debut (réponses)").sheet1
sheetFin = client.open("Questionnaire Gibaud Fin (réponses)").sheet1

dataDebut = sheetDebut.get_all_records()
dataFin = sheetFin.get_all_records()


"""
Les Data sont des listes (chaque item de la liste est une ligne)
Chaque item est un dictionnaire.


Dico : Clé Nom Défini Nombre d'apparition

"""

pprint(dataDebut[5].values())