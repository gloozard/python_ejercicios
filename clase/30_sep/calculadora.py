opcion = int(input("Seleccione una opcion: \n 1)Suma \n 2)Resta \n 3)División \n 4)Multiplicación \n 0)Salir \n ==>"))

while opcion !=0:
    if opcion ==1:
    
        num1=float(input("Elige el primer numero a Sumar: "))
        num2=float(input("Elige el segundo numero a Sumar: "))
        print(f"\n**** la suma de {num1} + {num2} es {num2+num1} ****\n")
        input("Presiona ENTER para continuar...")
            
    if opcion ==2:
        
        num1=float(input("Elige el primer numero a Restar: "))
        num2=float(input("Elige el segundo numero a Restar: "))
        print(f"\n**** la Resta de {num1} - {num2} es {num1-num2} ****\n")
        input("Presiona ENTER para continuar...")
        
    if opcion ==3:
        
        num1=float(input("Elige el Dividendo: "))
        num2=float(input("Elige el Divisor: "))
        if num2 == 0:
            print("No se puede divir entre 0")
            continue
        print(f"\n**** la División de {num1}/{num2} es {num1/num2} ****\n")
        input("Presiona ENTER para continuar...")
        
    if opcion ==4:
        num1=float(input("Elige el primer numero a Multiplicar: "))
        num2=float(input("Elige el segundo numero a Multiplicar: "))
        print(f"\n**** la Multiplicación de {num1} * {num2} es {num1*num2} ****\n")
        input("Presiona ENTER para continuar...")
        
    if opcion!= range(5):
        print("Seleccione una opción valida")

    opcion = int(input("Seleccione una opcion: \n 1)Suma \n 2)Resta \n 3)División \n 4)Multiplicación \n 0)Salir \n ==>"))
    
print("Gracias por utilizar mi programa:D!")

        