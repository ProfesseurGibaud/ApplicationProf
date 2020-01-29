import sympy as sp
import numpy as np

from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy.solvers.inequalities import solve_rational_inequalities
from sympy import solveset,S,Interval
from sympy import together
from sympy.abc import x,y
from sympy import linsolve
from sympy import Function, Symbol
from sympy import functions
from sympy.functions.elementary import *
from sympy.simplify.simplify import *
from sympy import fraction, Rational, Symbol
import sympy.assumptions.handlers
from copy import *
import random as rd

if __name__ == '__main__':
    import os
    os.chdir("Google Drive//Python//ApplicationProf//GenerateurExercice")
from Archive import *





"""
Classe Exercices
"""


class Exercice:
    def __init__(self):
        self.der = 0
        self.res = 0
        self.CheckDomaine = 0
        self.Df = S.Reals
        self.expr = 0
        self.enonce = ""
        self.corr = 0
        self.correction = ""
        self.correction2 = ""
        self.correction3 = ""
        self.niveau = "Facile"
        self.numero = 1
        self.res = 0
        self.classe = "Seconde"
        self.type = "D\\'eveloppement"
        self.derive = ""
        self.StrExpr = ""

    def FaireEnonce(self):
        if self.type == "D\\'eveloppement":
            if self.niveau == "Facile":
                self.expr = AxPb() * AxPbCarre() + sgnnbre() * AxPb() * AxPbCarre()
                self.enonce = sp.latex(self.expr)
            if self.niveau == "Moyen":
                self.expr = self.expr = AxPbCarre() * AxPbCarre() + sgnnbre() * AxPbCarre() * AxPbCarre()
            if self.niveau == "Dur":
                self.expr = 1
                for k in range(3, 6):
                    self.expr = self.expr * AxPbCarre()
                    self.expr = self.expr + sgnnbre() * rd.randint(2, 10) * AxPb()
                self.expr = self.expr * AxPbCarre()
        if self.type == "In\\'equation":
            u = rd.randint(0, 1)
            v = rd.randint(0, 1)
            a = rd.randint(1, 9)
            b = rd.randint(1, 9)
            c = racinepib()
            d = racinepib()
            A = AxPb()
            B = AxPb()
            C = AxPb()
            D = AxPb()
            I = IdRemarq()
            J = IdRemarq()
            AA = AxPbCarreSeul()
            BB = AxPbCarreSeul()
            if self.classe == "Seconde":
                if self.niveau == "Facile":
                    if v == 0:
                        self.expr = A >= B
                        self.res = A - B
                    if v == 1:
                        self.expr = A <= B
                        self.res = B - A
                if self.niveau == "Moyen":
                    if v == 0:
                        self.expr = A / B >= c / d
                        self.res = A / B - c / d
                    if v == 1:
                        self.expr = A / B <= c / d
                        self.res = -A / B + c / d
                if self.niveau == "Dur":
                    if u == 0:
                        self.expr = I / A >= J / A
                        self.res = I / A - J / A
                    if u == 1:
                        self.expr = I / A <= J / A
                        self.res = J / A - I / A
            else:
                if self.niveau == "Facile":
                    if v == 0:
                        self.expr = AA >= BB
                        self.res = AA - BB
                    if v == 1:
                        self.expr = AA <= BB
                        self.res = BB - AA
                if self.niveau == "Moyen":
                    if v == 0:
                        self.expr = A / B >= c / d
                        self.res = A / B - c / d
                    if v == 1:
                        self.expr = A / B <= c / d
                        self.res = -A / B + c / d
                if self.niveau == "Dur":
                    if v == 0:
                        if u == 0:
                            self.expr = A / B >= C / D
                            self.res = A / B - C / D
                        if u == 1:
                            self.expr = A / B <= C / D
                            self.res = C / D - A / B
                    if v == 1:
                        if u == 0:
                            self.expr = I / A >= J / A
                            self.res = I / A - J / A
                        if u == 1:
                            self.expr = I / A <= J / A
                            self.res = J / A - I / A
        if self.type == "Equation":
            if self.niveau == "Facile":
                u = rd.randint(0, 1)
                if u == 0:
                    A = AxPb()
                    B = AxPb()
                    self.expr = A - B
                if u == 1:
                    n = rd.randint(2, 4)
                    self.expr = AxPbDur()
                    for i in range(0, n):
                        self.expr = self.expr * AxPbDur()
            if self.niveau == "Moyen":
                A = IdRemarq()
                b = rd.randint(1, 9)
                self.expr = A - b
            if self.niveau == "Dur":
                u = rd.randint(0, 1)
                v = rd.randint(0, 1)
                if self.classe == "Terminale":
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
                else:
                    if u == 0:
                        A = IdRemarq()
                        B = racinepib()
                    if u == 1:
                        A = IdRemarq()
                        B = IdRemarq()
                self.expr = A - B
            print(self.expr)

        if self.type == "Fraction":
            if self.niveau == "Facile":
                [self.enonce, self.correction] = StrExoFraction(self.classe)
            if self.niveau == "Moyen":
                [self.enonce, self.correction] = StrExoFractionMoyen(self.classe)
            if self.niveau == "Dur":
                [self.enonce, self.correction] = StrExoFractionDur(self.classe)
        if self.type == "Equation de Droite du Plan":
            if self.niveau == "Facile":
                [self.enonce, self.correction] = StrEqDroiteFacile(self.classe)
            if self.niveau == "Moyen":
                [self.enonce, self.correction] = StrEqDroiteMoyenne(self.classe)
            if self.niveau == "Dur":
                [self.enonce, self.correction, self.corr2] = StrEqDroiteDure(self.classe)
        if self.type == "Proba":
            [self.enonce, self.correction] = StrProba(self.classe)
        if self.type == "Tableaux de Variation":
            if self.niveau == "Facile":
                u = rd.randint(0, 2)
                if self.classe == "Seconde":
                    v = rd.randint(0, 2)
                    if v == 0:
                        self.expr = IdRemarq()
                    if v == 1:
                        self.expr = racinepib() * AxPb()
                    if v == 2:
                        A = IdRemarq()
                        self.CheckDomaine = A
                        self.expr = sp.sqrt(A)
                else:
                    if u == 0:
                        self.expr = AxPbCarreDur() + sgnnbre() + AxPb()
                    if u == 1:
                        self.expr = AxPbCarre() * AxPb()
                    if u == 2:
                        self.expr = AxPbCubeDur()
            if self.niveau == "Moyen":
                u = rd.randint(0, 3)
                if self.classe != "Terminale":
                    u = rd.randint(0, 1)
                if u == 0:
                    A = AxPb()
                    self.CheckDomaine = A
                    self.expr = AxPb() * sp.sqrt(A)
                if u == 2:
                    A = AxPb()
                    self.CheckDomaine = A
                    self.expr = sp.log(A) / A
                if u == 3:
                    self.expr = exp(AxPbCube())
                if u == 1:
                    self.expr = AxPbDur() / AxPbDur()
                if u == 4:  # Je n'arrive pas à résoudre par info le signe de la dérivée
                    A = AxPbDur()
                    self.CheckDomaine = A
                    self.expr = sp.log(A) + ((AxPbDur()) ** 3)
            if self.niveau == "Dur":
                u = rd.randint(0, 3)
                if self.classe != "Terminale":
                    u = rd.randint(0, 1)
                if u == 0:
                    A = AxPbCarre()
                    self.CheckDomaine = A
                    self.expr = racinepib() * sp.sqrt(A) * AxPbDur()
                if u == 1:
                    A = AxPbDur()
                    B = AxPbCarre()
                    self.CheckDomaine = B
                    self.expr = racinepib() * sp.sqrt(A) / B
                if u == 2:
                    self.expr = racinepib() * sp.exp(AxPbCarre()) * AxPb()
                if u == 3:
                    A = AxPbCarreDur() / AxPb()
                    self.CheckDomaine = A
                    self.expr = racinepib() * sp.log(A)

                if self.classe == "Seconde":
                    A = AxPbDur()
                    self.CheckDomaine = A
                    self.expr = self.expr = racinepib() * AxPbDur() * sp.sqrt(A)
        print(self.expr)

    def FaireCorrection(self):
        if self.type == "D\\'eveloppement":
            self.corr = self.expr.expand()
        if self.type == "In\\'equation":
            self.corr = solveset(self.res >= 0, domain=S.Reals)
        if self.type == "Equation":
            self.corr = solveset(self.expr, domain=S.Reals)
        if self.type == "Tableaux de Variation":
            self.der = sp.together(sp.expand(sp.together(sp.diff(self.expr, x))))
            self.Df = solveset(self.CheckDomaine >= 0, domain=S.Reals)
            [a, b] = fraction(self.der)
            self.res = solveset(a >= 0, domain=self.Df)

    def EcrireExo(self):
        with open("Exo.txt", "a") as Exo:
            Exo.write(self.type + " num\\'ero " + "{0}".format(self.numero))
            ajoutdevant = ""  # "f(x) = "*(self.type == "Tableaux de Variation")
            ajoutderriere = "= 0" * (self.type == "Equation")
            Exo.write(" \\[" + ajoutdevant + self.enonce + ajoutderriere + "\\]")

    def EcrireCorrection(self):
        if self.type == "Tableaux de Variation":
            with open("Correction.txt", "a") as Correction:
                Correction.write("\n Fonction {0}".format(self.numero))
                Correction.write("\\[ " + self.enonce + "\]")
                Correction.write("\n \\[f'(x) = " + sp.latex(self.der) + "\]")
                Correction.write("\n \\[" + sp.latex(self.res) + "\]")
        elif self.type == "Equation de Droite du Plan":  # Eq de Droite
            with open("Correction.txt", "a") as Correction:
                Correction.write("\n Correction " + self.type + " num\\'ero " + "{0}".format(self.numero))
                Correction.write("\n \\[" + self.correction + "\]")
                if self.niveau == "Dur":
                    Correction.write("\n L'intersection est \\[" + self.corr2 + "\]")
        else:
            with open("Correction.txt", "a") as Correction:
                Correction.write("\n Correction " + self.type + " num\\'ero " + "{0}".format(self.numero) + "\\[")
                Correction.write(self.correction)
                Correction.write("\n \\]")

    def VersLatex(self):
        if self.type == "Tableaux de Variation" or self.type == "Fraction" or self.type == "Equation de Droite du Plan":
            if self.type == "Tableaux de Variation":
                self.enonce = "f(x) = " + sp.latex(self.expr)
        else:
            self.enonce = sp.latex(self.expr)
            self.correction = sp.latex(self.corr)

