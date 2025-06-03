# kunai kura lai repetative kaam garnu paryo vane we use loop

# three things to know in loop
# initialization , condition, increament/decrement

#while loop
i=1
while i<10:
    print("Hello")
    i= i+1
    
# for loop
for i in range(10):
    print(i)
    
num = int(input("Enter the range:"))
sum = 0
for i in range(num):
    num2 = int(input("Enter the number to be added:"))
    sum = sum + num2
print(sum)

# Nested loop
for j in range(5):
    for k in range(j):
        print(j, end="")
    print()