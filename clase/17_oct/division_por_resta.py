dividendo=-1
divisor=-1

while dividendo<=0:
    dividendo= int(input("Escribe el dividendo: "))

while divisor<=0:
    divisor= int(input("Escribe el divisor: "))

    

cociente=0
residuo=dividendo

while divisor<=residuo:
    cociente+=1
    residuo-=divisor
    
    
print(cociente)
print(residuo)
