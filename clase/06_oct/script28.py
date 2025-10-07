# cancelar_clase.py
"""
Programa que decide si una clase se cancela según el tiempo de llegada de los estudiantes.
"""

def procesar_clase():
    print("Introduzca los datos:")

    # Leer y validar número de estudiantes
    while True:
        try:
            n = int(input("Número de estudiantes en el grupo: "))
            if n <= 0:
                print("El número de estudiantes debe ser un entero positivo. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Introduzca un entero positivo.")

    # Leer y validar el umbral
    while True:
        try:
            umbral = int(input("Umbral de cancelación (número mínimo de estudiantes a tiempo): "))
            if umbral < 0:
                print("El umbral no puede ser negativo. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Introduzca un entero (>= 0).")

    # Contador y lista de llegadas a tiempo
    contador = 0
    lista_a_tiempo = []

    # Leer tiempos de llegada
    for i in range(1, n + 1):
        while True:
            try:
                tiempo = int(input(f"Tiempo de llegada del estudiante {i} (minutos, negativos = llegó antes): "))
                break
            except ValueError:
                print("Entrada inválida. Introduzca un número entero (ej: -1, 0, 2).")

        if tiempo <= 0:
            contador += 1
            lista_a_tiempo.append(tiempo)

    # Resultado
    print()
    if contador >= umbral:
        print("La clase se imparte.")
        if lista_a_tiempo:
            print(f"Se requieren {umbral} estudiantes a tiempo para iniciar la clase, y hay {contador} que llegaron a tiempo: {', '.join(map(str, lista_a_tiempo))}.")
        else:
            print(f"Se requieren {umbral} estudiantes a tiempo para iniciar la clase, y hay {contador} que llegaron a tiempo.")
    else:
        print("La clase se cancela.")
        if lista_a_tiempo:
            print(f"Se requieren {umbral} estudiantes a tiempo para iniciar la clase, y solo {contador} llegaron a tiempo: {', '.join(map(str, lista_a_tiempo))}.")
        else:
            print(f"Se requieren {umbral} estudiantes a tiempo para iniciar la clase, y ninguno llegó a tiempo.")


if __name__ == '__main__':
    procesar_clase()
