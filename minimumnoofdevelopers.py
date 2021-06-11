answ = ""
def ans(op, ip, m, p, n, answer):
  if ip==m:
    if (op==((1<<n)-1)):
      global answ
      if((len(answ)==0) or (len(answer)<len(answ))):
        answ = answer
    return
    

  op1 = op
  op2 = op
  op2 = op2 | p[ip]
  ans1 = answer
  ans2 = answer
  ans2 = ans2 + str(ip)
  ip += 1
  ans(op1, ip, m, p, n, ans1) 
  ans(op2, ip, m, p, n, ans2)
  
  return


n = int(input())
l = {}

t = list(map(str,input().split()))
for i in range(n):
  l[t[i]] = i

m = int(input())
p = {}
for i in range(m):
  p[i] =0
  
for i in range(m):
  t = list(map(str,input().split()))
  for j in t:
    p[i] = p[i] | (1 << l[j])
    



ans(0,0,m,p, n,"")

print(answ)