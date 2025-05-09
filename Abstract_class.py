from abc import ABC, abstractmethod

# 1. Create an abstract class with abstract and non-abstract methods.
class AbstractBase(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("Non-abstract method in abstract class")

# 2. Create a sub class for an abstract class. Create an object in the child class for the  
# abstract class and access the non-abstract methods
# 3. Create an instance for the child class in child class and call abstract methods
# 4. Create an instance for the child class in child class and call non-abstract methods 
class ConcreteClass(AbstractBase):
    def abstract_method(self):
        print("Implemented abstract method in child class")

    def test_methods(self):
        obj = ConcreteClass()
        obj.abstract_method()
        obj.non_abstract_method()

def main():
    c = ConcreteClass()
    c.test_methods()

if __name__ == "__main__":
    main()
