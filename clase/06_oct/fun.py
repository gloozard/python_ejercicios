import math

def saludo():
    print("¡Hola a todas y todos!")
    
    
    
def saludo_nombre(nombre):
    print(f"Hola {nombre}, bienvenido(a)")
    
def matrimonio(nom1,nom2):
    print(f"{nom1} y {nom2} los declaro matromoniados, hasta que el tatuaje se borre la muerte los separe.")
    
def promedio(a,b,c):
    print("El promedio es de "(a+b+c)/3) 
    
    
def formula_general(a,b,c):
    print("Resultados")
    x1=((-b+ math.sqrt(b**2-4*a*c))/(2*a))
    x2=((-b- math.sqrt(b**2-4*a*c))/(2*a))
    
    print(f"x1= {x1}" )
    print(f"x2=  {x2}")
    
def suma_total(n):
    total=0
    for i in range(n+1):
        total+=i
        
    print(f"suma 1-{n}")
    
          
    
    
#saludo()
#nombre = input("Escribe tu nombre: ")

#saludo_nombre(nombre)
suma_total(10)
#formula_general(2,5,3)