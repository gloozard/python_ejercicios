def lower(oracion):


    for i in range(len(oracion)):
        
        vocal = ord(oracion[i])
        
        if vocal<91 and vocal>64:
            
            oracion =oracion.replace(chr(vocal),chr(vocal+32) )
            
    return oracion



mensaje = "Holaaaaa"


print(lower(mensaje))
    
    