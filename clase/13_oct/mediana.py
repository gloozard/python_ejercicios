def mediana(lista):
    
    lista.sort()
    
    if len(lista)%2 == 1:
        return lista[int(len(lista)/2)]
    else:
        return (lista[int(len(lista)/2)]+ lista[int(len(lista)/2-1)])/2
    
    

l2 = [2, 4, 4, 5, 3, 2, 5, 2, 1, 5, 1, 5, 3, 4, 2]
l3 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
l1 = [2, 4, 7, 3, 6, 5, 4, 8, 9, 1]

print(mediana(l1))
        
    