'''
#1
print("Hello JKLU" , "I am learning python")

#2
name2=str(input("enter the student name")) #str is string, description written inside the bracket, just for ex

name=input("Enter student name:")
branch=input("Enter the branch:")
print("Welcome! \n", name, branch)

#3
length = int(input("Length in metre:"))
width = int(input("Width in metre:"))
Area=length*width
print("The Area of the rectangular plot is:", Area, "sq. metre")

#4
length = int(input("Length in feet:"))
width = int(input("Width in feet:"))
Area=length*width
print("The Area of the rectangular plot is:", Area, "sq. metre")

len_m=length*0.3048 #feet to meter conversion

#5
x=int(input("Enter first positive integer:"))
y=int(input("Enter second positive integer:"))
if x>0 and y>0:
    if y % x ==0:
        print("Y is divisible by x")
    else:
        print("y is not divisible by x")
else:
    print("Invalid Input")
        
#6
x=int(input("Integer:"))
if x % 2 == 0:
    print("even")
else:
    print("Odd")
    
#7
r = int(input("Radius:"))
area = 3.14 *r *r
if 100>= r >=1:
    print('Area:', area, 'unit square')
else:
    print('Invalid input.')
    
#8
c = float(input("Temperature in Clecius:"))
F = c*1.8 + 32
K = c + 273.15
print('In Fahrenheit:', F, '\n' 'In Kelvin:', K)

#9
x = int(input("Give Seconds:"))
hour = x//3600
rem_sec = x%3600
minute = rem_sec//60
final_sec = rem_sec%60
if 86400>= x >=1:
    print(hour, ':', minute, ':', final_sec)
else:
    print('Invalid Input.')
    
#10
t = int(input("Total Classes:"))
a = int(input("Attended Classes:"))
percent = (a/t)*100
if percent>=75:
    print('Eligible.')
else:
    print('Not Eligible.')'''