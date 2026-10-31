'''
#1
x1=int(input('Enter X Coordinate Of Centre:'))
y1=int(input('Enter Y Coordinate Of Centre:'))
x2=int(input('Enter X Coordinate Of Second Point:'))
y2=int(input('Enter Y Coordinate Of Second Point:'))
r=int(input('Enter Radius:'))
d=((x2-x1)**2 + (y2-y1)**2)**0.5
if d>r:
    print('Point is Outside The Circle.')
elif r>d:
    print('Point Is Inside The Circle')
else:
    print('Point is On Boundary of The Circle')
    
#2
s=int(input('Enter Side Of Pentagon:'))
area=(5*s**2)/(4*0.726) #tan(pi/5)=0.726
print('Area:',area)

#3
a1=int(input('Enter First Angle:'))
a2=int(input('Enter Second Angle:'))
a3=int(input('Enter Third Angle:'))
if a1+a2+a3==180:
    if a1==a2==a3:
      print('Equilateral Triangle.')
    elif a1<90 and a2<90 and a3<90:
        print('Acute Angled Triangle.')
    elif a1>90 or a2>90 or a3>90:
        print('Obtuse Angled Triangle.')
    elif a1==90 or a2==90 or a3==90:
        print('Right Angled Triangle.')
else:
    print('Not a Triangle.')
    
#4
x=int(input('Enter 4 Digit Number:'))
a=x//1000
b=(x//100)%10
c=(x//10)%10
d=x%10
sum1=a+b
sum2=c+d
if sum1==sum2:
    print('The Two Sums Are Equal.')
else:
    print('The Two Sums Are Not Equal.')

#5
x=int(input('Enter The 5 Digit Number:'))
d1=x//10000
d2=(x//1000)%10
d3=(x//100)%10
d4=(x//10)%10
d5=x%10
largest=d1
position=1

if d2>largest:
    largest=d2
    position=2
if d3>largest:
    largest=d3
    position=3
if d4>largest:
    largest=d4
    position=4
if d5>largest:
    largest=d5
    position=5
print('Largest Digit:',largest,'\nPosition',position)

#6
a=int(input('Enter a Number:'))
b=int(input('Enter a Number:'))
c=int(input('Enter a Number:'))
a=a+b+c
b=a-b-c
c=a-b-c
a=a-b-c
print('a=',a)
print('b=',b)
print('c=',c)

#7
a=int(input('Enter a 3 digit No. :'))
d1=a//100
d2=(a//10)%10
d3=a%10
sum=d1+d2+d3
if a%sum==0:
    print('It is Harshad Number.')
else:
    print('It is Not a Harshad Number.')
    
#8
#Sum of GP of nth term=[a*(1-r**n)]/(1-r)
#Vn=V*(0.95)**n + {[1-(0.95)**n]/[1-0.95]}*10
n=int(input('Enter no. of days:'))
v=int(input('Give Initial Volume:'))
sum=(1-0.95**n)/0.05
vol=v*(0.95**n)+10*sum
print('Volume after',n,'days is:',vol)

#9
a1=int(input('Give Value of a1:'))
b1=int(input('Give Value of b1:'))
c1=int(input('Give Value of c1:'))
a2=int(input('Give Value of a2:'))
b2=int(input('Give Value of b2:'))
c2=int(input('Give Value of c2:'))
d=a1*b2-a2*b1
dx=c1*b2-c2*b1
dy=a1*c2-a2*c1
if d==0:
    if dx==0 and dy==0:
        print('The Lines Are Coincident.')
    else:
        print('The Lines Are Parallel.')
else:
    x=dx/d
    y=dy/d
    print(f"The Lines are Interesting at Point ({x:.2f}, {y:.2f})")'''