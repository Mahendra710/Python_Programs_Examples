sentence=input("Enter the sentence:")
string=sentence.lower()
print(string)
count=0
list=["a","e","i","o","u"]
for char in string:
    if char in list:
        count=count+1
print("number of vowels in sentence:",count)