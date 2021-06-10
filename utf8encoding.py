n = int(input())

l = list(map(int, input().split()))
def fun(l):
  rbytes= 0
  for i in l:
    if rbytes==0:
      if((i>>7)==0):
        rbytes= 0
      elif((i>>5)==6):
        rbytes= 1
      elif((i>>4)==14):
        rbytes= 2
      elif((i>>3)==30):
        rbytes= 3
      else:
        return False
    else:
      if((i>>6==2)):
        rbytes -= 1
      else:
        return False
     

    
  if(rbytes!=0):
    return False  
  else:
    return True   

print(fun(l)) 