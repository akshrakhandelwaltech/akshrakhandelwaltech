#lab 8

#question 1
a=input("enter a sentence: ")
v=0
c=0
d=0
s=0
o=0
for i in a :
    if i.isalpha() :
        if i in "aeiouAEIOU" :
            v+=1
        else :
            c+=1
    elif i.isdigit() :
        d+=1
    elif i==" " :
        s+=1
    else :
        o+=1
print("vowels=",v)
print("consonants=",c)
print("spaces=",s)
print("other symbols=",o)

#question 2
a=input("enter a string: ")
b=""
for i in range(len(a)) :
    c=a[i]
    if i%2==0 :
        c=c.upper()
    else :
        c=c.lower()
    b+=c
print(b)

#question 3
a=input("enter the password: ")
u=0
l=0
d=0
s=0
t=0
for i in a :
    if i.isalpha() :
        if i.isupper() :
            u+=1
        else :
            l+=1
    elif i.isdigit() :
        d+=1
    else :
        if i!=" " :
            s+=1
    t+=1
if t<8 :
    print("weak")
else :
    if u>0 and l>0 and d>0 and s>0 :
        print("strong")
    elif u>0 or l>0 or d>0 or s>0 :
        print("moderate")
    else :
        if u>0 and l==0 and d==0 and s==0 :
            print("weak")
        if u==0 and l>0 and d==0 and s==0 : 
            print("weak")
        if u>0 and l==0 and d>0 and s==0 : 
            print("weak")
        if u==0 and l==0 and d==0 and s>0 : 
            print("weak")

#question 4
a=input("enter a string: ")
b=input("enter a character: ")
c=0
d=" "
for i in range(len(a)) :
    if a[i]==b :
        c+=1
        d+=str(i) +" "
if c>0 :
    print("count:",c)
    print("positions:",d)
else :
    print("count:",c)
    print("positions: -1")

#question 5
a=input("enter a sentence: ").split()
for i in a :
    print(len(i),end=" ")

#question 6
a=input()
if len(a)==10 :
    if (
        a[0]=="R"
        and a[1]=="J"
        and a[2].isdigit()
        and a[3].isdigit()
        and a[4].isupper()
        and a[5].isupper()
        and a[6].isdigit()
        and a[7].isdigit()
        and a[8].isdigit()
        and a[9].isdigit()
    ) :
        print("true")
    else :
        print("false")
else :
    print("false")

#question 7
a=input("enter a sting: ")
i=1
t=0
j=0
if len(a)%2!=0 :
    n=int((len(a)-1)/2)
    for k in range(n) :
        if a[n+i]!=a[n-i] :
            t+=1
        i+=1
else :
    n=int(len(a)/2)
    for k in range(n) :
        if a[n-i]!=a[n+j] :
            t+=1
        i+=1
        j+=1
print("changes needed:",t)

#question 8
a=input("enter a string: ")
b=""
for i in a :
    if i not in b :
        b+=i
print(b)

#question 9
a=input("enter the code: ")
s=int(input("enter the shit: "))
d=""
for i in a :
    if i.isalpha() :
        b=ord(i)
        c=b+s
        if c<=ord("z") :
            j=chr(c)
        elif c>ord("z") :
            j=chr(c-26)
    else :
        if i==" " :
            j=" "
    d+=j
print(d)

#question 10
a=input("enter a string: ")
l=0
s=0
p=""
for i in a :
    if i==p :
        l+=1
    else :
        l=1
        p=i
    if l>s :
        s=l
        m=i
print(m, s)
