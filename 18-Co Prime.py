from math import gcd
num1=int(input("number1:"))
num2=int(input("number2:"))

if gcd(num1,num2)==1:
    print(num1,"and",num2,"are co-prime")
else:
    print("not coprime")


    # SECOND TYPE

num=int(input("number:"))
lower=int(input("lower limit:"))
upper=int(input("upper limit:"))
for i in range(lower,upper+1):
    if gcd(num,i)==1:
        print(i)

