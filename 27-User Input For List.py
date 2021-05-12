# n=int(input("Length of List:"))
# list1=[]
# for i in range(n):
#     element=int(input("Enter the element:"))
#     list1.append(element)
#
# print(list1)
# 
import ast
list1=[]
while True:
    element =ast.literal_eval(input("Enter the element:"))
    list1.append(element)
    choice=input("Want to stop? If yes press yes otherwise press any key")
    if choice=="yes":
        break
print(list1)