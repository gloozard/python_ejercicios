def maxOf(list):
    mayor =-9999999999999999999999
    
    for i in list:
        if i > mayor:
            mayor = i
    if mayor >0:
        return list.index(mayor)
    else:
        return -1    

    
    
l1 = [1,2,3,4,5,7,8,15,22,144]
l2 = []

    
    
print(maxOf(l2))
        