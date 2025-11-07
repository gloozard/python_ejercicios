def isUpper(oracion):
    alfabetico= False

    for i in range(len(oracion)):
        
        letra = ord(oracion[i])
        
        if letra>64 and letra<91:
            alfabetico= True
            continue
        if letra>98 and letra<123:
            return False
            continue
        
    return alfabetico



mensaje= "AAAAAAAAAAAAAA)))"

print(isUpper(mensaje))