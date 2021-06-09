n = int(input())
l= list(map(int, input().split()))

xor = 0
for i in l:
  xor = xor ^ i
  
rsb = (xor & (-xor)) 
x = 0
y =0
for i in l:
  if (i & rsb)==0:
    x = x ^ i
  else:
    y = y ^ i
    
    
if (x>y):
  print(y)
  print(x)
else:
  print(x)
  print(y)
  
    
