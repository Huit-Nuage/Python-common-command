# -*- coding: utf-8 -*-

GLOBAL = 10 #Global variables, capitalized by standard, can be used anywhere after definition

def fun():
    a = 20 #Local variables, can only be used in scope

fun()
#print(a) #Error, local variables cannot be used outside the scope

	
def fun2():
    global a
    a = 20 #Define global variables in the function, you can use after calling the function
    b = 30
    #global b #Error, b has been defined before being defined as a global variable

fun2()
print(a)
#print(b)


print(GLOBAL)