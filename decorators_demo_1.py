def fun(f): #string
    # Some functions need zero or more
    # arguements then we have to use
    # *args & **kwargs
    def wrapper(*args, **kwargs):
        print("Start")
        #print(string)
        # to return the values that are passed
        values = f(*args, **kwargs)
        print("End")
        return values

    # return the wrapper function being called use --> ()
    #return wrapper()
    return wrapper

@fun
def fun2(x):
    print("Funtion 2")
    return x

@fun
def fun3():
    print("Function 3")

### x = fun(fun2)
##fun(fun2)
##print()
##fun(fun3)

##fun2 = fun(fun2)
##fun3 = fun(fun3)

A = fun2('a')
print()
print(A)
print()
fun3()
