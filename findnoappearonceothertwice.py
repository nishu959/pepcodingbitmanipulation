import sys
n = int(input())
l = list(map(int, input().split()))


tn =sys.maxsize
tnp1 = 0
tnp2 = 0
for i in l:
  cwtn = tn & i
  cwtnp1 = tnp1 & i
  cwtnp2 = tnp2 & i
  
  tn = (tn & (~cwtn)) 
  tnp1 = (tnp1 | cwtn)
  
  tnp1 = (tnp1 & (~cwtnp1))
  tnp2 = (tnp2 | cwtnp1)
  
  tnp2 = (tnp2 & (~cwtnp2))
  tn = (tn | cwtnp2)
 
print(tnp1)