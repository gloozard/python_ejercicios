from random import randint


def insertion (lista):
    
    minimo = None
    aux = -1
    
    for j in range(len(lista)):
        for i in range(j,len(lista)):
         if i == j:
             minimo = i
         if lista[minimo]> lista[i]:
                minimo = i
        aux = lista[j] 
        lista[j] = lista[minimo]
        lista[minimo] = aux
    
    return lista


def listaRandom (nDeElementos = 10, desde = 1, hasta =10):
    lista = []
    
    for i in range(nDeElementos):
        lista.append(randint(desde,hasta))
    return lista
    

lista = listaRandom(20,1, 100)

print(lista)
print(insertion(lista))

        
        