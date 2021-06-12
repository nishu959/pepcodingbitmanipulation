n = int(input())

l =list(map(int, input().split()))
s =0
for i in range(33):
  diff = 0
  counton =0
  for j in l:
    if((j & (1<<i))!=0):
      counton += 1
  countoff = len(l) - counton
  diff = counton * countoff *2
  s += diff
  
  
print(s)
