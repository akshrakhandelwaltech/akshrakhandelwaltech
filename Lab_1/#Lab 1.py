#Lab 1

#pr 1
print("'Hello JKLU!'")
print("'I am learning Python'")

#pr 2
name= input("enter name: ")
branch=input("enter branch name: ")
print("Welcome to JKLU",name,"!")

#pr 3
l=int(input("enter the value of length in metres = "))
w= int(input("enter the value of width in metres = "))
area= l*w
print("area of rectangle is:",area,"m^2")

#pr 4
l=int(input("enter the value of length in feet = "))
w= int(input("enter the value of width in feet = "))
area=l*w*(0.305)**2
print("area of rectangle is:",area,"m^2")

#pr 5
x=int(input("enter a number= "))
y=int(input("enter a number= "))
if x<0 or y<0 :
    print("Invalid input")
else: 
    if y%x==0 :
        print(y,"is divisible by",x)
    else:
        print(y,"is not divisible by",x)

#pr 6
n= int(input("enter a number= "))
if n%2==0 :
    print(n, "is an even number")
else :
    print(n, "is an odd number")

#pr 7
r=int(input("enter the radius="))
if 1<r<100 :
    area= 3.14*(r)**2
    print("area=",area)
else :
    print("Invalid input")

#pr 8
c=int(input("enter temperature in celcius= "))
f= (c*9/5) + 32
k= c+273.15
print("temperature in fahrenheit= ",f)
print("temperature in fahrenheit= ",k)

#pr 9
s=int(input("enter the number of seconds = "))
if 1<=s<=86400 :
    hh=s//3600
    mm= (s%3600)//60
    ss=(s%3600)%60
    print(hh,":",mm,":",ss)
else :
    print("Invalid input")

#pr 10 (a)
att=int(input("enter your attendance: "))
if att>=75 :
    print("you are eligible")
else :
    print("you are not eligible")

#pr 10 (b)
units=int(input("enter the number of electricity units consumed: "))
rs= int(input("per unit cost: "))
bill= units*rs
print("total electricity bill=",bill)

#pr 10 (c)
pin= int(input("enter the pin: "))
atm=1234
if pin==atm :
    print("pin validated correctly")
else :
    print("pin invalid")
    