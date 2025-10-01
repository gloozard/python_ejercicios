n = int(input())
#1
for i in range(n+1):
    if i%2==0:
        print(i, end=" " )
print()
#2
for i in range(n):
    print(i*2, end=" " )        
    
print()
#3
for i in range(4,n+1):
    print(i*3, end=" " )    
    
print()
#4  
for i in range(5,n+1):
    print(i*7, end=" " )

print()
#5
for i in range(1,n+1):
    print(100-i*5)
    
    
print()
#6
while n%13!=0:
       n = int(input(end=" "))
       
#7       
ciclos =int(input("Escribe la cantidad de numeros que vas a ingresar: "))

if ciclos<=0:
    exit()
    
num =int(input("Escribe un numero: "))
mayor=num
print(f"{mayor} es el mayor del momento")

for i in range(0,ciclos-1):
    num =int(input("Escribe un numero: "))
    if num> mayor:
        mayor=num
        print(f"{mayor} es el mayor del momento")
       
       
    




