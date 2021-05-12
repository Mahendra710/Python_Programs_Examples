# num=int(input("Enter the number:"))
# reverse=int(str(num)[::-1])
# if num==reverse:
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 print(num,"is not prime number! but it is palindrome")
#                 break
#         else:
#             print(num,"is palindromic prime number")
# else:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not prime number! as well as it is not palindrome")
#             break
#     else:
#         print(num, "is prime number but it is not palindrome")





# SECOND TYPE:


lower=int(input("Enter the lower number:"))
upper=int(input("Enter the upper number:"))
for num in range(lower,upper+1):
    reverse=int(str(num)[::-1])
    if num==reverse:
        if num>1:
            for i in range(2,num):
                if (num%i)==0:

                     break
            else:
                print(num,"is palindromic prime number")

