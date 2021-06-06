n = int(input())
count = 0

while(n!=0):
  rsbm = n & -n
  n = n - rsbm
  count +=1
 
print(count)