x,y,z="orange","apple","banana"
print(x,y,z)

x=y=z="grapes"
print(x,y,z)

a="Sai Dhanush"
age=20
height=5.9
print(a)
print(age)
print(height)

A="Hello"
B=20
print(A,B ,sep=" ")

n=int(input("Enter the number of hi's you want to print: "))
for i in range(n):
    print("hi")

n=int(input("Enter your age: "))
if n>18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")    

# Apples=["Red","Green","Yellow"]
# Apple is red color,so we can say that Apple is Red color.
# i'm very happy to see you.you are my best friend.

x=122
y=55.5
z=1j
print(type(x))
print(type(y))
print(type(z))

q=int(1)
w=int(2.8)
print(q)
print(w)

q=float(1)
w=float(2.8)
print(q)
print(w)

q=str(1)
w=str(2.8)
print(q)
print(w)

#SCLICING OF STRING
text="KLH BOWREMPET"
print(text[2:5])

text="KLH BOWREMPET"
print(text[:5])

text="KLH BOWREMPET"
print(text[5:])

#Negative Indexing
text="KLH BOWREMPET"
print(text[-10:-4])

A="KONERU LAKSHMMAIAHA EDUCATION FOUNDATION"
print(A.lower())
print(A.find("E"))
print(A.capitalize())
print(A.swapcase())
print(A.title())
print(len(A))

#CONCATENATION OF STRING
A="KONERU"
B="LAKSHMMAIAHA"
C=A+" "+B
print(C)
#STRING FORMATTING
txt1="my name is {fname} and I am {age} years old".format(fname="Sai Dhanush",age=20)
txt2="my name is {0} and I am {1} years old".format("Sai Dhanush",20)
txt3="my name is {} and I am {} years old".format("Sai Dhanush",20)
print(txt1)
print(txt2)
print(txt3)