a, b = input().split() 
a = int(a); b = int(b)
n = int(input())
s = []
s1 = []
for i in range(n):
    x, y = input().split()
    x = int(x); y = int(y)
    s.append(((a-x)**2+(b-y)**2)**(0.5)) 
    s1.append([x, y])
s2 = s.copy()
s.sort()
for i in range(n):
    print(*s1[s2.index(s[i])])