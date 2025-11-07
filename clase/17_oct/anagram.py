def isAnagram(oracion, oracion2):
    mapeo = {}
    mapeo2 = {}
    
    oracion = oracion.replace(" ","")
    oracion = oracion.lower()
    
    oracion2 = oracion2.replace(" ","")
    oracion2 = oracion2.lower()
    
    
    for i in oracion:
        if i in mapeo:
            mapeo[i]+=1
        else:
            mapeo[i] =1 

    for i in oracion2:
        if i in mapeo2:
            mapeo2[i] +=1
        else:
            mapeo2[i] = 1
            
    if mapeo == mapeo2:
        return True
    
    return False



mensaje = "ni te vale"
mensaje2 = "Valiente"
print(isAnagram(mensaje, mensaje2))