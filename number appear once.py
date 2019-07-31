num=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
  if(a.count(i)<2):
    if i not in b:
      b.append(i)
print(*b)
