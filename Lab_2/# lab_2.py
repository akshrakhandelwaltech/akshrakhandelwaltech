# lab 2

#question 1
n=int(input("enter a no.: "))
if n%5==0 :
    print("Hi")
else :
    print("Bye")

#question 2
x= int(input("enter the length of parallel side 1 of trapezium: "))
y= int(input("enter the length of parallel side 2 of trapezium: "))
h= int(input("enter the height of trapezium: "))
area= (x+y)*h/2
print("area of trapezium=",area)

#question 3
w= int(input("enter the person's weight in kgs: "))
h= int(input("enter the person's height in meters: "))
bmi= w/(h)**2
if bmi<18.5 :
    print("underweight")
elif 18.5<=bmi<25 :
    print("normal weight")
elif 25<=bmi<30 :
    print("slightly overweight")
elif 30<=bmi<35 :
    print("obese")
elif bmi>=35 :
    print("clinically obese")

#question 5
initial= 2.19 * 10**14
final= 4.68 * 10**14
per= ((final-initial)/initial)*100
print("percentage of bacterial growth=", round(per,0))

#question 6
m= int(input("enter the number of months: "))
yy= m//12
mm= m%12
print(yy,"years and",mm,"months")

#question 7
color= input("enter the color: ")
mode= input("enter the mode: ")
if color== "blue" and mode=="steady" :
    print("clear view")
elif color== "blue" and mode=="flashing" :
    print("clouds due")
elif color== "red" and mode=="steady" :
    print("rain ahead")
else :
    print("snow instead")

#question 8
cost= int(input("enter the cost: "))
rev= int(input("enter the revenue: "))
if cost==rev :
    print("break even")
elif cost>rev :
    print("loss")
else :
    print("profit")

#question 9
wid= int(input("no. of widgets ordered: "))
if wid<100 :
    print("total cost=", wid*25, "cents")
else :
    print("total cost=", wid*20, "cents")

#question 10
p= int(input("enter the number of pounds: "))
cost= float(input("amount of cash tendered: "))
if cost<p*2.50 :
    v= p*2.50 - (cost)
    print("you owe",v,"more.")
else :
    print("transaction completed")

#question 11
a= int(input("enter a number: "))
b= int(input("enter a number: "))
c= int(input("enter a number: "))
if a>=b :
    if a>=c :
        lar= a
    else :
        lar= c
else :
    if b>=c :
        lar=b
    else :
        lar= c
print("The largest number is:",lar)

#question 12
basic= int(input("enter the basic salary: "))
hra= basic*0.2
ta= basic*0.05
da= basic*0.1
print("gross salary=", basic+hra+ta+da)

#question 13
basic= int(input("enter the basic salary: "))
hra= basic*0.2
ta= basic*0.05
da= basic*0.1
gross= basic+hra+ta+da
print("gross salary=", gross)
if gross<300000 :
    print("0 income tax")
elif 300000<=gross<1000000 :
    print("income tax= 10 percent of gross salary")
elif 1000000<=gross<2500000 :
    print("income tax= 20 percent of gross salary")
else :
    print("income tax= 30 percent of gross salary")

#question 14
inc= int(input("enter taxable income: "))
if inc<=20000 :
    set_tax=inc*0.02
else :
    if inc<=50000 :
        set_tax= 400 + 0.025*(inc-20000)
    else :
        set_tax= 1150 + 0.035*(inc-50000)
print("tax=",set_tax)

#question 4
a=input("enter an alphabet: ")
if a in "aeiouAEIOU" :
    print("it's a vowel")
else :
    print("it's a consonant")