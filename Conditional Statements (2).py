'''
#1
number=int(input("Write the Number:"))
if number%5==0:
    print("Hi")
else: print("Bye")

#2
x=int(input("Length of first parallel side:"))
y=int(input("Length of second parallel side:"))
h=int(input("Height of trapezoid:"))
Area=( x + y )/2* h
print(Area)

#3
h=float(input("Height(in m):"))
w=float(input("Weight(in kg):"))
b=w/(h*h)
print(b)
if b <= 18.5:
    print("You Are Underweight.")
elif 18.5<b<=25:
        print("You Have Normal Weight.")
elif 25<b<=30:
            print("You Are Slightly Overweight.")
elif 30<b<=35:
                print("You Are Obese.")
elif 35<b:
            print("You Are Clinically Obese.")
    
#4
Alpha = input("alphabets:")
if (Alpha == "a" or Alpha == "e" or Alpha == "i" or Alpha == "o" or Alpha == "u"):
   print("Vowel")
else: print("Consonant")

#5
ibc = 2.19*10**14
fbc = 4.68*10**14
pbc = (fbc/ibc)*100
x = pbc%1
if x<0.50:
    print(pbc//1)
else:
    print(pbc//1 + 1)
    
#6
x = int(input("Whole Number Of Months:"))
years = x//12
months = x%12
print(years, 'Years', months,'Months')

#7
color = input("Colour:")
mode = input("Code:")
if color==("blue") and mode==("steady"):
    print('Clear View...')
elif color==("blue") and ("flashing"):
    print('Clouds Due...')
elif color==("red") and mode("steady"):
    print('Rain Ahead...')
elif color==('red') and mode('flashing'):
    print('Snow Instead...')

#8
x = int(input("Total Costs:"))
y = int(input("Total Revenue:"))
if x == y:
    print('Break Even.')
elif x>y:
    print('Loss.')
else:
    print('Profit.')
    
#9
x = float(input('No. Of Widgets:'))
y = x*20
z = x*25
if x >= 100:
    print("Total Cost:", y)
else:
    print('Total Cost:', z)
    
#10
x = float(input('No. Of Pounds:'))
y = float(input('Amount Given:'))
z = x*2.50
change = y-z
remain = z-y
if y>=z:
    print('Change:', change, '$')
else:
    print('You Owe', remain, '$ more')
    
#11
x = int(input('Give 1st Number:'))
y = int(input('Give 2nd Number:'))
z = int(input('Give 3rd Number:'))
if x > y:
      if x>z:
        print('Max:', x)
      else:
        print('Max:', z)
else:
   if y>z:
    print('Max:', y)
   else:
    print('Max:', z)
    
#12
x = float(input('Base Salary:'))
gross = x*(20+10+5)/100
z = x + gross
print('Gross Salary:', z)

#13
sal = int(input('Gross Salary:'))
if sal>2500000:
    print('30% of the Gross Salary')
elif 1000000<sal<=2500000:
    print("20% of the Gross Salary")
elif 300000<sal<=1000000:
    print('10% of the Gross Salary')
else:
    print('No Tax')

#14
income=int(input('Enter Salary:'))
if income<=20000:
    print('Tax Is',0.02*income)
elif income<=50000:
    print('Tax Is',0.025*(income-20000)+400)
else:
    print('Tax Is',1150+0.035*(income-50000)) '''