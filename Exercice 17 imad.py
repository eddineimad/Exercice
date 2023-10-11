ht = float(input("please enter the price excluding tax : ")) 
tva = int(input("enter category : ")) 
if tva == 7 : 
     print("the price TTC is : " , ht * (1 + ( 7 / 100 ) ) ) 
elif tva == 20 : 
     print("the price TTC is : " , ht * (1 + ( 20/ 100 ) ) )  
elif tva == 25 : 
     print("the price TTC is : " , ht * (1 + ( 25/ 100 ) ) ) 
else : 
     print("invalid")
