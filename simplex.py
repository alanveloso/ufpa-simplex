def getSmallerNumber(matrix):
    i = 0
    minimun = min(matrix[-1][1:])
    while matrix[-1][i] != minimun: i = i + 1
    return i

def getIndexLine(matrix, indexCol):
    indexLine = 0
    smaller = float('inf')
    for i in range(1, len(matrix[1:])):
        if matrix[i][indexCol] > 0 and smaller > matrix[i][-1]/matrix[i][indexCol]:
            smaller = matrix[i][-1]/matrix[i][indexCol]
            print(smaller)
            indexLine = i
    return indexLine


def func1(matrix):
    while (min(matrix[-1][1:]) < 0 ):

        indexLine = 0
        indexCol = 0
        num = 0
        divisor = 1

        indexCol = getSmallerNumber(matrix)
        # Procura a linha que sai
        indexLine = getIndexLine(matrix, indexCol)
        matrix[indexLine][0] = matrix[0][indexCol]
        divisor = matrix[indexLine][indexCol]

        for i in range(1, len(matrix[indexLine])):
            matrix[indexLine][i] = matrix[indexLine][i] / divisor

        for i in range(1, len(matrix)):
            print("########## Tableu #########")
            num = 0
            if i != indexLine:
                num = matrix[i][indexCol] * matrix[indexLine][indexCol] * (-1)
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = matrix[indexLine][j] * num + matrix[i][j]
            printMatrix(matrix)


def setMatrixCanonical(objectiveFunction, restrictions):
    matrix = [[]] * (len(restrictions) + 2)
    for i in range(len(matrix)):
        matrix[i] = [0] * len(restrictions[0])
    for i in range(len(restrictions)):
        k = 0
        for j in range(len(restrictions[0]) - 1):
            if type(restrictions[i][j]) is str:
                matrix[i+1][j+1] = restrictions[i][k+1]
            else:
                matrix[i+1][j+1] = restrictions[i][k]
                k = k + 1
    for i in range(len(objectiveFunction)):
        matrix[-1][i+1] = objectiveFunction[i]
    for i in range(len(matrix[0][1:])-1):
        matrix[0][i+1] = "x_%s" %(i+1)
    for i in range(1, len(matrix) - 1):
            if i != len(matrix):
                matrix[i][0] = "x_%s" % (len(restrictions) + i - 1)
    matrix[-1][0] = "F.O"

    return matrix

def printMatrix(matrix):
    for line in matrix:
        for element in line:
            print(element, "\t", end="")
        print()

def changeStandardForm(kind, objectiveFunction, restrictions):
    j = len(objectiveFunction)
    if kind == "max":
        kind = "min"
        for i in range(len(objectiveFunction)):
            objectiveFunction[i] = objectiveFunction[i] * (-1)
    for line in restrictions:
        for i in range(len(line)):
            if line[i] in ['<=', '=<']:
                line[i] = '='
                line[j] = 1
                j = j + 1
            elif line[i] in ['>=', '=>']:
                line[i] = '='
                line[j] = -1
                j = j + 1

    return kind, objectiveFunction, restrictions

def printPPL(kind, objectiveFunction, restrictions):
    if kind == "max":
        print("Max. Z: ", end="")
    elif kind == "min":
        print("Min. Z: ", end="")
    else:
        print("Please, Choice Max or Min...")
        return;
    for i in range(len(objectiveFunction)):
        if objectiveFunction[i] < 0:
            print ("",objectiveFunction[i],"x_",i+1, end="", sep="")
        elif objectiveFunction[i] > 0:
            print ("+",objectiveFunction[i],"x_",i+1, end="", sep= "")
        if objectiveFunction[i] != 0:
           print(" ", end="")
    print()
    print("Suj.a:")
    for line in restrictions:
        print("\t{ ", end="")
        for i in range(len(line)):
            if line[i-1] in ["<=", "=<", "=>", ">=", "="]:
                print(line[i], end="")
            elif type(line[i]) is int and line[i] < 0:
                print (" ",line[i],"x_",i+1, end="", sep="")
            elif type(line [i]) is int and line[i] > 0:
                print (" +",line[i],"x_",i+1, end="", sep="")
            elif line[i] in ["<=", "=<", "=>", ">=", "="]:
                print(" ",line[i]," ", end="")
        print()

def setPPL():
    choice = input("\n[1] Max\n[2] Min\nChoice: ")
    if choice == "1":
        kind = "max"
    elif choice == "2":
        kind = "min"
    else:
        print("Exit...")
        return 0
    varCount = int(input("How many variables?\n: "))
    restrictionCount = int(input("How many retrictions?\n: "))
    objetiveFunction = []

    restrictions = [[]] * restrictionCount
    for i in range(len(restrictions)):
        restrictions[i] = [0] * (varCount + restrictionCount)
    printMatrix(restrictions)
    print("\n############# In Objective Function ##############")
    for i in range(varCount):
        factor = int(input("What is the factor of variable x_%s?\n: " %(i+1)))
        objetiveFunction = objetiveFunction + [factor]
    print("\n############### In Restrictions #################")
    
    for i in range(restrictionCount):
        print("restriction %s:" %(i+1))
        for j in range(varCount+2):
            printMatrix(restrictions)
            if j < varCount:
                factor = int(input("What is the factor of variable x_%s?\n: " %(j+1)))
                restrictions[i][j] = factor
            elif j == varCount:
                restrictions[i] = restrictions[i] + [input("<= or >=?\n: ")]
            else:
                restrictions[i] = restrictions[i] + [int(input("Result:\n: "))]
    
    return kind, objetiveFunction, restrictions
