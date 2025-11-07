from random import shuffle

l1 = [3,1,2,6,2,3,8,7,2,9,4,2,0,24,654,32]
iterador = 0
while l1 != sorted(l1):
    shuffle(l1)
    iterador+=1
    print(l1, iterador)
