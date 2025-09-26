num = int(input("Ingresa el numero al que le quieras calcular el factorial: "))
result= 1
for i in range(1, num+1):
    result*= i

print(f"El numero factorial de {num} es de: {result:,.0f}")    
    