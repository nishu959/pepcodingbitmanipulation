n= int(input())

l = list(map(int, input().split()))
xor =0
for i in l:
  xor = xor ^ i
 
print(2*xor)