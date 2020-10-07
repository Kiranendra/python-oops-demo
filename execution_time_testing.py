from time import time

class ObjectTimeClass:
    def __init__(self):
        pass
        
    def checking(self):
        self.st = time()
        for _ in range(100000000):
                pass
        self.et = time() - self.st
        return self.et

obj = ObjectTimeClass()

def cal_time():
    a = obj.checking()
    b = ObjectTimeClass.checking(obj)
    if a > b:
        print('Calling a class method using INSTANCE is EXPENSIVE')
    else:
        print('Calling a class method using CLASSNAME is EXPENSIVE')
    print(f"\nUsing Instance : {a} seconds \nUsing Classname : {b} seconds")

if __name__ == "__main__":
    cal_time()
