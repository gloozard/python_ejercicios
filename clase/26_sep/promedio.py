alumnos= int(input("Numero de alumnos: "))

suma=0

for i in range(0,alumnos):
    suma += int(input(f"Escribe calificación {i+1}: "))

promedio= suma / alumnos

print(f"El promedio del grupo es de {promedio:.1f}")