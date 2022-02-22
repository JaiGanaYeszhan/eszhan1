a = input().split()
for i in range(len(a)):
    a[i]=int(a[i])
b = 1
for i in range(a.count(0)):
    f = a.index(0)
    if len(a)-1==f:
        break
    b = 0
    for i in range(1, f):
        if i + a[i]>f:
            a[f] = f-i; b=1; break
print(b)