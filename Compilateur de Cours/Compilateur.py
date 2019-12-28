import os
import codecs
def dossier():
    os.chdir("Google Drive//Python//Compilateur de Cours")
dossier()
os.chdir("Test")

with codecs.open("NC1.tex","r", encoding = 'utf-8') as file:
    d = file.read()

with codecs.open("test.tex","w",encoding = 'utf-8') as file:
    file.write(d)