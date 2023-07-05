#functions refers to grouped statements.


num1 = 20
num2 = 100
num3 = num1+num2
print(num3)

def sum():
    num1,num2 = 30,50
    num3 = num1+num2
    print(num3)

sum()
#line 14 tells the comp to go up and execute line 10,11,12 basing on the name of the function which is called 'sum()'
#line 12 can't

def sub():
    num1,num2 =400,9
    num3=num1-num2
    print(num3)

sub()

#the one that gets a remainder of two variables.
def rem():
    num1,num2 =9,7
    num3=num1%num2
    print(num3)
rem() #this is calling the function 'rem' as defined above.
#% (modulus),represents a remainder.
#a named group of statements is called a function.
#a function that will give a list ofnumbers from 1-10
def myList():
    list1 =[1,2,3,4,5,6,7,8,9,10]
    print(list1)
myList()

def food():
  fruits = ["oranges","pineapples"]
  print(fruits)

food()

def parts():
    zebra = {"name":"tongs","legs":4,"color":"black & white","sex":"male"}
    print(zebra.keys())
    print(zebra)
    zebra.__delitem__("name")
    print(zebra)
   
parts()

def numbers():
    myTuple = [10,20,30,40,50]
    print(myTuple)

numbers()
'''
multi-line comments
This means that you can write more that one line of comments within this triple qoutation
This should be written above the function
Endever to always put comments in your code.
'''
def figures():
    myList = [0,1,2,3,4,5,6,7,8,9]
    myList2 =[10,20,30,40,50]
    osman = [100,[200]]
    osman2 = [1000,[[2000,3000]]]
    print(myList)

figures()    
'''
Afunction is defined
The above functions are called static functions
'''

