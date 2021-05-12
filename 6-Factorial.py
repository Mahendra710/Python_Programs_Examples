n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print(f)


# n=int(input())
# fac=1
# if n<0:
#     print("error")
# elif n==0:
#     print(1)
# else:
#     for i in range(1,n+1):
#         fac=fac*i
#     print(fac)


# def fac(n):
#     fac=1
#     if n==0:
#         return 1
#     else:
#         for i in range(1,n+1):
#             fac=fac*i
#
#     return fac
# v=fac(4)
# print(v)


import math
r=math.factorial(n)
print(r)

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))