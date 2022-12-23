l=int(input())
total = 0

for number in range(1, l+1):
    if(number % 2 == 0):
        total = total + number
    
print("The Sum of Even Numbers from 1 to l",total)