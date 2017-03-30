#!/usr/local/bin/python3
#conding: utf-8

from simplex import *

print("Module started")
print("############################## Problema ###############################")
tipo, funcaoObjetiva, restricoes = "max", [4,7], [[1,0,0,0,0,"<=", 6],[0,1,0,0,0,"<=", 8], [4,-2,0,0,0,"<=", 10]]
printPPL(tipo, funcaoObjetiva, restricoes)
print("########################### Forma Padrão #############################")
tipo, funcaoObjetiva, restricoes = changeStandardForm(tipo, funcaoObjetiva, restricoes)
printPPL(tipo, funcaoObjetiva, restricoes)
matriz = setMatrixCanonical(funcaoObjetiva, restricoes)

calcOptimalAnswer(matriz)
