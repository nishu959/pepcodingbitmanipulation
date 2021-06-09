n = int(input())

l = list(map(int, input().split()))
c =0
for i in range(0,len(l)):
  val = l[i]
  for k in range(i+1,len(l)):
    val ^= l[k] 
    if (val==0):
      c += k - i
     
print(c)
   