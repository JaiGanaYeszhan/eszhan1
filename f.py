n=int(input())
a=[]
for i in range(n):
   a.append(int(input()))
for i in range(len(a)):
   if a[i]<=10 :
       print('Go to work!')
   if 10>a[i] and a[i]<=25 :
       print('You are weak')
   if a[i]>25 and a[i]<=45 :
       print('Okay, fine')
   if 45<a[i] :
       print('Burn! Burn! Burn Young!')