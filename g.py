def Todecimal(a): 
    if a == 1 or a == 0:
        return a
    return a%10 + 2*Todecimal(a//10) 
b = int(input()) 
print(Todecimal(b))