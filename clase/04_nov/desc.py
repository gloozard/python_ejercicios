
from random import randint


def createList (n, start = 1, end =10):
    
    list = []
    for i in range(n):
        list.append(randint(start,end))
    return list



def descendiente (lista):
    for i in range(len(lista)-1):
        print(lista[i], lista[i+1])
        if lista[i]< lista[i+1]:
            return False
        
    return True



l1 = [5,8,0,5,4,2,9]
l2 = [9,8,7,6,5,4]
l3 = createList(10)

print(l3)


print(descendiente(l1))
        