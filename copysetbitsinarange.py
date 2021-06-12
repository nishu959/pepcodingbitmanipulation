r = int(input())
l = int(input())
a= int(input())
b= int(input())


m1 =1
m2= (m1<<(r-l+1)) #10000 type
m2 -= 1           #01111 type
m3 = (m2<<(l-1))  #111100.... Type


fm = (a & m3)   #this mask has the bits between l to r same as a
b = (b | fm) 

print(b)

#print(bin(30))