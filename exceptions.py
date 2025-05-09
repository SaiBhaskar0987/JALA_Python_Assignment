# 1. Write a program to generate Arithmetic Exception without exception handling
def generate_arithmetic_exception():
    x = 10 / 0  # ZeroDivisionError

# 2. Handle the Arithmetic exception using try-catch block
def handle_arithmetic_exception():
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError")

# 3. Write a method which throws exception, Call that method in main class without try block
def method_throwing_exception():
    raise ValueError("This is a thrown exception")

# 4. Write a program with multiple catch blocks
def multiple_catch_blocks():
    try:
        x = int("abc")
    except ValueError:
        print("ValueError caught")
    except TypeError:
        print("TypeError caught")

# 5. Write a program to throw exception with your own message
def custom_exception_message():
    raise ArithmeticError("Custom message for arithmetic error")

# 6. Write a program to create your own exception
class MyCustomException(Exception):
    pass

def raise_custom_exception():
    raise MyCustomException("This is my custom exception")

# 7. Write a program with finally block
def try_finally_block():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Handled exception")
    finally:
        print("Finally block executed")

# 8. Write a program to generate Arithmetic Exception
def generate_arithmetic_again():
    print(5 / 0)

# 9. Write a program to generate FileNotFoundException
def generate_file_not_found():
    with open("non_existent.txt", "r") as f:
        f.read()

# 10. Write a program to generate ClassNotFoundException
import importlib

def generate_class_not_found():
    importlib.import_module("non_existent_module")

# 11. Write a program to generate IOException
def generate_io_exception():
    import os
    os.rename("non_existent.txt", "another.txt")

# 12. Write a program to generate NoSuchFieldException
class Dummy:
    def __init__(self):
        self.x = 10

def generate_no_such_field():
    d = Dummy()
    print(d.y)  # AttributeError

def main():
    # Uncomment one at a time to see the result
    # generate_arithmetic_exception()
    handle_arithmetic_exception()
    # method_throwing_exception()
    multiple_catch_blocks()
    # custom_exception_message()
    # raise_custom_exception()
    try_finally_block()
    # generate_arithmetic_again()
    # generate_file_not_found()
    # generate_class_not_found()
    # generate_io_exception()
    # generate_no_such_field()

if __name__ == "__main__":
    main()