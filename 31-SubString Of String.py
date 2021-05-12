str1=input("Enter the string:")
list1=[]
for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        list1.append(str1[i:j])

print(list1)