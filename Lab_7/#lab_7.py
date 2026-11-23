#lab_7.py

#question 1
a=input("enter a string: ")
b=""
for i in range(-1,-len(a)-1,-1) :
    b+=a[i]
print(b)

#question 2
a=input("enter a sentence: ")
b=a.split()
print(len(b[-1]))

#question 3    using inbuilt string functions
a=input("enter a word: ")
b=input("enter a sentence: ")
c=b.split()
d=0
for i in c :
    if a==i :
        d+=1
if d==0 :
    print(a,"doesn't occur in","'",b,"'")
else :
    print(a,"occors",d,"times in","'",b,"'")

#question 3            without using inbuilt string functions
a=input("enter a sentence: ")
b=input("enter a word: ")
c=""
d=""
a=a+" "
cnt=0
for i in a :
    if i==" " :
        c=d
        d=""
        if c==b :
            cnt+=1
            c=""
        continue
    d=d+i
print(cnt)

#question 4
a=input("enter a string: ")
b="abcdefghijklmnopqrstuvwxyz"
c=a.lower()
flag=True
for i in b :
    if i not in c :
        flag=False
        break
    else :
        continue
if flag :
    print("Pangram")
else :
    print("Not a pangram")

#question 5
key=input("enter a string: ")
shift=int(input("enter a number: "))
k=key.lower()
n=""
for i in key :
    if i!=" " :
        a=ord(i)
        b=a+shift
        if b<=ord("z") :
            c=chr(b)
        elif b>ord("z") :
            c=chr(b-26)
        n=n+c
print(n)

#question 7
a=input("enter a string: ")
b=""
c=""
for i in a :
    if i!=" " :
        b+=i
for i in range(-1,-len(b)-1,-1) :
    d=b[i]
    c+=d
if c==b :
    print("palindrome")
else :
    print("not a palindrome")

#question 8
#(i)
n=int(input("enter n: "))
a=[]
b=0
for i in range(n) :
    e=int(input())
    a.append(e)
for i in a :
    b+=i
print(b)

#(ii)
n=int(input("enter n: "))
a=[]
b=1
for i in range(n) :
    e=int(input())
    a.append(e)
for i in a :
    b*=i
print(b)

#(iii)
n=int(input("enter n: "))
a=[]
for i in range(n) :
    e=int(input())
    a.append(e)
b=a[0]
for i in range(1,len(a)) :
    if a[i]<a[0] :
        b=a[i]
print(b)

#question 9
n=int(input("enter a number: "))
a=[]
for i in range(n) :
    e=int(input())
    a.append(e)
for i in range(n) :
    for j in range(len(a)-1) :
        if a[j]<a[j+1] :
            a[j],a[j+1]=a[j+1],a[j]
print(a)

#question 10
a=input().split("-")
b=len(a)
c=""
for i in range(b) :
    for j in range(len(a)-1) :
        if a[j]>a[j+1] :
            a[j],a[j+1]=a[j+1],a[j]
for i in a :
    if i!=a[-1] :
        c+=i+"-"
    elif i==a[-1] :
        c+=i
print(c)

#question 11
b=input()
d=0
a=0
s=0
u=0
l=0
for i in b :
    if i.isdigit() :
        d+=1
    elif i.isalpha() :
        a+=1
        if i.isupper() :
            u+=1
        else :
            l+=1
    else :
        if i!=" " :
            s+=1
print("digits:",d)
print("alphabets:",a)
print("special characters:",s)
print("uppercase alphabets:",u)
print("lowercase alphabets:",l)

#question 12
a=input("enter a string: ")
b=""
for i in a :
    if i not in b :
        b+=i
print(b)