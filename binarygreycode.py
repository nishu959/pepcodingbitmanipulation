n = int(input())

def bgc(n):
  if n==1:
    return ["0","1"]
  l = bgc(n-1)
  s = []
  for i in range(0,len(l)):
    s.append("0" + l[i])
    
  for i in range(len(l)-1,-1,-1):
    s.append("1" + l[i])
    
  return s
 

print(bgc(n)) 

