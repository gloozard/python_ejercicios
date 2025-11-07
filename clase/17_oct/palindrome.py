def isPalindrome(oracion):
    oracion = oracion.replace(" ", "")
    oracion = oracion.lower()
    print(oracion)
    for i in range(int(len(oracion)/2)):
        left =  oracion[i]
        right = oracion[i*-1-1]
        if left != right:
            return False
        
    return True
    
    
    
mensaje ="anita lava la tina"

print(isPalindrome(mensaje))
        