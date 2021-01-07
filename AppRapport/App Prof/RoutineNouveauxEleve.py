import sqlite3
conn = sqlite3.connect("Eleve.db")
cursor = conn.cursor()
Classe = input("Entrer la classe de l'élève").upper()
Nom = input("Entrer le nom de l'élève (Fin si vous voulez vous arréter")

while Nom.upper() != "FIN":
    Prenom = input("Entrer le prénom")
    Sexe = input("Entrer le genre de l'élève : H/F").upper()
    cursor.execute("INSERT INTO Eleve (Nom,Prenom,Classe,Sexe,Bavardages,ChangePlace,Materiel,Dort,CasquetteBonjour,Animaux,DevoirNonFaits,Retourne,ParleFort,FaitRire,Repond,RefuseCarnet,PasCarnet,Internet,Rigole) VALUES ('{}','{}','{}','{}',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);".format(Nom,Prenom,Classe,Sexe))

conn.close()