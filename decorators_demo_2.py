from time import time

# this is a decorator for calculating execution time for every function
def timer(f):
    def tester(*args,  **kwargs):
        start = time()
        rv = f()
        total = time() - start
        print(f"Total time taken : {total}")

    return tester

@timer
def test():
    for _ in range(10000000):
        pass

test()
