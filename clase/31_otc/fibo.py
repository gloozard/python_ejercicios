def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Ejemplo de uso:
# print(fibonacci_recursivo(5)) # Esto devolvería 5 (0, 1, 1, 2, 3, 5)


print(fibonacci_recursivo(10))