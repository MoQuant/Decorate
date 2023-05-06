import asyncio
import numpy as np

# This function allows the user to print out the output of their
# function using a decorator
def Problem1():
    def decorator(f):
        def handle(*a, **b):
            z = f(*a, **b)
            print(z)
        return handle

    # Syntax for using a decorator on a function
    @decorator
    def add(x, y):
        return x + y

    @decorator
    def mult(x, y):
        return x*y


    x0, y0 = 4, 5

    result_add = add(x0, y0)
    result_mult = mult(x0, y0)


# This function creates a decorator which takes in its own argument
# and multiplies that number into the result of the function it is wrapping
def Problem2():

    def decorator(x):
        def decorate(f):
            def handle(*a, **b):
                z = f(*a, **b)
                z *= x
                return z
            return handle
        return decorate

    # Input an argument of the number 5 into the decorator
    @decorator(5)
    def add(x, y, z):
        return x + y + z

    x0, y0, z0 = 1, 2, 3
    result = add(x0, y0, z0)
    print(result)


# This function shows how to create a decorator for an asynchronus function
def Problem3():
    def decorator(f):
        # Notice you have to use async and await in the handle function,
        # but not on the outer function
        async def handle(*a, **b):
            z = await f(*a, **b)
            z = (z + 6)*3*z
            return z
        return handle

    # Decorate async function
    @decorator
    async def mult(x, y):
        return x*y

    x0, y0 = 3, 2
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(mult(x0, y0))
            
    print(result)


# This function shows how to use a decorator solve for a multi-variable
# regression model's coefficents
def Problem4():

    def solve(f):
        def quant(*a, **b):
            x, y = f(*a, **b)
            XTX = x.T.dot(x)
            XTY = x.T.dot(y)
            beta = np.linalg.inv(XTX).dot(XTY)
            return beta
        return quant

    # Converts datasets and solves for the regression model
    @solve
    def regression(x, y):
        X = [[1] + i for i in x]
        Y = [[q] for q in y]
        X, Y = np.array(X), np.array(Y)
        return X, Y


    import random as rd

    # Build a random dataset
    
    build = lambda m, n: [[rd.random() for j in range(n)] for i in range(m)]

    m = 50
    n = 5
    x0 = build(m, n)
    y0 = [rd.random() for j in range(m)]

    print(regression(x0, y0))


# This decorator calculates the time it takes to run a function. This is
# very useful for performance testing
def Problem5():
    import time

    # Timestamp function
    dt = lambda: int(time.time())

    def time_running_function(f):
        def handle(*a, **b):
            # Calculates the time
            t0 = dt()
            f(*a, **b)
            t1 = dt()
            return f'The function {__name__} took {t1 - t0} seconds to run'
        return handle

    @time_running_function
    def longx():
        total = 0
        for i in range(20000000):
            total += i

    @time_running_function
    def shortx():
        total = 1093839
        for i in range(1000):
            total *= (i+1)

    dlong = longx()
    dshort = shortx()

    print(dlong)
    print(dshort)









    
