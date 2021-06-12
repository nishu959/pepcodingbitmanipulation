n = int(input())
#if number has total odd no. Of bit then consider msb bit as 0


em = 0xAAAAAAAA #we can use binary as well
om = 0x55555555

a =(n & em) 
b = (n & om) 

b =(b<<1) #left shift odd to cross even bit for swap
a = (a>>1) #right shift odd to cross odd bit for swap

p = a | b
print(bin(n))

print(bin(p))

