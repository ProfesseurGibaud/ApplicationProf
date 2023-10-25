import os
import sympy as sp
import numpy as np 
import random as rd
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

