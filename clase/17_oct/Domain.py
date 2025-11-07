def changeDomain(mail):
    index = mail.split("@")
    
    print(mail)
    print(index)
    index[1] = "proton.me"
    
    mail = "@".join(index)
    
    return mail
        
        
        
mail = "kickemiliano@outlook.com"



newMail= changeDomain(mail)

print(newMail)