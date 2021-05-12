def sumofdigits(n):
    res=0
    rem=0
    while n>0:
        rem=n%10
        res=res+(rem*rem)
        n=n//10
    return res

n=int(input("Enter the number:"))
result=n
while result!=1 and result!=4:
    result=sumofdigits(result)
if result==1:
    print(n,"is Happy Number")
else:
    print(n,"is not Happy Number")
