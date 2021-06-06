#right most set bit


x =int(input())

print(bin(x&(-x))[2:])