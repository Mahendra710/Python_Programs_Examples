# import math
# print(math.gcd(34,44))


def evaluateGCD(a,b):
    if b==0:
        return a
    else:
        return evaluateGCD(b,a%b)
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print(evaluateGCD(num1,num2))
