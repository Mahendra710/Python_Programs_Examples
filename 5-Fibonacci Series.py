# n=int(input("Enter your number\n"))  HERE n==7
a=0
b=1
print(a)
print(b)
for i in range(1,7):
    c=a+b
    a=b
    b=c
    print(c)
