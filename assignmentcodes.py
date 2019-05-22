import math
print ("--------------------------CHOICES-------------------------")
print("1.)              Calculation for Area of CIRCLE")
print("2.)              Checking for +ve , -ve or zero")
print("3.)              Computation for (n+nn+nnn)")
print("4.)              Calculation for Volume of SPHERE")
print("5.)              Calculating difference between number & 17 ")
print("6.)              String appending 'IS'")
print("7.)              Printing Copies of String ")
print("8.)              Checking whether ODD or EVEN")
print("9.)              Checking between VOWEL or CONSONANT")
print("10.)             Calculation for Area of TRIANGLE")
print("11.)             Checking for Equality , Difference or Sum")
print("12.)             Computation of (x+y)*(x+y)")
print("13.)             Computing Distance between two coordinates")
print("14.)             Calculating HYPOTENUSE of a RIGHT-ANGLED TRIANGLE")
print("15.)             Conversion to SECONDS")
print("16.)             Calculating SUM of first N Natural Numbers")
print("17.)             Printing the multiplication table of a number")
print("18.)             Printing pattern of STARS")
print("19.)             Printing pattern of NUMERALS")
print("20.)             Printing pattern of INCREASING NUMERALS")
INPUT=int(input())
if(INPUT==1):
# write a python program which accepts the radius of a circle from the user and compute the area
    radius=float(input("Enter the radius of circle : "))
    circle_area=3.142*radius*radius
#can be written in both the ways
    print("The area of circle with radius " + str(radius)+ " is " + str(circle_area))
    print("The area of circle with radius",radius,"is",circle_area)
elif(INPUT==2):
   #write a program to check wether the number is positive, negative or zero
    user_input=float(input("Enter a number to check whether it is positive, negative or zero : "))
    if(user_input>0):
        print(user_input,"is a positive number")
    elif(user_input<0):
        print(user_input,"is a negative number")
    else:
        print("Number is zero")
elif(INPUT==3):
#write a pyhthon program to accept an inetger(n) nd compute (n+nn+nnn)
    user_input=int(input("Enter an integer to compute n+nn+nnn : "))
    number=user_input
    user_input+=(user_input*user_input)+(user_input*user_input*user_input)
    print("The result of n+nn+nnn where n is",number,"is :",user_input)
elif(INPUT==4):
#volume of sphere
    user_input=float(input("Please Enter radius to find the volume of sphere: "))
    volume=(4/3)*(3.142*user_input*user_input*user_input)
    print("The volume of sphere of radius",user_input,"is",volume)
elif(INPUT==5):
#difference
    user_input=float(input("Enter a number to find the difference with 17 : "))
    difference=0
    if(user_input<17):
        difference=17-user_input
    else:
        difference=user_input-17
    print("The difference between",user_input,"and",17,"is",difference)
elif(INPUT==6):
#string
    user_input_string=input("Enter a string of your choice : ")
    if(user_input_string[0:2]=="Is" or user_input_string[0:2]=="is" or user_input_string[0:2]=="IS"):
        print(user_input_string)
    else:
        string_array="Is " + user_input_string
    print(string_array)
elif(INPUT==7):
#string copies
    user_string=input("Enter a string of your choice : ")
    n=int(input("Enter the number of copies you want : "))
    for i in range(n):
        print(user_string," ")
elif(INPUT==8):
#even odd
    user_input=int(input("Enter a number to check whether the number is even or odd : "))
    if(user_input%2==0):
        print("The number is even")
    else:
        print("The number is odd")
elif(INPUT==18):
#pattern printing using nested for loop
    for i in range(1,6):
        for j in range(i):
            print("*",end="")
        print("\n")
    for i in range(4,0,-1):
        for j in range(i):
            print("*",end="")
        print("\n")
elif(INPUT==19):
#printing pattern using numerals
    for i in range(1,6):
        for j in range(1,i+1):
            print(j,end="")
        print("\n")
    for i in range(4,0,-1):
        for j in range(1,i+1):
            print(j,end="")
        print("\n")
elif(INPUT==20):
#pattern from 1 to 9
    for i in range(1,10):
        for j in range(i):
           print (i,end="")
        print("\n")
elif(INPUT==17):
#multiplication table
    user_input=int(input("Enter a number to print its table : "))
    for i in range(1,11):
         print(user_input,"x",i,"=",i*user_input)
elif(INPUT==9):
    user_input=input("Enter an aphabet to check whether it is a vowel or consonant ")
    string_array=["a","e","i","o","u","A","E","I","O","U"]
    bool=False
    for i in range(0,9):
        if(user_input==string_array[i]):
           bool=True
           break
    if(bool==True):
        print("The letter",user_input,"is a vowel")
    else:
        print("The letter",user_input,"is a consonant")
elif(INPUT==10):
#base_height area of triangle
    user_input_base=float(input("Enter base :  "))
    user_input_height=float(input("Enter height :  "))
    area_of_triangle=0.5*user_input_base*user_input_height
    print("The area_of_triangle is",area_of_triangle)
elif(INPUT==11):
    user_input1=int(input("Enter First number : "))
    user_input2=int(input("Enter Second number : "))
    if(user_input1==user_input2 or user_input1-user_input2==5 or user_input1+user_input2==5 or user_input2-user_input1==5):
        print(True)
    else:
        print(False)
elif(INPUT==12):
#(x+y)(x+y)
    user_input1=int(input("Enter x : "))
    user_input2=int(input("Enter y : "))
    square=((user_input1+user_input2)*(user_input1+user_input2))
    print("The result of (x+y)*(x+y) i.e. (",user_input1,"+",user_input2,")*(",user_input1,"+",user_input2,") is", square)
elif(INPUT==13):
#distance between two points

    print("Enter the points of first coordinate")
    user_input1=int(input("Enter x : "))
    user_input2=int(input("Enter y : "))
    print("Enter the points of Second coordinate")
    user_input3=int(input("Enter x : "))
    user_input4=int(input("Enter y : "))
    var1=(user_input1-user_input3)*(user_input1-user_input3)
    var2=(user_input2-user_input4)*(user_input2-user_input4)
    distance=math.sqrt(var1+var2)
    print("The distance between (",user_input1,",",user_input2,") and (",user_input3,",",user_input4,") is",distance)
elif(INPUT==14):
#hypotnenus
    base=float(input("Enter base of right-angled triangle : "))
    perp=float(input("Enter perpendicular of right-angled triangle : "))
    hypt=math.sqrt((base*base)+(perp*perp))
    print("The hypotenous of right-angled triangle is",hypt )
elif(INPUT==15):
    print("Enter your choice : ")
    print("1). Conversion from minutes to seconds")
    print("2). Conversion from hours to second")
    input_time=0
    choice=int(input())
    if(choice==1):
        time=int(input("Enter time in minutes : "))
        input_time=time
        time*=60
        print("Minutes :",input_time,"==","Seconds :",time)
    elif(choice==2):
        time=int(input("Enter time in hours : "))
        input_time=time
        time*=3600
        print("Hours :",input_time,"==","Seconds :",time)
    else:
        print("invalid choice")
elif(INPUT==16):
#sum of first n positive integers
    user_input=int(input("Enter n to find the sum of first n positive integers : "))
    sum=((user_input+1)*user_input)/2
    print("The sum of first",user_input,"natural positive numbers is",sum)
else:
    print("invalid choice")
