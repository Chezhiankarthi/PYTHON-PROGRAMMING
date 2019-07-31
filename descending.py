num=int(input())
a=list(map(int,input().split()))[:num]
a.sort(reverse=True)
if a[0]==0:
  print("0")
else:
  print(*a,sep="")
