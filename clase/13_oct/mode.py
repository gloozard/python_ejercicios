def mode (lista):
    mayor = 0
    lista.sort()
    for i in lista:
        
        if lista.count(i) >mayor:
            mayor = i
            
    return mayor
        


numeros = [2, 4, 4, 6, 7, 7, 7, 8]

l3 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
l2 = [2, 4, 4, 5, 3, 2, 5, 2, 1, 5, 1, 5, 3, 4, 2]

print(mode(l2))