
def tsb(n):
  c = 0
  while(n!=0):
    rsb = (n & -n)
    n -= rsb
    c += 1
  return c
 
def ncr(n, r):
  if r>n:
    return 0
  r = 1
  for i in range(0,r):
    r = r * (n-i)
    r = r // (i+1)
  return r
 

def solution(n, s, tb):
  if tb==0:
    return 0
  res = 0
  mask = 1 << tb
  if((n&mask==0)):
    res = solution(n, s, tb-1)
  else:
    res1 = solution(n, s-1,tb-1)
    res2 = ncr(tb, s)
    res = res1 + res2
    
  return res
  
  
n = int(input()) 
s = tsb(n)
print(solution(n, s, 63)) 
    
  