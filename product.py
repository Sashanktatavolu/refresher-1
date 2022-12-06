product1= float(input("enter product1 quantity "))
product2= float(input("enter product2 quantity "))    
product3= float(input("enter product3 quantity "))
if(product1<=0 or product2<=0):
    print("Enter a positive number")
else:    
    priceOfProduct1 = float(input("enter product1 price "))
    priceOfProduct2 = float(input("enter product1 price "))
    priceOfProduct3 = float(input("enter product1 price "))
    totalquantity=product1+product2+product3
    total =(priceOfProduct1*product1+ priceOfProduct2*product2+ priceOfProduct3*product3 )
    print("the total quantity is",totalquantity)
    print("the total amount is",total)
