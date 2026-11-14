# lab 3

#question 1
x1= int(input("enter x1: "))
y1= int(input("enter y1: "))
x2= int(input("enter x2: "))
y2= int(input("enter y2: "))
r= int(input("enter the radius: "))
dis= ((x2-x1)**2 + (y2-y1)**2)**1/2
if dis<r :
    print("point lies inside the boundary")
elif dis== r :
    print("point lies on the boundary")
else :
    print("point lies outside the boundary")

#question 2
s= int(input("enter the side length of a regular polygon: "))
area= (5*(s)**2)/(4*0.726)
print("area=",area)

#question 3
a= int("enter angle 1: ")
b= int("enter angle 2: ")
c= int("enter angle 3: ")
if a>0 and b>0 and c>0 :
    if a+b+c==180 :
        print("they can form the angles of a triangle")
        if a==90 or b==90 or c==90 :
            print("it will form a right angled triangle")
        elif a<90 and b<90 and c<90 :
            print("it will form an acute angle triangle")
        else :
            print("it will form an obtuse angle triangle")
    else :
        print("they can't form the angles of a triangle")
else :
    print("invalid input")

# question 4
n= int(input("enter a four digit number: "))
n1= n//1000
n2= (n%1000)//100
n3= (n%100)//3
n4= n%10
first= n1+n2
sec= n3+n4
print("sum of first two digits of",n,"=",first)
print("sum of last two digits=",n,"=",sec)
if first==sec :
    print("sum of first and last two digits is equal")
else :
    print("sum of first and last two digits is not equal")

#question 5
n= int(input("enter a 5 digit number: "))
n1= n//10000
n2= (n%10000)//1000
n3= (n%1000)//100
n4= (n%100)//10
n5= n%10
if n1>=n2 and n1>=n3 and n1>=n4 and n1>=n5 :
    print(n1,"is the largest digit and it's the first digit from the left")
elif n2>=n1 and n2>=n3 and n2>=n4 and n2>=n5 :
    print(n2,"is the largest digit and it's the second digit from the left")
elif n3>=n1 and n3>=n3 and n3>=n4 and n3>=n5 :
    print(n3,"is the largest digit and it's the third digit from the left")
elif n4>=n1 and n4>=n2 and n4>=n3 and n4>=n5 :
    print(n4,"is the largest digit and it's the fourth digit from the left")
else :
    print(n5,"is the largest digit and it's the fifth digit from the left")

#question 6
a= int(input("enter a number: "))
b= int(input("enter a number: "))
c= int(input("enter a number: "))
print("a=",c)
print("b=",a)
print("c=",b)

#question 7
n= int(input("enter a three digit number: "))
n1= n//100
n2= (n%100)//10
n3= n%10
sum= n1 +n2 + n3
if n%sum==0 :
    print("it's a harshad number")
else : 
    print("it's not a harshad number")

#question 8
v= int(input("enter the initial volume of water: "))
n= int(input("enter the number of days: "))
if v>0 and n>0 :
    vf= 200 + (v-200)*(0.95**n)
    print("final volume=",vf)
else :
    print("invalid inputs")

#question 9
a1= float(input("enter the value of a1: "))
b1= float(input("enter the value of b1: "))
c1= float(input("enter the value of c1: "))
a2= float(input("enter the value of a2: "))
b2= float(input("enter the value of b2: "))
c2= float(input("enter the value of c2: "))
if a1/a2 !=b1/b2 :
    x=(b1*c2 - b2*c1)/(a2*b1 - a1*b2)
    y=(c1-a1*x)/b1
    print("point of intersection=","("+ x +","+y+ ")")
elif a1/a2 ==b1/b2 ==c1/c2 :
    print("coincident or parallel lines")

