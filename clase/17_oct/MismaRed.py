def sameWifi(ip, ip2):
    
    
    
    wifiSplited = ip.split(".")
    wifiSplited2 = ip2.split(".")
    
    
    if wifiSplited[0] ==wifiSplited2[0] and  wifiSplited[1] ==wifiSplited2[1] and  wifiSplited[2] ==wifiSplited2[2]:
        return "Si son de la misma red papu"
    else:
        return "No papu"
         
    
    
    
ip = "165.15.2.14"
ip2 = "165.15.22.124"



print(sameWifi(ip,ip2))