N = int(input("enter copies Number : ")) 
if  N <= 10 : 
     print ("the price is : " , N * 0.30 , "DH" ) 
elif N > 10 and N <= 30 : 
     print ( "the price is: " , 10 * 0.30 + (N - 10) * 0.25 , "DH" ) 
elif N > 30 : 
     print ("the price is : " , 10 * 0.30 + 20 * 0.25 + (N-30) * 0.20 , "DH") 
else : 
     print ("enter the correct number")