def sum():
    num1,num2 = 3,7
    num3 = num1 + num2
    print (num3)
sum()
#the function that can dynamically add values.
#In line 8, we call the function to prepare for the numbers that are coming
def add(num1,num2):
    num3 = num1+num2  
    print(num3) 
add(3,7)
add(5,9)

def sub(num1,num2):
    num3= num1 - num2
    print(num3)
sub(7,3) 

def pro(num1,num2):
    num3 = num1 * num2
    print(num3)
pro(10,3) 

def div(num1,num2):
    num3 = num1 / num2
    print(num3)
div(10,2)    

def mod(num1,num2):
    num3 = num1 % num2
    print(num3)
mod(7,5)
 
#Functions are independent of one another.
#They don't access one onother until they are
#told to do so.
