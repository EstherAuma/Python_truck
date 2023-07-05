  

def add(num1,num2):
    num3 = num1 + num2
    print(num3)


def sub(num1,num2):
    num3= num1 - num2
    print(num3)
#Forcing functions to communicate

def add2(num1,num2): # num1 and num2 are caled parameters
    num3 = num1 + num2
    print(num3)
    return num3 
    
'''
return num3 is telling the computer to return the
value of num3 fro function add2 to function sub2
    
''' 
    
def sub2(num1):
    num3 = add2(4,12) - num1
    print(num3)

sub2(5)
 #5 is an argument or actual parameters or formal parameters, (value given during the function call)
#The above function is called 
# dynamic or parameterised functions.   
add2(100,200)

ans = add2(10,2)
print(ans)
print(add2(4,12))
#when u print a function call without having a return statement
#the value printed will be none
#A function that calls a returned value from another function is
#called a calling function.