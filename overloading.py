# 1. Write a class with a default constructor, one argument constructor and two argument constructors.
class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default constructor")
        elif b is None:
            print("One-argument constructor:", a)
        else:
            print("Two-argument constructor:", a, b)

# 2. Call the constructors(both default and argument constructors) of super class from a child class
class Parent:
    def __init__(self, value=None):
        if value is None:
            print("Parent default constructor")
        else:
            print("Parent argument constructor:", value)

class Child(Parent):
    def __init__(self, value=None):
        if value is None:
            super().__init__()
        else:
            super().__init__(value)
        print("Child constructor")

# 3. Apply private, public, protected and default access modifiers to the constructor
class ModifierExample:
    def __init__(self):
        print("Public constructor")
    def _protected_constructor(self):
        print("Protected constructor")
    def __private_constructor(self):
        print("Private constructor")

# 4. Write a program which illustrates the concept of attributes of a constructor.
class AttributeExample:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

def main():
    obj1 = MyClass()
    obj2 = MyClass(10)
    obj3 = MyClass(10, 20)

    c1 = Child()
    c2 = Child("hello")

    mod = ModifierExample()
    mod._protected_constructor()
    # mod.__private_constructor()  # Not accessible directly

    attr_obj = AttributeExample("Alice", 25)
    attr_obj.display()

if __name__ == "__main__":
    main()
