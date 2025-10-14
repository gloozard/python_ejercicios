import random

def par(n):
    if n%2 ==0:
        return True
    else:
        return False
pares=0
nones=0

for i in range(100):
    numero=random.randint(1, 101)    
    if par(numero):
        pares+=1
    else:
        nones+=1

print(f"pares: {pares}")
print(f"nones: {nones}")
