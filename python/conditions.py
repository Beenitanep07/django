num1 = int(input("Enter value of num1\t"))
num2 = int(input("Enter Value of num2\t"))
num3 = int(input("Enter value if num3\t"))

if num1 > num2 and num1 > num3:
    print(num1, "is greater than", num2, "and", num3)
elif num2> num1 and num2 > num3:
    print(num2 , "is greater than", num2 , "and", num3)
else:
    print(num3, "is greater")
    
    
    
# for odd and even number
if num1==0:
    print(num1 , "is zero")
elif num1%2==0:
    print(num1, "is even number")
else:
    print(num1, "is odd number")
