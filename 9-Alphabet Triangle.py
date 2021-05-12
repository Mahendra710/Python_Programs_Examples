n=int(input("How many rows are there?\n"))
print(ord("A"))
for a in range(1,n+1):
    for b in range(1,a+1):
        print(chr(64+b),end=" ")
    print()
