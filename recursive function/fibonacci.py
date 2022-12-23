def Rec_fibo(n):
    if(n<=1):
        return n
    else:
        return(Rec_fibo(n-1) + Rec_fibo(n-2))

ni=int(input("enter a number:"))
if(ni<=0):
    print("invalid entry")
else:
    print("fibonacci series:")
    for i in range(ni):
        print(Rec_fibo(i))    
