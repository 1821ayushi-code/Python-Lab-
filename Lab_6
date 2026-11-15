'''
#1
print("                     Addition Table")
for i in range(1,10):
    if i==1:
        print("       ",i,end="")
    else:
        print("    ",i,end="")
print()
print("   ","-"*55)
for i in range(1,10):
    print(i,"|",end=" ")
    for j in range(1,10):
        print(f"{i+j:>5}",end=" ")
    print()


#2
n=int(input())
i=0
while i!=1001:
    if i%n==0 and i%4!=0:
        print(i,end=" ")
    i=i+1


#3
#A
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i+1


#B
n=int(input())
i=n
while i>0:
    j=1
    while i>=j:
        print('*',end=" ")         
        j=j+1
    print()
    i=i-1
    
#C
n=int(input())
i=n
while i>0:
    j=1
    while i>=j:
        print(' ',end=" ")         
        j=j+1
    print()
    i=i-1
    i=1
while i<=n:
    j=1
    while i>=j:
        print('*',end=" ")         
        j=j+1
    print()
    i=i+1

#4
n=int(input())
octalnum=''
while n>0:
    digit=n%8
    octalnum=str(digit)+octalnum
    n=n//8
print(octalnum)


#5
n=int(input('Enter the total data frequency:'))
data=int(input())
largest=data
for i in range(n-1):
    data=int(input())
    if data>largest:
        seclarge=largest
        largest=data
print()
print(largest)
print(seclarge)


#6
n=int(input())
for i in range(1,n+1):
    sum=0
    digit=i
    for j in range(i):
        sum+=(digit%10)**len(str(i))
        digit=digit//10
    if sum==i:
        print(i)
        
        
#7
print(f"{'N':<5}{'N^2':<7}{'N^3':<8}{'Square Root':<10}")

for i in range(1,16):
    print(f"{i:<5}{i**2:<7}{i**3:<8}{i**(1/2):.4f}")
    
    
#8
n=int(input())
for i in range(1,n+1):
    print(' '*(n+1-i),end='')
    for j in range(i):
        print(i,end=' ')
    print()
    
    
#9
n=int(input())
sum=1
for i in range(1,n+1):
    for j in range(i):
        print(sum,end=' ')
        sum+=1
    print()
    
    
#10
n=int(input())
for i in range(1,((n+1)//2)+1):
    print(' '*(n+1-i),end='')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(((n+1)//2)-1,0,-1):
    print(' '*(n+1-i),end='')
    for j in range(i):
        print('*',end=' ')
    print()
'''
























