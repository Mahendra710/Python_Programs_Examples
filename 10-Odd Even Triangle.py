n=int(input("How many rows are there?\n"))
for a in range(1,n+1):
    for b in range(1,a+1):
        if (a+b)%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()