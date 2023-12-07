# calling a function again and again by itself 
# it is also known as circular definition or self-reference 
def factorial(x):    #this is a recursive function to find the the factorial of an integer
    if (x==1 or x==0):
        return 1
    else:
        return(x*factorial(x-1))
num=3
print("the factorial of",num,"is",factorial(num))    

    
    

