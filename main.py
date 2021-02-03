def reversal(w):
    
    rever = w[len (w) - 1]
    for i in range(2, len(w)+ 1):
        rever = rever + w[len (w) - i]
    
    return rever 

print(reversal("potato"))
