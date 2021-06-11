m= int(input())
n= int(input())

flipbit = m^n
count = 0
while(flipbit!=0):
  rsb = (flipbit & (-flipbit))
  flipbit -= rsb
  count +=1
 
print(count)