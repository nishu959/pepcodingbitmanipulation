
s = input()
l = 1 << len(s)
p = len(s)-1
for i in range(l):
  count =0
  a = ""
  for j in range(len(s)):
    q = (1<<(p-j))
    if ((i & q)==0):
      if count==0:
        a = a+s[j]
      else:
        a = a + str(count)
        a = a + s[j]
        count =0
    else:
      count+=1
  if count!=0:
    a = a +str(count)  
  
  print(a)
        
    
  
  
  

