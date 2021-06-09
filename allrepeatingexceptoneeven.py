n = int(input())
l = list(map(int, input().split()))

uni = 0

for i in l:
  uni ^= i
 
print(uni)