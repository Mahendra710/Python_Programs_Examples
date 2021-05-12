n=input("Enter a number To check is Prime or not\n")
n=int(n)
for i in range(2,n):
    if n%i==0:
        print(f"{n} is Not Prime Number")
        break
else:
    print(f"{n} is a Prime Number")


# Now check for in Range

lower=int(input("Enter lower Range"))
upper=int(input("Enter upper Range"))
for n in range(lower,upper):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)