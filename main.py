#!/usr/local/bin/python3
#conding: utf-8

from simplex import *

def main():
    
    kind , oF, rest = setPPL()
    printPPL(kind, oF, rest)
    kind, oF, rest = changeStandardForm(kind, oF, rest)
    printPPL(kind, oF, rest)

    matrix = setMatrixCanonical(oF, rest)

    calcOptimalAnswer(matrix)

if __name__ == "__main__":
    print("Main started")
    main()

