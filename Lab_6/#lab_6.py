#lab_6.py

#question 1
for i in range(1,10) :
    for j in range(1,10) :
        print(f"{i+j:>2}",end=" ")
    print()

#question 2
n=int(input("enter n: "))
for i in range(1,1001) :
    if i%n==0 and i%4!=0:
        print(i,end=" ")
    else :
        continue

#question 3
#(a)
n=int(input("enter n: "))
for i in range(n) :
    for j in range(i+1) :
        print(j+1,end=" ")
    print()

#(b)
n=int(input("enter n: "))
for i in range(n) :
    for j in range(i,n) :
        print("*",end=" ")
    print()

#(c)
n=int(input("enter n: "))
for i in range(n) :
    for j in range(i,n-1) :
        print(" ",end=" ") 
    for j in range(i+1) :
        print("*",end=" ")
    print()

#question 4
n=int(input("enter a number: "))
sum=0
t=0
while n!=0 :
    x=n%8
    sum=sum*10 +x
    n=n//8
while sum!=0 :
    y=sum%10
    t=t*10+y
    sum=sum//10
print(t)

#question 5
n=int(input("enter n: "))
l=0
sl=0
for i in range(n) :
    x=int(input())
    if x>l :
        l=x
    elif x<l and x>sl :
        sl=x
print(l)
print(sl)


#question 6
n=int(input("enter n: "))
for i in range(1,n+1) :
    d=0
    s=0
    a=i
    b=i
    while a!=0 :
        y=a%10
        d+=1
        a=a//10
    while b!=0 :
        x=b%10
        s+=x**d
        b=b//10
    if s==i :
        print(i,end=" ")
    else :
        continue

#question 7
n=int(input("enter n: "))
print("N  N^2  N^3   square root")
for i in range(1,n+1) :
    for j in range(1) :
        print(i,f"{i**2:>3}",f"{i**3:>5}",f"{i**(0.5):.4f}")
    print()

#question 8
n=int(input("enter n: "))
for i in range(1,n+1) :
    print(" "*(n-i),end=" ")
    for j in range(i) :
        print(i,end=" ") 
    print()   

#question 9
n=int(input('enter n: '))
p=1
for i in range(n) :
    for j in range(i+1) :
        print(p,end=" ")
        p+=1
    print()

#question 10
n=int(input("enter n: "))
p=int((n+1)/2)
for i in range(p) :
    for j in range(i,p-1) :
        print(" ",end=" ")
    for j in range(i+1) :
        print("*",end=" ")
    for j in range(i) :
        print("*",end=" ")
    print()
for i in range(n-p) :
    for j in range(i+1) :
        print(" ",end=" ")
    for j in range(i,n-p) :
        print("*",end=" ")
    for j in range(i,n-p-1) :
        print("*",end=" ")
    print()