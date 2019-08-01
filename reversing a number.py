num=int(input())
r=0
while(num>0):
  dig=num%10
  r=r*10+dig
  num=num//10
print(r)
