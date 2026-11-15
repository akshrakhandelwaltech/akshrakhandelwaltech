#lab 5(a)

#question 1
x=int(input("enter a number: "))
y=int(input("enter a number: "))
n=int(input("enter n: "))
if x<y :
    for i in range(x,y+1) :
        if i%n==0 :
            print(i,end=" ")
        i+=1
else :
    print("enter first number smaller than second one")

#question 2
n=int(input("enter a number: "))
sum=0
while n!=0 :
    x=n%10
    n=n//10
    sum+=x
print(sum)

#question 3
n=int(input("enter a n: "))
i=0
total=0
sum=0
while i!=-999 :
    i=int(input("enter a number: "))
    if i%n==0 :
        sum+=1
print("numbers divisible by",n, "=",sum)
print("numbers not divisible by",n, total-sum)

#question 4
n=int(input("enter a number: "))
pro=1
for i in range(1,n+1) :
    pro*=i
    i+=1
print(pro)

#question 5
n=int(input("enter a number: "))
v=n
sum=0
while n!=0 :
    x=n%10
    n=n//10
    sum=sum*10 + x
print(sum)
if sum==v :
    print("it's a palindrome")
else :
    print("it's not a palindrome")

#question 6
a=0
b=1
n=int(input("enter a number: "))
for i in range(n) :
    temp=a
    a=b
    b=temp+b
    print(a,end=" ")

#question 7
n=int(input("enter a number: "))
is_prime=True
for i in range(2,n) :
    if n%i==0 :
        is_prime=False
    i+=1
if is_prime :
    print("prime")
else :
    print("not prime")

#question 8
a=input("enter a sentence: ")
c=0
s=0
d=0
sp=0
for i in a :
    if i!=" " :
        if i.isalpha() :
            if i.islower() :
                s+=1
            else :
                c+=1
        elif i.isdigit() :
            d+=1
        else :
            sp+=1
print("capital letters:",c)
print("small letters:",s)
print("digits:",d)
print("special characters:", sp)
    