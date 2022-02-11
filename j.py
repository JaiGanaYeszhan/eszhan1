n=int(input())
s=[]
for i in range(n):
   s.append(str(input()))
for i in s:
   if i[len(i)-10:len(i)]=="@gmail.com":
       i=i[0:len(i)-10]
       print(i)