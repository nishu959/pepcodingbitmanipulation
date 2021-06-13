def hp2(n):
  x =0
  while((1<<x) <= n):
    x+=1
  return (x-1)
 

def solve(n):
  if(n==0 or n==1):
    return n
  x = hp2(n)
  stn2 =0
  stn2 = x* (1<<(x-1))
  numnto2 = n - (1<<x) + 1
  remain = n - (1<<x)
  ans = stn2 + numnto2 + solve(remain)
  return ans
 
 
n = int(input())
print(solve(n))
    
    