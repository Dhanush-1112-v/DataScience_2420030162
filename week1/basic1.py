#Greast among three numbers
a=30
b=20
c=45
if a>b and a>c:
    print("a is greatest")
elif b>c:
    print("b is greatest")
else:
    print("c is greatest")
#EVEN OR ODD
n=int(input("Enter a number: "))
if n%2==0:
    print("Even number")
else:
    print("Odd number")    

#Grade of the student 3 subjects
sub1=int(input("Enter marks of subject 1: "))
sub2=int(input("Enter marks of subject 2: "))
sub3=int(input("Enter marks of subject 3: "))
total=sub1+sub2+sub3
avg=total/3
if avg>=90:
    print("Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=70:
    print("Grade C")
else:
    print("FAIL")    

#FOR LOOP
fruits=["Apple","Banana","Mango"]
for i in fruits:
    print(i)

for x in range(5):
    print(x)

#printing even numbers from 1 to 100
for i in range(1,101):
    if i%2==0:
        print(i)
        2
#palindrome number
n=int(input("Enter a number: "))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")


#prime or not
n=int(input("Enter a number: "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

#funtions
def cal_sum(data1, data2):
    result=data1+data2
    return result
result=cal_sum(10,20)
print("The sum is:",result)