#it is like a function inside a function
def square(x):
    return x**2
def cube(x):
    return x**3
n=int(input("enter the value of n"))
result=square(cube(n))
print(result)

    