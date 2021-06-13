n = int(input())

flag = False
rev =0
j =0
#for printing binary
for i in range(31,-1,-1):
  mask =(1<<i)
  if(flag):
    if ((n & mask)!=0):
      print(1,end="")
      smask = (1<<j)
      rev = (rev |smask)
      
    else:
      print(0,end="")  
    j += 1
  else:
    if((n & mask)!=0):
      flag = True
      print(1,end="")
      smask = (1<<j)
      rev = (rev |smask) 
      j += 1
print()
print(rev)