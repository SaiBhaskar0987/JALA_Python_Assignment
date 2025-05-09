# 1. Create a class with PRIVATE fields, private method and a main method. 
# Print the fields in main method. Call the private method in main method. 
# Create a sub class and try to access the private fields and methods from sub class.

class PrivateExample:
    def __init__(self):
        self.__private_field = "Private Field"

    def __private_method(self):
        print("Private Method Called")

    def access_private(self):
        print(self.__private_field)
        self.__private_method()

class SubPrivateExample(PrivateExample):
    def try_access_private(self):
        # These will raise AttributeError if uncommented, as private members can't be accessed directly
        # print(self.__private_field)
        # self.__private_method()
        print("Cannot access private members of superclass directly")

def main1():
    obj = PrivateExample()
    obj.access_private()
    sub_obj = SubPrivateExample()
    sub_obj.try_access_private()


# 2. Create a class with PROTECTED fields and methods. 
# Access these fields and methods from any other class in the same package.  
# Also, Access the PROTECTED fields and methods from child class located in a different package 
# Access the PROTECTED fields and methods from any class in different package

class ProtectedExample:
    def __init__(self):
        self._protected_field = "Protected Field"

    def _protected_method(self):
        print("Protected Method Called")

class SamePackageAccess:
    def access_protected(self):
        obj = ProtectedExample()
        print(obj._protected_field)
        obj._protected_method()

class ChildInOtherPackage(ProtectedExample):
    def access_from_child(self):
        print(self._protected_field)
        self._protected_method()

def main2():
    same = SamePackageAccess()
    same.access_protected()

    child = ChildInOtherPackage()
    child.access_from_child()


# 3. Create a class with PUBLIC fields and methods.  
# Access the public methods and fields from any class in the same package or different package.

class PublicExample:
    def __init__(self):
        self.public_field = "Public Field"

    def public_method(self):
        print("Public Method Called")

class AnyClass:
    def access_public(self):
        obj = PublicExample()
        print(obj.public_field)
        obj.public_method()

def main3():
    anyclass = AnyClass()
    anyclass.access_public()


if __name__ == "__main__":
    print("\n--- Private Access Example ---")
    main1()

    print("\n--- Protected Access Example ---")
    main2()

    print("\n--- Public Access Example ---")
    main3()