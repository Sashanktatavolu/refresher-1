import pandas as pd
# a=[1,2,3,4,5]
# myvar=pd.Series(a,index=["a","b","c","d","e"])
# print(myvar)

# b=[6,7,8,9,10]
# y=pd.Series(b,index=["me","we","us","he","she"])
# print(y)

# for i in range(5):
#     n=int(input("Enter the marks:"))
names=[input("enter the names:")for _ in range(5)]
marks=[int(input("enter the marks:"))for _ in range(5)]
z=pd.Series(marks,index=["names"])
print(z)

