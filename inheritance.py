# A, B and C are classes. A is a super class. B is a sub class of A. C is a sub class of B.
class A:
    def __init__(self):
        self.name = "Class A"

    def method1(self):
        print("A: method1")

    def method2(self):
        print("A: method2")

    def common(self):
        print("A: overridden method")

class B(A):
    def __init__(self):
        super().__init__()
        self.name = "Class B"

    def method1(self):
        print("B: method1")

    def method2(self):
        print("B: method2")

    def common(self):
        print("B: overridden method")

class C(B):
    def __init__(self):
        super().__init__()
        self.name = "Class C"

    def method1(self):
        print("C: method1")

    def method2(self):
        print("C: method2")

    def common(self):
        print("C: overridden method")

# Create a class with main method. Create an object for each class A, B and C in main method 
# and call every method of each class using its own object/instance.
def main():
    objA = A()
    objB = B()
    objC = C()

    print("\n--- Using A object ---")
    objA.method1()
    objA.method2()
    objA.common()

    print("\n--- Using B object ---")
    objB.method1()
    objB.method2()
    objB.common()

    print("\n--- Using C object ---")
    objC.method1()
    objC.method2()
    objC.common()

    # Call an overridden method with super class reference to B and C class’s objects
    print("\n--- Super class reference to B and C ---")
    refA: A = objB
    refA.common()

    refA = objC
    refA.common()

    # Runtime Polymorphism with Data Members/Instance variables, 
    # Repeat the above process only for data members
    print("\n--- Accessing data members using A reference to B and C ---")
    refA = objB
    print("Data member (A ref to B):", refA.name)

    refA = objC
    print("Data member (A ref to C):", refA.name)

if __name__ == "__main__":
    main()
