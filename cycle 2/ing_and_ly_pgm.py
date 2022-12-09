def ing_ly():
    
    str=input("Enter the String : ")
    
    a=str[-3:]
    
    print(a)
    
    if a=="ing":
        
        str=str+"ly"
        
    else:
        
        str=str+"ing"
        
    print(str)
    
ing_ly()
