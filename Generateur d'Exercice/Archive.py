import sympy as sp
import numpy as np
from sympy.abc import x,y
from sympy import linsolve
from sympy import Function, Symbol
from sympy import functions

from copy import *
import random as rd
"""
**********************************************************************
**********************************************************************
**********************************************************************
ARCHIVE (Ne pas jeter (des fonctions appellent l'archive))
ARCHIVE (Ne pas jeter (des fonctions appellent l'archive))
ARCHIVE (Ne pas jeter (des fonctions appellent l'archive))
**********************************************************************
**********************************************************************
**********************************************************************
"""

"""
****************************************************************************
Fonction d'Exercices
****************************************************************************
"""


def StrDevSimple(classe):
    expr = AxPb() * AxPbCarre() + sgnnbre() * AxPb() * AxPbCarre()
    return [sp.latex(expr) + "\\\\", sp.latex(expr.expand())]


def StrDevMoyen(classe):
    expr = AxPbCarre() * AxPbCarre() + sgnnbre() * AxPbCarre() * AxPbCarre()
    return [sp.latex(expr) + "\\\\", sp.latex(expr.expand())]


def StrDevDur(classe):
    S = 1
    for k in range(3, 6):
        S = S * AxPbCarreDur()
        S = S + sgnnbre() * rd.randint(2, 10) * AxPb()
    S = S * AxPbCarreDur()
    return [sp.latex(S) + "\\\\", sp.latex(S.expand())]


def StrIneSimple(classe):
    u = rd.randint(0, 1)
    v = rd.randint(0, 1)
    A = AxPb()
    B = AxPb()
    AA = AxPbCarreSeul()
    BB = AxPbCarreSeul()
    if classe == "Seconde":
        u = 0
    if u == 0:
        if v == 0:
            expr = A >= B
            res = A - B
        if v == 1:
            expr = A <= B
            res = B - A
    if u == 1:
        if v == 0:
            expr = AA >= BB
            res = AA - BB
        if v == 1:
            expr = AA <= BB
            res = BB - AA

    resultat = solveset(res >= 0, domain=S.Reals)
    return [sp.latex(expr) + "\\\\", sp.latex(resultat)]


def StrIneMoyen(classe):
    a = rd.randint(1, 9)
    b = rd.randint(1, 9)
    u = rd.randint(0, 1)
    v = rd.randint(0, 1)
    A = AxPb()
    B = AxPb()
    c = racinepib()
    d = racinepib()
    if v == 0:
        expr = A / B >= c / d
        res = A / B - c / d
    if v == 1:
        expr = A / B <= c / d
        res = -A / B + c / d
    exprcorrige = solveset(res >= 0, domain=S.Reals)
    return [sp.latex(expr) + "\\\\", sp.latex(exprcorrige)]


def StrIneDur(classe):
    u = rd.randint(0, 1)
    v = rd.randint(0, 1)
    A = AxPb()
    B = AxPb()
    C = AxPb()
    D = AxPb()
    I = IdRemarq()
    J = IdRemarq()
    if classe == "Seconde":
        if u == 0:
            expr = I / A >= J / A
            res = I / A - J / A
        if u == 1:
            expr = I / A <= J / A
            res = J / A - I / A
    else:
        if v == 0:
            if u == 0:
                expr = A / B >= C / D
                res = A / B - C / D
            if u == 1:
                expr = A / B <= C / D
                res = C / D - A / B
        if v == 1:
            if u == 0:
                expr = I / A >= J / A
                res = I / A - J / A
            if u == 1:
                expr = I / A <= J / A
                res = J / A - I / A
    exprcorrige = solveset(res >= 0, domain=S.Reals)
    return [sp.latex(expr) + "\\\\", sp.latex(exprcorrige)]


def StrTabVarSimple(classe):
    u = rd.randint(0, 2)
    if classe == "Seconde":
        u = -1
        v = rd.randint(0, 2)
    if u == -1:
        if v == 0:
            A = IdRemarq()
            S1 = StrFexpr(A)
            expr = A
        if v == 1:
            A = racinepib() * AxPb()
            S1 = StrFexpr(A)
            expr = A
        if v == 2:
            A = IdRemarq()
            expr = sp.sqrt(A)
            S1 = StrFexpr(expr)
            deriv = sp.diff(expr, x)
            [a, b] = fraction(deriv)
            resultat = solveset(a >= 0, domain=S.Reals)
    if u == 0:
        expr = AxPbCarreDur() + sgnnbre() + AxPb()
        S1 = StrFexpr(expr)
    if u == 1:
        expr = AxPb() * AxPb()
        S1 = StrFexpr(expr)
    if u == 2:
        expr = AxPbCubeDur()
        S1 = StrFexpr(expr)
    if (u != -1 or v != 2):
        deriv = sp.diff(expr, x)
        resultat = solveset(deriv >= 0, domain=S.Reals)
    return [S1, sp.latex(resultat), sp.latex(deriv)]


def StrTabVarMoyen(classe):
    u = rd.randint(0, 2)
    if u == 2:
        expr = AxPbCubeDur() + sgnnbre() * AxPbCarreDur()
        if classe == "Seconde":
            a = rd.randint(1, 9)
            b = rd.randint(1, 8)
            expr = (a * x + b) ** 3
        S1 = StrFexpr(expr)
    if u == 0:
        expr = AxPb() * AxPb()
        S1 = StrFexpr(expr)
    if u == 1:
        expr = AxPb() / AxPb()
        S1 = StrFexpr(expr)
    deriv = sp.diff(expr, x)
    resultat = solveset(deriv >= 0, domain=S.Reals)
    return [S1, sp.latex(resultat), sp.latex(deriv)]


def StrTabVarDur(classe):
    u = rd.randint(0, 2)
    if classe == "Seconde":
        u = 0
    if classe == "Terminale":
        u = rd.randint(3, 4)
        v = rd.randint(0, 2)
    if u == 0:
        expr = racine() * AxPbCubeDur()
        if classe == "Seconde":
            a = rd.randint(1, 9) * racinepib()
            b = rd.randint(1, 8) * racinepib()
            expr = (a * x + b) ** 3
        S1 = StrFexpr(expr)
    if u == 1:
        expr = AxPb() * racine() * AxPbCarreDur()
        S1 = StrFexpr(expr)
    if u == 2:
        expr = AxPbCarreDur() / AxPb()
        S1 = StrFexpr(expr)
    if u == 3:  # Exponentielle
        if v == 0:
            expr = sp.exp(AxPbCarre() / AxPb())
            [S1, deriv, resultat] = AnalyseExpo(expr)
        if v == 1:
            expr = sp.exp(AxPb() * racinepib() * AxPbCarreDur())
            [S1, deriv, resultat] = AnalyseExpo(expr)
        if v == 2:
            expr = AxPb() * sp.exp(AxPb())
            [S1, deriv, resultat] = AnalyseExpo(expr)
    if u == 4:  # Logarithme
        if v == 0:
            A = AxPbCarre() / AxPb()
            Df = sp.solveset(A > 0, domain=S.Reals)
            expr = sp.ln(A)
            [S1, deriv, resultat] = AnalyseLog(expr, Df)
        if v == 1:
            A = AxPb()
            expr = AxPbCube() + sp.ln(A)
            Df = sp.solveset(A > 0, domain=S.Reals)
            [S1, deriv, resultat] = AnalyseLog(expr, Df)
        if v == 2:
            A = AxPb()
            expr = sp.ln(A) / A
            Df = sp.solveset(A > 0, domain=S.Reals)
            [S1, deriv, resultat] = AnalyseLog(expr, Df)
    if classe != "Terminale":
        deriv = sp.diff(expr, x)
        resultat = solveset(deriv >= 0, domain=S.Reals)
    return [S1, sp.latex(resultat), sp.latex(deriv)]


def StrEqSimple(classe):
    u = rd.randint(0, 1)
    if u == 0:
        A = AxPb()
        B = AxPb()
        expr = A - B
        pprint = sp.latex(A) + "=" + sp.latex(B)
    if u == 1:
        n = rd.randint(2, 4)
        expr = AxPbDur()
        for i in range(0, n):
            expr = expr * AxPbDur()
        pprint = sp.latex(expr) + "= 0"
    Sol = solveset(expr, domain=S.Reals)
    return [pprint + "\\\\", sp.latex(Sol)]


def StrEqMoyenne(classe):
    A = IdRemarq()
    b = rd.randint(1, 9)
    expr = A - b
    Sol = solveset(expr, domain=S.Reals)
    return [sp.latex(A) + "= 0" + "\\\\", sp.latex(Sol)]


def StrEqDure(classe):
    u = rd.randint(0, 1)
    v = rd.randint(0, 1)
    if u == 0:
        A = IdRemarq()
        B = racinepib()
    if u == 1:
        A = IdRemarq()
        B = IdRemarq()
    if classe == "Terminale":
        AA = AxPb()
        BB = AxPb()
        if u == 0:
            if v == 0:
                A = sp.exp(AA)
                B = sp.exp(BB)
            if v == 1:
                A = exp(AA)
                B = rd.randint(-5, 20)
        if u == 1:
            if v == 0:
                A = sp.log(AA)
                B = sp.log(BB)
            if v == 1:
                A = sp.log(AA)
                B = rd.randint(-5, 20)
    expr = A - B
    Sol = solveset(expr, domain=S.Reals)
    return [sp.latex(A) + "=" + sp.latex(B), sp.latex(Sol)]


def StrExoFraction(classe):
    a = rd.randint(1, 100)
    b = rd.randint(1, 100)
    return ["\\frac{" + "{0}".format(a) + "}" + "{" + "{0}".format(b) + "}", sp.latex(Rational(a, b))]


def StrExoFractionMoyen(classe):
    a = rd.randint(1, 50)
    b = rd.randint(1, 50)
    c = rd.randint(1, 50)
    d = rd.randint(1, 50)
    e = rd.randint(1, 50)
    f = rd.randint(1, 50)
    u = rd.randint(0, 5)
    v = rd.randint(0, 1)
    u = 1
    if u == 0:
        if v == 0:
            S1 = "\\frac{" + "{0}".format(a) + "}" + "{" + "{0}".format(b) + "}" + " + " + "\\frac{" + "{0}".format(
                c) + "}" + "{" + "{0}".format(d) + "}"
            res = Rational(a, b) + Rational(c, d)
        if v == 1:
            S1 = "\\frac{" + "{0}".format(a) + "}" + "{" + "{0}".format(b) + "}" + " - " + "\\frac{" + "{0}".format(
                c) + "}" + "-" + "{" + "{0}".format(d) + "}"
            res = Rational(a, b) - Rational(c, d)
    if u > 0:
        A = AxPb()
        B = AxPb()
        C = AxPb()
        D = AxPb()
        AA = sp.latex(A)
        BB = sp.latex(B)
        CC = sp.latex(C)
        DD = sp.latex(D)
        if v == 0:
            S1 = "\\frac{" + AA + "}" + "{" + BB + "}" + " + " + "\\frac{" + CC + "}" + "{" + DD + "}"
            res = sp.together(A / B + C / D)
        if v == 1:
            S1 = "\\frac{" + AA + "}" + "{" + BB + "}" + " - " + "\\frac{" + CC + "}" + "{" + DD + "}"
            res = sp.together(A / B - C / D)
    [a, b] = fraction(res)
    a = sp.expand(a)
    res = a / b
    return [S1, sp.latex(res)]


def StrExoFractionDur(classe):
    a = rd.randint(1, 5) * racinepib()
    b = rd.randint(1, 5) * racinepib()
    c = rd.randint(1, 5) * racinepib()
    d = rd.randint(1, 5) * racinepib()
    e = rd.randint(1, 5) * racinepib()
    f = rd.randint(1, 5) * racinepib()
    u = rd.randint(0, 5)
    v = rd.randint(0, 1)
    u = 1
    if u == 0:
        if v == 0:
            S1 = "\\frac{" + "{0}".format(a) + "}" + "{" + "{0}".format(b) + "}" + " + " + "\\frac{" + "{0}".format(
                c) + "}" + "{" + "{0}".format(d) + "}"
            res = Rational(a, b) + Rational(c, d)
        if v == 1:
            S1 = "\\frac{" + "{0}".format(a) + "}" + "{" + "{0}".format(b) + "}" + " - " + "\\frac{" + "{0}".format(
                c) + "}" + "-" + "{" + "{0}".format(d) + "}"
            res = Rational(a, b) - Rational(c, d)
    if u > 0:
        A = AxPb()
        B = AxPb()
        C = AxPb()
        D = AxPb()
        AA = sp.latex(A)
        BB = sp.latex(B)
        CC = sp.latex(C)
        DD = sp.latex(D)
        if v == 0:
            S1 = "\\frac{" + AA + "}" + "{" + BB + "}" + " + " + "\\frac{" + CC + "}" + "{" + DD + "}"
            res = sp.together(A / B + C / D)
        if v == 1:
            S1 = "\\frac{" + AA + "}" + "{" + BB + "}" + " - " + "\\frac{" + CC + "}" + "{" + DD + "}"
            res = sp.together(A / B - C / D)
    return [S1, sp.latex(res)]


def StrEqDroiteFacile(Classe):
    xa = rd.randint(1, 9)
    ya = rd.randint(1, 9)
    xb = rd.randint(1, 9)
    yb = rd.randint(1, 9)
    S1 = "\\text{Droite passant par }A" + Vecteur2(xa, ya) + "\\text{ et }B" + Vecteur2(xb, yb)
    corr = (x - xa) * (yb - ya) - (y - ya) * (xb - xa)
    return [S1, sp.latex(corr) + " =0"]


def StrEqDroiteMoyenne(Classe):
    xa = rd.randint(1, 9) * racinepib()
    ya = rd.randint(1, 9) * racinepib()
    xb = rd.randint(1, 9) * racinepib()
    yb = rd.randint(1, 9) * racinepib()
    xc = rd.randint(1, 9) * racinepib()
    yc = rd.randint(1, 9) * racinepib()
    xd = rd.randint(1, 9) * racinepib()
    yd = rd.randint(1, 9) * racinepib()

    S1 = "\\text{Droite passant par }A " + Vecteur2(xa, ya) + "\\text{ et } B" + Vecteur2(xb,
                                                                                          yb) + "\\text{ et la Droite passant par }C" + Vecteur2(
        xc, yc) + "\\text{ et } D" + Vecteur2(xd, yd)
    corr1 = (x - xa) * (yb - ya) - (y - ya) * (xb - xa)
    corr1 = sp.latex(corr1) + "=0"
    corr2 = (x - xc) * (yd - yc) - (y - yc) * (xd - xc)
    corr2 = sp.latex(corr2) + "=0"
    Corr = "\\begin{array}{l}" + "{0}".format(corr1) + " \\\\ " + "{0}".format(corr2) + "\\end{array}"
    return [S1, Corr]


def StrEqDroiteDure(Classe):
    xa = rd.randint(1, 9)
    ya = rd.randint(1, 9)
    xb = rd.randint(1, 9)
    yb = rd.randint(1, 9)
    xc = rd.randint(1, 9)
    yc = rd.randint(1, 9)
    xd = rd.randint(1, 9)
    yd = rd.randint(1, 9)

    S1 = "\\text{Droite passant par }A " + Vecteur2(xa, ya) + "\\text{ et } B" + Vecteur2(xb,
                                                                                          yb) + "\\text{ et la Droite passant par }C" + Vecteur2(
        xc, yc) + "\\text{ et } D" + Vecteur2(xd, yd)
    corr1 = (x - xa) * (yb - ya) - (y - ya) * (xb - xa)
    Corr1 = sp.latex(corr1) + "=0"
    corr2 = (x - xc) * (yd - yc) - (y - yc) * (xd - xc)
    Corr2 = sp.latex(corr2) + "=0"
    Corr = "\\begin{array}{l}" + "{0}".format(Corr1) + " \\\\ " + "{0}".format(Corr2) + "\\end{array}"
    Corr2 = sp.latex(linsolve([corr1, corr2], [x, y]))
    return [S1, Corr, Corr2]


def StrProba(Classe):
    A = rd.randint(0, 100)
    BsA = rd.randint(0, 100)
    BsAb = rd.randint(0, 100)

    Enonce = 'Un évenement $A$ arrive avec probabilité ${0}(A) =  {1}\%$ et un évenement $B$ arrive avec probabilité ${0}_A(B) =  {2}\% $  et ${0}_{3} (B) = {4}\%$'.format(
        '\mathbb{P}', A, BsA, '{\overline{A}}', BsAb)
    Question = "  \\begin{enumerate} \item Calculer $\mathbb{P}(A \cap B)$ \item Calculer $\mathbb{P}(B)$ \item Calculer $\mathbb{P}_B(A)$ \\end{enumerate}"

    S1 = Enonce + Question

    Corr1 = " \[  {0} (A \cap B) = {0}(A) \cdot {0}_A(B) = {1} \% \cdot {2} \% = {3}\] ".format("\mathbb{P}", A, BsA,
                                                                                                A * BsA / 10000)
    Corr2 = "\[ {0} (B) = {0} (A \cap B) + {0} ({1} \cap B) = {2} \]".format("\mathbb{P}", "\overline{A}",
                                                                             A * BsA / 10000 + (100 - A) * BsAb / 10000)
    Corr3 = "\[ {0}_B(A) = \\frac{1} {0} (A \cap B) {2} {1} {0} (B) {2} = \\frac {1} {3} {2} {1} {4} {2} = {5} \]".format(
        "\mathbb{P}", "{", "}", A * BsA / 10000, A * BsA / 10000 + (100 - A) * BsAb / 10000,
        (A * BsA / 10000) / (A * BsA / 10000 + (100 - A) * BsAb / 10000))
    Corr = Corr1 + Corr2 + Corr3

    return [S1, Corr]


def ExoDeProba(m):
    [o, Exo, Correction] = Preambule("Exercice de Probabilité", "S.Gibaud", "Pour la noter", "Seconde")
    [o, Exo, Correction] = Ouverture(o)
    for i in range(m):
        [S1, Corr] = StrProba("")
        Exo.write("\n \\section{Exercice %d} \n" % i)
        Exo.write(S1)
        Correction.write("\\section{Correction Exercice %d}" % i)
        Correction.write(Corr)
    Correction.close()
    Coorection = open('Correction.txt', 'r')
    t = Coorection.read()
    Exo.write(t)
    Exo.write("\n \\end{document}")
    Exo.close()
    Coorection.close()
    # os.system("pdflatex Exo.txt")
    # os.remove("Exo.txt")
    # os.remove("Exo.log")
    # os.remove("Exo.aux")


"""

******************************************************************************
Formation de parenthèses
******************************************************************************

"""


def racinepib():
    return pi() * racine()


def supinf():
    u = rd.randint(0, 1)
    if u == 0:
        return r"\geq"
    if u == 1:
        return r"\leq"


def Vecteur2(a, b):
    a = sp.latex(a)
    b = sp.latex(b)
    return "\\left( \\begin{array}{c}" + "{0}".format(a) + "\\\\" + "{0}".format(b) + "\\end{array}\\right)"


def Vecteur3(a, b, c):
    return "\\left( \\begin{array}{c}" + "{0}".format(a) + "\\\\" + "{0}".format(b) + "\\\\" + "{0}".format(
        c) + "\\end{array}\\right)"


def StrFexpr(expr):
    return "f(x) = " + sp.latex(expr) + "\\\\"


def AnalyseExpo(expr):
    S1 = StrFexpr(expr)
    deriv = sp.diff(expr, x)
    sgn = together(deriv / expr)
    [a, b] = fraction(sgn)
    a = a.expand()
    sgn = a / b
    deriv = sgn * expr
    resultat = solveset(sgn > 0, domain=S.Reals)
    return [S1, deriv, resultat]


def AnalyseLogA(expr):
    S1 = StrFexpr(expr)
    deriv = sp.diff(expr, x)
    sgn = together(deriv)
    [a, b] = fraction(sgn)
    a = a.expand()
    sgn = a / b
    deriv = sgn
    resultat = solveset(sgn > 0, domain=S.Reals)
    return [S1, deriv, resultat]


def AnalyseLog(expr, Df):
    S1 = StrFexpr(expr)
    deriv = sp.diff(expr, x)
    resultat = solveset(deriv > 0, domain=Df)
    return [S1, deriv, resultat]


def AnalyseLogFrac(expr, Df):
    S1 = StrFexpr(expr)
    deriv = sp.diff(expr, x)
    resultat = solveset(deriv > 0, domain=Df)
    return [S1, deriv, resultat]


def sqrt():
    return "\\sqrt"


def sqrtalea():
    u = rd.randint(0, 1)
    if u == 0:
        return "\\sqrt"
    if u == 1:
        return ""


def pi():
    u = rd.randint(0, 1)
    if u == 0:
        return sp.pi
    if u == 1:
        return 1


def racine():
    u = rd.randint(0, 5)
    v = rd.randint(1, 20)
    expr = sp.sqrt(v)
    if u < 5:
        return expr
    if u == 5:
        return 1


def sgnadd():
    u = rd.randint(0, 1)
    if u == 0:
        return " + "
    if u == 1:
        return " - "


def sgnadda():
    u = rd.randint(0, 1)
    if u == 0:
        return +rd.randint(1, 9)
    if u == 1:
        return -rd.randint(1, 9)


def sgnaddmult():
    u = rd.randint(0, 5)
    if u == 0:
        return " +{0} ".format(rd.randint(1, 9))
    if u == 1:
        return " -{0} ".format(rd.randint(1, 9))
    if u >= 2:
        return "{0}".format(rd.randint(1, 9))


def sgnnbre():
    u = rd.randint(0, 5)
    if u == 0:
        return 1
    if u > 0:
        return -1


def Carre(expr):
    u = rd.randint(0, 5)
    if u > 0:
        return expr ** 2
    if u == 0:
        return expr


def Cube(expr):
    u = rd.randint(0, 1)
    if u == 0:
        return expr ** 3
    if u == 1:
        return expr


def AxPb():
    a = rd.randint(1, 10)
    b = rd.randint(1, 10)
    return a * x + b


def AxPbDur():
    return racinepib() * x + racinepib()


def AxPbCarre():
    u = rd.randint(0, 5)
    if u == 1 or u == 2:
        a = rd.randint(0, 9)
        b = rd.randint(0, 9)
        c = rd.randint(0, 9)
        return a * x ** 2 + b * x + c
    if u == 0:
        return AxPb()
    if u > 2:
        return AxPb() ** 2


def AxPbCubeDur():
    a = rd.randint(1, 9)
    b = rd.randint(1, 9)
    c = rd.randint(1, 9)
    d = rd.randint(1, 9)
    u = rd.randint(0, 1)
    expr1 = (racinepib() * a * x + b * racinepib()) ** 3
    expr2 = a * racinepib() * x ** 3 + b * racinepib() * x ** 2 + racinepib() * c * x + d * racinepib()
    if u == 0:
        return expr1
    if u == 1:
        return expr2


def AxPbCube():
    a = rd.randint(1, 9)
    b = rd.randint(1, 9)
    c = rd.randint(1, 9)
    d = rd.randint(1, 9)
    u = rd.randint(0, 1)
    expr1 = (a * x + b) ** 3
    expr2 = a * x ** 3 + b * x ** 2 + c * x + d
    if u == 0:
        return expr1
    if u == 1:
        return expr2


def AxPbCarreDur():
    return racinepib() * Carre(x) + sgnnbre() + racinepib() * x + sgnnbre() + racinepib()


def AxPbCarreSeul():
    u = rd.randint(0, 5)
    if u == 1 or u == 2:
        a = rd.randint(0, 9)
        b = rd.randint(0, 9)
        c = rd.randint(0, 9)
        return a * x ** 2 + b * x + c
    if u == 0:
        return AxPb()
    if u > 2:
        return AxPb() ** 2


def IdRemarq():
    a = rd.randint(1, 5)
    b = rd.randint(1, 5)
    expr = (a * x + sgnnbre() * b) ** 2
    return expr.expand()

