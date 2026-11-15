#lab 5(b)


#question 1
x=int(input("enter x: "))
y=int(input("enter y: "))
n=int(input("enter n: "))
digit=0
for i in range(x,y) :
    if i%n!=0 :
        print(i,end=" ")
        digit+=1
print()
print(digit)




#question 2
n=int(input("enter n: "))
pro=1
while n!=0 :
    x=n%10
    n=n//10
    pro=pro*x
print(pro)




#question 3
n=int(input("enter n: "))
b=0
digit=0
sum=0
while b!=-999 :
    b=int(input("enter bill: "))
    if b==-999 :
        break
    if b>n :
        digit+=1
    else :
        sum+=1
print(digit)
print(sum)

#question 4
n=int(input("enter n: "))
p=int(input("enter p: "))
pro=1
for i in range(p) :
    pro*=n 
print(pro)

#question 5
a=int(input("enter a number: "))
b=int(input("enter a number: "))
num=0
while a!=0 :
    x=a%10
    a=a//10
    num=num*10 +x
if num==b :
    print("second number is the exact reverse of the first one")
else :
    print("second number is not the exact reverse of the first one")

#question 6
n=int(input("enter a number: "))
pro=1
for i in range(n) :
    print(pro,end=" ")
    pro*=2

#question 7
n=int(input("enter a number: "))
sum=0
for i in range(1,n) :
    if n%i==0 :
        sum+=i
if sum==n :
    print("perfect number")
else :
    print("not a perfect number")

#question 8
n=int(input("enter a number: "))
for i in range(n) :
    for j in range(i+1) :
        print("*",end=" ")
    print()

#question 9
d=int(input("enter a digit: "))
n=int(input("enter a number: "))
a=0
while n!=0 :
    x=n%10
    if x==d :
        a+=1
    n=n//10
print(a)

#question 10
n=int(input("enter a number: "))
sum=0
for i in range(1,n+1) :
    if n%i==0 :
        print(i)
        sum+=1
print("total divisors:",sum)
if sum>2 :
    print("not a prime number")
else :
    print("prime number")