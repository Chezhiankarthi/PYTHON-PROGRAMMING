num=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
print(*a,sep="")
