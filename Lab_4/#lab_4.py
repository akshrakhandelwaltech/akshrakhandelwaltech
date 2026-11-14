# lab 4

# question 1
sal= int(input("enter the salary: "))
years= int(input("enter the number of years: "))
if years<=5 :
    print("no bonus given")
else :
    print("bonus of",sal*0.05,"rs.") 

# question 2
password= input("enter the password: ")
if password== "s3cr3t!P@ssw0rd" :
    print("Welcome")
else :
    print("Wrong password")

# question 3
shape= input("enter the shape: ")
if shape=="square" :
    s= float(input("enter the side of square"))
    area= s**2
    print("area=",round(area,3)) 
elif shape=="rectangle" :
    l= float(input("enter the lenght: "))
    w= float(input("enter the length of width: "))
    area= l*w
    print("area=",round(area,3))
elif shape=="circle" :
    r= float(input("enter the radius: "))
    area= 3.14*r**2
    print("area=",round(area,3))
elif shape=="traiangle" :
    b= float(input("enter the base: "))
    h= float(input("enter the height: "))
    area= (b*h)/2
    print("area=",round(area,3))

# question 4
h= int(input("enter hours: "))
m= int(input("enter minutes: "))
if 0<=h<=23 and 0<=m<=59 :
    mm= h*60 +m +15
    h= mm//60
    m=mm%60
    if 0<=h<=23 and 10<=m<=59 :
        print(h,":",m,sep="")
    elif 0<=h<=23 and 0<=m<=9 :
        print(h,":0",m,sep="")
    elif h==24 and m>=10 :
        print("00:",m,sep="")
    elif h==24 and 0<=m<=9 :
        print("00:0",m,sep="")
else :
    print("invalid input")

# question 5
n= int(input("enter the number of kms: "))
per= input("enter the period of the day: ")
if n>=100 :
    print("Train=",n*2.88,"rs.")
elif 20<=n<100 :
    print("Bus=",n*4.32,"rs.")
elif n<20 and per=="day" :
    print("taxi=",33.58 + n*37.89) 
else :
    print("taxi=",33.58 + n*43.17) 

# question 6
holi= int(input("enter the number of holidays: "))
work=365-holi
t_mins= 365*24*60
mins=holi*127 +work*63
diff=t_mins-mins
if diff>=30000 :
    print("Tom can sleep well")
else :
    print("Tom can't sleep well")

# question 7
bgn=int(input("enter the budget: "))
s= input("enter the season: ")
if bgn<=100 and s=="summer" :
    print("camping in bulgaria, amount spend=",bgn*0.3)
elif bgn<=100 and s=="winter" :
    print("stay in a hotel in bulgaria, amount spend=",bgn*0.7)
elif 100<bgn<=1000 and s=="winter" :
     print("stay in a hotel in balkans, amount spend=",bgn*0.8)
elif 100<bgn<=1000 and s=="summer" :
    print("camping in balkans, amount spend=",bgn*0.4)
else :
    print("stay in a hotel in europe, amount spend=",bgn*0.9)

# question 8
i=6
while i<=1000 :
    print(i,end=" ")
    j=i+10
    i=j
   
# question 9
n= int(input("enter n: "))
sum=0
for i in range(1,n+1) :
    num=int(input("enter the number: "))
    i+=1
    sum+=num
print(sum)

# question 10
n=int(input("enter the number: "))
for i in range(1,21) :
    print(n,"x",i,"=",n*i)
    i+=1