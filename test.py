#!/usr/local/bin/python3
#conding: utf-8

from simplex import *

print("######################################################################")
tipo, funcaoObjetiva, restricoes = "max", [4,7], [[1,0,0,0,0,"<=", 6],[0,1,0,0,0,"<=", 8], [4,-2,0,0,0,"<=", 10]]
printPPL(tipo, funcaoObjetiva, restricoes)
print("########################### Forma Padrão #############################")
tipo, funcaoObjetiva, restricoes = changeStandardForm(tipo, funcaoObjetiva, restricoes)
printMatrix(restricoes)
printPPL(tipo, funcaoObjetiva, restricoes)

matriz = setMatrixCanonical(funcaoObjetiva, restricoes)

print ("###############")
printMatrix(matriz)
print ("###############")
func1(matriz)


print(divideLine([1,2,3,4], 2))
