n = int(input())
l = list(map(int, input().split()))

xor = 0
for i in l:
  xor ^= i
 
for i in range(1,n+1):
  xor ^= i
 

rsb = (xor & -xor)

x = 0
y = 0
for i in l:
  if((i&rsb)==0):
    x ^= i
  else:
    y ^= i
 

for i in range(1,n+1):
  if((i&rsb)==0):
    x ^= i
  else:
    y ^= i
  
 
if x in l:
  print("missing number ->", y)
  print("duplicate number ->", x)
else:
  print("missing number ->", x)
  print("duplicate number ->", y) 