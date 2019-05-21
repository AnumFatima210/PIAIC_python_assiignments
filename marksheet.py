print("*************************MARKSHEET GENERATOR*************************")
input_roll=int(input("Enter your roll_number(XXXXXX) : "))
print("CHOOSE YOUR MAJOR SUBJECT")
print("             1. SCIENCE \n             2. COMPUTER")
user_input_major_subject=int(input())
if(user_input_major_subject==1 or user_input_major_subject==2):
    subject1=float(input("Enter your marks for SINDHI subject :         "))
    subject2=float(input("Enter your marks for ENGLISH subject :        "))
    subject3=float(input("Enter your marks for CHEMISTRY subject :      "))
    subject4=float(input("Enter your marks for PAK.STUDIES subject :    "))
    if(user_input_major_subject==1):
        subject5=float(input("Enter your marks for BIOLOGY subject :        "))
    else:
        subject5=float(input("Enter your marks for COMPUTER subject  :      "))
    sum=((subject1+subject2+subject3+subject4+subject5)/425)*100
    print("                                 \n\n\n---------------------MARKSHEET---------------------")
    print("     \nRoll_Number:    ",input_roll,"\n\n\n")
    print("         -----------------------------------------")
    print("         |SUBJECTS","             ","MARKS-OBTAINED   |" )
    print("         -----------------------------------------")
    print("         |SINDHI","               ","        ",subject1,"    |")
    print("         |ENGLISH","              ","        ",subject2,"    |")
    print("         |CHEMISTRY","            ","        ",subject3,"    |")
    print("         |PAK-STUDIES","          ","        ",subject4,"    |")
    if(user_input_major_subject==1):
        print("         |BIOLOGY","              ","        ",subject5,"    |")
        print("         -----------------------------------------")
    else:
        print("         |COMPUTER","             ","        ",subject5,"    |")
        print("         -----------------------------------------")
    print("                         Percentage Obtained:    ",sum)
else:
    print("Invalid Choice")


