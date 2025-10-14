def letra_min(mensaje):
    letra_min = mensaje[0]
    for letra in mensaje:
        codigo = ord(letra)
        if codigo >=65 and codigo <=90 or codigo >=97 and codigo<=122 and letra < letra_min:
            letra_min = letra
    return letra_min
    
    
def letramin2 (mensaje):
    
    mensaje2 = mensaje.replace(" ", "")
    
    mensaje2 = sorted(mensaje2)
    return mensaje2[0]
    
    
    
def primer_palabra (mensaje):
    
    for i in range(len(mensaje)):
        
        if mensaje[i] ==" ":
            return mensaje[0:i]
        

mensaje = ",hol mucho gusto"

print(letramin2(mensaje))

print(letra_min(mensaje))
print(primer_palabra(mensaje))

