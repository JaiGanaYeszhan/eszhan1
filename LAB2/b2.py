input()
a = input().split()
for i in range(len(a)):
    a[i]=int(a[i])
a.sort()
product = a[-1]*a[-2]
print(product)

