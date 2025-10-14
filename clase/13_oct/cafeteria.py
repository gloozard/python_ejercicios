lista= [] 

for i in range(6):
    lista.append(float(input(f"Ingrese el número de horas trabajadas del empleado {i+1}: ")))
    
pago_hora = float(input("Escriba el pago por hora: "))

for i in range(6):
    
    print(f"Salario bruto del empleado {i+1}: {35.5*lista[i]:,.2f}")