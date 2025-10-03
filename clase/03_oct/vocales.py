texto = input("Coloca tu texto: ")
texto=texto.lower()
vocales=0
for i in texto:
    if(i=='a'or i =='e' or i=='u' or i=='o' or i=='i'):
        vocales+=1
        
print(vocales)