n=input()
a=list(map(int,input().split()))
b=[]
for i in a:
  if(a.count(i)>1):
    if i not in b:
      b.append(i)
if(len(b)==0):
    print("unique")
b.sort()
print(*b)
