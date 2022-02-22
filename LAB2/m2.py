r=[]
while True:
    a = input().split()
    if a[0]=='0':
        break
    r.append(a[::-1])
r.sort()
for i in r:
    print(*i[::-1])