n = int(input("¿Cuántos números serán?: "))
suma=0
for i in range (n):
    suma+= int(input(f"Ingrese el número {i+1}: "))
    
print(f"La suma es de {suma}")