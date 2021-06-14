n = int(input())

def getrev(n):
  rev = 0
  while(n!=0):
    lb = (n & 1)
    rev = rev | lb
    n = n >> 1
    rev = rev <<1
  rev = rev >> 1
  return rev


count = 1
l = 1
while(count <n):
  l+=1
  eftl = (1<<((l-1)//2))
  count += eftl
  
count = count - (1<<((l-1)//2))
offset = n-count-1

ans = (1<<(l-1))
ans |= (offset<<(l//2))

vfr = (ans >> (l//2))

rev = getrev(vfr)

print(bin(rev |ans)[2:])
