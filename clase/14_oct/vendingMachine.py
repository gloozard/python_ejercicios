
machine = [[14,14,10,8],[15,12,12,13],[12,10,10,10]]

dinero = int(input())
n_articulos = 0
cambio= dinero
comando=""
fila = 0
columna = 0
comando = input()

while comando != "0":
    
    
    if comando[0]=="A":
        columna= 0
    elif comando[0] =="B":
        columna= 1
        fila = int(comando[1])
    elif comando[0] =="C":
        columna=2
    
    
    
    
    
    
    if dinero >= machine[columna][fila-1]:
        n_articulos+=1
        dinero -=machine[columna][fila-1]
        
    
    
    else:
        print("INSUFICIENTE", dinero)
        
        
    comando = input()
    
    print(n_articulos, dinero)

        