from datetime import date
import math
def divisiblity():

    user_input1=int(input("Enter First Number : "))
    user_input2=int(input("Enter Second Number : "))
    if(user_input1%user_input2==0):
            print(user_input1,"is completely divisible by",user_input2)
    else:
            print(user_input1,"is not  completely divisible by",user_input2)
def int_bin_oct_hex():
    user_input=int(input("Enter an integer : "))
    print(" 1. Binary \n 2. Octal \n 3. Hexadecimal")
    choice=int(input())
    convert=0
    if(choice in range(1,4)):
            if(choice==1):
                convert=bin(user_input)
            elif(choice==2):
                convert=oct(user_input)
            else:
                convert=hex(user_input)
            print(user_input,"is converted as",convert)
    else:
        print("invalid choice")
def bin_decimal():
    user_binary_input=input("Enter binary value : ")
    print(int(user_binary_input,2))
def occurence_of_string():
    user_input=input("Enter a string of your choice : ")
    find_ch=input("Enter the character which u want to count in given string : ")
    count=0
    for i in range(len(user_input)):
        if user_input[i]==find_ch:
            count+=1
    if count==0:
        print(find_ch,"is not present in",user_input)
    else:
        print(find_ch,"is present",count,"times in",user_input)
def vowels_consonants():
    user_string=input("Enter a string of your choice : ")
    length=len(user_string)
    vowels=0
    spaces=0
    for i in range(length):
        if user_string[i] in 'aeiou' or user_string[i] in 'AEIOU':
            vowels+=1
        if user_string[i]==" ":
            spaces+=1
    print("The number of vowels:",vowels)
    print("The number of consonants:",(length-spaces-vowels))
def name_reverse():
    user_first_name=input("Enter First Name : ")
    user_last_name=input("Enter Last Name : ")
    array=user_first_name+" "+user_last_name
    print(array[::-1])
def palindrome_text():
    user_input=input("Enter a string of your choice : ")
    if user_input[:]==user_input[::-1]: # user_input==user_input[::-1] also working
        print(user_input,"is palindrome")
    else:
        print(user_input,"is not palindrome")
def integer_palindrome():
    user_input=input("Enter a number : ")
    user_input_reverse=int(user_input[::-1])
    user_input_reverse+=int(user_input)
    print(user_input_reverse)
def digits_letters():
    user_input=input("Enter a string : ")
    letters=0
    spaces=0
    digits=0
    for i in range(len(user_input)):
        if user_input[i] in '0123456789':
            digits+=1
        elif user_input[i] in '" ".~!@#$%^&*()_+{}|:<>?':
            spaces+=1
        else:
            letters+=1
    print("letters :",letters)
    print("digits :",digits)
    print("other characters along spaces :",spaces)
def mile_yard_inches():
    user_input=float(input("Enter distance in feet : "))
    print("***************Choose any 1 of the options for Conversion***************")
    print("1. Inches")
    print("2. Yard")
    print("3. Mile")
    choice=int(input())
    if choice in (1,2,3):
        if choice==1:
            print(user_input," Feet ==",12*user_input,"inch(es)")
        elif choice==2:
            print(user_input," Feet ==",user_input/3,"Yard(s)")
        else:
            print(user_input," Feet ==",user_input/5280,"Mile(s)")
    else:
        print("invalid choice")
def int_sum():
    user_input=input("Enter an integer : ")
    sum=0
    for i in range(len(user_input)):
        sum+=int(user_input[i])
    print(sum)
def feet_inch_cent():
    print("Enter Height \n1.Feet to Centimeters \n2.Inches to Centimeter")
    choice=int(input())
    if choice in (1,2):
        if choice==1:
            user_height=float(input("Enter Height in Feet : "))
            print(user_height,"Feet ==",user_height*150,"Centimeters")
        else:
            user_height=float(input("Enter Height in Inches : "))
            print(user_height,"Inches ==",user_height*2.5,"Centimeters")
    else:
        print("invalid choice")
def fibonacci():
    first=0 
    second=1
    for i in range(51):
        if i <=1:
            next_=0
        else:
            next_=first+second
            first=second
            second=next_
        print("The fibnoncci series: ",next_)
def GCD_LCM():
        user_input1=int(input("Enter First Number : "))
        user_input2=int(input("Enter Second Number : "))
        temp1=user_input1
        temp2=user_input2
        while user_input1!=user_input2:
            if user_input1>user_input2:
                user_input1-=user_input2
            else:
                user_input2-=user_input1
        print("The GCD of",temp1,"and",temp2,"is",user_input1)
        print("The LCM of",temp1,"and",temp2,"is",(temp1*temp2)/user_input1)
def future_amount():
        amount=float(input("Enter amount : "))
        rate=float(input("Enter rate : "))
        years=int(input("Enter year(s) :"))
        future_value=amount*((1+rate)**years)
        print("The Future Value is :",future_value)
def body_mass_index():
        mass=float(input("Enter MASS in kg(s) : "))
        height=float(input("Enter HEIGHT in meter(s)"))
        body_mass_index=mass/(height**2)
        print("The BODY MASS INDEX is :",body_mass_index)
def number_of_days():
        day1=int(input("Enter date1 :"))
        month1=int(input("Enter month1 :"))
        year1=int(input("Enter year1 :"))
        day2=int(input("Enter date2 :"))
        month2=int(input("Enter month2 :"))
        year2=int(input("Enter year2 :"))
        first=date(year1,month1,day1)
        second=date(year2,month2,day2)
        print("The number of days : ",abs(second-first).days)
def temperature_conversion():
    print("Enter temperature : ")
    temperature=float(input())
    temp=temperature
    print("**********CHOOSE ANY ONE OF THE FOLLOWING**********")
    print("1. Fahrenheit to Celsius ")
    print("2. Celsius to Fahrenheit ")
    choice=int(input())
    if choice==1 or choice==2:
        if choice==1:
            temperature=((temperature-32)/1.8)
            print("FAHRENHIET :",temp,"F == CELSIUS",temperature,"C")
        else:
            temperature=((temperature*1.8)+1.8)
            print("CELSIUS :",temp,"C == FAHRENHIET",temperature,"F")
    else:
        print("invalid option")
def time_conversion():
        user_input=int(input("Enter time in second(s) : "))
        print("1. Second(s) TO Day :")
        print("2. Second(s) TO Hour :")
        print("3. Second(s) TO Minutes :")
        choice=input("Enter your Choice")
        if choice in '123':
            if choice=='1':
                print("Seconds : ",user_input,"==",(user_input/(24*60*60)),"Day(s)")
            elif choice=='2':
                print("Seconds : ",user_input,"==",(user_input/(60*60)),"Hour(s)")
            else:
                print("Seconds : ",user_input,"==",(user_input/(60)),"Minute(s)")
        else:
            print("Invalid Choice")
print("********************************OPTIONS********************************")
print("         1.Divisibilty Check")
print("         2.Conversion from integer to Binary , Octal or Hexadecimal" )
print("         3.Binary to Decimal")
print("         4.Check for the Particular Character in string")
print("         5.Counts of VOWELS and Consonants in String")
print("         6.Name Reverse")
print("         7.Text Palindrome")
print("         8.Integer Palindrome")
print("         9.Counts of Digit(s) & Letter(s)")
print("         10.Conversion into MILE,YADS & INCHES")
print("         11.SUM OF INTEGER")
print("         12.Conversion from FEET to INCHES OR CENTIMETERS")
print("         13.FIBONACCI SERIES")
print("         14. GCD and LCM")
print("         15. Future Amount Calculation")
print("         16. BODY MASS INDEX Calculation")
print("         17. Number Of Days Calculation")
print("         18. TEMPERATURE Conversion")
print("         19. TIME Conversion")
user_choice=int(input())
if user_choice==1:
    divisiblity()
elif user_choice==2:
    int_bin_oct_hex()
elif user_choice==3:
    bin_decimal()
elif user_choice==4:
    occurence_of_string()
elif user_choice==5:
    vowels_consonants()
elif user_choice==6:
    name_reverse()
elif user_choice==7:
    palindrome_text()
elif user_choice==8:
    integer_palindrome()
elif user_choice==9:
   digits_letters()
elif user_choice==10:
    mile_yard_inches()
elif user_choice==11:
    int_sum()
elif user_choice==12:
    feet_inch_cent()
elif user_choice==13:
    fibonacci()
elif user_choice==14:
    GCD_LCM()
elif user_choice==15:
    future_amount()
elif user_choice==16:
    body_mass_index()
elif user_choice==17:
    number_of_days()
elif user_choice==18:
    temperature_conversion()
elif user_choice==19:
    time_conversion()
else:
    print("invalid choice")





