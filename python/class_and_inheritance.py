#basic class
class A:
    def display_name():
        print("This is class A")
class B(A): #inheritance #single level inheritance
    def print_name():
        print("This is class B")
class C(B): #multi level inheritance
    def print_data():
        print("This is class c")

# obj = A #intance call gareko i.e. tyo class ko copy banako 
# obj.display_name()

# obj2 = B
# obj2.print_name()
# obj2.display_name() #this can be done due to inheritance

obj3 = C
obj3.print_data()
obj3.display_name()
obj3.print_name()