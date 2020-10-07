# Printing top ten values
class Demo:
    def __init__(self):
        self.num = 1

    # We are overriding the existing itertion methods 
    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            # to stop a for loop we have to raise the exception
            # the for loop will handle the exception internally
            raise StopIteration


values = Demo()

#print(values.__next__()) ==> Not recommended

print(Demo.__next__(values))

print(next(values))


# The iterator starts from the value '3', since it has already 
# printed two values '1' & '2'

# Uncomment the next line to see the diffence
#print()

for i in values:
    print(i)
