a = input()
b=''
for i in a:
    if i not in ',.!?+-':
        b+=i
b1 = set(b.split())
print(len(b1), *sorted(b1), sep='\n')
