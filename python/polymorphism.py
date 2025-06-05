#polymorphism: method overriding huncha......function override garnu pareko case ma polymorphism use garne......same name vayo vane
#override gareko ho....agadi inheritance ma hamle differenr function name use gareko tyo because tesma method override hunna tyo
# already previous vako function lai override garera different class ma use garnu nai polymorphism ho

class A:
    def display_name():
        print("This is class A")
class B(A): #inheritance #single level inheritance
    def display_name():
        print("This is class B")
class C(B): #multi level inheritance
    def display_name():
        print("This is class c")
    
    def sum(a=0,b=0,c=0,d=0):
        add =a+b+c+d
        return add
    
        
obj = B
obj.display_name()
#run time polymorphism

#compile time polymorphism
obj = C
result = obj.sum(1)
result2 = obj.sum(10,20,30)
print(result2)