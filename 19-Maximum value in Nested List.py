list2=[]
def get_max(list1):
    for i in list1:
        if type(i)==list:
            get_max(i)
        else:
            list2.append(i)

    return max(list2)

list1=[12,2,[2,3,45,32],35,7]
print(get_max(list1))