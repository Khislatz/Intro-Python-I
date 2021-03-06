# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
def change_x():
    x = 99
    print(x) #prints 99

change_x()
print(x) # prints 12


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        y = 999
        print(y)

    inner() # prints 999

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer() # to print all the outputs that is in this function

