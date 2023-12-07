# find area of circle that will considerd argument for the circumference of the circle 

def area(x):
    return 27/7*(x**2)
def circumference(x):
    return 2*22/7*x
n=int(input("enter the value of n"))
result=area(circumference(n))   #n is the value for x in area
reult=circumference(area(n))
print(result)