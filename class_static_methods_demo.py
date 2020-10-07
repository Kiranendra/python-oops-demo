class Demo:
    value = 9 # Constant for every class instance
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, {self.name}")

    @classmethod
    def the_class_method(cls):
        return cls.value

    @staticmethod
    def class_info():
        print("The static method is like a general function that is written inside a class")


obj = Demo('Kiranendra')

#obj.greet() ==> Not recommended
Demo.greet(obj)
print(f"Class Method called : {Demo.the_class_method()}")
Demo.class_info()

