n = input()
so =0
se =0
for i in range(len(n)):
  p = int(n[i]) 
  if(i%2==0):
    se += p
  else:
    so += p
    
if((so-se)%11==0):
  print(True)   
else:
  print(False)
    
  
