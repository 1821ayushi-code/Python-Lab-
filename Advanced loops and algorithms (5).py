'''
A
#1
x=int(input("Give First Number:"))
y=int(input("Give Second Number:"))
n=int(input("Give Third Number(N):"))
for i in range(x+1,y+1):
    if i%n==0:
        print(i)


#2
n=int(input("Give A Positive Integer:"))
sum=0
i=1
while n!=0:
    y=n%10
    n=n//10
    i+=1
    sum+=y
print(sum)


#3
N=int(input("Give A Positive Integer:"))
i=0
n=0
c=0
d=0
e=0
while n!=-999:
    n=int(input("Give A Integer:"))
    if n%N==0:
        c+=1
    elif n==-999:
        e+=1
    else:
        d+=1
    i+=1
print("No. Divisible By N:",c)
print("No. Not Divisible By N:",d)


#4
n=int(input("Give A positive Integer:"))
multiply=1
for i in range(1,n+1):
    multiply*=i
print(multiply)


#5
n=int(input("Give A Positive Integer:"))
rev=0
v=n
while n>0:
    digit=n%10
    rev=rev*10 + digit
    n=n//10
print(rev)

if rev==v:
    print("Pallindrome")
else:
    print("Not A Pallindrome")


#6
n=int(input("Give Positive Number For Fibonacci Series:"))
a=1
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c


#7
n=int(input("Give Integer No.:"))
if n<=1:
    print("Invalid.")
else:
    f=0
    for i in range(2,n):
        if n%i==0:
            f=1
            break
if f==0:
    print("Prime.")
else:
    print("Not Prime.")


#8
s=input('Enter a sentence:')
i=0
capital=0
small=0
digit=0
special=0

while 

'''





'''
#B
#1
x=int(input("Starting Number(1<=x):"))
y=int(input("End Number(y<=10000):"))
n=int(input("Number To Divide:"))
count=0
for i in range(x,y):
    if i%n==0:
        print(i, end=" ")
        count+=1
        print("Total No is:",count)


#2
n=int(input("Give A Positive Integer:"))
product=1
while n>0:
    lastdigit=n%10
    product=product*lastdigit
    n=n//10
   
print("Product Of Digits:", product)


#3
n=int(input("Give The Integer N:"))
x=0
large=0
small=0
a=0
while x!=-999:
    x=int(input("Give The Bill Amount:"))
    if x>n:
        large+=1
    elif x==-999:
        a+=1
    else:
        small+=1
print("Total Large Bills:", large)
print("Total Small Bills:", small)


#4
n=int(input("Give First Positive Integer:"))
p=int(input("Give Second Positive Integer:"))
i=1
r=1
while i!=p+1:
    r=r*n
    i+=1
print(r)

  
#5
n=int(input("Give First Positive Integer:"))
p=int(input("Give Second Positive Integer:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10 + digit
    n=n//10
if rev==p:
    print("Exact Reverse.")
else:
    print("Not Exact Reverse.")


#6
n=2
p=int(input("Give Positive Integer:"))
i=1
r=1
while i!=p+1:
    r=r*n
    print(r,end=" ")
    i+=1


#7
n=int(input("Give The Integer:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("Its A Perfect Number.")
else:
    print("Its Not A Perfect Number.")


#8
n=int(input("Give A Positive Integer:"))
for i in range(n+1):
    print("*"*i)


#9
n=int(input("Enter A Integer:"))
d=int(input("Enter A Single Digit:"))
sum=0
while n!=0:
    x=n%10
    n=n//10
    if x==d:
        sum+=1
print("No. Of Times Appeared:",sum)


#10
n=int(input("Give A Positive Integer:"))
sum=0
for i in range(1,n+1):
    if n%i==0:
        print(i)
        sum+=1
print("Total Count Of Divisors:",sum)
if sum>2:
    print("Integer is Not a Prime Number.")
else:
    print("Integer is a Prime Number.")
'''













