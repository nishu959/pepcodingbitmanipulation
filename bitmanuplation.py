#Bits are numbered from least significant bit to right significant bit
n= int(input())
i = int(input())
j = int(input())
k = int(input())
c = int(input())

#it left shift has less precedence then = so written in brackets
#for onmask | is used 1 is powerful
onmask = (1<<i)
#for offmask & is used 0 is powerful
offmask = ~(1<<j)
#for togglemask ^ is used 1 is powerful
togglemask = (1<<k)
#for checkmask & or | operator is used
checkmask = (1<<c)


print(n | onmask)
print(n & offmask)
print(n ^ togglemask)
if (n & checkmask==0) :
  print(False) 
else:
  print(True)
