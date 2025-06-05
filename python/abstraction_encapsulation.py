#abstraction
# kunai kunai class or function private banauna parcha tyo chai kahi bhata ni acccess nahos tyai class vitra ko arko function lay matra
# use hos tesko case ma abstraction use garchau 

#encapsulation
# kunai pani class vitra ko function haru  lai private, public , protected banauna milyo 
#private: within the same class use garna milyo......__engine mean it is private
#protected: within this program matra use garna milyo...._engine mean it is protected
#public: same file matra haina aru file haru bhatha ni call garna milyo 



from abc import ABC, abstractmethod

class Cars(ABC):
    # this is abstract class so i can't be access directly
    @abstractmethod
    def start_engine(self):
        pass
    

class Ford(Cars):
    # this can be used as this is not abstract class
    def start_engine():
        print ("Ford Started")
    
    def display_name():
        print ("Ford Car")
        
class Bikes:
    def color():
        return "Red"
    
    def _model():
        return"Yamaha"
        
    def __engine():
        return "250cc"
        
obj = Ford
obj.start_engine()
obj.display_name()

bike = Bikes
print("name= ", bike._model(), "color= ", bike.color())
# In above bikes class color and model is public and protected so it can be access but engine is private so it can't be access