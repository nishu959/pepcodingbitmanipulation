def hp2(n):
  i =1
  while(i*2<=n):
    i = i * 2   
  return i

def ans(n):
  hp = hp2(n)
  l = n - hp
  return (2*l+1)

n = int(input())
print(ans(n))

