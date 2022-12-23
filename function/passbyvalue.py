def ChangeNum(mylist):
    mylist.append([1,2,3,4,5])
    print("values iside the function",mylist)
    return

mylist=[6,7,8,9]
print("values outside the function",mylist)
ChangeNum(mylist)


