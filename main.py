def reversal(w):
    
    reverse = w[len (w) - 1]
    for i in range(2, len(w)+ 1):
        reverse = reverse + w[len (w) - i]
    
    return reverse 

print(reversal("potato"))
