# Example for Recursive algorithm

def first_method():
    second_method()
    print("first method")

def second_method():
    third_method()
    print("second_method")

def third_method():
    forth_method()
    print("third_method")

def forth_method():
    print("forth method")

# first_method()

def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n - 1)
        print(n)

recursiveMethod(4)