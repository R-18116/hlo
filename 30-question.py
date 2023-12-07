a=int(input("a: "))
def chngeglobal():
    global a
    a=200
def changelocal():
    a=500
    print("loacal a value:",a)
print("global a before function call:",a)
chngeglobal() 
changelocal()  
print("global a after function call:",a)