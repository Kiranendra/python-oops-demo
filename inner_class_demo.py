class OuterClass:
    def __init__(self):
        self.name = 'Outer_Name'
        self.inner_class_object = self.InnerClass()

    def print_this(self):
        print("Outer Class")
        print(f"Name: {self.name}")

    class InnerClass:
        def __init__(self):
            self.name = 'Inner_Name'
        
        def print_this(self):
            # This method does not conflict with the outer class method
            print("Inner Class")
            print(f"Name: {self.name}")


outer_object = OuterClass() # Inner class object is also created with this
# outer_object.print_this() ==> Not recommended
OuterClass.print_this(outer_object)
# outer_object.inner_class_obj.print_this() ==> Not recommended
OuterClass.InnerClass.print_this(outer_object.inner_class_object)

