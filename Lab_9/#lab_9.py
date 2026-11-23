#lab_9.py

#question 1
n=int(input("enter n: "))
a=[]
b=[]
for i in range(n) :
    e=int(input())
    if e%2==0 :
        a.append(e)
    else :
        b.append(e)
print("Even:",a)
print("Odd:",b)

#question 2
a=input("enter a sentence: ")
b=a.split()
c=[]
for i in b :
    if len(i)>3 :
        c.append(i)
print(c)

#question 3
a=list(map(str,input().split()))
print(a)
t=0
w=0
b=0
sum=0
c=[]
for i in a :
    if i.isdigit() :
        t+=int(i)
    if i=="w" :
        w+=1
    if i=="4" or i=="6" :
        b+=1
    sum+=1
print("Total Runs:",t)
print("Wickets:",w)
print("Boundaries:",b)
for i in range(0,sum,6) :
    v=0
    for j in a[i:i+6] :
        if j.isdigit() :
            v+=int(j)
    c.append(v)
print("Runs Per Over:",c)



#question 4
a=list(map(int,input().split()))
print(a)
l=a[0]
s=a[0]
for i in range(len(a)) :
    if a[i]>l :
        l=a[i]
for i in range(len(a)) :
    if a[i]<s :
        s=a[i]
print("largest:",l)
print("smallest:",s)

#question 5
a=input("enter a sentence: ")
b=a.split()
c=0
l=""
for i in range(len(b)) :
    if len(b[i])>c :
        c=len(b[i])
        l=b[i]
print(l)

#question 6
a=list(map(str,input().split()))
b=list(map(int,input().split()))
c=list(map(str,input().split()))
d=[]
sum=0
for i in c :
    if i not in d :
        d.append(i)
for i in d :
    t=0
    for j in c :
        if i==j :
            t+=1
    p=0
    for j in range(len(a)) :
        if i==a[j] :
            p=b[j]
            break
    sum+=p*t
    print(i,"X",t,"=",p*t)
print("total:",sum)

#question 7
a=input("enter a sentence: ")
b=a.split()
d=""
for i in b :
    c=""
    for j in range(-1,-len(i)-1,-1) :
        c+=i[j]
    d=d+c+" "
print(d)

#question 8
a=input("enter a string: ")
b=[]
t=0
for i in a :
    if i.isdigit() :
        c=int(i)
        b.append(c)
print(b)
for i in b :
    t+=int(i)
print("Sum:",t)

#question 9
n=int(input("enter the number of students: "))
a=[]
b=[]
for i in range(n) :
    name=input().lower()
    a.append(name)
for i in a :
    d=i.split()
    b.append(i)
    c=b.count(i)
    if c==1 :
        print(d[0]+"."+d[1]+"@jklu.edu.in")
    else :
        print(d[0]+"."+d[1]+str(c)+"@jklu.edu.in")

#question 10
a=list(map(int,input().split()))
b=[]
d=0
for i in a :
    c=int(i)
    if i!=0 :
        b.append(i)
    else :
        d+=1
for i in range(d) :
    b.append("0")
print(b)