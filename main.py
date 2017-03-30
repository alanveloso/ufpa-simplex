#!/usr/local/bin/python3
#conding: utf-8

from simplex import *



def main():
    kind , oF, rest = setPPL()
    printPPL(kind, oF, rest)
    kind, oF, rest = changeStandardForm(kind, oF, rest)
    printPPL(kind, oF, rest)

    matrix = setMatrixCanonical(oF, rest)

    print ("###############")
    printMatrix(matrix)
    print ("###############")
    func1(matrix)

if __name__ == "__main__":
    print("Main started")
    main()
else:
    print("Module started")
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
