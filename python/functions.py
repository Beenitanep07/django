# functions in python : certain kura repetative use hune vayo vane we keep them in function....i.e. reuseability

# 1. function with no parameter and no return value
def display_hello_world():
    print("Hello World")
 
#calling function in for loop  
for i in range(5): 
    display_hello_world()
    
# 2. function with parameter and no return value
def sum(num1, numb2):
    add =  num1 + numb2
    print("The sum is", add)
    
a = 20
b = 30    
sum(a,b)

#functiom with parameter and return value

def fact(num):
    if num == 0:
        return 1
    else:
        i=1
        result = 1
        while i <= num:
            result = result * i
            i = i+1
    return result

num = int(input("Enter a number: "))
print("Factorial of", num , "is", fact(num))
    
    

    
