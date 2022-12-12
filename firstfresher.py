product_1=int(input('quantity of first product:'))
product_2=int(input('quantity of first product:'))
product_3=int(input('quantity of first product:'))
product_4=int(input('quantity of first product:'))
product_5=int(input('quantity of first product:'))
#Using the List
l=[product_1,product_2,product_3,product_4,product_5]
#using the loops
for i in l:
    print(i)
#using the if-else statements
if((product_1<=0)or (product_1<=0)or(product_3<=0)or(product_4<=0)or(product_5<=0)):
    print('please enter a positive value')
else:
    # print('the amount that you need to pay is:')
    total=product_1*300 +product_2*400 +product_3*500 +product_4*600+product_5*700
    entries={product_1:300,product_2 : 400,product_3:500 ,product_4:600,product_5:700}
    x=open("mydata.txt","a")
    print("the amount os all products")
    print("the amount os all products",file=x)
    # x.close()
    for i,p in entries.items():
        print(i,p)
        print(i,p,file=x)
    print('the amount that you need to pay is:',file=x)
    print(total)
    print(total,file=x)
