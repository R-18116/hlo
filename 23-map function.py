list1=[1,2,3,4,5]
def squares(x):
    return x**2
y=print(list(map(squares,list1)))    #square is the name of the 
# function list1 is the sequence  and list is used that we get single list with one to one maping. 


a={10,20,25,30}
def cuberoot(x):
    return (x/(1/3))
y=print(list(map(cuberoot,a)))



a={10,20,30,25}
def cube(x):
    return(x**3)      #if i write 5 or anything instead  of 3 it give another value then the cube function will not work
y=print(list(map(cube,a)))