n = int(input())

words = list(map(str, input().split()))
m = int(input())
puzzle =  list(map(str, input().split()))



mp = {}

for i in range(26):
  mp[chr(ord('a')+i)]= set()

for i in words:
  mask = 0
  for j in i:
    bit = ord(j) - 97
    mask = mask | ((1<<bit))
    
    
  for j in i:
    mp[j].add(mask)
    
    
 
ans = []
for i in puzzle:
  pmask = 0
  for j in i:
    bit = ord(j) - 97
    pmask = pmask | ((1<<bit))
  fi =i[0]
  l = mp[fi]
  count = 0
  for i in l:
    if ((i & pmask) ==i):
      print(pmask)
      count += 1
  ans.append(count)
  

print(ans)