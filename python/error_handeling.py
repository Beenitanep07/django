# 2 block in error handleing .....try block (it have main program....khi error aaula jasto cha vane tyo yasma huncha) 
# except block (yaha error aayo vane catch huncha)

num1=0
num2=20

try:
    if num1==0:
        raise ZeroDivisionError("Error: Division by zero is not allowed")
    result = num1 / num2
    print(result)
except ZeroDivisionError as e:
    print(e)