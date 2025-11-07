def vowelSwap(oracion, vowel):
    
    vocalEnInt= ord(vowel)
    
    print(vocalEnInt)
    if vocalEnInt<133:
        vocalEnInt = vocalEnInt+32
    
    else:
        vocalEnInt = vocalEnInt-32
    oracion = oracion.replace(vowel, chr(vocalEnInt))
    
    
    return oracion





oracion= "Hola buenos DIAS"


print(vowelSwap(oracion,"S"))
    
    