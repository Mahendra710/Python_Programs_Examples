q1="""What is the output of this 32*2 ?
a. 16
b. 64
c. 32
d. 48
"""
q2="""Which of the following is not a keyword?
a.eval
b.assert
c.local
d.pass"""
q3="""Which one of these is floor division?
a,/
b.//
c.%
d.None"""
q4="""What is the output of this 3*1**3?
a.27
b.9
c.3
d.1"""
q5=""""a"+"bc"==?
a.a
b.bc
c.bca
d.abc"""

questions={q1:"b",q2:"a",q3:"b",q4:"c",q5:"d"}

name=input("Enter your name:")
print("Hello",name,"Welcome to the quiz world")
score=0
for i in questions:
    print()
    print(i)
    skip=input("Do you want to skip this question(yes/no):")
    if skip=="yes":
        continue
    ans=input("Enter the Answer(a/b/c/d):")
    if ans==questions[i]:
        print("Correct Answer,you got 1 point")
        score=score+1
        print("Current Score is :",score)
    else:
        print("Wrong Answer,You lost 1 point")
        score=score-1
        print("Current Score is :",score)
    quit=input("Do you want to quit (yes/no):")
    if quit=="yes":
        break
print("Final score is :",score)
