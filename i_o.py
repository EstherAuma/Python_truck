def paye(salary,name):
   rate = 0.3
   tax = rate*salary
   net_pay = salary-tax
   print("*********************")
   print("Dear: ",name) 
   print("Your tax payable is: ",tax)
   print("And your take home salary is: ",net_pay)
   print(".....................")        



print ("You are wellcome! ")    
name = raw_input("Please input your name here: ")
salary = input("Please input your salary here: ")


paye (salary,name)    