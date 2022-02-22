a = input().split()
for i in range(len(a)):
    a[i]=int(a[i])
if len(a)==2:
    b = a[1]
    for i in range(1, a[0]):
        b^=a[1]+2*i    
else:    
    x = int(input())
    b = x 
    for i in range(1, a[0]):
        b^=x+2*i
print(b)