'''
#1
s=int(input('Give Salary:'))
y=int(input('Years Of Service:'))
nb=s*0.05
if y>=5:
    print('Net Bonus Amount:Rs.',nb)
else:
    print('No Bonus')

#2
x=str(input('Give Password:'))
y="s3cr3t!P@ssw0rd"
if x==y:
    print('Welcome')
else:
    print('Wrong Password')

#3
shape=str(input('Give Shape:'))
if shape=='circle':
    r=int(input('Give Radius:'))
    area=(22/7)*r*r
    print('Area Of Circle is:',f"{area:.3f}")
elif shape=='rectangle':
    l=int(input('Give Length:'))
    b=int(input('Give Width:'))
    area=l*b
    print('Area Of Rectangle is',f"{area:.3f}")
elif shape=="square":
    s=int(input('Give Side Of Square:'))
    area=s*s
    print('The Area Of The Square Is',f"{area:.3f}")
elif shape=='triangle':
    b=int(input('Give Base:'))
    a=int(input('Give Altitude:'))
    area=0.5*b*a
    print('The Area Of The Triangle Is:',f"{area:.3f}")
else:
    print('Invalid Input.')

#4
h=int(input("Enter Hours (0-23):"))
m=int(input("Enter Minutes (0-59):"))
m += 15
if m>=60:
    m -= 60
    h = h+1
if h >=24:
    h=h%24
if m<10:
    print(h,":0",m, sep="")
else:
    print(h,":",m, sep="")

#5
k=float(input("Enter Kilometres:")) 
p=input("Enter day or night:")

if p == "day":
   taxi=33.58 + k*37.89
else:
    taxi=33.58 + k*43.17
cheapest = taxi

if k>=20:
    bus = k*4.32
    if bus<cheapest:
        cheapest=bus

if k>=100:
    train=k*2.88
    if train<cheapest:
        cheapest=train
print("Cheapest Transport Price:",cheapest)

#6
hd=int(input("No. Of Holidays:"))
wd=365-hd
total=hd*127 + wd*63
if total<30000:
    nd= 30000-total
    print("Tom Can Sleep Well.","\nThe Difference from the Norm:",nd)
else:
    nd=total-30000
    print("Tom cannot Sleep Well.","\nThe Difference from the Norm:",nd)

#7
bud=int(input("Give Budget:"))
sea=input("Give Season (Summer or Winter):")
if bud<=100:
    print("Vacation Place: Bulgaria.")  
    if sea=="Summer":
        x=0.3*bud
        print("Money to Spend:",x)
    else:
        sea=="Winter"
        x=0.7*bud
        print("Money to Spend:",x)
elif bud<=1000:
    print("Vacation Place: Balkans.")  
    if sea=="Summer":
        x=0.4*bud
        print("Money to Spend:",x)
    else:
        sea=="Winter"
        x=0.8*bud
        print("Money to Spend:",x)
elif bud>1000:
    print("Vacation Place: Europe.")  
    if sea=="Summer":
        x=0.9*bud
        print("Money to Spend:",x)
    else:
        sea=="Winter"
        x=0.9*bud
        print("Money to Spend:",x)

#8
i=6
while i<=1000:
    print(i)
    i=i+10

#9
n=int(input("Enter total no.:"))
s=0
for i in range(n):
    a=int(input("Enter no.:"))
    s+=a
print("Sum=",s)

#10
n=int(input("Give Number:"))
for i in range(1,21):
    print(n,"X",i,"=",i*n)
'''