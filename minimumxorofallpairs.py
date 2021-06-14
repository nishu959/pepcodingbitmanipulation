import sys 
minimum = sys.maxsize

n = int(input())

l = list(map(int, input().split()))
l.sort()
ans = []

for i in range(len(l)-1):
  xor = l[i] ^ l[i+1]
  if (xor < minimum):
    ans = []
    minimum = xor
    ans.append((l[i],l[i+1])) 
  elif(xor == minimum):
    ans.append((l[i],l[i+1]))
 

for i, j in ans:
  print(i,j, sep = ",")
    
  
