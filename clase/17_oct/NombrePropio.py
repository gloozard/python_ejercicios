def primeraVocalMayuscula (nombre):
    
    
    
    nombre=nombre.split()
    for i in range(len(nombre)):
        
         nombre[i]= nombre[i].capitalize()
         
    cadena = " ".join(nombre)
    return cadena
    
    
    
    
nombre = "kick aaaa beasad"

print(primeraVocalMayuscula(nombre))