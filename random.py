import random
array=[]
for i in range(5):
    array.append(random.randint(10,1000))
print(array)
print("        *Choose one of the Following Options*")
print("  1> SUM OF ELEMENTS IN LIST")
print("  2> MIN OF ELEMENTS IN LIST")
print("  3> MAX OF ELEMENTS IN LIST")
user_choicce=int(input())
if(user_choicce==1):
   sum=0
   for i in range(len(array)):
    sum=sum+array[i]
   print (sum)
elif(user_choicce==2):
   min=array[0]  
   min_index=0
   for i in range(len(array)):
      if(min>array[i]):
       min=array[i]
       min_index=i
   print("The minimum value of list is: ",min)
   print("The index of minimum value is: ",min_index)
elif(user_choicce==3):
   max=array[0]  
   max_index=0
   for i in range(len(array)):
      if(max<array[i]):
       max=array[i]
       max_index=i
   print("The maximum value of list is: ",max)
   print("The index of maximum value is: ",max_index)
else:
   print("invalid choice")
