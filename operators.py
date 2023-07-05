#operators in python.
#what are operators?
#an operator tells a computer what to do with an operand.
#an operand is what an operator acts upon.
#these operators are categorised.
#arithmetic operators (+,-,/,// floor ivision,%,*).
num1=10
num2=20
print(num1 + num2)
print(num1-num2)
print(num1//num2)
print(num1%num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)

#assignment operators(=,+=,-=,*=,/=,%=,**=)
num3 =50
num4 =100
num3 += num4 #(is the same as num3=num3 + num4)
print(num3)
num3-=num4
print(num3)

#comparison operators (==,!=,>,<,>=,<=)
print(num1==num2)
print(num1!=num2)
print(num1<num2)
print(num1<=num2)

#logical operators (and, or, not)
print(True and True)
print(True and False)
print(True or False)
print(not True)

#Identity operators (is,is not)
name ="Esther"
print(num3 is num4)

print(num3 is not num4)

#Membership operators (in, not in)
print("a" in name)
print("e" in name)
print("A" in name)
print("o" not in name)