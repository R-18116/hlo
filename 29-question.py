# globvar="hello"
# def test1():
#     global globvar
#     globvar="Good Morning"

# def test2():
#     globvar="Good Evening"

# print(globvar)   #before updating global variable value is printed
# test1()      #updated global variable value
# test2()
# print(globvar)    #updated global variable value "Good morning is printed     





globvar="hello"
def test1():
    global globvar 
    globvar="good morning"
    print(globvar)
print(globvar)        
test1()
print(globvar) 
def test2():
    globvar="good evening"
    print(globvar)
test2()   
print(globvar)