from time import time

class ObjectTimeClassOuter:
    def __init__(self):
        self.inner_class_obj = self.ObjectTimeClassInner()

    def checking(self):
        self.st = time()
        for _ in range(100000000):
                pass
        self.et = time() - self.st
        return self.et

    class ObjectTimeClassInner:
        def __init__(self):
            pass

        def checking(self):
            self.st = time()
            for _ in range(100000000):
                pass
            self.et = time() - self.st
            return self.et


obj_outer = ObjectTimeClassOuter()

def cal_time():
    outer = obj_outer.checking()
    inner = obj_outer.inner_class_obj.checking()
    
    outer_with_class = ObjectTimeClassOuter.checking(obj_outer)
    inner_with_class = ObjectTimeClassOuter.ObjectTimeClassInner.checking(obj_outer)

    print(f"\nOuter Time using object : {outer} seconds \nInner Time using object : {inner} seconds")
    print(f"\nOuter Time using Classname : {outer_with_class} seconds \nInner Time using Classname : {inner_with_class} seconds")


if __name__ == '__main__':
    cal_time()
