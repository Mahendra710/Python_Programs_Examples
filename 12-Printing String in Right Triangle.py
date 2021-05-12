n=input("Enter a string\n")
length=len(n)
for a in range(length):
    for b in range(a+1):
        print(n[a],end=" ")
    print()