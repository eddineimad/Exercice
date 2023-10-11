A = float(input("enter a number : ")) 
B = float(input("enter a number : ")) 
if ( A >= 0 and B >= 0 ) or ( A <= 0 and B <= 0) : 
     C = A
     A = B 
     B = C
     print("the first number is : " , A) 
     print("the second number is : " , B) 
else : 
     print ("the sum is : " , A + B) 
     print ("and the multiplication is : ",A*B)
