#pre defined
def add(a,b=10):
    x=a+b
    print(x)
add(20)
def add(a,b=10):  #b value is known as the default value 
    x=a+b
    print(x)
add(20,5)   #in this value of b overright the default value

def add(a=4,b=2,c=1):
    x=a+b+c
    print(x)
add()    

#def add(a=34,c=34,b):
#incorect definition 
# we have to assign the default value from the last
    


