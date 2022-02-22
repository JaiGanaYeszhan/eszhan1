a = []
b = []
n = int(input())
for i in range(n):
    z = input().split()
    if len(z)==2:
        a+=[z[1]]
    else:
        b+=[a[0]]
        del a[0]
print(*b)