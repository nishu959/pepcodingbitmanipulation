n = int(input())

c = 0
while(n!=1):
  if ((n&1)==0):#or if(n%2==0)
    n = n //2
    #n = (n>>1) can also be used
    
  elif(n==3):
    c += 2
    break
  elif((n & 3)==1):# or if(n%4==1)
    n = n - 1
  elif((n&3)==3):# or if(n%4==3)
    n = n +1
    
    
    
  c += 1
  
print(c)
  
#print(64>>1,64<<1)

#>> used for division
#<< used for multiplication
 
