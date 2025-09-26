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
