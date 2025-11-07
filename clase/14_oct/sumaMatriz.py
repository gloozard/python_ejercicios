from random import randint
from mostrarMatriz import imprimirMatriz
def sumarMatrices (matrizA, matrizB):
    matrizC = []
    for i in range(len(matrizA)):
        matrizC.append([])

        for j in range(len(matrizA[i])):
            
            matrizC[i].append(matrizA[i][j]+matrizB[i][j])
            
    return matrizC


matrizA = [[randint(1,10) for i in range(5)]for i in range(4)]

matrizB = [[randint(1,10) for i in range(5)]for i in range(4)]

imprimirMatriz(matrizA)
print()
imprimirMatriz(matrizB)
print()

matrizC = sumarMatrices(matrizA,matrizB)

imprimirMatriz(matrizC)

            