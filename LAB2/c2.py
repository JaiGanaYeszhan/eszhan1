a = int(input())
for i in range(a):
    for j in range(a):
        if i==j:
            print(i*j, end=' ')
        elif i==0 or j==0:
            print(i+j, end=' ')
        else:
            print('0', end=' ')
    print()
