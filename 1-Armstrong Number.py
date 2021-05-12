# Armstrong Number

# A positive integer of n digits is called an Amstrong Number of order n
# EXAMPLE- Input=153
#          number=1*1*1* + 5*5*5 + 3*3*3 == 153
#          Output= yes 153 is an Armstorng Number

n=input("Enter a number to check it an Armstorng Number\n")
length=len(n)
n=int(n)
sum=0
num=n
while n>0:
      r=n%10
      sum=sum+(r**length)
      n=n//10
if sum==num:
    print(f"{num} is Armstorng Number")
else:
    print(f"{num} is not Armstorng Number")