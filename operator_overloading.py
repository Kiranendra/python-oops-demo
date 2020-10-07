# Need to learn more. This in not enough

class Demo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other): 
        # Operator '+' overloading
        # We are writing our own functionality for the '+' operator
        # to work with Demo class. We are writing custom integer addition 
        # function for our class
        a = self.a + other.a
        b = self.b + other.b
        c = Demo(a, b)
        return c


a = Demo(1, 2)
b = Demo(8, 5)
c = a + b
print(c.a) # 1 + 8 = 9
print(c.b) # 2 + 5 = 7

'''
    We can overwrite the in-built methods (operator methods) to define our own.
'''
