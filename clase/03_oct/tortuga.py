import turtle

#definir funciones
def dibujar_cuadro(lado):
    for i in range(4):
        tortuga.forward(lado)  # Avanzar 100 píxeles
        tortuga.left(90)  # Girar 90 grados a la izquierda
        
def dibujar_triangulo(lado):
    
    for i in range(3):
        tortuga.forward(lado)
        tortuga.left(120)
        
def poligono(n,lado):
    
    for i in range(n):
        
        
        tortuga.forward(lado)
        tortuga.left(360/n)
        
        
        
        
    
        


# Crear la ventana y la tortuga
ventana = turtle.Screen()  # Ventana de dibujo
ventana.title("Dibujo con Turtle")  # Título de la ventana
ventana.bgcolor("white")  # Color de fondo

tortuga = turtle.Turtle()  # Crear la tortuga
tortuga.shape("turtle")  # Cambiar la forma del cursor a una tortuga
tortuga.color("blue")  # Cambiar el color de la tortuga
tortuga.pensize(1)  # Cambiar el grosor del lápiz

# Dibujar un cuadrado
#tamaño = int(input("De qué tamaño? "))
#dibujar_cuadro(tamaño)
#/for i in range(10,200+1,20):
 #   dibujar_cuadro(i)

#dibujar_triangulo(300)
#poligono(360,2)
# Finalizar el dibujo
turtle.done()
