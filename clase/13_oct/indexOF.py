def indexOf (lista, nombre):
    for i in lista:
        if lista[lista.index(i)] == nombre:
            return lista.index(nombre)
        else:
            return -1

nombres = ["a","b","c","d","e"]


print(indexOf(nombres, ""))
        
        

       