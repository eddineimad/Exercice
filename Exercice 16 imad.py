n = int(input("enter your age : ")) 
sex = input("enter your gender : ") 
while n <= 0  : 
     n = int(input("enter corectly your age : ")) 
while (sex!= "male" and sex!= "female") : 
     sex = input("enter corectly your gender : ") 
if n > 20 and sex=="male" : 
     print("you are taxable") 
elif (n >= 18 and n <= 35) and sex == "female" : 
     print("you are taxable") 
else : 
     print("you aren't taxable")