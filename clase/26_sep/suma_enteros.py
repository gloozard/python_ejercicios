infe = int(input("Ingresa el limite inferior: "))
sup = int(input("Ingresa el limite superior: "))

while infe>sup:
    print("El limite inferior debe ser menor que la superior")
    infe = int(input("Ingresa el limite inferior: "))
    sup = int(input("Ingresa el limite superior: "))
    
sum=0

for i in range (infe,sup+1):
    sum+=i
    
print(f"La suma de los numeros comprendidos entre {infe} y {sup} es{sum}")    
