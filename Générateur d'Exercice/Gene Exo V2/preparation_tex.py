import os

preambule = "\documentclass{article}"
preambule += "\n \\usepackage[utf8]{inputenc}"
preambule += "\n  \\title{Devoir de Rattrapage}"
preambule += "\n  \date{A rendre pour le mardi 10 Octobre 8h}" 
preambule += "\\usepackage{natbib} \n \\usepackage{graphicx} \n \\usepackage{amsmath} \n \\usepackage{mathtools}"
preambule += "\\begin{document}"
preambule += "\maketitle"

for fichier in os.listdir("fichier_exo"):
    with open(f"fichier_exo/{fichier}","r") as file:
        texte = file.read()
    nouveau_texte = preambule + texte + "\end{document}"
    with open(f"fichier_tex/{fichier}".replace(".txt",'.tex'),"w+") as file:
        file.write(nouveau_texte)