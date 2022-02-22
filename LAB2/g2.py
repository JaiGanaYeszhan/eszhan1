a={}
n =int(input()) 
for i in range(n):
    b = input().split()[1]
    if b in a:
        a[b]+=1
    else:
        a[b]=1 
m = int(input())           
for i in range(m):
    b = input().split() 
    if b[1] in a.keys():
        if a[b[1]]<=int(b[2]): 
            a[b[1]] = 0
        else:
            a[b[1]] -= int(b[2])
print('Demons left:', sum(a.values()))