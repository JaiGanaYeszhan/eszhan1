x=int(input())
y=str(input())
z=float(0.0)
t=float(0.0)
if y=='k' :
   a=int(input())
   t= x / 1024
   z = round(z, a)
   print(t)
if y=='b':
    y= x*1024
    print(t)