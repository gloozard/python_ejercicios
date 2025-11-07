
def bubbleSort(lista):
    iteraciones = 0
        
    for i in range(len(lista)-1):
        temp = 0
        
        for j in range(len(lista)-1-i):
            iteraciones+=1
            if lista[j]> lista[j+1]:
                temp= lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista, iteraciones



l1 = [4,3,2,1,5,8,0,2,4,6,9,10,101,123]

l1 = bubbleSort(l1)

print(l1)