str1=input("string 1:")
str2=input("string 2:")
sorted_str1=sorted(str1)
sorted_str2=sorted(str2)
if len(str1)==len(str2):
    if sorted_str1==sorted_str2:
        print("Given strings are Anagrams")
    else:
        print("Given strings are not Anagrams")
else:
     print("Given strings are not Anagrams")
