def Random():
    L=['0','1','2','3','4','5','6','7','8','9','a','z','e','r','t','i','y','u','p']
    ch=""
    for i in range(3):
            ch=ch+L[i]
            ch=ch+L[i+10]
        
    return print(ch) 
Random()

