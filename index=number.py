num=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(num):
  if(a[i]==i):
    b.append(a[i])
if(len(b)==0):
  print("-1")
print(*b)
