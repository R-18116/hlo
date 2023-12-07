a=[1,3,5,6,7]
b=[110,20,30,3]
g=(list(filter(lambda x:x in a,b)))
print(g)


#filter using simple logic
a={10,20,30,40}
b={20,30,50,60}
def f(x):
    return x in a 
print(set(filter(f,b)))
    

# filter(function-name,sequence) 



