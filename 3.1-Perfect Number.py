# 6=1,2,3,6    1+2+3==6 then it is perfect number

num=int(input("Enter the number\n"))
sum=0
for i in range(1,num):
    if (num%i)==0:
        sum=sum+i
if sum==num:
    print("YES it is perfect number")
else:
    print("NO, It is not perfect number")