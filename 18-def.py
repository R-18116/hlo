def fun1(name='padma',age=12):         #default arguments
    print(name,'is',age,'years old.')
fun1('rishav',16)            #overright default fumction #positional argument
fun1(age=16,name="Karuna")      #keyword argument
fun1("padma",16)            #positional
fun1("karuna")              #only first value over right
fun1()                      #calling function