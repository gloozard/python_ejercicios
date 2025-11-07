def multiplicarMatriz(A,B):
    
    if len(A[0]) != len(B):
        return 0 
    matrizC =[[0 for i in range(len(B[0]))]for j in range (len(A))]
    
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            
            for k in range(len(A[0])):
                matrizC[i][j] += A[i][k] * B[k][j]
                
    return matrizC
        
    






matrizA =  [[1,2],[3,4]]
matrizB = [[5,6],[7,8]]

matrizC =multiplicarMatriz(matrizA,matrizB) 

print(matrizC)
