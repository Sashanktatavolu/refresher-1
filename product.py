#using input function

product1= int(input("enter product1 quantity "))
product2= int(input("enter product2 quantity "))    
product3= int(input("enter product3 quantity "))
# product4= int(input("enter product4 quantity "))
# product5= int(input("enter product5 quantity "))
# if(product1<=0 or product2<=0):
#     print("Enter a positive number")
# else:    
# priceOfProduct1 = float(input("enter product1 price "))
# priceOfProduct2 = float(input("enter product1 price "))
# priceOfProduct3 = float(input("enter product1 price "))

#using the list
# productlist =[product1,product2,product3]

# #using the for loop
# for s in productlist:
#     print(s) 
# price1=300
# price2=400
# price3=500
    # totalquantity=product1+product2+product3
    # total =(priceOfProduct1*product1+ priceOfProduct2*product2+ priceOfProduct3*product3 )
    # print("the total quantity is",totalquantity)
    # print("the total amount is",total)

#using the if-else statement
if((product1<=0) or (product2<=0) or(product3<=0)):
    print('please enter a positive number')
else:
    print('product quantity with price')
    total =(200*product1+ 300*product2+ 500*product3 )  
    entries = {product1:200,product2:300,product3:500}
    for i,p in entries.items():
        print(i,p)
    print('the amount that you nedd to pay :')
    print (total) 
